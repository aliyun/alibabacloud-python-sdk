# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class JobStatusDetailValue(TeaModel):
    def __init__(
        self,
        comment: str = None,
        job_result: str = None,
        time_stamps: str = None,
    ):
        self.comment = comment
        self.job_result = job_result
        self.time_stamps = time_stamps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.job_result is not None:
            result['jobResult'] = self.job_result
        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')
        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')
        return self


class JobsStatusDetailValue(TeaModel):
    def __init__(
        self,
        comment: str = None,
        job_result: str = None,
        time_stamps: str = None,
    ):
        self.comment = comment
        self.job_result = job_result
        self.time_stamps = time_stamps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.job_result is not None:
            result['jobResult'] = self.job_result
        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')
        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')
        return self


class AssociateGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        self.project_id = project_id
        # This parameter is required.
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class AssociateGroupResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AssociateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateParameterSetRequest(TeaModel):
    def __init__(
        self,
        parameter_set_ids: List[str] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.parameter_set_ids = parameter_set_ids
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set_ids is not None:
            result['parameterSetIds'] = self.parameter_set_ids
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameterSetIds') is not None:
            self.parameter_set_ids = m.get('parameterSetIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class AssociateParameterSetResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AssociateParameterSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateParameterSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachRabbitmqPublisherRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class AttachRabbitmqPublisherResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AttachRabbitmqPublisherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachRabbitmqPublisherResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelProjectBuildResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelProjectBuildResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelProjectBuildResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelProjectBuildResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRamPolicyExportTaskResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelRamPolicyExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelRamPolicyExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelRamPolicyExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        ram_role: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.ram_role = ram_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        return self


class CancelResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResourceNameRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        parent_id: str = None,
        resource_type: str = None,
    ):
        self.id = id
        # This parameter is required.
        self.name = name
        self.parent_id = parent_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class CheckResourceNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CheckResourceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckResourceNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckResourceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        resource_types: List[str] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name
        self.project_id = project_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.resource_types is not None:
            result['resourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resourceTypes') is not None:
            self.resource_types = m.get('resourceTypes')
        return self


class CloneGroupResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloneGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneModuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        module_id: str = None,
        module_source: str = None,
        module_version: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_source = module_source
        # This parameter is required.
        self.module_version = module_version
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
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_source is not None:
            result['moduleSource'] = self.module_source
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleSource') is not None:
            self.module_source = m.get('moduleSource')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CloneModuleResponseBody(TeaModel):
    def __init__(
        self,
        module_id: str = None,
        request_id: str = None,
    ):
        self.module_id = module_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloneModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        due_time: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        uid: int = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.due_time = due_time
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        self.name = name
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        authorization_id: str = None,
        request_id: str = None,
    ):
        self.authorization_id = authorization_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_id is not None:
            result['authorizationId'] = self.authorization_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationId') is not None:
            self.authorization_id = m.get('authorizationId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExplorerTaskRequest(TeaModel):
    def __init__(
        self,
        init_module_state: bool = None,
        terraform_version: str = None,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        client_token: str = None,
        description: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        skip_property_validation: bool = None,
        terraform_provider_version: str = None,
        trigger_value: str = None,
    ):
        self.init_module_state = init_module_state
        self.terraform_version = terraform_version
        # This parameter is required.
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.skip_property_validation = skip_property_validation
        self.terraform_provider_version = terraform_provider_version
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.init_module_state is not None:
            result['InitModuleState'] = self.init_module_state
        if self.terraform_version is not None:
            result['TerraformVersion'] = self.terraform_version
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitModuleState') is not None:
            self.init_module_state = m.get('InitModuleState')
        if m.get('TerraformVersion') is not None:
            self.terraform_version = m.get('TerraformVersion')
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class CreateExplorerTaskResponseBody(TeaModel):
    def __init__(
        self,
        explorer_task_id: str = None,
        request_id: str = None,
    ):
        self.explorer_task_id = explorer_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.explorer_task_id is not None:
            result['explorerTaskId'] = self.explorer_task_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('explorerTaskId') is not None:
            self.explorer_task_id = m.get('explorerTaskId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateExplorerTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExplorerTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExplorerTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequestNotifyConfig(TeaModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        return self


class CreateGroupRequestTriggerConfig(TeaModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        client_token: str = None,
        description: str = None,
        forced_setting: bool = None,
        name: str = None,
        notify_config: List[CreateGroupRequestNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        project_id: str = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        terraform_provider_version: str = None,
        trigger_config: List[CreateGroupRequestTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.forced_setting = forced_setting
        # This parameter is required.
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        # This parameter is required.
        self.project_id = project_id
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for k in self.notify_config:
                if k:
                    k.validate()
        if self.trigger_config:
            for k in self.trigger_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting
        if self.name is not None:
            result['name'] = self.name
        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k in self.notify_config:
                result['notifyConfig'].append(k.to_map() if k else None)
        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field
        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k in self.trigger_config:
                result['triggerConfig'].append(k.to_map() if k else None)
        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k in m.get('notifyConfig'):
                temp_model = CreateGroupRequestNotifyConfig()
                self.notify_config.append(temp_model.from_map(k))
        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')
        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k in m.get('triggerConfig'):
                temp_model = CreateGroupRequestTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k))
        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        request_id: str = None,
    ):
        self.group_id = group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execute_type: str = None,
        sub_command: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.description = description
        self.execute_type = execute_type
        self.sub_command = sub_command
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.execute_type is not None:
            result['executeType'] = self.execute_type
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class CreateModuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_info: CreateModuleRequestGroupInfo = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        version_strategy: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        # This parameter is required.
        self.name = name
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.version_strategy = version_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = CreateModuleRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class CreateModuleResponseBody(TeaModel):
    def __init__(
        self,
        module_id: str = None,
        request_id: str = None,
    ):
        self.module_id = module_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleVersionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        module_version: str = None,
        request_id: str = None,
    ):
        self.module_version = module_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParameterSetRequestParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateParameterSetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        parameters: List[CreateParameterSetRequestParameters] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name
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
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = CreateParameterSetRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class CreateParameterSetResponseBody(TeaModel):
    def __init__(
        self,
        parameter_set_id: str = None,
        request_id: str = None,
    ):
        self.parameter_set_id = parameter_set_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateParameterSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateParameterSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
    ):
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectBuildRequestTaskPolicies(TeaModel):
    def __init__(
        self,
        destroy_after_execution: bool = None,
        priority: int = None,
        task_id: str = None,
    ):
        self.destroy_after_execution = destroy_after_execution
        self.priority = priority
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destroy_after_execution is not None:
            result['destroyAfterExecution'] = self.destroy_after_execution
        if self.priority is not None:
            result['priority'] = self.priority
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destroyAfterExecution') is not None:
            self.destroy_after_execution = m.get('destroyAfterExecution')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateProjectBuildRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        group_id: str = None,
        project_build_action: str = None,
        task_ids: List[str] = None,
        task_policies: List[CreateProjectBuildRequestTaskPolicies] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.group_id = group_id
        # This parameter is required.
        self.project_build_action = project_build_action
        self.task_ids = task_ids
        self.task_policies = task_policies

    def validate(self):
        if self.task_policies:
            for k in self.task_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_build_action is not None:
            result['projectBuildAction'] = self.project_build_action
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        result['taskPolicies'] = []
        if self.task_policies is not None:
            for k in self.task_policies:
                result['taskPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectBuildAction') is not None:
            self.project_build_action = m.get('projectBuildAction')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        self.task_policies = []
        if m.get('taskPolicies') is not None:
            for k in m.get('taskPolicies'):
                temp_model = CreateProjectBuildRequestTaskPolicies()
                self.task_policies.append(temp_model.from_map(k))
        return self


class CreateProjectBuildResponseBody(TeaModel):
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
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectBuildResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectBuildResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectBuildResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRabbitmqPublisherRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        exchange_name: str = None,
        exchange_type: str = None,
        host_name: str = None,
        name: str = None,
        password: str = None,
        port: int = None,
        user_name: str = None,
        virtual_host: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        # This parameter is required.
        self.host_name = host_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.user_name = user_name
        # This parameter is required.
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.name is not None:
            result['name'] = self.name
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.virtual_host is not None:
            result['virtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('virtualHost') is not None:
            self.virtual_host = m.get('virtualHost')
        return self


class CreateRabbitmqPublisherResponseBody(TeaModel):
    def __init__(
        self,
        publisher_id: str = None,
        request_id: str = None,
    ):
        self.publisher_id = publisher_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.publisher_id is not None:
            result['publisherId'] = self.publisher_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publisherId') is not None:
            self.publisher_id = m.get('publisherId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRabbitmqPublisherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRabbitmqPublisherResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRamPolicyExportTaskRequest(TeaModel):
    def __init__(
        self,
        authorization_account_ids: List[int] = None,
        authorization_actions: List[str] = None,
        authorization_region_ids: List[str] = None,
        client_token: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        trigger_strategy: str = None,
    ):
        self.authorization_account_ids = authorization_account_ids
        self.authorization_actions = authorization_actions
        self.authorization_region_ids = authorization_region_ids
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.ram_role = ram_role
        self.terraform_provider_version = terraform_provider_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_account_ids is not None:
            result['authorizationAccountIds'] = self.authorization_account_ids
        if self.authorization_actions is not None:
            result['authorizationActions'] = self.authorization_actions
        if self.authorization_region_ids is not None:
            result['authorizationRegionIds'] = self.authorization_region_ids
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationAccountIds') is not None:
            self.authorization_account_ids = m.get('authorizationAccountIds')
        if m.get('authorizationActions') is not None:
            self.authorization_actions = m.get('authorizationActions')
        if m.get('authorizationRegionIds') is not None:
            self.authorization_region_ids = m.get('authorizationRegionIds')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class CreateRamPolicyExportTaskResponseBody(TeaModel):
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
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRamPolicyExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRamPolicyExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRamPolicyExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceExportTaskRequestExcludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateResourceExportTaskRequestExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class CreateResourceExportTaskRequestIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateResourceExportTaskRequestVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class CreateResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_path: str = None,
        description: str = None,
        exclude_rules: List[CreateResourceExportTaskRequestExcludeRules] = None,
        export_to_module: CreateResourceExportTaskRequestExportToModule = None,
        include_rules: List[CreateResourceExportTaskRequestIncludeRules] = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[CreateResourceExportTaskRequestVariables] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.config_path = config_path
        self.description = description
        self.exclude_rules = exclude_rules
        self.export_to_module = export_to_module
        self.include_rules = include_rules
        # This parameter is required.
        self.name = name
        self.ram_role = ram_role
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.variables = variables

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.config_path is not None:
            result['configPath'] = self.config_path
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('configPath') is not None:
            self.config_path = m.get('configPath')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = CreateResourceExportTaskRequestExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportToModule') is not None:
            temp_model = CreateResourceExportTaskRequestExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = CreateResourceExportTaskRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = CreateResourceExportTaskRequestVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class CreateResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class CreateTaskRequestTaskBackend(TeaModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        object_path: str = None,
    ):
        self.bucket_endpoint = bucket_endpoint
        self.bucket_name = bucket_name
        self.object_path = object_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_endpoint is not None:
            result['bucketEndpoint'] = self.bucket_endpoint
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.object_path is not None:
            result['objectPath'] = self.object_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketEndpoint') is not None:
            self.bucket_endpoint = m.get('bucketEndpoint')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('objectPath') is not None:
            self.object_path = m.get('objectPath')
        return self


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        client_token: str = None,
        description: str = None,
        group_info: CreateTaskRequestGroupInfo = None,
        init_module_state: bool = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        parameters: Dict[str, str] = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        task_backend: CreateTaskRequestTaskBackend = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        # This parameter is required.
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.parameters = parameters
        self.protection_strategy = protection_strategy
        # This parameter is required.
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.task_backend = task_backend
        self.terraform_version = terraform_version
        # This parameter is required.
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.task_backend:
            self.task_backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        if self.task_backend is not None:
            result['taskBackend'] = self.task_backend.to_map()
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = CreateTaskRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        if m.get('taskBackend') is not None:
            temp_model = CreateTaskRequestTaskBackend()
            self.task_backend = temp_model.from_map(m['taskBackend'])
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModuleResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParameterSetResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteParameterSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteParameterSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRabbitmqPublisherResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRabbitmqPublisherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRabbitmqPublisherResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRamPolicyExportTaskResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRamPolicyExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRamPolicyExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRamPolicyExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRamPolicyExportTaskVersionResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRamPolicyExportTaskVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRamPolicyExportTaskVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRamPolicyExportTaskVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceExportTaskResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneTestingTaskResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSceneTestingTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSceneTestingTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSceneTestingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachRabbitmqPublisherRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DetachRabbitmqPublisherResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DetachRabbitmqPublisherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachRabbitmqPublisherResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class DissociateGroupResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DissociateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateParameterSetRequest(TeaModel):
    def __init__(
        self,
        parameter_set_ids: List[str] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.parameter_set_ids = parameter_set_ids
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set_ids is not None:
            result['parameterSetIds'] = self.parameter_set_ids
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameterSetIds') is not None:
            self.parameter_set_ids = m.get('parameterSetIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class DissociateParameterSetResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DissociateParameterSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateParameterSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteRamPolicyExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteRamPolicyExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteRamPolicyExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteRamPolicyExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        ram_role: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.ram_role = ram_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        return self


class ExecuteResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExplorerTaskResponseBodyTaskUploadSignature(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket_name: str = None,
        key: str = None,
        policy: str = None,
        signature: str = None,
        url: str = None,
    ):
        self.access_key_id = access_key_id
        self.bucket_name = bucket_name
        self.key = key
        self.policy = policy
        self.signature = signature
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetExplorerTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        description: str = None,
        explorer_task_id: str = None,
        init_module_state: bool = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        skip_property_validation: bool = None,
        status: str = None,
        task_output_path: str = None,
        terraform_version: str = None,
        trigger_value: str = None,
        upload_signature: GetExplorerTaskResponseBodyTaskUploadSignature = None,
    ):
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.description = description
        self.explorer_task_id = explorer_task_id
        self.init_module_state = init_module_state
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.skip_property_validation = skip_property_validation
        self.status = status
        self.task_output_path = task_output_path
        self.terraform_version = terraform_version
        self.trigger_value = trigger_value
        self.upload_signature = upload_signature

    def validate(self):
        if self.upload_signature:
            self.upload_signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.description is not None:
            result['description'] = self.description
        if self.explorer_task_id is not None:
            result['explorerTaskId'] = self.explorer_task_id
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        if self.status is not None:
            result['status'] = self.status
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        if self.upload_signature is not None:
            result['uploadSignature'] = self.upload_signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('explorerTaskId') is not None:
            self.explorer_task_id = m.get('explorerTaskId')
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        if m.get('uploadSignature') is not None:
            temp_model = GetExplorerTaskResponseBodyTaskUploadSignature()
            self.upload_signature = temp_model.from_map(m['uploadSignature'])
        return self


class GetExplorerTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetExplorerTaskResponseBodyTask = None,
    ):
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetExplorerTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetExplorerTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExplorerTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExplorerTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupResponseBodyGroupNotifyConfig(TeaModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        return self


class GetGroupResponseBodyGroupTriggerConfig(TeaModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        create_time: str = None,
        description: str = None,
        forced_setting: bool = None,
        group_id: str = None,
        name: str = None,
        notify_config: List[GetGroupResponseBodyGroupNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        project_id: str = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        task_cnt: int = None,
        terraform_provider_version: str = None,
        trigger_config: List[GetGroupResponseBodyGroupTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        self.create_time = create_time
        self.description = description
        self.forced_setting = forced_setting
        self.group_id = group_id
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        self.project_id = project_id
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.task_cnt = task_cnt
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for k in self.notify_config:
                if k:
                    k.validate()
        if self.trigger_config:
            for k in self.trigger_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.name is not None:
            result['name'] = self.name
        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k in self.notify_config:
                result['notifyConfig'].append(k.to_map() if k else None)
        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field
        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k in self.trigger_config:
                result['triggerConfig'].append(k.to_map() if k else None)
        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k in m.get('notifyConfig'):
                temp_model = GetGroupResponseBodyGroupNotifyConfig()
                self.notify_config.append(temp_model.from_map(k))
        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')
        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k in m.get('triggerConfig'):
                temp_model = GetGroupResponseBodyGroupTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k))
        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: GetGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['group'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        task_type: str = None,
    ):
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class GetJobResponseBodyJobAssertCheckDetail(TeaModel):
    def __init__(
        self,
        comparison: str = None,
        expected_value: str = None,
        is_pass: bool = None,
        type: str = None,
    ):
        self.comparison = comparison
        self.expected_value = expected_value
        self.is_pass = is_pass
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison is not None:
            result['comparison'] = self.comparison
        if self.expected_value is not None:
            result['expectedValue'] = self.expected_value
        if self.is_pass is not None:
            result['isPass'] = self.is_pass
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparison') is not None:
            self.comparison = m.get('comparison')
        if m.get('expectedValue') is not None:
            self.expected_value = m.get('expectedValue')
        if m.get('isPass') is not None:
            self.is_pass = m.get('isPass')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetJobResponseBodyJobConfig(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        is_destroy: bool = None,
        module_version: str = None,
        resources_changed: str = None,
        sub_command: str = None,
    ):
        self.auto_apply = auto_apply
        self.is_destroy = is_destroy
        self.module_version = module_version
        self.resources_changed = resources_changed
        self.sub_command = sub_command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        return self


class GetJobResponseBodyJob(TeaModel):
    def __init__(
        self,
        assert_check_detail: List[GetJobResponseBodyJobAssertCheckDetail] = None,
        config: GetJobResponseBodyJobConfig = None,
        create_time: str = None,
        description: str = None,
        download_url: Dict[str, Any] = None,
        elapsed_time: int = None,
        execute_type: str = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        output: str = None,
        parameters: Dict[str, str] = None,
        runtime_type: str = None,
        status: str = None,
        status_detail: Dict[str, JobStatusDetailValue] = None,
        task_id: str = None,
        task_type: str = None,
        terraform_provider_version: str = None,
    ):
        self.assert_check_detail = assert_check_detail
        self.config = config
        self.create_time = create_time
        self.description = description
        self.download_url = download_url
        self.elapsed_time = elapsed_time
        self.execute_type = execute_type
        self.is_pass_assert_check = is_pass_assert_check
        self.job_id = job_id
        self.output = output
        self.parameters = parameters
        self.runtime_type = runtime_type
        self.status = status
        self.status_detail = status_detail
        self.task_id = task_id
        self.task_type = task_type
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        if self.assert_check_detail:
            for k in self.assert_check_detail:
                if k:
                    k.validate()
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v in self.status_detail.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['assertCheckDetail'] = []
        if self.assert_check_detail is not None:
            for k in self.assert_check_detail:
                result['assertCheckDetail'].append(k.to_map() if k else None)
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.execute_type is not None:
            result['executeType'] = self.execute_type
        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.output is not None:
            result['output'] = self.output
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.runtime_type is not None:
            result['runtimeType'] = self.runtime_type
        if self.status is not None:
            result['status'] = self.status
        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k, v in self.status_detail.items():
                result['statusDetail'][k] = v.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assert_check_detail = []
        if m.get('assertCheckDetail') is not None:
            for k in m.get('assertCheckDetail'):
                temp_model = GetJobResponseBodyJobAssertCheckDetail()
                self.assert_check_detail.append(temp_model.from_map(k))
        if m.get('config') is not None:
            temp_model = GetJobResponseBodyJobConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')
        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('runtimeType') is not None:
            self.runtime_type = m.get('runtimeType')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k, v in m.get('statusDetail').items():
                temp_model = JobStatusDetailValue()
                self.status_detail[k] = temp_model.from_map(v)
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        job: GetJobResponseBodyJob = None,
        request_id: str = None,
    ):
        self.job = job
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['job'] = self.job.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('job') is not None:
            temp_model = GetJobResponseBodyJob()
            self.job = temp_model.from_map(m['job'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleResponseBodyModule(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        latest_version: str = None,
        module_id: str = None,
        name: str = None,
        output_path: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        status: str = None,
        version_strategy: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.latest_version = latest_version
        self.module_id = module_id
        self.name = name
        self.output_path = output_path
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.status = status
        self.version_strategy = version_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        if self.output_path is not None:
            result['outputPath'] = self.output_path
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.status is not None:
            result['status'] = self.status
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('outputPath') is not None:
            self.output_path = m.get('outputPath')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class GetModuleResponseBody(TeaModel):
    def __init__(
        self,
        module: GetModuleResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = GetModuleResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleVersionResponseBodyVersion(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        terraform_context: Dict[str, Any] = None,
        version_strategy: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.terraform_context = terraform_context
        self.version_strategy = version_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class GetModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: GetModuleVersionResponseBodyVersion = None,
    ):
        self.request_id = request_id
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.version is not None:
            result['version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('version') is not None:
            temp_model = GetModuleVersionResponseBodyVersion()
            self.version = temp_model.from_map(m['version'])
        return self


class GetModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParameterSetResponseBodyParameterSetParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetParameterSetResponseBodyParameterSetRelationList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.create_time = create_time
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetParameterSetResponseBodyParameterSet(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        parameter_set_id: str = None,
        parameters: List[GetParameterSetResponseBodyParameterSetParameters] = None,
        relation_list: List[GetParameterSetResponseBodyParameterSetRelationList] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.parameter_set_id = parameter_set_id
        self.parameters = parameters
        self.relation_list = relation_list

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetParameterSetResponseBodyParameterSetParameters()
                self.parameters.append(temp_model.from_map(k))
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = GetParameterSetResponseBodyParameterSetRelationList()
                self.relation_list.append(temp_model.from_map(k))
        return self


class GetParameterSetResponseBody(TeaModel):
    def __init__(
        self,
        parameter_set: GetParameterSetResponseBodyParameterSet = None,
        request_id: str = None,
    ):
        self.parameter_set = parameter_set
        self.request_id = request_id

    def validate(self):
        if self.parameter_set:
            self.parameter_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_set is not None:
            result['parameterSet'] = self.parameter_set.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameterSet') is not None:
            temp_model = GetParameterSetResponseBodyParameterSet()
            self.parameter_set = temp_model.from_map(m['parameterSet'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetParameterSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetParameterSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetParameterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponseBodyProject(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.project_id = project_id
        self.task_cnt = task_cnt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: GetProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            temp_model = GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m['project'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectBuildContextRequest(TeaModel):
    def __init__(
        self,
        is_pass_assert_check: bool = None,
        status: str = None,
    ):
        self.is_pass_assert_check = is_pass_assert_check
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetProjectBuildContextResponseBodyProjectBuildJobList(TeaModel):
    def __init__(
        self,
        elapsed_time: int = None,
        is_deleted: int = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        status: str = None,
        task_id: str = None,
        terraform_provider_version: str = None,
        type: str = None,
    ):
        self.elapsed_time = elapsed_time
        self.is_deleted = is_deleted
        self.is_pass_assert_check = is_pass_assert_check
        self.job_id = job_id
        self.module_id = module_id
        self.module_name = module_name
        self.module_version = module_version
        self.name = name
        self.status = status
        self.task_id = task_id
        self.terraform_provider_version = terraform_provider_version
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.is_deleted is not None:
            result['isDeleted'] = self.is_deleted
        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('isDeleted') is not None:
            self.is_deleted = m.get('isDeleted')
        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetProjectBuildContextResponseBodyProjectBuildResourceList(TeaModel):
    def __init__(
        self,
        info: Dict[str, str] = None,
        resource_cnt: int = None,
        resource_type: str = None,
    ):
        self.info = info
        self.resource_cnt = resource_cnt
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['info'] = self.info
        if self.resource_cnt is not None:
            result['resourceCnt'] = self.resource_cnt
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('info') is not None:
            self.info = m.get('info')
        if m.get('resourceCnt') is not None:
            self.resource_cnt = m.get('resourceCnt')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetProjectBuildContextResponseBodyProjectBuild(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        fail_cnt: int = None,
        job_list: List[GetProjectBuildContextResponseBodyProjectBuildJobList] = None,
        job_total_cnt: int = None,
        project_build_id: str = None,
        project_id: str = None,
        resource_cnt: int = None,
        resource_list: List[GetProjectBuildContextResponseBodyProjectBuildResourceList] = None,
        resource_type_cnt: int = None,
        status: str = None,
        success_cnt: int = None,
        terraform_provider_version: str = None,
        trigger_strategy: str = None,
    ):
        self.end_time = end_time
        self.fail_cnt = fail_cnt
        self.job_list = job_list
        self.job_total_cnt = job_total_cnt
        self.project_build_id = project_build_id
        self.project_id = project_id
        self.resource_cnt = resource_cnt
        self.resource_list = resource_list
        self.resource_type_cnt = resource_type_cnt
        self.status = status
        self.success_cnt = success_cnt
        self.terraform_provider_version = terraform_provider_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.fail_cnt is not None:
            result['failCnt'] = self.fail_cnt
        result['jobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['jobList'].append(k.to_map() if k else None)
        if self.job_total_cnt is not None:
            result['jobTotalCnt'] = self.job_total_cnt
        if self.project_build_id is not None:
            result['projectBuildId'] = self.project_build_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.resource_cnt is not None:
            result['resourceCnt'] = self.resource_cnt
        result['resourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['resourceList'].append(k.to_map() if k else None)
        if self.resource_type_cnt is not None:
            result['resourceTypeCnt'] = self.resource_type_cnt
        if self.status is not None:
            result['status'] = self.status
        if self.success_cnt is not None:
            result['successCnt'] = self.success_cnt
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('failCnt') is not None:
            self.fail_cnt = m.get('failCnt')
        self.job_list = []
        if m.get('jobList') is not None:
            for k in m.get('jobList'):
                temp_model = GetProjectBuildContextResponseBodyProjectBuildJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('jobTotalCnt') is not None:
            self.job_total_cnt = m.get('jobTotalCnt')
        if m.get('projectBuildId') is not None:
            self.project_build_id = m.get('projectBuildId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resourceCnt') is not None:
            self.resource_cnt = m.get('resourceCnt')
        self.resource_list = []
        if m.get('resourceList') is not None:
            for k in m.get('resourceList'):
                temp_model = GetProjectBuildContextResponseBodyProjectBuildResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('resourceTypeCnt') is not None:
            self.resource_type_cnt = m.get('resourceTypeCnt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('successCnt') is not None:
            self.success_cnt = m.get('successCnt')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class GetProjectBuildContextResponseBody(TeaModel):
    def __init__(
        self,
        project_build: GetProjectBuildContextResponseBodyProjectBuild = None,
        request_id: str = None,
    ):
        self.project_build = project_build
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.project_build:
            self.project_build.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_build is not None:
            result['ProjectBuild'] = self.project_build.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectBuild') is not None:
            temp_model = GetProjectBuildContextResponseBodyProjectBuild()
            self.project_build = temp_model.from_map(m['ProjectBuild'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectBuildContextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectBuildContextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectBuildContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRabbitmqPublisherResponseBodyPublisher(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        exchange_name: str = None,
        exchange_type: str = None,
        host_name: str = None,
        name: str = None,
        port: int = None,
        publisher_id: str = None,
        task_ids: List[str] = None,
        user_name: str = None,
        virtual_host: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.host_name = host_name
        self.name = name
        self.port = port
        self.publisher_id = publisher_id
        self.task_ids = task_ids
        self.user_name = user_name
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.publisher_id is not None:
            result['publisherId'] = self.publisher_id
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.virtual_host is not None:
            result['virtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('publisherId') is not None:
            self.publisher_id = m.get('publisherId')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('virtualHost') is not None:
            self.virtual_host = m.get('virtualHost')
        return self


class GetRabbitmqPublisherResponseBody(TeaModel):
    def __init__(
        self,
        publisher: GetRabbitmqPublisherResponseBodyPublisher = None,
        request_id: str = None,
    ):
        self.publisher = publisher
        self.request_id = request_id

    def validate(self):
        if self.publisher:
            self.publisher.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.publisher is not None:
            result['publisher'] = self.publisher.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publisher') is not None:
            temp_model = GetRabbitmqPublisherResponseBodyPublisher()
            self.publisher = temp_model.from_map(m['publisher'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRabbitmqPublisherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRabbitmqPublisherResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRabbitmqPublisherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRamPolicyExportTaskResponseBodyRamPolicyExportTask(TeaModel):
    def __init__(
        self,
        authorization_account_ids: List[int] = None,
        authorization_actions: List[str] = None,
        authorization_region_ids: List[str] = None,
        create_time: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        ram_policy_export_task_id: str = None,
        ram_role: str = None,
        status: str = None,
        task_output_path: str = None,
        terraform_provider_version: str = None,
        trigger_strategy: str = None,
    ):
        self.authorization_account_ids = authorization_account_ids
        self.authorization_actions = authorization_actions
        self.authorization_region_ids = authorization_region_ids
        self.create_time = create_time
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.ram_policy_export_task_id = ram_policy_export_task_id
        self.ram_role = ram_role
        self.status = status
        self.task_output_path = task_output_path
        self.terraform_provider_version = terraform_provider_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_account_ids is not None:
            result['authorizationAccountIds'] = self.authorization_account_ids
        if self.authorization_actions is not None:
            result['authorizationActions'] = self.authorization_actions
        if self.authorization_region_ids is not None:
            result['authorizationRegionIds'] = self.authorization_region_ids
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.ram_policy_export_task_id is not None:
            result['ramPolicyExportTaskId'] = self.ram_policy_export_task_id
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.status is not None:
            result['status'] = self.status
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationAccountIds') is not None:
            self.authorization_account_ids = m.get('authorizationAccountIds')
        if m.get('authorizationActions') is not None:
            self.authorization_actions = m.get('authorizationActions')
        if m.get('authorizationRegionIds') is not None:
            self.authorization_region_ids = m.get('authorizationRegionIds')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramPolicyExportTaskId') is not None:
            self.ram_policy_export_task_id = m.get('ramPolicyExportTaskId')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class GetRamPolicyExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        ram_policy_export_task: GetRamPolicyExportTaskResponseBodyRamPolicyExportTask = None,
        request_id: str = None,
    ):
        self.ram_policy_export_task = ram_policy_export_task
        self.request_id = request_id

    def validate(self):
        if self.ram_policy_export_task:
            self.ram_policy_export_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ram_policy_export_task is not None:
            result['ramPolicyExportTask'] = self.ram_policy_export_task.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ramPolicyExportTask') is not None:
            temp_model = GetRamPolicyExportTaskResponseBodyRamPolicyExportTask()
            self.ram_policy_export_task = temp_model.from_map(m['ramPolicyExportTask'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRamPolicyExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRamPolicyExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRamPolicyExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRamPolicyExportTaskVersionResponseBodyRamPolicyExportTaskVersion(TeaModel):
    def __init__(
        self,
        authorization_account_ids: List[int] = None,
        authorization_actions: List[str] = None,
        authorization_region_ids: List[str] = None,
        create_time: str = None,
        elapsed_time: int = None,
        export_version: str = None,
        failed_reason: str = None,
        missing_actions: List[str] = None,
        module_id: str = None,
        module_version: str = None,
        no_support_resource_types: List[str] = None,
        policy_document: str = None,
        ram_policy_export_task_id: str = None,
        status: str = None,
        terraform_provider_version: str = None,
        unauthorized_actions: List[str] = None,
        warn_message: str = None,
    ):
        self.authorization_account_ids = authorization_account_ids
        self.authorization_actions = authorization_actions
        self.authorization_region_ids = authorization_region_ids
        self.create_time = create_time
        self.elapsed_time = elapsed_time
        self.export_version = export_version
        self.failed_reason = failed_reason
        self.missing_actions = missing_actions
        self.module_id = module_id
        self.module_version = module_version
        self.no_support_resource_types = no_support_resource_types
        self.policy_document = policy_document
        self.ram_policy_export_task_id = ram_policy_export_task_id
        self.status = status
        self.terraform_provider_version = terraform_provider_version
        self.unauthorized_actions = unauthorized_actions
        self.warn_message = warn_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_account_ids is not None:
            result['authorizationAccountIds'] = self.authorization_account_ids
        if self.authorization_actions is not None:
            result['authorizationActions'] = self.authorization_actions
        if self.authorization_region_ids is not None:
            result['authorizationRegionIds'] = self.authorization_region_ids
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        if self.missing_actions is not None:
            result['missingActions'] = self.missing_actions
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.no_support_resource_types is not None:
            result['noSupportResourceTypes'] = self.no_support_resource_types
        if self.policy_document is not None:
            result['policyDocument'] = self.policy_document
        if self.ram_policy_export_task_id is not None:
            result['ramPolicyExportTaskId'] = self.ram_policy_export_task_id
        if self.status is not None:
            result['status'] = self.status
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.unauthorized_actions is not None:
            result['unauthorizedActions'] = self.unauthorized_actions
        if self.warn_message is not None:
            result['warnMessage'] = self.warn_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationAccountIds') is not None:
            self.authorization_account_ids = m.get('authorizationAccountIds')
        if m.get('authorizationActions') is not None:
            self.authorization_actions = m.get('authorizationActions')
        if m.get('authorizationRegionIds') is not None:
            self.authorization_region_ids = m.get('authorizationRegionIds')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        if m.get('missingActions') is not None:
            self.missing_actions = m.get('missingActions')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('noSupportResourceTypes') is not None:
            self.no_support_resource_types = m.get('noSupportResourceTypes')
        if m.get('policyDocument') is not None:
            self.policy_document = m.get('policyDocument')
        if m.get('ramPolicyExportTaskId') is not None:
            self.ram_policy_export_task_id = m.get('ramPolicyExportTaskId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('unauthorizedActions') is not None:
            self.unauthorized_actions = m.get('unauthorizedActions')
        if m.get('warnMessage') is not None:
            self.warn_message = m.get('warnMessage')
        return self


class GetRamPolicyExportTaskVersionResponseBody(TeaModel):
    def __init__(
        self,
        ram_policy_export_task_version: GetRamPolicyExportTaskVersionResponseBodyRamPolicyExportTaskVersion = None,
        request_id: str = None,
    ):
        self.ram_policy_export_task_version = ram_policy_export_task_version
        self.request_id = request_id

    def validate(self):
        if self.ram_policy_export_task_version:
            self.ram_policy_export_task_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ram_policy_export_task_version is not None:
            result['ramPolicyExportTaskVersion'] = self.ram_policy_export_task_version.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ramPolicyExportTaskVersion') is not None:
            temp_model = GetRamPolicyExportTaskVersionResponseBodyRamPolicyExportTaskVersion()
            self.ram_policy_export_task_version = temp_model.from_map(m['ramPolicyExportTaskVersion'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRamPolicyExportTaskVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRamPolicyExportTaskVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRamPolicyExportTaskVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        export_version: str = None,
    ):
        self.export_version = export_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        return self


class GetResourceExportTaskResponseBodyTaskExcludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetResourceExportTaskResponseBodyTaskExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class GetResourceExportTaskResponseBodyTaskIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetResourceExportTaskResponseBodyTaskModules(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetResourceExportTaskResponseBodyTaskVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetResourceExportTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        config_path: str = None,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        exclude_rules: List[GetResourceExportTaskResponseBodyTaskExcludeRules] = None,
        export_task_id: str = None,
        export_to_module: GetResourceExportTaskResponseBodyTaskExportToModule = None,
        export_version: str = None,
        failed_reason: str = None,
        include_rules: List[GetResourceExportTaskResponseBodyTaskIncludeRules] = None,
        modules: List[GetResourceExportTaskResponseBodyTaskModules] = None,
        name: str = None,
        ram_role: str = None,
        status: str = None,
        task_output_path: str = None,
        terraform_context: Dict[str, Any] = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[GetResourceExportTaskResponseBodyTaskVariables] = None,
    ):
        self.config_path = config_path
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.exclude_rules = exclude_rules
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.failed_reason = failed_reason
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.ram_role = ram_role
        self.status = status
        self.task_output_path = task_output_path
        self.terraform_context = terraform_context
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.variables = variables

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_path is not None:
            result['configPath'] = self.config_path
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.status is not None:
            result['status'] = self.status
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configPath') is not None:
            self.config_path = m.get('configPath')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = GetResourceExportTaskResponseBodyTaskExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = GetResourceExportTaskResponseBodyTaskExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = GetResourceExportTaskResponseBodyTaskIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = GetResourceExportTaskResponseBodyTaskModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = GetResourceExportTaskResponseBodyTaskVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetResourceExportTaskResponseBodyTask = None,
    ):
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetResourceExportTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBodyTaskGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        description: str = None,
        group_info: GetTaskResponseBodyTaskGroupInfo = None,
        init_module_state: bool = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        parameters: Dict[str, str] = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        status: str = None,
        task_id: str = None,
        task_output_path: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.parameters = parameters
        self.protection_strategy = protection_strategy
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.status = status
        self.task_id = task_id
        self.task_output_path = task_output_path
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = GetTaskResponseBodyTaskGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetTaskResponseBodyTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskPolicyRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTaskPolicyResponseBodyTaskPolicyTaskPolicies(TeaModel):
    def __init__(
        self,
        priority: int = None,
        task_id: str = None,
        task_name: str = None,
        type: str = None,
    ):
        self.priority = priority
        self.task_id = task_id
        self.task_name = task_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['priority'] = self.priority
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_name is not None:
            result['taskName'] = self.task_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTaskPolicyResponseBodyTaskPolicy(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        task_policies: List[GetTaskPolicyResponseBodyTaskPolicyTaskPolicies] = None,
    ):
        self.group_id = group_id
        self.task_policies = task_policies

    def validate(self):
        if self.task_policies:
            for k in self.task_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['taskPolicies'] = []
        if self.task_policies is not None:
            for k in self.task_policies:
                result['taskPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.task_policies = []
        if m.get('taskPolicies') is not None:
            for k in m.get('taskPolicies'):
                temp_model = GetTaskPolicyResponseBodyTaskPolicyTaskPolicies()
                self.task_policies.append(temp_model.from_map(k))
        return self


class GetTaskPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_policy: GetTaskPolicyResponseBodyTaskPolicy = None,
    ):
        self.request_id = request_id
        self.task_policy = task_policy

    def validate(self):
        if self.task_policy:
            self.task_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task_policy is not None:
            result['taskPolicy'] = self.task_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskPolicy') is not None:
            temp_model = GetTaskPolicyResponseBodyTaskPolicy()
            self.task_policy = temp_model.from_map(m['taskPolicy'])
        return self


class GetTaskPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationsRequest(TeaModel):
    def __init__(
        self,
        authorization_id: str = None,
        authorization_type: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.authorization_id = authorization_id
        # This parameter is required.
        self.authorization_type = authorization_type
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_id is not None:
            result['authorizationId'] = self.authorization_id
        if self.authorization_type is not None:
            result['authorizationType'] = self.authorization_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationId') is not None:
            self.authorization_id = m.get('authorizationId')
        if m.get('authorizationType') is not None:
            self.authorization_type = m.get('authorizationType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAuthorizationsResponseBodyAuthorizations(TeaModel):
    def __init__(
        self,
        authorization_id: str = None,
        create_time: str = None,
        due_time: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        owner_uid: int = None,
        uid: int = None,
    ):
        self.authorization_id = authorization_id
        self.create_time = create_time
        self.due_time = due_time
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.owner_uid = owner_uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_id is not None:
            result['authorizationId'] = self.authorization_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.owner_uid is not None:
            result['ownerUid'] = self.owner_uid
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationId') is not None:
            self.authorization_id = m.get('authorizationId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ownerUid') is not None:
            self.owner_uid = m.get('ownerUid')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListAuthorizationsResponseBody(TeaModel):
    def __init__(
        self,
        authorizations: List[ListAuthorizationsResponseBodyAuthorizations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorizations = authorizations
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorizations:
            for k in self.authorizations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['authorizations'] = []
        if self.authorizations is not None:
            for k in self.authorizations:
                result['authorizations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorizations = []
        if m.get('authorizations') is not None:
            for k in m.get('authorizations'):
                temp_model = ListAuthorizationsResponseBodyAuthorizations()
                self.authorizations.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAuthorizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAuthorizationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAuthorizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableTerraformVersionsRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['keyWord'] = self.key_word
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyWord') is not None:
            self.key_word = m.get('keyWord')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAvailableTerraformVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        verison_list: List[str] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.verison_list = verison_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.verison_list is not None:
            result['verisonList'] = self.verison_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('verisonList') is not None:
            self.verison_list = m.get('verisonList')
        return self


class ListAvailableTerraformVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableTerraformVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAvailableTerraformVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExplorerTasksRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_result: str = None,
        module_id: str = None,
        next_token: str = None,
    ):
        self.keyword = keyword
        self.max_result = max_result
        self.module_id = module_id
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_result is not None:
            result['maxResult'] = self.max_result
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResult') is not None:
            self.max_result = m.get('maxResult')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListExplorerTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        current_job_status: str = None,
        deletion_protection: bool = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.auto_apply = auto_apply
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.current_job_status = current_job_status
        self.deletion_protection = deletion_protection
        self.module_id = module_id
        self.module_name = module_name
        self.module_version = module_version
        self.name = name
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListExplorerTasksResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tasks: List[ListExplorerTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListExplorerTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListExplorerTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExplorerTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExplorerTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRequestTag(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGroupRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: str = None,
        tag: List[ListGroupRequestTag] = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
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
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: str = None,
        tag_shrink: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListGroupResponseBodyGroupsTags(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGroupResponseBodyGroups(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        is_default: bool = None,
        module_cnt: int = None,
        name: str = None,
        project_id: str = None,
        scene_testing_task_cnt: int = None,
        tags: List[ListGroupResponseBodyGroupsTags] = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.is_default = is_default
        self.module_cnt = module_cnt
        self.name = name
        self.project_id = project_id
        self.scene_testing_task_cnt = scene_testing_task_cnt
        self.tags = tags
        self.task_cnt = task_cnt

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.module_cnt is not None:
            result['moduleCnt'] = self.module_cnt
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.scene_testing_task_cnt is not None:
            result['sceneTestingTaskCnt'] = self.scene_testing_task_cnt
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('moduleCnt') is not None:
            self.module_cnt = m.get('moduleCnt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('sceneTestingTaskCnt') is not None:
            self.scene_testing_task_cnt = m.get('sceneTestingTaskCnt')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListGroupResponseBodyGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class ListGroupResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        groups: List[ListGroupResponseBodyGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.count = count
        self.groups = groups
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

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
        if self.count is not None:
            result['count'] = self.count
        result['groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.groups = []
        if m.get('groups') is not None:
            for k in m.get('groups'):
                temp_model = ListGroupResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        task_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class ListJobsResponseBodyJobsConfig(TeaModel):
    def __init__(
        self,
        is_destroy: bool = None,
        module_version: str = None,
        resources_changed: str = None,
        sub_command: str = None,
    ):
        self.is_destroy = is_destroy
        self.module_version = module_version
        self.resources_changed = resources_changed
        self.sub_command = sub_command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        config: ListJobsResponseBodyJobsConfig = None,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        execute_type: str = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        status: str = None,
        status_detail: Dict[str, JobsStatusDetailValue] = None,
        task_id: str = None,
        terraform_provider_version: str = None,
    ):
        self.config = config
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.execute_type = execute_type
        self.is_pass_assert_check = is_pass_assert_check
        self.job_id = job_id
        self.status = status
        self.status_detail = status_detail
        self.task_id = task_id
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v in self.status_detail.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.execute_type is not None:
            result['executeType'] = self.execute_type
        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.status is not None:
            result['status'] = self.status
        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k, v in self.status_detail.items():
                result['statusDetail'][k] = v.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = ListJobsResponseBodyJobsConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')
        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k, v in m.get('statusDetail').items():
                temp_model = JobsStatusDetailValue()
                self.status_detail[k] = temp_model.from_map(v)
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.jobs = jobs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleVersionRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListModuleVersionResponseBodyVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        source_path: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        return self


class ListModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[ListModuleVersionResponseBodyVersions] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListModuleVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesRequestTag(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListModulesRequest(TeaModel):
    def __init__(
        self,
        exclude_module_ids: List[str] = None,
        group_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        tag: List[ListModulesRequestTag] = None,
    ):
        self.exclude_module_ids = exclude_module_ids
        self.group_id = group_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
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
        if self.exclude_module_ids is not None:
            result['excludeModuleIds'] = self.exclude_module_ids
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('excludeModuleIds') is not None:
            self.exclude_module_ids = m.get('excludeModuleIds')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListModulesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListModulesShrinkRequest(TeaModel):
    def __init__(
        self,
        exclude_module_ids_shrink: str = None,
        group_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        tag_shrink: str = None,
    ):
        self.exclude_module_ids_shrink = exclude_module_ids_shrink
        self.group_id = group_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_module_ids_shrink is not None:
            result['excludeModuleIds'] = self.exclude_module_ids_shrink
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('excludeModuleIds') is not None:
            self.exclude_module_ids_shrink = m.get('excludeModuleIds')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListModulesResponseBodyModulesGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ListModulesResponseBodyModulesTags(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListModulesResponseBodyModules(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        group_info: ListModulesResponseBodyModulesGroupInfo = None,
        latest_version: str = None,
        meta: Dict[str, Any] = None,
        module_id: str = None,
        name: str = None,
        source: str = None,
        source_config: Dict[str, Any] = None,
        status: str = None,
        tags: List[ListModulesResponseBodyModulesTags] = None,
    ):
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.description = description
        self.group_info = group_info
        self.latest_version = latest_version
        self.meta = meta
        self.module_id = module_id
        self.name = name
        self.source = source
        self.source_config = source_config
        self.status = status
        self.tags = tags

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.meta is not None:
            result['meta'] = self.meta
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_config is not None:
            result['sourceConfig'] = self.source_config
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = ListModulesResponseBodyModulesGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceConfig') is not None:
            self.source_config = m.get('sourceConfig')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListModulesResponseBodyModulesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListModulesResponseBody(TeaModel):
    def __init__(
        self,
        modules: List[ListModulesResponseBodyModules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.modules = modules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListModulesResponseBodyModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterSetRelationRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListParameterSetRelationResponseBodyParameterSets(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        parameter_set_id: str = None,
        parameters: Dict[str, str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.parameter_set_id = parameter_set_id
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class ListParameterSetRelationResponseBody(TeaModel):
    def __init__(
        self,
        parameter_sets: List[ListParameterSetRelationResponseBodyParameterSets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.parameter_sets = parameter_sets
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.parameter_sets:
            for k in self.parameter_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['parameterSets'] = []
        if self.parameter_sets is not None:
            for k in self.parameter_sets:
                result['parameterSets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_sets = []
        if m.get('parameterSets') is not None:
            for k in m.get('parameterSets'):
                temp_model = ListParameterSetRelationResponseBodyParameterSets()
                self.parameter_sets.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListParameterSetRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParameterSetRelationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListParameterSetRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterSetsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListParameterSetsResponseBodyParameterSetsParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListParameterSetsResponseBodyParameterSetsRelationList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.create_time = create_time
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListParameterSetsResponseBodyParameterSets(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        name: str = None,
        parameter_set_id: str = None,
        parameters: List[ListParameterSetsResponseBodyParameterSetsParameters] = None,
        relation_list: List[ListParameterSetsResponseBodyParameterSetsRelationList] = None,
    ):
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.description = description
        self.name = name
        self.parameter_set_id = parameter_set_id
        self.parameters = parameters
        self.relation_list = relation_list

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        result['relationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['relationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = ListParameterSetsResponseBodyParameterSetsParameters()
                self.parameters.append(temp_model.from_map(k))
        self.relation_list = []
        if m.get('relationList') is not None:
            for k in m.get('relationList'):
                temp_model = ListParameterSetsResponseBodyParameterSetsRelationList()
                self.relation_list.append(temp_model.from_map(k))
        return self


class ListParameterSetsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parameter_sets: List[ListParameterSetsResponseBodyParameterSets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.parameter_sets = parameter_sets
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.parameter_sets:
            for k in self.parameter_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['parameterSets'] = []
        if self.parameter_sets is not None:
            for k in self.parameter_sets:
                result['parameterSets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.parameter_sets = []
        if m.get('parameterSets') is not None:
            for k in m.get('parameterSets'):
                temp_model = ListParameterSetsResponseBodyParameterSets()
                self.parameter_sets.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListParameterSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParameterSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListParameterSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequestTag(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProjectRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        tag: List[ListProjectRequestTag] = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
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
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListProjectRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        tag_shrink: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListProjectResponseBodyProjectsTags(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProjectResponseBodyProjects(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        tags: List[ListProjectResponseBodyProjectsTags] = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.project_id = project_id
        self.tags = tags
        self.task_cnt = task_cnt

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListProjectResponseBodyProjectsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        projects: List[ListProjectResponseBodyProjects] = None,
        request_id: str = None,
    ):
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.projects = projects
        self.request_id = request_id

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectBuildsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        page_number: str = None,
        page_size: str = None,
        project_build_action: str = None,
    ):
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.project_build_action = project_build_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_build_action is not None:
            result['projectBuildAction'] = self.project_build_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectBuildAction') is not None:
            self.project_build_action = m.get('projectBuildAction')
        return self


class ListProjectBuildsResponseBodyProjectBuilds(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        project_build_action: str = None,
        project_build_id: str = None,
        project_build_index: int = None,
        project_id: str = None,
        status: str = None,
        terraform_provider_version: str = None,
        timestamp: int = None,
        trigger_strategy: str = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.project_build_action = project_build_action
        self.project_build_id = project_build_id
        self.project_build_index = project_build_index
        self.project_id = project_id
        self.status = status
        self.terraform_provider_version = terraform_provider_version
        self.timestamp = timestamp
        self.trigger_strategy = trigger_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.project_build_action is not None:
            result['projectBuildAction'] = self.project_build_action
        if self.project_build_id is not None:
            result['projectBuildId'] = self.project_build_id
        if self.project_build_index is not None:
            result['projectBuildIndex'] = self.project_build_index
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('projectBuildAction') is not None:
            self.project_build_action = m.get('projectBuildAction')
        if m.get('projectBuildId') is not None:
            self.project_build_id = m.get('projectBuildId')
        if m.get('projectBuildIndex') is not None:
            self.project_build_index = m.get('projectBuildIndex')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class ListProjectBuildsResponseBody(TeaModel):
    def __init__(
        self,
        project_builds: List[ListProjectBuildsResponseBodyProjectBuilds] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.project_builds = project_builds
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.project_builds:
            for k in self.project_builds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProjectBuilds'] = []
        if self.project_builds is not None:
            for k in self.project_builds:
                result['ProjectBuilds'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project_builds = []
        if m.get('ProjectBuilds') is not None:
            for k in m.get('ProjectBuilds'):
                temp_model = ListProjectBuildsResponseBodyProjectBuilds()
                self.project_builds.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProjectBuildsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectBuildsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectBuildsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRabbitmqPublishersRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRabbitmqPublishersResponseBodyAuthorizations(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        exchange_name: str = None,
        exchange_type: str = None,
        host_name: str = None,
        name: str = None,
        port: int = None,
        publisher_id: str = None,
        user_name: str = None,
        virtual_host: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.host_name = host_name
        self.name = name
        self.port = port
        self.publisher_id = publisher_id
        self.user_name = user_name
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.publisher_id is not None:
            result['publisherId'] = self.publisher_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.virtual_host is not None:
            result['virtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('publisherId') is not None:
            self.publisher_id = m.get('publisherId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('virtualHost') is not None:
            self.virtual_host = m.get('virtualHost')
        return self


class ListRabbitmqPublishersResponseBody(TeaModel):
    def __init__(
        self,
        authorizations: List[ListRabbitmqPublishersResponseBodyAuthorizations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorizations = authorizations
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorizations:
            for k in self.authorizations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['authorizations'] = []
        if self.authorizations is not None:
            for k in self.authorizations:
                result['authorizations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorizations = []
        if m.get('authorizations') is not None:
            for k in m.get('authorizations'):
                temp_model = ListRabbitmqPublishersResponseBodyAuthorizations()
                self.authorizations.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRabbitmqPublishersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRabbitmqPublishersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRabbitmqPublishersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRamPolicyExportTaskVersionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListRamPolicyExportTaskVersionsResponseBodyRamPolicyExportTaskVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        elapsed_time: int = None,
        export_version: str = None,
        module_id: str = None,
        module_version: str = None,
        ram_policy_export_task_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.elapsed_time = elapsed_time
        self.export_version = export_version
        self.module_id = module_id
        self.module_version = module_version
        self.ram_policy_export_task_id = ram_policy_export_task_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.ram_policy_export_task_id is not None:
            result['ramPolicyExportTaskId'] = self.ram_policy_export_task_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('ramPolicyExportTaskId') is not None:
            self.ram_policy_export_task_id = m.get('ramPolicyExportTaskId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListRamPolicyExportTaskVersionsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        ram_policy_export_task_versions: List[ListRamPolicyExportTaskVersionsResponseBodyRamPolicyExportTaskVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.ram_policy_export_task_versions = ram_policy_export_task_versions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ram_policy_export_task_versions:
            for k in self.ram_policy_export_task_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['ramPolicyExportTaskVersions'] = []
        if self.ram_policy_export_task_versions is not None:
            for k in self.ram_policy_export_task_versions:
                result['ramPolicyExportTaskVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.ram_policy_export_task_versions = []
        if m.get('ramPolicyExportTaskVersions') is not None:
            for k in m.get('ramPolicyExportTaskVersions'):
                temp_model = ListRamPolicyExportTaskVersionsResponseBodyRamPolicyExportTaskVersions()
                self.ram_policy_export_task_versions.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRamPolicyExportTaskVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRamPolicyExportTaskVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRamPolicyExportTaskVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRamPolicyExportTasksRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        module_id: str = None,
        module_version: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.module_id = module_id
        self.module_version = module_version
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRamPolicyExportTasksResponseBodyRamPolicyExportTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        current_policy_status: str = None,
        current_policy_version: str = None,
        elapsed_time: int = None,
        export_time: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        ram_policy_export_task_id: str = None,
        status: str = None,
        task_output_path: str = None,
    ):
        self.create_time = create_time
        self.current_policy_status = current_policy_status
        self.current_policy_version = current_policy_version
        self.elapsed_time = elapsed_time
        self.export_time = export_time
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.ram_policy_export_task_id = ram_policy_export_task_id
        self.status = status
        self.task_output_path = task_output_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_policy_status is not None:
            result['currentPolicyStatus'] = self.current_policy_status
        if self.current_policy_version is not None:
            result['currentPolicyVersion'] = self.current_policy_version
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.export_time is not None:
            result['exportTime'] = self.export_time
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.ram_policy_export_task_id is not None:
            result['ramPolicyExportTaskId'] = self.ram_policy_export_task_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentPolicyStatus') is not None:
            self.current_policy_status = m.get('currentPolicyStatus')
        if m.get('currentPolicyVersion') is not None:
            self.current_policy_version = m.get('currentPolicyVersion')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('exportTime') is not None:
            self.export_time = m.get('exportTime')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramPolicyExportTaskId') is not None:
            self.ram_policy_export_task_id = m.get('ramPolicyExportTaskId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        return self


class ListRamPolicyExportTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        ram_policy_export_tasks: List[ListRamPolicyExportTasksResponseBodyRamPolicyExportTasks] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.ram_policy_export_tasks = ram_policy_export_tasks
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ram_policy_export_tasks:
            for k in self.ram_policy_export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['ramPolicyExportTasks'] = []
        if self.ram_policy_export_tasks is not None:
            for k in self.ram_policy_export_tasks:
                result['ramPolicyExportTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.ram_policy_export_tasks = []
        if m.get('ramPolicyExportTasks') is not None:
            for k in m.get('ramPolicyExportTasks'):
                temp_model = ListRamPolicyExportTasksResponseBodyRamPolicyExportTasks()
                self.ram_policy_export_tasks.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRamPolicyExportTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRamPolicyExportTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRamPolicyExportTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExportTaskVersionsRequest(TeaModel):
    def __init__(
        self,
        export_version: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.export_version = export_version
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksModules(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        exclude_rules: List[ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules] = None,
        export_task_id: str = None,
        export_to_module: ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule = None,
        export_version: str = None,
        failed_reason: str = None,
        has_destroy: bool = None,
        include_rules: List[ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules] = None,
        modules: List[ListResourceExportTaskVersionsResponseBodyExportTasksModules] = None,
        name: str = None,
        status: str = None,
        variables: List[ListResourceExportTaskVersionsResponseBodyExportTasksVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.exclude_rules = exclude_rules
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.failed_reason = failed_reason
        self.has_destroy = has_destroy
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.status = status
        self.variables = variables

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        if self.has_destroy is not None:
            result['hasDestroy'] = self.has_destroy
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        if m.get('hasDestroy') is not None:
            self.has_destroy = m.get('hasDestroy')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListResourceExportTaskVersionsResponseBody(TeaModel):
    def __init__(
        self,
        export_tasks: List[ListResourceExportTaskVersionsResponseBodyExportTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.export_tasks = export_tasks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.export_tasks:
            for k in self.export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k in self.export_tasks:
                result['exportTasks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k in m.get('exportTasks'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceExportTaskVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceExportTaskVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceExportTaskVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExportTasksRequest(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.export_task_id = export_task_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListResourceExportTasksResponseBodyExportTasksExcludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTasksResponseBodyExportTasksExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class ListResourceExportTasksResponseBodyExportTasksIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTasksResponseBodyExportTasksModules(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListResourceExportTasksResponseBodyExportTasksVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceExportTasksResponseBodyExportTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        exclude_rules: List[ListResourceExportTasksResponseBodyExportTasksExcludeRules] = None,
        export_status: str = None,
        export_task_id: str = None,
        export_to_module: ListResourceExportTasksResponseBodyExportTasksExportToModule = None,
        export_version: str = None,
        has_destroy: bool = None,
        include_rules: List[ListResourceExportTasksResponseBodyExportTasksIncludeRules] = None,
        modules: List[ListResourceExportTasksResponseBodyExportTasksModules] = None,
        name: str = None,
        status: str = None,
        variables: List[ListResourceExportTasksResponseBodyExportTasksVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.exclude_rules = exclude_rules
        self.export_status = export_status
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.has_destroy = has_destroy
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.status = status
        self.variables = variables

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_status is not None:
            result['exportStatus'] = self.export_status
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.has_destroy is not None:
            result['hasDestroy'] = self.has_destroy
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportStatus') is not None:
            self.export_status = m.get('exportStatus')
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = ListResourceExportTasksResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('hasDestroy') is not None:
            self.has_destroy = m.get('hasDestroy')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListResourceExportTasksResponseBody(TeaModel):
    def __init__(
        self,
        export_tasks: List[ListResourceExportTasksResponseBodyExportTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.export_tasks = export_tasks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.export_tasks:
            for k in self.export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k in self.export_tasks:
                result['exportTasks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k in m.get('exportTasks'):
                temp_model = ListResourceExportTasksResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceExportTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceExportTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceExportTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        source_type: str = None,
        source_value: str = None,
        spec_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.source_value = source_value
        # This parameter is required.
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.source_value is not None:
            result['sourceValue'] = self.source_value
        if self.spec_type is not None:
            result['specType'] = self.spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('sourceValue') is not None:
            self.source_value = m.get('sourceValue')
        if m.get('specType') is not None:
            self.spec_type = m.get('specType')
        return self


class ListResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        depends_on_resource_ids: List[str] = None,
        product_code: str = None,
        properties: Dict[str, Any] = None,
        property_variables: Dict[str, Any] = None,
        region_id: str = None,
        resource_arn: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[ListResourcesResponseBodyResourcesTags] = None,
        terraform_arn: str = None,
        terraform_code: str = None,
        zone_id: str = None,
    ):
        self.account_id = account_id
        self.create_time = create_time
        self.depends_on_resource_ids = depends_on_resource_ids
        self.product_code = product_code
        self.properties = properties
        self.property_variables = property_variables
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.status = status
        self.tags = tags
        self.terraform_arn = terraform_arn
        self.terraform_code = terraform_code
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.depends_on_resource_ids is not None:
            result['dependsOnResourceIds'] = self.depends_on_resource_ids
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.properties is not None:
            result['properties'] = self.properties
        if self.property_variables is not None:
            result['propertyVariables'] = self.property_variables
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.terraform_arn is not None:
            result['terraformArn'] = self.terraform_arn
        if self.terraform_code is not None:
            result['terraformCode'] = self.terraform_code
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dependsOnResourceIds') is not None:
            self.depends_on_resource_ids = m.get('dependsOnResourceIds')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('propertyVariables') is not None:
            self.property_variables = m.get('propertyVariables')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('terraformArn') is not None:
            self.terraform_arn = m.get('terraformArn')
        if m.get('terraformCode') is not None:
            self.terraform_code = m.get('terraformCode')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        resources: List[ListResourcesResponseBodyResources] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.resources = resources
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequestTag(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        exclude_task_ids: List[str] = None,
        group_id: str = None,
        keyword: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        tag: List[ListTasksRequestTag] = None,
        task_id: str = None,
    ):
        self.exclude_task_ids = exclude_task_ids
        self.group_id = group_id
        self.keyword = keyword
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.status = status
        self.tag = tag
        self.task_id = task_id

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
        if self.exclude_task_ids is not None:
            result['excludeTaskIds'] = self.exclude_task_ids
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('excludeTaskIds') is not None:
            self.exclude_task_ids = m.get('excludeTaskIds')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListTasksRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        exclude_task_ids_shrink: str = None,
        group_id: str = None,
        keyword: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        tag_shrink: str = None,
        task_id: str = None,
    ):
        self.exclude_task_ids_shrink = exclude_task_ids_shrink
        self.group_id = group_id
        self.keyword = keyword
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.status = status
        self.tag_shrink = tag_shrink
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_task_ids_shrink is not None:
            result['excludeTaskIds'] = self.exclude_task_ids_shrink
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('excludeTaskIds') is not None:
            self.exclude_task_ids_shrink = m.get('excludeTaskIds')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBodyTasksGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ListTasksResponseBodyTasksTags(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        current_job_status: str = None,
        deletion_protection: bool = None,
        group_info: ListTasksResponseBodyTasksGroupInfo = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        status: str = None,
        tags: List[ListTasksResponseBodyTasksTags] = None,
        task_id: str = None,
    ):
        self.auto_apply = auto_apply
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.current_job_status = current_job_status
        self.deletion_protection = deletion_protection
        self.group_info = group_info
        self.module_id = module_id
        self.module_name = module_name
        self.module_version = module_version
        self.name = name
        self.status = status
        self.tags = tags
        self.task_id = task_id

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('groupInfo') is not None:
            temp_model = ListTasksResponseBodyTasksGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListTasksResponseBodyTasksTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTerraformProviderVersionsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        usage: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.usage is not None:
            result['usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        return self


class ListTerraformProviderVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        published_time: str = None,
        status: str = None,
        version: str = None,
    ):
        self.published_time = published_time
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.published_time is not None:
            result['publishedTime'] = self.published_time
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListTerraformProviderVersionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        verison_list: List[str] = None,
        versions: List[ListTerraformProviderVersionsResponseBodyVersions] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.verison_list = verison_list
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.verison_list is not None:
            result['verisonList'] = self.verison_list
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('verisonList') is not None:
            self.verison_list = m.get('verisonList')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListTerraformProviderVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListTerraformProviderVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTerraformProviderVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTerraformProviderVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateJobRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.comment = comment
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class OperateJobResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OperateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveResourceExportTaskVersionResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveResourceExportTaskVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveResourceExportTaskVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveResourceExportTaskVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTags(TeaModel):
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
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[TagResourcesRequestTags] = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.resource_ids = resource_ids
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = TagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class UpdateAuthorizationAttributeRequest(TeaModel):
    def __init__(
        self,
        due_time: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.due_time = due_time
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateAuthorizationAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateAuthorizationAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAuthorizationAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAuthorizationAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExplorerTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        explorer_task_name: str = None,
        module_id: str = None,
        module_version: str = None,
        terraform_provider_version: str = None,
    ):
        self.auto_apply = auto_apply
        self.explorer_task_name = explorer_task_name
        self.module_id = module_id
        self.module_version = module_version
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.explorer_task_name is not None:
            result['explorerTaskName'] = self.explorer_task_name
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('explorerTaskName') is not None:
            self.explorer_task_name = m.get('explorerTaskName')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class UpdateExplorerTaskAttributeResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateExplorerTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExplorerTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExplorerTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequestNotifyConfig(TeaModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        return self


class UpdateGroupRequestTriggerConfig(TeaModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        client_token: str = None,
        description: str = None,
        forced_setting: bool = None,
        name: str = None,
        notify_config: List[UpdateGroupRequestNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        terraform_provider_version: str = None,
        trigger_config: List[UpdateGroupRequestTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.forced_setting = forced_setting
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for k in self.notify_config:
                if k:
                    k.validate()
        if self.trigger_config:
            for k in self.trigger_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting
        if self.name is not None:
            result['name'] = self.name
        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k in self.notify_config:
                result['notifyConfig'].append(k.to_map() if k else None)
        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field
        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k in self.trigger_config:
                result['triggerConfig'].append(k.to_map() if k else None)
        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k in m.get('notifyConfig'):
                temp_model = UpdateGroupRequestNotifyConfig()
                self.notify_config.append(temp_model.from_map(k))
        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')
        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k in m.get('triggerConfig'):
                temp_model = UpdateGroupRequestTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k))
        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')
        return self


class UpdateGroupResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModuleAttributeRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class UpdateModuleAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_info: UpdateModuleAttributeRequestGroupInfo = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        version_strategy: str = None,
    ):
        self.description = description
        self.group_info = group_info
        self.name = name
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.version_strategy = version_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = UpdateModuleAttributeRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class UpdateModuleAttributeResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateModuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModuleAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParameterSetAttributeRequestParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateParameterSetAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: List[UpdateParameterSetAttributeRequestParameters] = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
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
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = UpdateParameterSetAttributeRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class UpdateParameterSetAttributeResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateParameterSetAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateParameterSetAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateParameterSetAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateProjectResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRabbitmqPublisherAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        exchange_name: str = None,
        exchange_type: str = None,
        name: str = None,
    ):
        self.description = description
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
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
            result['description'] = self.description
        if self.exchange_name is not None:
            result['exchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['exchangeType'] = self.exchange_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exchangeName') is not None:
            self.exchange_name = m.get('exchangeName')
        if m.get('exchangeType') is not None:
            self.exchange_type = m.get('exchangeType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateRabbitmqPublisherAttributeResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateRabbitmqPublisherAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRabbitmqPublisherAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRabbitmqPublisherAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRamPolicyExportTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        authorization_account_ids: List[int] = None,
        authorization_actions: List[str] = None,
        authorization_region_ids: List[str] = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        ram_role: str = None,
        trigger_strategy: str = None,
    ):
        self.authorization_account_ids = authorization_account_ids
        self.authorization_actions = authorization_actions
        self.authorization_region_ids = authorization_region_ids
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.ram_role = ram_role
        self.trigger_strategy = trigger_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_account_ids is not None:
            result['authorizationAccountIds'] = self.authorization_account_ids
        if self.authorization_actions is not None:
            result['authorizationActions'] = self.authorization_actions
        if self.authorization_region_ids is not None:
            result['authorizationRegionIds'] = self.authorization_region_ids
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationAccountIds') is not None:
            self.authorization_account_ids = m.get('authorizationAccountIds')
        if m.get('authorizationActions') is not None:
            self.authorization_actions = m.get('authorizationActions')
        if m.get('authorizationRegionIds') is not None:
            self.authorization_region_ids = m.get('authorizationRegionIds')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class UpdateRamPolicyExportTaskAttributeResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateRamPolicyExportTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRamPolicyExportTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRamPolicyExportTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceExportTaskAttributeRequestExcludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateResourceExportTaskAttributeRequestExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class UpdateResourceExportTaskAttributeRequestIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateResourceExportTaskAttributeRequestVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class UpdateResourceExportTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_path: str = None,
        description: str = None,
        exclude_rules: List[UpdateResourceExportTaskAttributeRequestExcludeRules] = None,
        export_to_module: UpdateResourceExportTaskAttributeRequestExportToModule = None,
        include_rules: List[UpdateResourceExportTaskAttributeRequestIncludeRules] = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[UpdateResourceExportTaskAttributeRequestVariables] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.config_path = config_path
        self.description = description
        self.exclude_rules = exclude_rules
        self.export_to_module = export_to_module
        self.include_rules = include_rules
        # This parameter is required.
        self.name = name
        self.ram_role = ram_role
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.variables = variables

    def validate(self):
        if self.exclude_rules:
            for k in self.exclude_rules:
                if k:
                    k.validate()
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.config_path is not None:
            result['configPath'] = self.config_path
        if self.description is not None:
            result['description'] = self.description
        result['excludeRules'] = []
        if self.exclude_rules is not None:
            for k in self.exclude_rules:
                result['excludeRules'].append(k.to_map() if k else None)
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('configPath') is not None:
            self.config_path = m.get('configPath')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.exclude_rules = []
        if m.get('excludeRules') is not None:
            for k in m.get('excludeRules'):
                temp_model = UpdateResourceExportTaskAttributeRequestExcludeRules()
                self.exclude_rules.append(temp_model.from_map(k))
        if m.get('exportToModule') is not None:
            temp_model = UpdateResourceExportTaskAttributeRequestExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = UpdateResourceExportTaskAttributeRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = UpdateResourceExportTaskAttributeRequestVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class UpdateResourceExportTaskAttributeResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateResourceExportTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceExportTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceExportTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskAttributeRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class UpdateTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        description: str = None,
        group_info: UpdateTaskAttributeRequestGroupInfo = None,
        init_module_state: bool = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        parameters: Dict[str, str] = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        # This parameter is required.
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.parameters = parameters
        self.protection_strategy = protection_strategy
        # This parameter is required.
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.terraform_version = terraform_version
        # This parameter is required.
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        if self.group_info:
            self.group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = UpdateTaskAttributeRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class UpdateTaskAttributeResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskPolicyRequestTaskPolicies(TeaModel):
    def __init__(
        self,
        priority: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.priority = priority
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['priority'] = self.priority
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateTaskPolicyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        task_policies: List[UpdateTaskPolicyRequestTaskPolicies] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.task_policies = task_policies

    def validate(self):
        if self.task_policies:
            for k in self.task_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        result['taskPolicies'] = []
        if self.task_policies is not None:
            for k in self.task_policies:
                result['taskPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        self.task_policies = []
        if m.get('taskPolicies') is not None:
            for k in m.get('taskPolicies'):
                temp_model = UpdateTaskPolicyRequestTaskPolicies()
                self.task_policies.append(temp_model.from_map(k))
        return self


class UpdateTaskPolicyResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateTaskPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTaskPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


