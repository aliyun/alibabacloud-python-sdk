# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddProjectMembersRequest(TeaModel):
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


class AddProjectMembersResponseBody(TeaModel):
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


class AddProjectMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddProjectMembersResponseBody = None,
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
            temp_model = AddProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplySmallMicroRequest(TeaModel):
    def __init__(
        self,
        org_id: str = None,
        type: str = None,
        org_name: str = None,
        applicant_name: str = None,
        applicant_tel: str = None,
        applicant_email: str = None,
        applicant_position: str = None,
        develop_scale: str = None,
        develop_language: str = None,
        business_model: str = None,
        solution: str = None,
        for_help: str = None,
    ):
        self.org_id = org_id
        self.type = type
        self.org_name = org_name
        self.applicant_name = applicant_name
        self.applicant_tel = applicant_tel
        self.applicant_email = applicant_email
        self.applicant_position = applicant_position
        self.develop_scale = develop_scale
        self.develop_language = develop_language
        self.business_model = business_model
        self.solution = solution
        self.for_help = for_help

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.type is not None:
            result['Type'] = self.type
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.applicant_tel is not None:
            result['ApplicantTel'] = self.applicant_tel
        if self.applicant_email is not None:
            result['ApplicantEmail'] = self.applicant_email
        if self.applicant_position is not None:
            result['ApplicantPosition'] = self.applicant_position
        if self.develop_scale is not None:
            result['DevelopScale'] = self.develop_scale
        if self.develop_language is not None:
            result['DevelopLanguage'] = self.develop_language
        if self.business_model is not None:
            result['BusinessModel'] = self.business_model
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.for_help is not None:
            result['ForHelp'] = self.for_help
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicantTel') is not None:
            self.applicant_tel = m.get('ApplicantTel')
        if m.get('ApplicantEmail') is not None:
            self.applicant_email = m.get('ApplicantEmail')
        if m.get('ApplicantPosition') is not None:
            self.applicant_position = m.get('ApplicantPosition')
        if m.get('DevelopScale') is not None:
            self.develop_scale = m.get('DevelopScale')
        if m.get('DevelopLanguage') is not None:
            self.develop_language = m.get('DevelopLanguage')
        if m.get('BusinessModel') is not None:
            self.business_model = m.get('BusinessModel')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('ForHelp') is not None:
            self.for_help = m.get('ForHelp')
        return self


class ApplySmallMicroResponseBody(TeaModel):
    def __init__(
        self,
        result: Dict[str, Any] = None,
        code: int = None,
        request_id: str = None,
        raw: bool = None,
        message: bool = None,
    ):
        self.result = result
        self.code = code
        self.request_id = request_id
        self.raw = raw
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.code is not None:
            result['code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.raw is not None:
            result['raw'] = self.raw
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('raw') is not None:
            self.raw = m.get('raw')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ApplySmallMicroResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplySmallMicroResponseBody = None,
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
            temp_model = ApplySmallMicroResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BactchInsertMembersRequest(TeaModel):
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


class BactchInsertMembersResponseBody(TeaModel):
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


class BactchInsertMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BactchInsertMembersResponseBody = None,
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
            temp_model = BactchInsertMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAliyunUserExistsRequest(TeaModel):
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


class CheckAliyunUserExistsResponseBody(TeaModel):
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


class CheckAliyunUserExistsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckAliyunUserExistsResponseBody = None,
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
            temp_model = CheckAliyunUserExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevopsOrgRequest(TeaModel):
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


class CreateDevopsOrgResponseBody(TeaModel):
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


class CreateDevopsOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevopsOrgResponseBody = None,
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
            temp_model = CreateDevopsOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
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


class CreateProjectResponseBody(TeaModel):
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


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectSprintRequest(TeaModel):
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


class CreateProjectSprintResponseBodyObjectPlanToDo(TeaModel):
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


class CreateProjectSprintResponseBodyObject(TeaModel):
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
        plan_to_do: CreateProjectSprintResponseBodyObjectPlanToDo = None,
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
            temp_model = CreateProjectSprintResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateProjectSprintResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: CreateProjectSprintResponseBodyObject = None,
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
            temp_model = CreateProjectSprintResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class CreateProjectSprintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectSprintResponseBody = None,
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
            temp_model = CreateProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectTaskRequest(TeaModel):
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


class CreateProjectTaskResponseBodyObject(TeaModel):
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


class CreateProjectTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: CreateProjectTaskResponseBodyObject = None,
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
            temp_model = CreateProjectTaskResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class CreateProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectTaskResponseBody = None,
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
            temp_model = CreateProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMembersForOrgRequest(TeaModel):
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


class DeleteMembersForOrgResponseBody(TeaModel):
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


class DeleteMembersForOrgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMembersForOrgResponseBody = None,
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
            temp_model = DeleteMembersForOrgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
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


class DeleteProjectResponseBody(TeaModel):
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


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectMembersRequest(TeaModel):
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


class DeleteProjectMembersResponseBody(TeaModel):
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


class DeleteProjectMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectMembersResponseBody = None,
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
            temp_model = DeleteProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectSprintRequest(TeaModel):
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


class DeleteProjectSprintResponseBody(TeaModel):
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


class DeleteProjectSprintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectSprintResponseBody = None,
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
            temp_model = DeleteProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectTaskRequest(TeaModel):
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


class DeleteProjectTaskResponseBody(TeaModel):
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


class DeleteProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectTaskResponseBody = None,
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
            temp_model = DeleteProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationMembersRequest(TeaModel):
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


class GetOrganizationMembersResponseBodyObject(TeaModel):
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


class GetOrganizationMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[GetOrganizationMembersResponseBodyObject] = None,
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
                temp_model = GetOrganizationMembersResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetOrganizationMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrganizationMembersResponseBody = None,
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
            temp_model = GetOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectInfoRequest(TeaModel):
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


class GetProjectInfoResponseBodyObject(TeaModel):
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


class GetProjectInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetProjectInfoResponseBodyObject = None,
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
            temp_model = GetProjectInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetProjectInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectInfoResponseBody = None,
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
            temp_model = GetProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectMembersRequest(TeaModel):
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


class GetProjectMembersResponseBodyObject(TeaModel):
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


class GetProjectMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[GetProjectMembersResponseBodyObject] = None,
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
                temp_model = GetProjectMembersResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetProjectMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectMembersResponseBody = None,
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
            temp_model = GetProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectSprintInfoRequest(TeaModel):
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


class GetProjectSprintInfoResponseBodyObjectPlanToDo(TeaModel):
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


class GetProjectSprintInfoResponseBodyObject(TeaModel):
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
        plan_to_do: GetProjectSprintInfoResponseBodyObjectPlanToDo = None,
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
            temp_model = GetProjectSprintInfoResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectSprintInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetProjectSprintInfoResponseBodyObject = None,
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
            temp_model = GetProjectSprintInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetProjectSprintInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectSprintInfoResponseBody = None,
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
            temp_model = GetProjectSprintInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectTaskInfoRequest(TeaModel):
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


class GetProjectTaskInfoResponseBodyObject(TeaModel):
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


class GetProjectTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetProjectTaskInfoResponseBodyObject = None,
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
            temp_model = GetProjectTaskInfoResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetProjectTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectTaskInfoResponseBody = None,
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
            temp_model = GetProjectTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserByUidRequest(TeaModel):
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


class GetUserByUidResponseBodyObject(TeaModel):
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


class GetUserByUidResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: GetUserByUidResponseBodyObject = None,
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
            temp_model = GetUserByUidResponseBodyObject()
            self.object = temp_model.from_map(m['Object'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class GetUserByUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserByUidResponseBody = None,
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
            temp_model = GetUserByUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertDevopsMemberRequest(TeaModel):
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


class InsertDevopsMemberResponseBody(TeaModel):
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


class InsertDevopsMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertDevopsMemberResponseBody = None,
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
            temp_model = InsertDevopsMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectSprintsRequest(TeaModel):
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


class ListProjectSprintsResponseBodyObjectPlanToDo(TeaModel):
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


class ListProjectSprintsResponseBodyObject(TeaModel):
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
        plan_to_do: ListProjectSprintsResponseBodyObjectPlanToDo = None,
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
            temp_model = ListProjectSprintsResponseBodyObjectPlanToDo()
            self.plan_to_do = temp_model.from_map(m['PlanToDo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListProjectSprintsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListProjectSprintsResponseBodyObject] = None,
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
                temp_model = ListProjectSprintsResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListProjectSprintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectSprintsResponseBody = None,
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
            temp_model = ListProjectSprintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectTaskFlowRequest(TeaModel):
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


class ListProjectTaskFlowResponseBodyObject(TeaModel):
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


class ListProjectTaskFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListProjectTaskFlowResponseBodyObject] = None,
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
                temp_model = ListProjectTaskFlowResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListProjectTaskFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectTaskFlowResponseBody = None,
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
            temp_model = ListProjectTaskFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectTaskFlowStatusRequest(TeaModel):
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


class ListProjectTaskFlowStatusResponseBodyObject(TeaModel):
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


class ListProjectTaskFlowStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListProjectTaskFlowStatusResponseBodyObject] = None,
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
                temp_model = ListProjectTaskFlowStatusResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListProjectTaskFlowStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectTaskFlowStatusResponseBody = None,
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
            temp_model = ListProjectTaskFlowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectTasksRequest(TeaModel):
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


class ListProjectTasksResponseBodyObject(TeaModel):
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


class ListProjectTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListProjectTasksResponseBodyObject] = None,
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
                temp_model = ListProjectTasksResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListProjectTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectTasksResponseBody = None,
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
            temp_model = ListProjectTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenarioFieldConfigRequest(TeaModel):
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


class ListScenarioFieldConfigResponseBodyObject(TeaModel):
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


class ListScenarioFieldConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_msg: str = None,
        object: List[ListScenarioFieldConfigResponseBodyObject] = None,
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
                temp_model = ListScenarioFieldConfigResponseBodyObject()
                self.object.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Successful') is not None:
            self.successful = m.get('Successful')
        return self


class ListScenarioFieldConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScenarioFieldConfigResponseBody = None,
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
            temp_model = ListScenarioFieldConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
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


class UpdateProjectResponseBody(TeaModel):
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


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectSprintRequest(TeaModel):
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


class UpdateProjectSprintResponseBody(TeaModel):
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


class UpdateProjectSprintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectSprintResponseBody = None,
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
            temp_model = UpdateProjectSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectTaskRequest(TeaModel):
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


class UpdateProjectTaskResponseBody(TeaModel):
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


class UpdateProjectTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectTaskResponseBody = None,
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
            temp_model = UpdateProjectTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


