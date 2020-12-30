# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BatchInsertMembersRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        members: str = None,
        real_pk: str = None,
    ):
        self.org_id = org_id
        self.members = members
        self.real_pk = real_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.members is not None:
            result['Members'] = self.members
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class BatchInsertMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchInsertMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchInsertMembersResponseBody = None,
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
            temp_model = BatchInsertMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPipelineRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        flow_instance_id: int = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.flow_instance_id = flow_instance_id
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CancelPipelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelPipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelPipelineResponseBody = None,
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
            temp_model = CancelPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAliyunAccountExistsRequest(TeaModel):
    def __init__(
        self,
        user_pk: str = None,
    ):
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CheckAliyunAccountExistsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class CheckAliyunAccountExistsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckAliyunAccountExistsResponseBody = None,
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
            temp_model = CheckAliyunAccountExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCommonGroupRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        description: str = None,
        smart_group_id: str = None,
        name: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.description = description
        self.smart_group_id = smart_group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.description is not None:
            result['Description'] = self.description
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateCommonGroupResponseBodyObject(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateCommonGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: CreateCommonGroupResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = CreateCommonGroupResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class CreateCommonGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCommonGroupResponseBody = None,
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
            temp_model = CreateCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCredentialRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        name: str = None,
        user_name: str = None,
        password: str = None,
        type: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.name = name
        self.user_name = user_name
        self.password = password
        self.type = type
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.type is not None:
            result['Type'] = self.type
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CreateCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCredentialResponseBody = None,
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
            temp_model = CreateCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsOrganizationRequest(TeaModel):
    def __init__(
        self,
        org_name: str = None,
        source: str = None,
        real_pk: str = None,
        desired_member_count: int = None,
    ):
        self.org_name = org_name
        self.source = source
        self.real_pk = real_pk
        self.desired_member_count = desired_member_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.source is not None:
            result['Source'] = self.source
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        if self.desired_member_count is not None:
            result['DesiredMemberCount'] = self.desired_member_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        if m.get('DesiredMemberCount') is not None:
            self.desired_member_count = m.get('DesiredMemberCount')
        return self


class CreateDevopsOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDevopsOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevopsOrganizationResponseBody = None,
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
            temp_model = CreateDevopsOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsProjectRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.org_id = org_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateDevopsProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDevopsProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevopsProjectResponseBody = None,
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
            temp_model = CreateDevopsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsProjectSprintRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        name: str = None,
        description: str = None,
        project_id: str = None,
        executor_id: str = None,
        start_date: str = None,
        due_date: str = None,
    ):
        self.org_id = org_id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.executor_id = executor_id
        self.start_date = start_date
        self.due_date = due_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        return self


class CreateDevopsProjectSprintResponseBodyObjectPlanToDo(TeaModel):
    def __init__(
        self,
        tasks: int = None,
        work_times: int = None,
        story_points: int = None,
    ):
        self.tasks = tasks
        self.work_times = work_times
        self.story_points = story_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.story_points is not None:
            result['StoryPoints'] = self.story_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('StoryPoints') is not None:
            self.story_points = m.get('StoryPoints')
        return self


class CreateDevopsProjectSprintResponseBodyObject(TeaModel):
    def __init__(
        self,
        status: str = None,
        project_id: str = None,
        start_date: str = None,
        creator_id: str = None,
        executor: str = None,
        description: str = None,
        accomplished: str = None,
        is_deleted: bool = None,
        updated: str = None,
        due_date: str = None,
        name: str = None,
        created: str = None,
        plan_to_do: CreateDevopsProjectSprintResponseBodyObjectPlanToDo = None,
        id: str = None,
    ):
        self.status = status
        self.project_id = project_id
        self.start_date = start_date
        self.creator_id = creator_id
        self.executor = executor
        self.description = description
        self.accomplished = accomplished
        self.is_deleted = is_deleted
        self.updated = updated
        self.due_date = due_date
        self.name = name
        self.created = created
        self.plan_to_do = plan_to_do
        self.id = id

    def validate(self):
        if self.plan_to_do:
            self.plan_to_do.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.executor is not None:
            result['Executor'] = self.executor
        if self.description is not None:
            result['Description'] = self.description
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.plan_to_do is not None:
            result['PlanToDo'] = self.plan_to_do.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Executor') is not None:
            self.executor = m.get('Executor')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('PlanToDo') is not None:
            temp_model = CreateDevopsProjectSprintResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateDevopsProjectSprintResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: CreateDevopsProjectSprintResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = CreateDevopsProjectSprintResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class CreateDevopsProjectSprintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevopsProjectSprintResponseBody = None,
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
            temp_model = CreateDevopsProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsProjectTaskRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        content: str = None,
        project_id: str = None,
        executor_id: str = None,
        start_date: str = None,
        due_date: str = None,
        scenario_field_config_id: str = None,
        task_flow_status_id: str = None,
        note: str = None,
        priority: int = None,
        visible: str = None,
        parent_task_id: str = None,
        sprint_id: str = None,
        task_list_id: str = None,
    ):
        self.org_id = org_id
        self.content = content
        self.project_id = project_id
        self.executor_id = executor_id
        self.start_date = start_date
        self.due_date = due_date
        self.scenario_field_config_id = scenario_field_config_id
        self.task_flow_status_id = task_flow_status_id
        self.note = note
        self.priority = priority
        self.visible = visible
        self.parent_task_id = parent_task_id
        self.sprint_id = sprint_id
        self.task_list_id = task_list_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.content is not None:
            result['Content'] = self.content
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.scenario_field_config_id is not None:
            result['ScenarioFieldConfigId'] = self.scenario_field_config_id
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.note is not None:
            result['Note'] = self.note
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.task_list_id is not None:
            result['TaskListId'] = self.task_list_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('ScenarioFieldConfigId') is not None:
            self.scenario_field_config_id = m.get('ScenarioFieldConfigId')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('TaskListId') is not None:
            self.task_list_id = m.get('TaskListId')
        return self


class CreateDevopsProjectTaskResponseBodyObject(TeaModel):
    def __init__(
        self,
        executor_id: str = None,
        project_id: str = None,
        priority: int = None,
        scenario_field_config_id: str = None,
        ancestor_ids: str = None,
        task_type: str = None,
        tasklist_id: str = None,
        taskflowstatus_id: str = None,
        note: str = None,
        updated: str = None,
        unique_id: int = None,
        content: str = None,
        rating: int = None,
        pos: int = None,
        start_date: str = None,
        story_point: str = None,
        creator_id: str = None,
        source: str = None,
        organization_id: str = None,
        visible: str = None,
        is_done: bool = None,
        sprint_id: str = None,
        due_date: str = None,
        created: str = None,
        id: str = None,
    ):
        self.executor_id = executor_id
        self.project_id = project_id
        self.priority = priority
        self.scenario_field_config_id = scenario_field_config_id
        self.ancestor_ids = ancestor_ids
        self.task_type = task_type
        self.tasklist_id = tasklist_id
        self.taskflowstatus_id = taskflowstatus_id
        self.note = note
        self.updated = updated
        self.unique_id = unique_id
        self.content = content
        self.rating = rating
        self.pos = pos
        self.start_date = start_date
        self.story_point = story_point
        self.creator_id = creator_id
        self.source = source
        self.organization_id = organization_id
        self.visible = visible
        self.is_done = is_done
        self.sprint_id = sprint_id
        self.due_date = due_date
        self.created = created
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.scenario_field_config_id is not None:
            result['ScenarioFieldConfigId'] = self.scenario_field_config_id
        if self.ancestor_ids is not None:
            result['AncestorIds'] = self.ancestor_ids
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.tasklist_id is not None:
            result['TasklistId'] = self.tasklist_id
        if self.taskflowstatus_id is not None:
            result['TaskflowstatusId'] = self.taskflowstatus_id
        if self.note is not None:
            result['Note'] = self.note
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.content is not None:
            result['Content'] = self.content
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source is not None:
            result['Source'] = self.source
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.created is not None:
            result['Created'] = self.created
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScenarioFieldConfigId') is not None:
            self.scenario_field_config_id = m.get('ScenarioFieldConfigId')
        if m.get('AncestorIds') is not None:
            self.ancestor_ids = m.get('AncestorIds')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TasklistId') is not None:
            self.tasklist_id = m.get('TasklistId')
        if m.get('TaskflowstatusId') is not None:
            self.taskflowstatus_id = m.get('TaskflowstatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateDevopsProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: CreateDevopsProjectTaskResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = CreateDevopsProjectTaskResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class CreateDevopsProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevopsProjectTaskResponseBody = None,
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
            temp_model = CreateDevopsProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelineRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline = pipeline
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline is not None:
            result['Pipeline'] = self.pipeline
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Pipeline') is not None:
            self.pipeline = m.get('Pipeline')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class CreatePipelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePipelineResponseBody = None,
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
            temp_model = CreatePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceConnectionRequest(TeaModel):
    def __init__(
        self,
        service_connection_type: str = None,
        user_pk: str = None,
        org_id: str = None,
    ):
        self.service_connection_type = service_connection_type
        self.user_pk = user_pk
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_connection_type is not None:
            result['ServiceConnectionType'] = self.service_connection_type
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceConnectionType') is not None:
            self.service_connection_type = m.get('ServiceConnectionType')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class CreateServiceConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateServiceConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceConnectionResponseBody = None,
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
            temp_model = CreateServiceConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommonGroupRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        common_group_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.common_group_id = common_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.common_group_id is not None:
            result['CommonGroupId'] = self.common_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CommonGroupId') is not None:
            self.common_group_id = m.get('CommonGroupId')
        return self


class DeleteCommonGroupResponseBodyObject(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteCommonGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: DeleteCommonGroupResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = DeleteCommonGroupResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class DeleteCommonGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCommonGroupResponseBody = None,
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
            temp_model = DeleteCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsOrganizationMembersRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        user_id: str = None,
        real_pk: str = None,
    ):
        self.org_id = org_id
        self.user_id = user_id
        self.real_pk = real_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class DeleteDevopsOrganizationMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDevopsOrganizationMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevopsOrganizationMembersResponseBody = None,
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
            temp_model = DeleteDevopsOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteDevopsProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDevopsProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevopsProjectResponseBody = None,
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
            temp_model = DeleteDevopsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectMembersRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        user_ids: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class DeleteDevopsProjectMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class DeleteDevopsProjectMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevopsProjectMembersResponseBody = None,
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
            temp_model = DeleteDevopsProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectSprintRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        sprint_id: str = None,
    ):
        self.org_id = org_id
        self.sprint_id = sprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class DeleteDevopsProjectSprintResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class DeleteDevopsProjectSprintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevopsProjectSprintResponseBody = None,
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
            temp_model = DeleteDevopsProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevopsProjectTaskRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        task_id: str = None,
    ):
        self.org_id = org_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteDevopsProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class DeleteDevopsProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevopsProjectTaskResponseBody = None,
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
            temp_model = DeleteDevopsProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineMemberRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        user_id: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeletePipelineMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePipelineMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePipelineMemberResponseBody = None,
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
            temp_model = DeletePipelineMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecutePipelineRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        parameters: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.parameters = parameters
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ExecutePipelineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecutePipelineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecutePipelineResponseBody = None,
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
            temp_model = ExecutePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsOrganizationMembersRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
    ):
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        return self


class GetDevopsOrganizationMembersResponseBodyObject(TeaModel):
    def __init__(
        self,
        email: str = None,
        avatar_url: str = None,
        user_id: str = None,
        member_id: str = None,
        role: int = None,
        name: str = None,
        phone: str = None,
    ):
        self.email = email
        self.avatar_url = avatar_url
        self.user_id = user_id
        self.member_id = member_id
        self.role = role
        self.name = name
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetDevopsOrganizationMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[GetDevopsOrganizationMembersResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetDevopsOrganizationMembersResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetDevopsOrganizationMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevopsOrganizationMembersResponseBody = None,
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
            temp_model = GetDevopsOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectInfoRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetDevopsProjectInfoResponseBodyObject(TeaModel):
    def __init__(
        self,
        sort_method: str = None,
        unique_id_prefix: str = None,
        normal_type: str = None,
        modifier_id: str = None,
        source_type: str = None,
        is_template: bool = None,
        description: str = None,
        default_role_id: str = None,
        root_collection_id: str = None,
        is_deleted: bool = None,
        updated: str = None,
        is_archived: bool = None,
        name: str = None,
        end_date: str = None,
        logo: str = None,
        start_date: str = None,
        pinyin: str = None,
        creator_id: str = None,
        source_id: str = None,
        organization_id: str = None,
        is_suspended: bool = None,
        default_collection_id: str = None,
        visibility: str = None,
        py: str = None,
        category: str = None,
        next_task_unique_id: int = None,
        customfields: str = None,
        created: str = None,
        id: str = None,
    ):
        self.sort_method = sort_method
        self.unique_id_prefix = unique_id_prefix
        self.normal_type = normal_type
        self.modifier_id = modifier_id
        self.source_type = source_type
        self.is_template = is_template
        self.description = description
        self.default_role_id = default_role_id
        self.root_collection_id = root_collection_id
        self.is_deleted = is_deleted
        self.updated = updated
        self.is_archived = is_archived
        self.name = name
        self.end_date = end_date
        self.logo = logo
        self.start_date = start_date
        self.pinyin = pinyin
        self.creator_id = creator_id
        self.source_id = source_id
        self.organization_id = organization_id
        self.is_suspended = is_suspended
        self.default_collection_id = default_collection_id
        self.visibility = visibility
        self.py = py
        self.category = category
        self.next_task_unique_id = next_task_unique_id
        self.customfields = customfields
        self.created = created
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sort_method is not None:
            result['SortMethod'] = self.sort_method
        if self.unique_id_prefix is not None:
            result['UniqueIdPrefix'] = self.unique_id_prefix
        if self.normal_type is not None:
            result['NormalType'] = self.normal_type
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.description is not None:
            result['Description'] = self.description
        if self.default_role_id is not None:
            result['DefaultRoleId'] = self.default_role_id
        if self.root_collection_id is not None:
            result['RootCollectionId'] = self.root_collection_id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.name is not None:
            result['Name'] = self.name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.is_suspended is not None:
            result['IsSuspended'] = self.is_suspended
        if self.default_collection_id is not None:
            result['DefaultCollectionId'] = self.default_collection_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.py is not None:
            result['Py'] = self.py
        if self.category is not None:
            result['Category'] = self.category
        if self.next_task_unique_id is not None:
            result['NextTaskUniqueId'] = self.next_task_unique_id
        if self.customfields is not None:
            result['Customfields'] = self.customfields
        if self.created is not None:
            result['Created'] = self.created
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SortMethod') is not None:
            self.sort_method = m.get('SortMethod')
        if m.get('UniqueIdPrefix') is not None:
            self.unique_id_prefix = m.get('UniqueIdPrefix')
        if m.get('NormalType') is not None:
            self.normal_type = m.get('NormalType')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DefaultRoleId') is not None:
            self.default_role_id = m.get('DefaultRoleId')
        if m.get('RootCollectionId') is not None:
            self.root_collection_id = m.get('RootCollectionId')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('IsSuspended') is not None:
            self.is_suspended = m.get('IsSuspended')
        if m.get('DefaultCollectionId') is not None:
            self.default_collection_id = m.get('DefaultCollectionId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('Py') is not None:
            self.py = m.get('Py')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('NextTaskUniqueId') is not None:
            self.next_task_unique_id = m.get('NextTaskUniqueId')
        if m.get('Customfields') is not None:
            self.customfields = m.get('Customfields')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDevopsProjectInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetDevopsProjectInfoResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = GetDevopsProjectInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetDevopsProjectInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevopsProjectInfoResponseBody = None,
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
            temp_model = GetDevopsProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectMembersRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetDevopsProjectMembersResponseBodyObject(TeaModel):
    def __init__(
        self,
        email: str = None,
        avatar_url: str = None,
        user_id: str = None,
        member_id: str = None,
        role: int = None,
        name: str = None,
        phone: str = None,
    ):
        self.email = email
        self.avatar_url = avatar_url
        self.user_id = user_id
        self.member_id = member_id
        self.role = role
        self.name = name
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.role is not None:
            result['Role'] = self.role
        if self.name is not None:
            result['Name'] = self.name
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetDevopsProjectMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[GetDevopsProjectMembersResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetDevopsProjectMembersResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetDevopsProjectMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevopsProjectMembersResponseBody = None,
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
            temp_model = GetDevopsProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectSprintInfoRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        sprint_id: str = None,
    ):
        self.org_id = org_id
        self.sprint_id = sprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo(TeaModel):
    def __init__(
        self,
        tasks: int = None,
        work_times: int = None,
        story_points: int = None,
    ):
        self.tasks = tasks
        self.work_times = work_times
        self.story_points = story_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.story_points is not None:
            result['StoryPoints'] = self.story_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('StoryPoints') is not None:
            self.story_points = m.get('StoryPoints')
        return self


class GetDevopsProjectSprintInfoResponseBodyObject(TeaModel):
    def __init__(
        self,
        status: str = None,
        project_id: str = None,
        start_date: str = None,
        creator_id: str = None,
        accomplished: str = None,
        is_deleted: bool = None,
        updated: str = None,
        due_date: str = None,
        name: str = None,
        created: str = None,
        plan_to_do: GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo = None,
        id: str = None,
    ):
        self.status = status
        self.project_id = project_id
        self.start_date = start_date
        self.creator_id = creator_id
        self.accomplished = accomplished
        self.is_deleted = is_deleted
        self.updated = updated
        self.due_date = due_date
        self.name = name
        self.created = created
        self.plan_to_do = plan_to_do
        self.id = id

    def validate(self):
        if self.plan_to_do:
            self.plan_to_do.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.plan_to_do is not None:
            result['PlanToDo'] = self.plan_to_do.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('PlanToDo') is not None:
            temp_model = GetDevopsProjectSprintInfoResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDevopsProjectSprintInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetDevopsProjectSprintInfoResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = GetDevopsProjectSprintInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetDevopsProjectSprintInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevopsProjectSprintInfoResponseBody = None,
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
            temp_model = GetDevopsProjectSprintInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevopsProjectTaskInfoRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        task_id: str = None,
    ):
        self.org_id = org_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDevopsProjectTaskInfoResponseBodyObject(TeaModel):
    def __init__(
        self,
        executor_id: str = None,
        project_id: str = None,
        story_point: str = None,
        start_date: str = None,
        is_top_in_project: bool = None,
        priority: str = None,
        creator_id: str = None,
        organization_id: str = None,
        task_type: str = None,
        tasklist_id: str = None,
        visible: str = None,
        is_done: bool = None,
        is_deleted: bool = None,
        taskflowstatus_id: str = None,
        note: str = None,
        sprint_id: str = None,
        updated: str = None,
        involve_members: List[str] = None,
        due_date: str = None,
        created: str = None,
        content: str = None,
        id: str = None,
    ):
        self.executor_id = executor_id
        self.project_id = project_id
        self.story_point = story_point
        self.start_date = start_date
        self.is_top_in_project = is_top_in_project
        self.priority = priority
        self.creator_id = creator_id
        self.organization_id = organization_id
        self.task_type = task_type
        self.tasklist_id = tasklist_id
        self.visible = visible
        self.is_done = is_done
        self.is_deleted = is_deleted
        self.taskflowstatus_id = taskflowstatus_id
        self.note = note
        self.sprint_id = sprint_id
        self.updated = updated
        self.involve_members = involve_members
        self.due_date = due_date
        self.created = created
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.is_top_in_project is not None:
            result['IsTopInProject'] = self.is_top_in_project
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.tasklist_id is not None:
            result['TasklistId'] = self.tasklist_id
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.taskflowstatus_id is not None:
            result['TaskflowstatusId'] = self.taskflowstatus_id
        if self.note is not None:
            result['Note'] = self.note
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.created is not None:
            result['Created'] = self.created
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('IsTopInProject') is not None:
            self.is_top_in_project = m.get('IsTopInProject')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TasklistId') is not None:
            self.tasklist_id = m.get('TasklistId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('TaskflowstatusId') is not None:
            self.taskflowstatus_id = m.get('TaskflowstatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDevopsProjectTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetDevopsProjectTaskInfoResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = GetDevopsProjectTaskInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetDevopsProjectTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevopsProjectTaskInfoResponseBody = None,
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
            temp_model = GetDevopsProjectTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceBuildNumberStatusRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        build_num: int = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.build_num = build_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.build_num is not None:
            result['BuildNum'] = self.build_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('BuildNum') is not None:
            self.build_num = m.get('BuildNum')
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents(TeaModel):
    def __init__(
        self,
        status: str = None,
        job_id: int = None,
        name: str = None,
    ):
        self.status = status
        self.job_id = job_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages(TeaModel):
    def __init__(
        self,
        status: str = None,
        sign: str = None,
        components: List[GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents] = None,
    ):
        self.status = status
        self.sign = sign
        self.components = components

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sign is not None:
            result['Sign'] = self.sign
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStagesComponents()
                self.components.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups(TeaModel):
    def __init__(
        self,
        status: str = None,
        stages: List[GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages] = None,
        name: str = None,
    ):
        self.status = status
        self.stages = stages
        self.name = name

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroupsStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPipelineInstanceBuildNumberStatusResponseBodyObject(TeaModel):
    def __init__(
        self,
        status: str = None,
        groups: List[GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups] = None,
    ):
        self.status = status
        self.groups = groups

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObjectGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceBuildNumberStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: GetPipelineInstanceBuildNumberStatusResponseBodyObject = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object.to_map()
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
        if m.get('Object') is not None:
            temp_model = GetPipelineInstanceBuildNumberStatusResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineInstanceBuildNumberStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineInstanceBuildNumberStatusResponseBody = None,
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
            temp_model = GetPipelineInstanceBuildNumberStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceGroupStatusRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        flow_instance_id: int = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.flow_instance_id = flow_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        return self


class GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents(TeaModel):
    def __init__(
        self,
        status: str = None,
        job_id: str = None,
        name: str = None,
    ):
        self.status = status
        self.job_id = job_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages(TeaModel):
    def __init__(
        self,
        status: str = None,
        sign: str = None,
        components: List[GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents] = None,
    ):
        self.status = status
        self.sign = sign
        self.components = components

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sign is not None:
            result['Sign'] = self.sign
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStagesComponents()
                self.components.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceGroupStatusResponseBodyObjectGroups(TeaModel):
    def __init__(
        self,
        status: str = None,
        stages: List[GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages] = None,
        name: str = None,
    ):
        self.status = status
        self.stages = stages
        self.name = name

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetPipelineInstanceGroupStatusResponseBodyObjectGroupsStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPipelineInstanceGroupStatusResponseBodyObject(TeaModel):
    def __init__(
        self,
        status: str = None,
        groups: List[GetPipelineInstanceGroupStatusResponseBodyObjectGroups] = None,
    ):
        self.status = status
        self.groups = groups

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipelineInstanceGroupStatusResponseBodyObjectGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class GetPipelineInstanceGroupStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: GetPipelineInstanceGroupStatusResponseBodyObject = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object.to_map()
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
        if m.get('Object') is not None:
            temp_model = GetPipelineInstanceGroupStatusResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineInstanceGroupStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineInstanceGroupStatusResponseBody = None,
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
            temp_model = GetPipelineInstanceGroupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        flow_instance_id: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.flow_instance_id = flow_instance_id
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetPipelineInstanceInfoResponseBodyObject(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: str = None,
        start_time: int = None,
        package_download_urls: List[str] = None,
        employee_id: str = None,
        docker_images: List[str] = None,
        sources: str = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.package_download_urls = package_download_urls
        self.employee_id = employee_id
        self.docker_images = docker_images
        self.sources = sources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.package_download_urls is not None:
            result['PackageDownloadUrls'] = self.package_download_urls
        if self.employee_id is not None:
            result['EmployeeId'] = self.employee_id
        if self.docker_images is not None:
            result['DockerImages'] = self.docker_images
        if self.sources is not None:
            result['Sources'] = self.sources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PackageDownloadUrls') is not None:
            self.package_download_urls = m.get('PackageDownloadUrls')
        if m.get('EmployeeId') is not None:
            self.employee_id = m.get('EmployeeId')
        if m.get('DockerImages') is not None:
            self.docker_images = m.get('DockerImages')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        return self


class GetPipelineInstanceInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: GetPipelineInstanceInfoResponseBodyObject = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object.to_map()
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
        if m.get('Object') is not None:
            temp_model = GetPipelineInstanceInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineInstanceInfoResponseBody = None,
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
            temp_model = GetPipelineInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        flow_instance_id: int = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.flow_instance_id = flow_instance_id
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetPipelineInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineInstanceStatusResponseBody = None,
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
            temp_model = GetPipelineInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineInstHistoryRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        start_time: str = None,
        end_time: str = None,
        page_start: int = None,
        page_size: int = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.start_time = start_time
        self.end_time = end_time
        self.page_start = page_start
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult(TeaModel):
    def __init__(
        self,
        engine_pipeline_number: int = None,
        mix_flow_inst_id: str = None,
        engine_pipeline_name: str = None,
        engine_pipeline_id: int = None,
        engine_pipeline_inst_id: int = None,
        time_stamp: str = None,
        trigger_mode: str = None,
        sources: str = None,
        caches: str = None,
        date_time: str = None,
    ):
        self.engine_pipeline_number = engine_pipeline_number
        self.mix_flow_inst_id = mix_flow_inst_id
        self.engine_pipeline_name = engine_pipeline_name
        self.engine_pipeline_id = engine_pipeline_id
        self.engine_pipeline_inst_id = engine_pipeline_inst_id
        self.time_stamp = time_stamp
        self.trigger_mode = trigger_mode
        self.sources = sources
        self.caches = caches
        self.date_time = date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.engine_pipeline_number is not None:
            result['EnginePipelineNumber'] = self.engine_pipeline_number
        if self.mix_flow_inst_id is not None:
            result['MixFlowInstId'] = self.mix_flow_inst_id
        if self.engine_pipeline_name is not None:
            result['EnginePipelineName'] = self.engine_pipeline_name
        if self.engine_pipeline_id is not None:
            result['EnginePipelineId'] = self.engine_pipeline_id
        if self.engine_pipeline_inst_id is not None:
            result['EnginePipelineInstId'] = self.engine_pipeline_inst_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.caches is not None:
            result['Caches'] = self.caches
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnginePipelineNumber') is not None:
            self.engine_pipeline_number = m.get('EnginePipelineNumber')
        if m.get('MixFlowInstId') is not None:
            self.mix_flow_inst_id = m.get('MixFlowInstId')
        if m.get('EnginePipelineName') is not None:
            self.engine_pipeline_name = m.get('EnginePipelineName')
        if m.get('EnginePipelineId') is not None:
            self.engine_pipeline_id = m.get('EnginePipelineId')
        if m.get('EnginePipelineInstId') is not None:
            self.engine_pipeline_inst_id = m.get('EnginePipelineInstId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('Caches') is not None:
            self.caches = m.get('Caches')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups(TeaModel):
    def __init__(
        self,
        status: str = None,
        create_time: int = None,
        delete_status: str = None,
        id_extent: int = None,
        creator: str = None,
        end_time: int = None,
        start_time: int = None,
        modifier: str = None,
        result_status: str = None,
        flow_inst_id: int = None,
        name: str = None,
        id: int = None,
        modify_time: int = None,
    ):
        self.status = status
        self.create_time = create_time
        self.delete_status = delete_status
        self.id_extent = id_extent
        self.creator = creator
        self.end_time = end_time
        self.start_time = start_time
        self.modifier = modifier
        self.result_status = result_status
        self.flow_inst_id = flow_inst_id
        self.name = name
        self.id = id
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delete_status is not None:
            result['DeleteStatus'] = self.delete_status
        if self.id_extent is not None:
            result['IdExtent'] = self.id_extent
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.result_status is not None:
            result['ResultStatus'] = self.result_status
        if self.flow_inst_id is not None:
            result['FlowInstId'] = self.flow_inst_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeleteStatus') is not None:
            self.delete_status = m.get('DeleteStatus')
        if m.get('IdExtent') is not None:
            self.id_extent = m.get('IdExtent')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ResultStatus') is not None:
            self.result_status = m.get('ResultStatus')
        if m.get('FlowInstId') is not None:
            self.flow_inst_id = m.get('FlowInstId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetPipelineInstHistoryResponseBodyDataDataListFlowInstance(TeaModel):
    def __init__(
        self,
        status: str = None,
        stages: Dict[str, Any] = None,
        result: GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult = None,
        create_time: int = None,
        status_name: str = None,
        running_status: str = None,
        stage_topo: str = None,
        creator: str = None,
        modifier: str = None,
        groups: List[GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups] = None,
        auto_driven_status: bool = None,
        result_status: str = None,
        id: int = None,
        system_code: str = None,
        modify_time: int = None,
        system_id: str = None,
    ):
        self.status = status
        self.stages = stages
        self.result = result
        self.create_time = create_time
        self.status_name = status_name
        self.running_status = running_status
        self.stage_topo = stage_topo
        self.creator = creator
        self.modifier = modifier
        self.groups = groups
        self.auto_driven_status = auto_driven_status
        self.result_status = result_status
        self.id = id
        self.system_code = system_code
        self.modify_time = modify_time
        self.system_id = system_id

    def validate(self):
        if self.result:
            self.result.validate()
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.stages is not None:
            result['Stages'] = self.stages
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.running_status is not None:
            result['RunningStatus'] = self.running_status
        if self.stage_topo is not None:
            result['StageTopo'] = self.stage_topo
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.auto_driven_status is not None:
            result['AutoDrivenStatus'] = self.auto_driven_status
        if self.result_status is not None:
            result['ResultStatus'] = self.result_status
        if self.id is not None:
            result['Id'] = self.id
        if self.system_code is not None:
            result['SystemCode'] = self.system_code
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.system_id is not None:
            result['SystemId'] = self.system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Stages') is not None:
            self.stages = m.get('Stages')
        if m.get('Result') is not None:
            temp_model = GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('RunningStatus') is not None:
            self.running_status = m.get('RunningStatus')
        if m.get('StageTopo') is not None:
            self.stage_topo = m.get('StageTopo')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipelineInstHistoryResponseBodyDataDataListFlowInstanceGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('AutoDrivenStatus') is not None:
            self.auto_driven_status = m.get('AutoDrivenStatus')
        if m.get('ResultStatus') is not None:
            self.result_status = m.get('ResultStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SystemCode') is not None:
            self.system_code = m.get('SystemCode')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SystemId') is not None:
            self.system_id = m.get('SystemId')
        return self


class GetPipelineInstHistoryResponseBodyDataDataList(TeaModel):
    def __init__(
        self,
        status: str = None,
        create_time: int = None,
        status_name: str = None,
        deletion: str = None,
        pipeline_config_id: int = None,
        trigger_mode: int = None,
        creator: str = None,
        inst_number: int = None,
        modifier: str = None,
        flow_instance: GetPipelineInstHistoryResponseBodyDataDataListFlowInstance = None,
        packages: str = None,
        flow_inst_id: int = None,
        pipeline_id: int = None,
        id: int = None,
        modify_time: int = None,
    ):
        self.status = status
        self.create_time = create_time
        self.status_name = status_name
        self.deletion = deletion
        self.pipeline_config_id = pipeline_config_id
        self.trigger_mode = trigger_mode
        self.creator = creator
        self.inst_number = inst_number
        self.modifier = modifier
        self.flow_instance = flow_instance
        self.packages = packages
        self.flow_inst_id = flow_inst_id
        self.pipeline_id = pipeline_id
        self.id = id
        self.modify_time = modify_time

    def validate(self):
        if self.flow_instance:
            self.flow_instance.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.deletion is not None:
            result['Deletion'] = self.deletion
        if self.pipeline_config_id is not None:
            result['PipelineConfigId'] = self.pipeline_config_id
        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.inst_number is not None:
            result['InstNumber'] = self.inst_number
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.flow_instance is not None:
            result['FlowInstance'] = self.flow_instance.to_map()
        if self.packages is not None:
            result['Packages'] = self.packages
        if self.flow_inst_id is not None:
            result['FlowInstId'] = self.flow_inst_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('Deletion') is not None:
            self.deletion = m.get('Deletion')
        if m.get('PipelineConfigId') is not None:
            self.pipeline_config_id = m.get('PipelineConfigId')
        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('InstNumber') is not None:
            self.inst_number = m.get('InstNumber')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('FlowInstance') is not None:
            temp_model = GetPipelineInstHistoryResponseBodyDataDataListFlowInstance()
            self.flow_instance = temp_model.from_map(m['FlowInstance'])
        if m.get('Packages') is not None:
            self.packages = m.get('Packages')
        if m.get('FlowInstId') is not None:
            self.flow_inst_id = m.get('FlowInstId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetPipelineInstHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        data_list: List[GetPipelineInstHistoryResponseBodyDataDataList] = None,
        total: int = None,
    ):
        self.data_list = data_list
        self.total = total

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = GetPipelineInstHistoryResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetPipelineInstHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetPipelineInstHistoryResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetPipelineInstHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineInstHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineInstHistoryResponseBody = None,
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
            temp_model = GetPipelineInstHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineLogRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        job_id: int = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPipelineLogResponseBodyObjectBuildProcessNodes(TeaModel):
    def __init__(
        self,
        status: str = None,
        node_name: str = None,
        node_index: int = None,
    ):
        self.status = status
        self.node_name = node_name
        self.node_index = node_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_index is not None:
            result['NodeIndex'] = self.node_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeIndex') is not None:
            self.node_index = m.get('NodeIndex')
        return self


class GetPipelineLogResponseBodyObject(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        job_id: int = None,
        action_name: str = None,
        build_process_nodes: List[GetPipelineLogResponseBodyObjectBuildProcessNodes] = None,
    ):
        self.start_time = start_time
        self.job_id = job_id
        self.action_name = action_name
        self.build_process_nodes = build_process_nodes

    def validate(self):
        if self.build_process_nodes:
            for k in self.build_process_nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        result['BuildProcessNodes'] = []
        if self.build_process_nodes is not None:
            for k in self.build_process_nodes:
                result['BuildProcessNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        self.build_process_nodes = []
        if m.get('BuildProcessNodes') is not None:
            for k in m.get('BuildProcessNodes'):
                temp_model = GetPipelineLogResponseBodyObjectBuildProcessNodes()
                self.build_process_nodes.append(temp_model.from_map(k))
        return self


class GetPipelineLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: List[GetPipelineLogResponseBodyObject] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
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
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetPipelineLogResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineLogResponseBody = None,
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
            temp_model = GetPipelineLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineStepLogRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        job_id: int = None,
        step_index: str = None,
        offset: int = None,
        limit: int = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.job_id = job_id
        self.step_index = step_index
        self.offset = offset
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.step_index is not None:
            result['StepIndex'] = self.step_index
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('StepIndex') is not None:
            self.step_index = m.get('StepIndex')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class GetPipelineStepLogResponseBodyObject(TeaModel):
    def __init__(
        self,
        logs: str = None,
        last: int = None,
        more: bool = None,
    ):
        self.logs = logs
        self.last = last
        self.more = more

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.last is not None:
            result['Last'] = self.last
        if self.more is not None:
            result['More'] = self.more
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Last') is not None:
            self.last = m.get('Last')
        if m.get('More') is not None:
            self.more = m.get('More')
        return self


class GetPipelineStepLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: GetPipelineStepLogResponseBodyObject = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object.to_map()
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
        if m.get('Object') is not None:
            temp_model = GetPipelineStepLogResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipelineStepLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipelineStepLogResponseBody = None,
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
            temp_model = GetPipelineStepLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipleineLatestInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents(TeaModel):
    def __init__(
        self,
        status: str = None,
        job_id: int = None,
        name: str = None,
    ):
        self.status = status
        self.job_id = job_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages(TeaModel):
    def __init__(
        self,
        status: str = None,
        sign: str = None,
        components: List[GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents] = None,
    ):
        self.status = status
        self.sign = sign
        self.components = components

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sign is not None:
            result['Sign'] = self.sign
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStagesComponents()
                self.components.append(temp_model.from_map(k))
        return self


class GetPipleineLatestInstanceStatusResponseBodyObjectGroups(TeaModel):
    def __init__(
        self,
        status: str = None,
        stages: List[GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages] = None,
        name: str = None,
    ):
        self.status = status
        self.stages = stages
        self.name = name

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetPipleineLatestInstanceStatusResponseBodyObjectGroupsStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPipleineLatestInstanceStatusResponseBodyObject(TeaModel):
    def __init__(
        self,
        status: str = None,
        groups: List[GetPipleineLatestInstanceStatusResponseBodyObjectGroups] = None,
    ):
        self.status = status
        self.groups = groups

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetPipleineLatestInstanceStatusResponseBodyObjectGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class GetPipleineLatestInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: GetPipleineLatestInstanceStatusResponseBodyObject = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object.to_map()
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
        if m.get('Object') is not None:
            temp_model = GetPipleineLatestInstanceStatusResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPipleineLatestInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPipleineLatestInstanceStatusResponseBody = None,
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
            temp_model = GetPipleineLatestInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectOptionRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        type: str = None,
        query: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.type = type
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class GetProjectOptionResponseBodyObject(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetProjectOptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[GetProjectOptionResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetProjectOptionResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetProjectOptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectOptionResponseBody = None,
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
            temp_model = GetProjectOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskDetailActivityRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        task_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskDetailActivityResponseBodyObject(TeaModel):
    def __init__(
        self,
        action: str = None,
        updated: str = None,
        title: str = None,
        created: str = None,
        content: Dict[str, Any] = None,
    ):
        self.action = action
        self.updated = updated
        self.title = title
        self.created = created
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.title is not None:
            result['Title'] = self.title
        if self.created is not None:
            result['Created'] = self.created
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetTaskDetailActivityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        error_msg: str = None,
        object: List[GetTaskDetailActivityResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = GetTaskDetailActivityResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetTaskDetailActivityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskDetailActivityResponseBody = None,
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
            temp_model = GetTaskDetailActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskDetailBaseRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        task_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskDetailBaseResponseBodyObjectTasklist(TeaModel):
    def __init__(
        self,
        title: str = None,
        id: str = None,
    ):
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectBadges(TeaModel):
    def __init__(
        self,
        likes_count: int = None,
        objectlinks_count: int = None,
        attachments_count: int = None,
        comments_count: int = None,
    ):
        self.likes_count = likes_count
        self.objectlinks_count = objectlinks_count
        self.attachments_count = attachments_count
        self.comments_count = comments_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        return self


class GetTaskDetailBaseResponseBodyObjectReminder(TeaModel):
    def __init__(
        self,
        type: str = None,
        members: List[str] = None,
        date: str = None,
        member_roles: List[str] = None,
        method: str = None,
        creator_id: str = None,
        rules: List[str] = None,
    ):
        self.type = type
        self.members = members
        self.date = date
        self.member_roles = member_roles
        self.method = method
        self.creator_id = creator_id
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.members is not None:
            result['Members'] = self.members
        if self.date is not None:
            result['Date'] = self.date
        if self.member_roles is not None:
            result['MemberRoles'] = self.member_roles
        if self.method is not None:
            result['Method'] = self.method
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('MemberRoles') is not None:
            self.member_roles = m.get('MemberRoles')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class GetTaskDetailBaseResponseBodyObjectStage(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectScenariofieldconfig(TeaModel):
    def __init__(
        self,
        icon: str = None,
        pro_template_config_type: str = None,
        name: str = None,
        id: str = None,
    ):
        self.icon = icon
        self.pro_template_config_type = pro_template_config_type
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.pro_template_config_type is not None:
            result['ProTemplateConfigType'] = self.pro_template_config_type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('ProTemplateConfigType') is not None:
            self.pro_template_config_type = m.get('ProTemplateConfigType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectWorkTime(TeaModel):
    def __init__(
        self,
        used_time: int = None,
        total_time: int = None,
        unit: str = None,
    ):
        self.used_time = used_time
        self.total_time = total_time
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetTaskDetailBaseResponseBodyObjectCreator(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectExecutor(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectSubtaskCount(TeaModel):
    def __init__(
        self,
        done: int = None,
        total: int = None,
    ):
        self.done = done
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTaskDetailBaseResponseBodyObjectInvolvers(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectSubtasks(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
    ):
        self.content = content
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectCustomfieldsValue(TeaModel):
    def __init__(
        self,
        title: str = None,
        id: str = None,
    ):
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObjectCustomfields(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: List[GetTaskDetailBaseResponseBodyObjectCustomfieldsValue] = None,
        values: List[str] = None,
        customfield_id: str = None,
    ):
        self.type = type
        self.value = value
        self.values = values
        self.customfield_id = customfield_id

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        result['Value'] = []
        if self.value is not None:
            for k in self.value:
                result['Value'].append(k.to_map() if k else None)
        if self.values is not None:
            result['Values'] = self.values
        if self.customfield_id is not None:
            result['CustomfieldId'] = self.customfield_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.value = []
        if m.get('Value') is not None:
            for k in m.get('Value'):
                temp_model = GetTaskDetailBaseResponseBodyObjectCustomfieldsValue()
                self.value.append(temp_model.from_map(k))
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('CustomfieldId') is not None:
            self.customfield_id = m.get('CustomfieldId')
        return self


class GetTaskDetailBaseResponseBodyObjectTaskflowstatus(TeaModel):
    def __init__(
        self,
        taskflow_id: str = None,
        kind: str = None,
        name: str = None,
        id: str = None,
    ):
        self.taskflow_id = taskflow_id
        self.kind = kind
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.taskflow_id is not None:
            result['TaskflowId'] = self.taskflow_id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskflowId') is not None:
            self.taskflow_id = m.get('TaskflowId')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBodyObject(TeaModel):
    def __init__(
        self,
        organization: str = None,
        scenariofieldconfig_id: str = None,
        project_id: str = None,
        is_top_in_project: bool = None,
        tasklist: GetTaskDetailBaseResponseBodyObjectTasklist = None,
        badges: GetTaskDetailBaseResponseBodyObjectBadges = None,
        ancestor_ids: List[str] = None,
        share_status: int = None,
        reminder: GetTaskDetailBaseResponseBodyObjectReminder = None,
        ancestors: List[str] = None,
        taskflowstatus_id: str = None,
        updated: str = None,
        note: str = None,
        is_archived: bool = None,
        content: str = None,
        rating: int = None,
        progress: int = None,
        stage: GetTaskDetailBaseResponseBodyObjectStage = None,
        labels: List[str] = None,
        start_date: str = None,
        sprint: str = None,
        creator_id: str = None,
        source_id: str = None,
        organization_id: str = None,
        source_date: str = None,
        is_favorite: bool = None,
        executor_id: str = None,
        scenariofieldconfig: GetTaskDetailBaseResponseBodyObjectScenariofieldconfig = None,
        work_time: GetTaskDetailBaseResponseBodyObjectWorkTime = None,
        tag_ids: List[str] = None,
        priority: int = None,
        creator: GetTaskDetailBaseResponseBodyObjectCreator = None,
        executor: GetTaskDetailBaseResponseBodyObjectExecutor = None,
        accomplished: str = None,
        involve_members: List[str] = None,
        unique_id: int = None,
        comments_count: int = None,
        recurrence: str = None,
        object_type: str = None,
        subtask_count: GetTaskDetailBaseResponseBodyObjectSubtaskCount = None,
        until_date: str = None,
        story_point: str = None,
        objectlinks_count: int = None,
        source: str = None,
        likes_count: int = None,
        stage_id: str = None,
        divisions: List[str] = None,
        visible: str = None,
        is_done: bool = None,
        involvers: List[GetTaskDetailBaseResponseBodyObjectInvolvers] = None,
        parent: str = None,
        sprint_id: str = None,
        due_date: str = None,
        attachments_count: int = None,
        subtasks: List[GetTaskDetailBaseResponseBodyObjectSubtasks] = None,
        customfields: List[GetTaskDetailBaseResponseBodyObjectCustomfields] = None,
        created: str = None,
        task_id: str = None,
        taskflowstatus: GetTaskDetailBaseResponseBodyObjectTaskflowstatus = None,
        id: str = None,
    ):
        self.organization = organization
        self.scenariofieldconfig_id = scenariofieldconfig_id
        self.project_id = project_id
        self.is_top_in_project = is_top_in_project
        self.tasklist = tasklist
        self.badges = badges
        self.ancestor_ids = ancestor_ids
        self.share_status = share_status
        self.reminder = reminder
        self.ancestors = ancestors
        self.taskflowstatus_id = taskflowstatus_id
        self.updated = updated
        self.note = note
        self.is_archived = is_archived
        self.content = content
        self.rating = rating
        self.progress = progress
        self.stage = stage
        self.labels = labels
        self.start_date = start_date
        self.sprint = sprint
        self.creator_id = creator_id
        self.source_id = source_id
        self.organization_id = organization_id
        self.source_date = source_date
        self.is_favorite = is_favorite
        self.executor_id = executor_id
        self.scenariofieldconfig = scenariofieldconfig
        self.work_time = work_time
        self.tag_ids = tag_ids
        self.priority = priority
        self.creator = creator
        self.executor = executor
        self.accomplished = accomplished
        self.involve_members = involve_members
        self.unique_id = unique_id
        self.comments_count = comments_count
        self.recurrence = recurrence
        self.object_type = object_type
        self.subtask_count = subtask_count
        self.until_date = until_date
        self.story_point = story_point
        self.objectlinks_count = objectlinks_count
        self.source = source
        self.likes_count = likes_count
        self.stage_id = stage_id
        self.divisions = divisions
        self.visible = visible
        self.is_done = is_done
        self.involvers = involvers
        self.parent = parent
        self.sprint_id = sprint_id
        self.due_date = due_date
        self.attachments_count = attachments_count
        self.subtasks = subtasks
        self.customfields = customfields
        self.created = created
        self.task_id = task_id
        self.taskflowstatus = taskflowstatus
        self.id = id

    def validate(self):
        if self.tasklist:
            self.tasklist.validate()
        if self.badges:
            self.badges.validate()
        if self.reminder:
            self.reminder.validate()
        if self.stage:
            self.stage.validate()
        if self.scenariofieldconfig:
            self.scenariofieldconfig.validate()
        if self.work_time:
            self.work_time.validate()
        if self.creator:
            self.creator.validate()
        if self.executor:
            self.executor.validate()
        if self.subtask_count:
            self.subtask_count.validate()
        if self.involvers:
            for k in self.involvers:
                if k:
                    k.validate()
        if self.subtasks:
            for k in self.subtasks:
                if k:
                    k.validate()
        if self.customfields:
            for k in self.customfields:
                if k:
                    k.validate()
        if self.taskflowstatus:
            self.taskflowstatus.validate()

    def to_map(self):
        result = dict()
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.scenariofieldconfig_id is not None:
            result['ScenariofieldconfigId'] = self.scenariofieldconfig_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_top_in_project is not None:
            result['IsTopInProject'] = self.is_top_in_project
        if self.tasklist is not None:
            result['Tasklist'] = self.tasklist.to_map()
        if self.badges is not None:
            result['Badges'] = self.badges.to_map()
        if self.ancestor_ids is not None:
            result['AncestorIds'] = self.ancestor_ids
        if self.share_status is not None:
            result['ShareStatus'] = self.share_status
        if self.reminder is not None:
            result['Reminder'] = self.reminder.to_map()
        if self.ancestors is not None:
            result['Ancestors'] = self.ancestors
        if self.taskflowstatus_id is not None:
            result['TaskflowstatusId'] = self.taskflowstatus_id
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.note is not None:
            result['Note'] = self.note
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.content is not None:
            result['Content'] = self.content
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.stage is not None:
            result['Stage'] = self.stage.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.sprint is not None:
            result['Sprint'] = self.sprint
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.source_date is not None:
            result['SourceDate'] = self.source_date
        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.scenariofieldconfig is not None:
            result['Scenariofieldconfig'] = self.scenariofieldconfig.to_map()
        if self.work_time is not None:
            result['WorkTime'] = self.work_time.to_map()
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.subtask_count is not None:
            result['SubtaskCount'] = self.subtask_count.to_map()
        if self.until_date is not None:
            result['UntilDate'] = self.until_date
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.source is not None:
            result['Source'] = self.source
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.divisions is not None:
            result['Divisions'] = self.divisions
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        result['Involvers'] = []
        if self.involvers is not None:
            for k in self.involvers:
                result['Involvers'].append(k.to_map() if k else None)
        if self.parent is not None:
            result['Parent'] = self.parent
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        result['Subtasks'] = []
        if self.subtasks is not None:
            for k in self.subtasks:
                result['Subtasks'].append(k.to_map() if k else None)
        result['Customfields'] = []
        if self.customfields is not None:
            for k in self.customfields:
                result['Customfields'].append(k.to_map() if k else None)
        if self.created is not None:
            result['Created'] = self.created
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.taskflowstatus is not None:
            result['Taskflowstatus'] = self.taskflowstatus.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('ScenariofieldconfigId') is not None:
            self.scenariofieldconfig_id = m.get('ScenariofieldconfigId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsTopInProject') is not None:
            self.is_top_in_project = m.get('IsTopInProject')
        if m.get('Tasklist') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectTasklist()
            self.tasklist = temp_model.from_map(m['Tasklist'])
        if m.get('Badges') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectBadges()
            self.badges = temp_model.from_map(m['Badges'])
        if m.get('AncestorIds') is not None:
            self.ancestor_ids = m.get('AncestorIds')
        if m.get('ShareStatus') is not None:
            self.share_status = m.get('ShareStatus')
        if m.get('Reminder') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectReminder()
            self.reminder = temp_model.from_map(m['Reminder'])
        if m.get('Ancestors') is not None:
            self.ancestors = m.get('Ancestors')
        if m.get('TaskflowstatusId') is not None:
            self.taskflowstatus_id = m.get('TaskflowstatusId')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Stage') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectStage()
            self.stage = temp_model.from_map(m['Stage'])
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Sprint') is not None:
            self.sprint = m.get('Sprint')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SourceDate') is not None:
            self.source_date = m.get('SourceDate')
        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('Scenariofieldconfig') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectScenariofieldconfig()
            self.scenariofieldconfig = temp_model.from_map(m['Scenariofieldconfig'])
        if m.get('WorkTime') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectWorkTime()
            self.work_time = temp_model.from_map(m['WorkTime'])
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Creator') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Executor') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SubtaskCount') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectSubtaskCount()
            self.subtask_count = temp_model.from_map(m['SubtaskCount'])
        if m.get('UntilDate') is not None:
            self.until_date = m.get('UntilDate')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Divisions') is not None:
            self.divisions = m.get('Divisions')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        self.involvers = []
        if m.get('Involvers') is not None:
            for k in m.get('Involvers'):
                temp_model = GetTaskDetailBaseResponseBodyObjectInvolvers()
                self.involvers.append(temp_model.from_map(k))
        if m.get('Parent') is not None:
            self.parent = m.get('Parent')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        self.subtasks = []
        if m.get('Subtasks') is not None:
            for k in m.get('Subtasks'):
                temp_model = GetTaskDetailBaseResponseBodyObjectSubtasks()
                self.subtasks.append(temp_model.from_map(k))
        self.customfields = []
        if m.get('Customfields') is not None:
            for k in m.get('Customfields'):
                temp_model = GetTaskDetailBaseResponseBodyObjectCustomfields()
                self.customfields.append(temp_model.from_map(k))
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Taskflowstatus') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObjectTaskflowstatus()
            self.taskflowstatus = temp_model.from_map(m['Taskflowstatus'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskDetailBaseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetTaskDetailBaseResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = GetTaskDetailBaseResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetTaskDetailBaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskDetailBaseResponseBody = None,
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
            temp_model = GetTaskDetailBaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskListFilterRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        scenario_field_config_id: str = None,
        name: str = None,
        order_condition: str = None,
        order: str = None,
        executor_id: str = None,
        tag_id: str = None,
        due_date_start: str = None,
        due_date_end: str = None,
        creator_id: str = None,
        involve_members: str = None,
        is_done: bool = None,
        priority: str = None,
        page_size: int = None,
        page_token: str = None,
        object_type: str = None,
        task_flow_status_id: str = None,
        sprint_id: str = None,
        extra: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.scenario_field_config_id = scenario_field_config_id
        self.name = name
        self.order_condition = order_condition
        self.order = order
        self.executor_id = executor_id
        self.tag_id = tag_id
        self.due_date_start = due_date_start
        self.due_date_end = due_date_end
        self.creator_id = creator_id
        self.involve_members = involve_members
        self.is_done = is_done
        self.priority = priority
        self.page_size = page_size
        self.page_token = page_token
        self.object_type = object_type
        self.task_flow_status_id = task_flow_status_id
        self.sprint_id = sprint_id
        self.extra = extra

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.scenario_field_config_id is not None:
            result['ScenarioFieldConfigId'] = self.scenario_field_config_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_condition is not None:
            result['OrderCondition'] = self.order_condition
        if self.order is not None:
            result['Order'] = self.order
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.due_date_start is not None:
            result['DueDateStart'] = self.due_date_start
        if self.due_date_end is not None:
            result['DueDateEnd'] = self.due_date_end
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_token is not None:
            result['PageToken'] = self.page_token
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.extra is not None:
            result['Extra'] = self.extra
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ScenarioFieldConfigId') is not None:
            self.scenario_field_config_id = m.get('ScenarioFieldConfigId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderCondition') is not None:
            self.order_condition = m.get('OrderCondition')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('DueDateStart') is not None:
            self.due_date_start = m.get('DueDateStart')
        if m.get('DueDateEnd') is not None:
            self.due_date_end = m.get('DueDateEnd')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageToken') is not None:
            self.page_token = m.get('PageToken')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        return self


class GetTaskListFilterResponseBodyObjectResultBadges(TeaModel):
    def __init__(
        self,
        likes_count: int = None,
        objectlinks_count: int = None,
        attachments_count: int = None,
        comments_count: int = None,
    ):
        self.likes_count = likes_count
        self.objectlinks_count = objectlinks_count
        self.attachments_count = attachments_count
        self.comments_count = comments_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        return self


class GetTaskListFilterResponseBodyObjectResultReminder(TeaModel):
    def __init__(
        self,
        type: str = None,
        members: List[str] = None,
        date: str = None,
        creator_id: str = None,
        rules: List[str] = None,
    ):
        self.type = type
        self.members = members
        self.date = date
        self.creator_id = creator_id
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.members is not None:
            result['Members'] = self.members
        if self.date is not None:
            result['Date'] = self.date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class GetTaskListFilterResponseBodyObjectResultStage(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultWorkTime(TeaModel):
    def __init__(
        self,
        used_time: int = None,
        total_time: int = None,
        unit: str = None,
    ):
        self.used_time = used_time
        self.total_time = total_time
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetTaskListFilterResponseBodyObjectResultCreator(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultExecutor(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultTaskFlowStatus(TeaModel):
    def __init__(
        self,
        task_flow_id: str = None,
        pos: int = None,
        kind: str = None,
        name: str = None,
        id: str = None,
    ):
        self.task_flow_id = task_flow_id
        self.pos = pos
        self.kind = kind
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultSubtaskCount(TeaModel):
    def __init__(
        self,
        done: int = None,
        total: int = None,
    ):
        self.done = done
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetTaskListFilterResponseBodyObjectResultCustomfieldsValue(TeaModel):
    def __init__(
        self,
        title: str = None,
        id: str = None,
    ):
        self.title = title
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObjectResultCustomfields(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: List[GetTaskListFilterResponseBodyObjectResultCustomfieldsValue] = None,
        values: str = None,
        customfield_id: str = None,
    ):
        self.type = type
        self.value = value
        self.values = values
        self.customfield_id = customfield_id

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        result['Value'] = []
        if self.value is not None:
            for k in self.value:
                result['Value'].append(k.to_map() if k else None)
        if self.values is not None:
            result['Values'] = self.values
        if self.customfield_id is not None:
            result['CustomfieldId'] = self.customfield_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.value = []
        if m.get('Value') is not None:
            for k in m.get('Value'):
                temp_model = GetTaskListFilterResponseBodyObjectResultCustomfieldsValue()
                self.value.append(temp_model.from_map(k))
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('CustomfieldId') is not None:
            self.customfield_id = m.get('CustomfieldId')
        return self


class GetTaskListFilterResponseBodyObjectResult(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        is_top_in_project: bool = None,
        badges: GetTaskListFilterResponseBodyObjectResultBadges = None,
        ancestor_ids: List[str] = None,
        share_status: int = None,
        reminder: GetTaskListFilterResponseBodyObjectResultReminder = None,
        note: str = None,
        updated: str = None,
        is_archived: bool = None,
        content: str = None,
        rating: int = None,
        task_flow_status_id: str = None,
        progress: int = None,
        stage: GetTaskListFilterResponseBodyObjectResultStage = None,
        labels: List[str] = None,
        pos: int = None,
        start_date: str = None,
        sprint: str = None,
        creator_id: str = None,
        source_id: str = None,
        organization_id: str = None,
        source_date: str = None,
        is_favorite: bool = None,
        executor_id: str = None,
        work_time: GetTaskListFilterResponseBodyObjectResultWorkTime = None,
        tag_ids: List[str] = None,
        priority: int = None,
        scenariof_feld_config_id: str = None,
        creator: GetTaskListFilterResponseBodyObjectResultCreator = None,
        executor: GetTaskListFilterResponseBodyObjectResultExecutor = None,
        accomplished: str = None,
        task_list_id: str = None,
        involve_members: List[str] = None,
        unique_id: int = None,
        task_flow_status: GetTaskListFilterResponseBodyObjectResultTaskFlowStatus = None,
        comments_count: int = None,
        recurrence: str = None,
        object_type: str = None,
        subtask_count: GetTaskListFilterResponseBodyObjectResultSubtaskCount = None,
        until_date: str = None,
        story_point: str = None,
        objectlinks_count: int = None,
        source: str = None,
        likes_count: int = None,
        stage_id: str = None,
        divisions: List[str] = None,
        visible: str = None,
        is_done: bool = None,
        parent: str = None,
        sprint_id: str = None,
        due_date: str = None,
        attachments_count: int = None,
        customfields: List[GetTaskListFilterResponseBodyObjectResultCustomfields] = None,
        created: str = None,
        task_unique_id: str = None,
        task_id: str = None,
        id: str = None,
    ):
        self.project_id = project_id
        self.is_top_in_project = is_top_in_project
        self.badges = badges
        self.ancestor_ids = ancestor_ids
        self.share_status = share_status
        self.reminder = reminder
        self.note = note
        self.updated = updated
        self.is_archived = is_archived
        self.content = content
        self.rating = rating
        self.task_flow_status_id = task_flow_status_id
        self.progress = progress
        self.stage = stage
        self.labels = labels
        self.pos = pos
        self.start_date = start_date
        self.sprint = sprint
        self.creator_id = creator_id
        self.source_id = source_id
        self.organization_id = organization_id
        self.source_date = source_date
        self.is_favorite = is_favorite
        self.executor_id = executor_id
        self.work_time = work_time
        self.tag_ids = tag_ids
        self.priority = priority
        self.scenariof_feld_config_id = scenariof_feld_config_id
        self.creator = creator
        self.executor = executor
        self.accomplished = accomplished
        self.task_list_id = task_list_id
        self.involve_members = involve_members
        self.unique_id = unique_id
        self.task_flow_status = task_flow_status
        self.comments_count = comments_count
        self.recurrence = recurrence
        self.object_type = object_type
        self.subtask_count = subtask_count
        self.until_date = until_date
        self.story_point = story_point
        self.objectlinks_count = objectlinks_count
        self.source = source
        self.likes_count = likes_count
        self.stage_id = stage_id
        self.divisions = divisions
        self.visible = visible
        self.is_done = is_done
        self.parent = parent
        self.sprint_id = sprint_id
        self.due_date = due_date
        self.attachments_count = attachments_count
        self.customfields = customfields
        self.created = created
        self.task_unique_id = task_unique_id
        self.task_id = task_id
        self.id = id

    def validate(self):
        if self.badges:
            self.badges.validate()
        if self.reminder:
            self.reminder.validate()
        if self.stage:
            self.stage.validate()
        if self.work_time:
            self.work_time.validate()
        if self.creator:
            self.creator.validate()
        if self.executor:
            self.executor.validate()
        if self.task_flow_status:
            self.task_flow_status.validate()
        if self.subtask_count:
            self.subtask_count.validate()
        if self.customfields:
            for k in self.customfields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_top_in_project is not None:
            result['IsTopInProject'] = self.is_top_in_project
        if self.badges is not None:
            result['Badges'] = self.badges.to_map()
        if self.ancestor_ids is not None:
            result['AncestorIds'] = self.ancestor_ids
        if self.share_status is not None:
            result['ShareStatus'] = self.share_status
        if self.reminder is not None:
            result['Reminder'] = self.reminder.to_map()
        if self.note is not None:
            result['Note'] = self.note
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.is_archived is not None:
            result['IsArchived'] = self.is_archived
        if self.content is not None:
            result['Content'] = self.content
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.stage is not None:
            result['Stage'] = self.stage.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.sprint is not None:
            result['Sprint'] = self.sprint
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.source_date is not None:
            result['SourceDate'] = self.source_date
        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.work_time is not None:
            result['WorkTime'] = self.work_time.to_map()
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.scenariof_feld_config_id is not None:
            result['ScenariofFeldConfigId'] = self.scenariof_feld_config_id
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.executor is not None:
            result['Executor'] = self.executor.to_map()
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.task_list_id is not None:
            result['TaskListId'] = self.task_list_id
        if self.involve_members is not None:
            result['InvolveMembers'] = self.involve_members
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.task_flow_status is not None:
            result['TaskFlowStatus'] = self.task_flow_status.to_map()
        if self.comments_count is not None:
            result['CommentsCount'] = self.comments_count
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.subtask_count is not None:
            result['SubtaskCount'] = self.subtask_count.to_map()
        if self.until_date is not None:
            result['UntilDate'] = self.until_date
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.objectlinks_count is not None:
            result['ObjectlinksCount'] = self.objectlinks_count
        if self.source is not None:
            result['Source'] = self.source
        if self.likes_count is not None:
            result['LikesCount'] = self.likes_count
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.divisions is not None:
            result['Divisions'] = self.divisions
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.is_done is not None:
            result['IsDone'] = self.is_done
        if self.parent is not None:
            result['Parent'] = self.parent
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.attachments_count is not None:
            result['AttachmentsCount'] = self.attachments_count
        result['Customfields'] = []
        if self.customfields is not None:
            for k in self.customfields:
                result['Customfields'].append(k.to_map() if k else None)
        if self.created is not None:
            result['Created'] = self.created
        if self.task_unique_id is not None:
            result['TaskUniqueId'] = self.task_unique_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsTopInProject') is not None:
            self.is_top_in_project = m.get('IsTopInProject')
        if m.get('Badges') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultBadges()
            self.badges = temp_model.from_map(m['Badges'])
        if m.get('AncestorIds') is not None:
            self.ancestor_ids = m.get('AncestorIds')
        if m.get('ShareStatus') is not None:
            self.share_status = m.get('ShareStatus')
        if m.get('Reminder') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultReminder()
            self.reminder = temp_model.from_map(m['Reminder'])
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('IsArchived') is not None:
            self.is_archived = m.get('IsArchived')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Stage') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultStage()
            self.stage = temp_model.from_map(m['Stage'])
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Sprint') is not None:
            self.sprint = m.get('Sprint')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SourceDate') is not None:
            self.source_date = m.get('SourceDate')
        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('WorkTime') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultWorkTime()
            self.work_time = temp_model.from_map(m['WorkTime'])
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ScenariofFeldConfigId') is not None:
            self.scenariof_feld_config_id = m.get('ScenariofFeldConfigId')
        if m.get('Creator') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Executor') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultExecutor()
            self.executor = temp_model.from_map(m['Executor'])
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('TaskListId') is not None:
            self.task_list_id = m.get('TaskListId')
        if m.get('InvolveMembers') is not None:
            self.involve_members = m.get('InvolveMembers')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('TaskFlowStatus') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultTaskFlowStatus()
            self.task_flow_status = temp_model.from_map(m['TaskFlowStatus'])
        if m.get('CommentsCount') is not None:
            self.comments_count = m.get('CommentsCount')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SubtaskCount') is not None:
            temp_model = GetTaskListFilterResponseBodyObjectResultSubtaskCount()
            self.subtask_count = temp_model.from_map(m['SubtaskCount'])
        if m.get('UntilDate') is not None:
            self.until_date = m.get('UntilDate')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('ObjectlinksCount') is not None:
            self.objectlinks_count = m.get('ObjectlinksCount')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('LikesCount') is not None:
            self.likes_count = m.get('LikesCount')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Divisions') is not None:
            self.divisions = m.get('Divisions')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('IsDone') is not None:
            self.is_done = m.get('IsDone')
        if m.get('Parent') is not None:
            self.parent = m.get('Parent')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('AttachmentsCount') is not None:
            self.attachments_count = m.get('AttachmentsCount')
        self.customfields = []
        if m.get('Customfields') is not None:
            for k in m.get('Customfields'):
                temp_model = GetTaskListFilterResponseBodyObjectResultCustomfields()
                self.customfields.append(temp_model.from_map(k))
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('TaskUniqueId') is not None:
            self.task_unique_id = m.get('TaskUniqueId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTaskListFilterResponseBodyObject(TeaModel):
    def __init__(
        self,
        next_page_token: str = None,
        result: List[GetTaskListFilterResponseBodyObjectResult] = None,
        total_size: int = None,
    ):
        self.next_page_token = next_page_token
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTaskListFilterResponseBodyObjectResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class GetTaskListFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetTaskListFilterResponseBodyObject = None,
        error_code: str = None,
        successful: str = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = GetTaskListFilterResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetTaskListFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskListFilterResponseBody = None,
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
            temp_model = GetTaskListFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserByAliyunUidRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class GetUserByAliyunUidResponseBodyObject(TeaModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        email: str = None,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
        phone: str = None,
    ):
        self.aliyun_pk = aliyun_pk
        self.email = email
        self.avatar_url = avatar_url
        self.name = name
        self.id = id
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetUserByAliyunUidResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetUserByAliyunUidResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = GetUserByAliyunUidResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetUserByAliyunUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserByAliyunUidResponseBody = None,
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
            temp_model = GetUserByAliyunUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserNameRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        user_id: str = None,
    ):
        self.org_id = org_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: str = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetUserNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserNameResponseBody = None,
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
            temp_model = GetUserNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertDevopsUserRequest(TeaModel):
    def __init__(
        self,
        user_pk: str = None,
        user_name: str = None,
        phone: str = None,
        email: str = None,
    ):
        self.user_pk = user_pk
        self.user_name = user_name
        self.phone = phone
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class InsertDevopsUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertDevopsUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertDevopsUserResponseBody = None,
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
            temp_model = InsertDevopsUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertPipelineMemberRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        user_id: str = None,
        role_name: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.user_id = user_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class InsertPipelineMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertPipelineMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertPipelineMemberResponseBody = None,
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
            temp_model = InsertPipelineMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertProjectMembersRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        members: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class InsertProjectMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class InsertProjectMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertProjectMembersResponseBody = None,
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
            temp_model = InsertProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonGroupRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        smart_group_id: str = None,
        all: bool = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.smart_group_id = smart_group_id
        self.all = all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class ListCommonGroupResponseBodyObject(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        smart_group_id: str = None,
        pos: int = None,
        project_id: str = None,
        is_root: bool = None,
        pinyin: str = None,
        creator_id: str = None,
        name: str = None,
        id: str = None,
    ):
        self.resource_count = resource_count
        self.smart_group_id = smart_group_id
        self.pos = pos
        self.project_id = project_id
        self.is_root = is_root
        self.pinyin = pinyin
        self.creator_id = creator_id
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.is_root is not None:
            result['IsRoot'] = self.is_root
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListCommonGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListCommonGroupResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListCommonGroupResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListCommonGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCommonGroupResponseBody = None,
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
            temp_model = ListCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCredentialsRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ListCredentialsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: List[Dict[str, Any]] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCredentialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCredentialsResponseBody = None,
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
            temp_model = ListCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectSprintsRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsProjectSprintsResponseBodyObjectPlanToDo(TeaModel):
    def __init__(
        self,
        tasks: int = None,
        work_times: int = None,
        story_points: int = None,
    ):
        self.tasks = tasks
        self.work_times = work_times
        self.story_points = story_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.story_points is not None:
            result['StoryPoints'] = self.story_points
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('StoryPoints') is not None:
            self.story_points = m.get('StoryPoints')
        return self


class ListDevopsProjectSprintsResponseBodyObject(TeaModel):
    def __init__(
        self,
        status: str = None,
        project_id: str = None,
        start_date: str = None,
        creator_id: str = None,
        accomplished: str = None,
        is_deleted: bool = None,
        updated: str = None,
        due_date: str = None,
        name: str = None,
        created: str = None,
        plan_to_do: ListDevopsProjectSprintsResponseBodyObjectPlanToDo = None,
        id: str = None,
    ):
        self.status = status
        self.project_id = project_id
        self.start_date = start_date
        self.creator_id = creator_id
        self.accomplished = accomplished
        self.is_deleted = is_deleted
        self.updated = updated
        self.due_date = due_date
        self.name = name
        self.created = created
        self.plan_to_do = plan_to_do
        self.id = id

    def validate(self):
        if self.plan_to_do:
            self.plan_to_do.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.accomplished is not None:
            result['Accomplished'] = self.accomplished
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.plan_to_do is not None:
            result['PlanToDo'] = self.plan_to_do.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Accomplished') is not None:
            self.accomplished = m.get('Accomplished')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('PlanToDo') is not None:
            temp_model = ListDevopsProjectSprintsResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectSprintsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListDevopsProjectSprintsResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectSprintsResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListDevopsProjectSprintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevopsProjectSprintsResponseBody = None,
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
            temp_model = ListDevopsProjectSprintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTaskFlowRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsProjectTaskFlowResponseBodyObject(TeaModel):
    def __init__(
        self,
        type: str = None,
        name: str = None,
        id: str = None,
    ):
        self.type = type
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTaskFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListDevopsProjectTaskFlowResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectTaskFlowResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListDevopsProjectTaskFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevopsProjectTaskFlowResponseBody = None,
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
            temp_model = ListDevopsProjectTaskFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTaskFlowStatusRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        task_flow_id: str = None,
    ):
        self.org_id = org_id
        self.task_flow_id = task_flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        return self


class ListDevopsProjectTaskFlowStatusResponseBodyObject(TeaModel):
    def __init__(
        self,
        taskflow_id: str = None,
        kind: str = None,
        pos: int = None,
        is_deleted: bool = None,
        updated: str = None,
        creator_id: str = None,
        name: str = None,
        created: str = None,
        reject_status_ids: str = None,
        id: str = None,
    ):
        self.taskflow_id = taskflow_id
        self.kind = kind
        self.pos = pos
        self.is_deleted = is_deleted
        self.updated = updated
        self.creator_id = creator_id
        self.name = name
        self.created = created
        self.reject_status_ids = reject_status_ids
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.taskflow_id is not None:
            result['TaskflowId'] = self.taskflow_id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.name is not None:
            result['Name'] = self.name
        if self.created is not None:
            result['Created'] = self.created
        if self.reject_status_ids is not None:
            result['RejectStatusIds'] = self.reject_status_ids
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskflowId') is not None:
            self.taskflow_id = m.get('TaskflowId')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('RejectStatusIds') is not None:
            self.reject_status_ids = m.get('RejectStatusIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTaskFlowStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListDevopsProjectTaskFlowStatusResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectTaskFlowStatusResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListDevopsProjectTaskFlowStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevopsProjectTaskFlowStatusResponseBody = None,
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
            temp_model = ListDevopsProjectTaskFlowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTaskListRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsProjectTaskListResponseBodyObjectResult(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTaskListResponseBodyObject(TeaModel):
    def __init__(
        self,
        result: List[ListDevopsProjectTaskListResponseBodyObjectResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDevopsProjectTaskListResponseBodyObjectResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDevopsProjectTaskListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: ListDevopsProjectTaskListResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = ListDevopsProjectTaskListResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListDevopsProjectTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevopsProjectTaskListResponseBody = None,
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
            temp_model = ListDevopsProjectTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsProjectTasksRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_ids: str = None,
    ):
        self.org_id = org_id
        self.project_ids = project_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class ListDevopsProjectTasksResponseBodyObject(TeaModel):
    def __init__(
        self,
        taskgroup_id: str = None,
        tasklist_id: str = None,
        project_id: str = None,
        modifier_id: str = None,
        updated: str = None,
        creator_id: str = None,
        created: str = None,
        name: str = None,
        id: str = None,
    ):
        self.taskgroup_id = taskgroup_id
        self.tasklist_id = tasklist_id
        self.project_id = project_id
        self.modifier_id = modifier_id
        self.updated = updated
        self.creator_id = creator_id
        self.created = created
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.taskgroup_id is not None:
            result['TaskgroupId'] = self.taskgroup_id
        if self.tasklist_id is not None:
            result['TasklistId'] = self.tasklist_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.created is not None:
            result['Created'] = self.created
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskgroupId') is not None:
            self.taskgroup_id = m.get('TaskgroupId')
        if m.get('TasklistId') is not None:
            self.tasklist_id = m.get('TasklistId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsProjectTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListDevopsProjectTasksResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsProjectTasksResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListDevopsProjectTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevopsProjectTasksResponseBody = None,
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
            temp_model = ListDevopsProjectTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevopsScenarioFieldConfigRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListDevopsScenarioFieldConfigResponseBodyObject(TeaModel):
    def __init__(
        self,
        type: str = None,
        id: str = None,
    ):
        self.type = type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListDevopsScenarioFieldConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListDevopsScenarioFieldConfigResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListDevopsScenarioFieldConfigResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListDevopsScenarioFieldConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevopsScenarioFieldConfigResponseBody = None,
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
            temp_model = ListDevopsScenarioFieldConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelinesRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_name: str = None,
        creators: str = None,
        operators: str = None,
        result_status_list: str = None,
        create_start_time: str = None,
        create_end_time: str = None,
        execute_start_time: str = None,
        execute_end_time: str = None,
        page_size: int = None,
        page_start: int = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.pipeline_name = pipeline_name
        self.creators = creators
        self.operators = operators
        self.result_status_list = result_status_list
        self.create_start_time = create_start_time
        self.create_end_time = create_end_time
        self.execute_start_time = execute_start_time
        self.execute_end_time = execute_end_time
        self.page_size = page_size
        self.page_start = page_start
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.creators is not None:
            result['Creators'] = self.creators
        if self.operators is not None:
            result['Operators'] = self.operators
        if self.result_status_list is not None:
            result['ResultStatusList'] = self.result_status_list
        if self.create_start_time is not None:
            result['CreateStartTime'] = self.create_start_time
        if self.create_end_time is not None:
            result['CreateEndTime'] = self.create_end_time
        if self.execute_start_time is not None:
            result['ExecuteStartTime'] = self.execute_start_time
        if self.execute_end_time is not None:
            result['ExecuteEndTime'] = self.execute_end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('Creators') is not None:
            self.creators = m.get('Creators')
        if m.get('Operators') is not None:
            self.operators = m.get('Operators')
        if m.get('ResultStatusList') is not None:
            self.result_status_list = m.get('ResultStatusList')
        if m.get('CreateStartTime') is not None:
            self.create_start_time = m.get('CreateStartTime')
        if m.get('CreateEndTime') is not None:
            self.create_end_time = m.get('CreateEndTime')
        if m.get('ExecuteStartTime') is not None:
            self.execute_start_time = m.get('ExecuteStartTime')
        if m.get('ExecuteEndTime') is not None:
            self.execute_end_time = m.get('ExecuteEndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ListPipelinesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: Dict[str, Any] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPipelinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPipelinesResponseBody = None,
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
            temp_model = ListPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectCustomFieldsRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListProjectCustomFieldsResponseBodyObjectValues(TeaModel):
    def __init__(
        self,
        value: str = None,
        id: str = None,
    ):
        self.value = value
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListProjectCustomFieldsResponseBodyObject(TeaModel):
    def __init__(
        self,
        type: str = None,
        subtype: str = None,
        values: List[ListProjectCustomFieldsResponseBodyObjectValues] = None,
        custom_field_id: str = None,
        name: str = None,
    ):
        self.type = type
        self.subtype = subtype
        self.values = values
        self.custom_field_id = custom_field_id
        self.name = name

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.subtype is not None:
            result['Subtype'] = self.subtype
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        if self.custom_field_id is not None:
            result['CustomFieldId'] = self.custom_field_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListProjectCustomFieldsResponseBodyObjectValues()
                self.values.append(temp_model.from_map(k))
        if m.get('CustomFieldId') is not None:
            self.custom_field_id = m.get('CustomFieldId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListProjectCustomFieldsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListProjectCustomFieldsResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListProjectCustomFieldsResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListProjectCustomFieldsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectCustomFieldsResponseBody = None,
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
            temp_model = ListProjectCustomFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceConnectionsRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        sc_type: str = None,
        user_pk: str = None,
    ):
        self.org_id = org_id
        self.sc_type = sc_type
        self.user_pk = user_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.sc_type is not None:
            result['ScType'] = self.sc_type
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ScType') is not None:
            self.sc_type = m.get('ScType')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        return self


class ListServiceConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: List[Dict[str, Any]] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListServiceConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceConnectionsResponseBody = None,
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
            temp_model = ListServiceConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSmartGroupRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListSmartGroupResponseBodyObject(TeaModel):
    def __init__(
        self,
        type: str = None,
        id: str = None,
    ):
        self.type = type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListSmartGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListSmartGroupResponseBodyObject] = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            for k in self.object:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['Object'] = []
        if self.object is not None:
            for k in self.object:
                result['Object'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.object = []
        if m.get('Object') is not None:
            for k in m.get('Object'):
                temp_model = ListSmartGroupResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListSmartGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSmartGroupResponseBody = None,
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
            temp_model = ListSmartGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserOrganizationRequest(TeaModel):
    def __init__(
        self,
        real_pk: str = None,
    ):
        self.real_pk = real_pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.real_pk is not None:
            result['RealPk'] = self.real_pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealPk') is not None:
            self.real_pk = m.get('RealPk')
        return self


class ListUserOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserOrganizationResponseBody = None,
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
            temp_model = ListUserOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferPipelineOwnerRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        new_owner_id: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.new_owner_id = new_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.new_owner_id is not None:
            result['NewOwnerId'] = self.new_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('NewOwnerId') is not None:
            self.new_owner_id = m.get('NewOwnerId')
        return self


class TransferPipelineOwnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: Dict[str, Any] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferPipelineOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferPipelineOwnerResponseBody = None,
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
            temp_model = TransferPipelineOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCommonGroupRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        project_id: str = None,
        description: str = None,
        smart_group_id: str = None,
        common_group_id: str = None,
        name: str = None,
    ):
        self.org_id = org_id
        self.project_id = project_id
        self.description = description
        self.smart_group_id = smart_group_id
        self.common_group_id = common_group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.description is not None:
            result['Description'] = self.description
        if self.smart_group_id is not None:
            result['SmartGroupId'] = self.smart_group_id
        if self.common_group_id is not None:
            result['CommonGroupId'] = self.common_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SmartGroupId') is not None:
            self.smart_group_id = m.get('SmartGroupId')
        if m.get('CommonGroupId') is not None:
            self.common_group_id = m.get('CommonGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCommonGroupResponseBodyObject(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateCommonGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: UpdateCommonGroupResponseBodyObject = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        if self.object:
            self.object.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            temp_model = UpdateCommonGroupResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class UpdateCommonGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCommonGroupResponseBody = None,
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
            temp_model = UpdateCommonGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevopsProjectRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        name: str = None,
        description: str = None,
        project_id: str = None,
    ):
        self.org_id = org_id
        self.name = name
        self.description = description
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateDevopsProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDevopsProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevopsProjectResponseBody = None,
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
            temp_model = UpdateDevopsProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevopsProjectSprintRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        name: str = None,
        description: str = None,
        project_id: str = None,
        executor_id: str = None,
        start_date: str = None,
        due_date: str = None,
        sprint_id: str = None,
    ):
        self.org_id = org_id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.executor_id = executor_id
        self.start_date = start_date
        self.due_date = due_date
        self.sprint_id = sprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class UpdateDevopsProjectSprintResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class UpdateDevopsProjectSprintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevopsProjectSprintResponseBody = None,
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
            temp_model = UpdateDevopsProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevopsProjectTaskRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        content: str = None,
        project_id: str = None,
        executor_id: str = None,
        start_date: str = None,
        due_date: str = None,
        scenario_fiield_config_id: str = None,
        task_flow_status_id: str = None,
        note: str = None,
        priority: int = None,
        visible: str = None,
        parent_task_id: str = None,
        sprint_id: str = None,
        task_id: str = None,
    ):
        self.org_id = org_id
        self.content = content
        self.project_id = project_id
        self.executor_id = executor_id
        self.start_date = start_date
        self.due_date = due_date
        self.scenario_fiield_config_id = scenario_fiield_config_id
        self.task_flow_status_id = task_flow_status_id
        self.note = note
        self.priority = priority
        self.visible = visible
        self.parent_task_id = parent_task_id
        self.sprint_id = sprint_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.content is not None:
            result['Content'] = self.content
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.scenario_fiield_config_id is not None:
            result['ScenarioFiieldConfigId'] = self.scenario_fiield_config_id
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.note is not None:
            result['Note'] = self.note
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('ScenarioFiieldConfigId') is not None:
            self.scenario_fiield_config_id = m.get('ScenarioFiieldConfigId')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateDevopsProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class UpdateDevopsProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevopsProjectTaskResponseBody = None,
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
            temp_model = UpdateDevopsProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineMemberRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        pipeline_id: int = None,
        user_pk: str = None,
        user_id: str = None,
        role_name: str = None,
    ):
        self.org_id = org_id
        self.pipeline_id = pipeline_id
        self.user_pk = user_pk
        self.user_id = user_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.user_pk is not None:
            result['UserPk'] = self.user_pk
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('UserPk') is not None:
            self.user_pk = m.get('UserPk')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdatePipelineMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        object: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.object = object
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.object is not None:
            result['Object'] = self.object
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
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePipelineMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePipelineMemberResponseBody = None,
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
            temp_model = UpdatePipelineMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskDetailRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        content: str = None,
        project_id: str = None,
        executor_id: str = None,
        start_date: str = None,
        due_date: str = None,
        task_flow_status_id: str = None,
        note: str = None,
        priority: int = None,
        sprint_id: str = None,
        task_id: str = None,
        work_times: int = None,
        custom_field_id: str = None,
        custom_field_values: str = None,
        story_point: str = None,
        tag_ids: str = None,
        del_involvers: str = None,
        add_involvers: str = None,
    ):
        self.org_id = org_id
        self.content = content
        self.project_id = project_id
        self.executor_id = executor_id
        self.start_date = start_date
        self.due_date = due_date
        self.task_flow_status_id = task_flow_status_id
        self.note = note
        self.priority = priority
        self.sprint_id = sprint_id
        self.task_id = task_id
        self.work_times = work_times
        self.custom_field_id = custom_field_id
        self.custom_field_values = custom_field_values
        self.story_point = story_point
        self.tag_ids = tag_ids
        self.del_involvers = del_involvers
        self.add_involvers = add_involvers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.content is not None:
            result['Content'] = self.content
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.due_date is not None:
            result['DueDate'] = self.due_date
        if self.task_flow_status_id is not None:
            result['TaskFlowStatusId'] = self.task_flow_status_id
        if self.note is not None:
            result['Note'] = self.note
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.work_times is not None:
            result['WorkTimes'] = self.work_times
        if self.custom_field_id is not None:
            result['CustomFieldId'] = self.custom_field_id
        if self.custom_field_values is not None:
            result['CustomFieldValues'] = self.custom_field_values
        if self.story_point is not None:
            result['StoryPoint'] = self.story_point
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.del_involvers is not None:
            result['DelInvolvers'] = self.del_involvers
        if self.add_involvers is not None:
            result['AddInvolvers'] = self.add_involvers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DueDate') is not None:
            self.due_date = m.get('DueDate')
        if m.get('TaskFlowStatusId') is not None:
            self.task_flow_status_id = m.get('TaskFlowStatusId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkTimes') is not None:
            self.work_times = m.get('WorkTimes')
        if m.get('CustomFieldId') is not None:
            self.custom_field_id = m.get('CustomFieldId')
        if m.get('CustomFieldValues') is not None:
            self.custom_field_values = m.get('CustomFieldValues')
        if m.get('StoryPoint') is not None:
            self.story_point = m.get('StoryPoint')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('DelInvolvers') is not None:
            self.del_involvers = m.get('DelInvolvers')
        if m.get('AddInvolvers') is not None:
            self.add_involvers = m.get('AddInvolvers')
        return self


class UpdateTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: bool = None,
        error_code: str = None,
        successful: bool = None,
    ):
        self.request_id = request_id
        self.error_msg = error_msg
        self.object = object
        self.error_code = error_code
        self.successful = successful

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.object is not None:
            result['Object'] = self.object
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.successful is not None:
            result['Successful'] = self.successful
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class UpdateTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTaskDetailResponseBody = None,
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
            temp_model = UpdateTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


