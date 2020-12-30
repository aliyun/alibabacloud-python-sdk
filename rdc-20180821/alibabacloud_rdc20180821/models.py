# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddEnterpriseMemberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        staff_id: str = None,
        operator: str = None,
    ):
        self.instance_id = instance_id
        self.staff_id = staff_id
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.staff_id is not None:
            result['StaffId'] = self.staff_id
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StaffId') is not None:
            self.staff_id = m.get('StaffId')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class AddEnterpriseMemberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddEnterpriseMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddEnterpriseMemberResponseBody = None,
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
            temp_model = AddEnterpriseMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRamMemberRequest(TeaModel):
    def __init__(
        self,
        corp_identifier: str = None,
        staff_identifier: str = None,
    ):
        self.corp_identifier = corp_identifier
        self.staff_identifier = staff_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.staff_identifier is not None:
            result['StaffIdentifier'] = self.staff_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('StaffIdentifier') is not None:
            self.staff_identifier = m.get('StaffIdentifier')
        return self


class AddRamMemberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRamMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRamMemberResponseBody = None,
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
            temp_model = AddRamMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveJoinCompanyRequest(TeaModel):
    def __init__(
        self,
        corp_identifier: str = None,
        application_ids: str = None,
    ):
        self.corp_identifier = corp_identifier
        self.application_ids = application_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        return self


class ApproveJoinCompanyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApproveJoinCompanyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveJoinCompanyResponseBody = None,
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
            temp_model = ApproveJoinCompanyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnterpriseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        emails: Dict[str, Any] = None,
        domain: str = None,
        creator_staff_id: str = None,
    ):
        self.name = name
        self.description = description
        self.emails = emails
        self.domain = domain
        self.creator_staff_id = creator_staff_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.creator_staff_id is not None:
            result['CreatorStaffId'] = self.creator_staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CreatorStaffId') is not None:
            self.creator_staff_id = m.get('CreatorStaffId')
        return self


class CreateEnterpriseShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        emails_shrink: str = None,
        domain: str = None,
        creator_staff_id: str = None,
    ):
        self.name = name
        self.description = description
        self.emails_shrink = emails_shrink
        self.domain = domain
        self.creator_staff_id = creator_staff_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.emails_shrink is not None:
            result['Emails'] = self.emails_shrink
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.creator_staff_id is not None:
            result['CreatorStaffId'] = self.creator_staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Emails') is not None:
            self.emails_shrink = m.get('Emails')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CreatorStaffId') is not None:
            self.creator_staff_id = m.get('CreatorStaffId')
        return self


class CreateEnterpriseResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        prohibit_code: int = None,
        identifier: str = None,
        name: str = None,
        id: int = None,
    ):
        self.status = status
        self.type = type
        self.prohibit_code = prohibit_code
        self.identifier = identifier
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.prohibit_code is not None:
            result['ProhibitCode'] = self.prohibit_code
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProhibitCode') is not None:
            self.prohibit_code = m.get('ProhibitCode')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateEnterpriseResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateEnterpriseResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateEnterpriseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEnterpriseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnterpriseResponseBody = None,
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
            temp_model = CreateEnterpriseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkitemRequest(TeaModel):
    def __init__(
        self,
        corp_identifier: str = None,
        author: str = None,
        assigned_to: str = None,
        template_id: int = None,
        subject: str = None,
        description: str = None,
        stamp: str = None,
        akproject_id: int = None,
        cf_list: str = None,
        verifier: str = None,
        priority_id: int = None,
        serious_level_id: int = None,
        watcher_users: str = None,
        module_ids: str = None,
    ):
        self.corp_identifier = corp_identifier
        self.author = author
        self.assigned_to = assigned_to
        self.template_id = template_id
        self.subject = subject
        self.description = description
        self.stamp = stamp
        self.akproject_id = akproject_id
        self.cf_list = cf_list
        self.verifier = verifier
        self.priority_id = priority_id
        self.serious_level_id = serious_level_id
        self.watcher_users = watcher_users
        self.module_ids = module_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.author is not None:
            result['Author'] = self.author
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.description is not None:
            result['Description'] = self.description
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.akproject_id is not None:
            result['AKProjectId'] = self.akproject_id
        if self.cf_list is not None:
            result['CfList'] = self.cf_list
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id
        if self.serious_level_id is not None:
            result['SeriousLevelId'] = self.serious_level_id
        if self.watcher_users is not None:
            result['WatcherUsers'] = self.watcher_users
        if self.module_ids is not None:
            result['ModuleIds'] = self.module_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('AKProjectId') is not None:
            self.akproject_id = m.get('AKProjectId')
        if m.get('CfList') is not None:
            self.cf_list = m.get('CfList')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')
        if m.get('SeriousLevelId') is not None:
            self.serious_level_id = m.get('SeriousLevelId')
        if m.get('WatcherUsers') is not None:
            self.watcher_users = m.get('WatcherUsers')
        if m.get('ModuleIds') is not None:
            self.module_ids = m.get('ModuleIds')
        return self


class CreateWorkitemResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: int = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateWorkitemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWorkitemResponseBody = None,
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
            temp_model = CreateWorkitemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindedUserByDingIdRequest(TeaModel):
    def __init__(
        self,
        ding_id: str = None,
    ):
        self.ding_id = ding_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ding_id is not None:
            result['DingId'] = self.ding_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingId') is not None:
            self.ding_id = m.get('DingId')
        return self


class GetBindedUserByDingIdResponseBodyDataDingtalkUser(TeaModel):
    def __init__(
        self,
        dingtalk_user_id: int = None,
        ding_id: str = None,
        union_id: str = None,
        nick: str = None,
        code_user_name: str = None,
        id: int = None,
    ):
        self.dingtalk_user_id = dingtalk_user_id
        self.ding_id = ding_id
        self.union_id = union_id
        self.nick = nick
        self.code_user_name = code_user_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dingtalk_user_id is not None:
            result['DingtalkUserId'] = self.dingtalk_user_id
        if self.ding_id is not None:
            result['DingId'] = self.ding_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.code_user_name is not None:
            result['CodeUserName'] = self.code_user_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingtalkUserId') is not None:
            self.dingtalk_user_id = m.get('DingtalkUserId')
        if m.get('DingId') is not None:
            self.ding_id = m.get('DingId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('CodeUserName') is not None:
            self.code_user_name = m.get('CodeUserName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetBindedUserByDingIdResponseBodyDataUserProfileDTO(TeaModel):
    def __init__(
        self,
        data_source: str = None,
        avatar: str = None,
        email: str = None,
        mobile: str = None,
        user_id: int = None,
        created_at: int = None,
        english_name: str = None,
        nick_name: str = None,
        name: str = None,
    ):
        self.data_source = data_source
        self.avatar = avatar
        self.email = email
        self.mobile = mobile
        self.user_id = user_id
        self.created_at = created_at
        self.english_name = english_name
        self.nick_name = nick_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetBindedUserByDingIdResponseBodyDataAliyunUser(TeaModel):
    def __init__(
        self,
        email: str = None,
        havana_id: str = None,
        taobao_nick: str = None,
        kp: str = None,
        realname: str = None,
        nick_name: str = None,
        account_structure: int = None,
        aliyun_id: str = None,
        id: int = None,
    ):
        self.email = email
        self.havana_id = havana_id
        self.taobao_nick = taobao_nick
        self.kp = kp
        self.realname = realname
        self.nick_name = nick_name
        self.account_structure = account_structure
        self.aliyun_id = aliyun_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id
        if self.taobao_nick is not None:
            result['TaobaoNick'] = self.taobao_nick
        if self.kp is not None:
            result['Kp'] = self.kp
        if self.realname is not None:
            result['Realname'] = self.realname
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.account_structure is not None:
            result['AccountStructure'] = self.account_structure
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')
        if m.get('TaobaoNick') is not None:
            self.taobao_nick = m.get('TaobaoNick')
        if m.get('Kp') is not None:
            self.kp = m.get('Kp')
        if m.get('Realname') is not None:
            self.realname = m.get('Realname')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('AccountStructure') is not None:
            self.account_structure = m.get('AccountStructure')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetBindedUserByDingIdResponseBodyData(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        guid: str = None,
        dingtalk_user: GetBindedUserByDingIdResponseBodyDataDingtalkUser = None,
        user_profile_dto: GetBindedUserByDingIdResponseBodyDataUserProfileDTO = None,
        nick_name: str = None,
        main_account_type: str = None,
        aliyun_user: GetBindedUserByDingIdResponseBodyDataAliyunUser = None,
        is_valid: bool = None,
        id: int = None,
    ):
        self.uuid = uuid
        self.guid = guid
        self.dingtalk_user = dingtalk_user
        self.user_profile_dto = user_profile_dto
        self.nick_name = nick_name
        self.main_account_type = main_account_type
        self.aliyun_user = aliyun_user
        self.is_valid = is_valid
        self.id = id

    def validate(self):
        if self.dingtalk_user:
            self.dingtalk_user.validate()
        if self.user_profile_dto:
            self.user_profile_dto.validate()
        if self.aliyun_user:
            self.aliyun_user.validate()

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.guid is not None:
            result['Guid'] = self.guid
        if self.dingtalk_user is not None:
            result['DingtalkUser'] = self.dingtalk_user.to_map()
        if self.user_profile_dto is not None:
            result['UserProfileDTO'] = self.user_profile_dto.to_map()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.main_account_type is not None:
            result['MainAccountType'] = self.main_account_type
        if self.aliyun_user is not None:
            result['AliyunUser'] = self.aliyun_user.to_map()
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        if m.get('DingtalkUser') is not None:
            temp_model = GetBindedUserByDingIdResponseBodyDataDingtalkUser()
            self.dingtalk_user = temp_model.from_map(m['DingtalkUser'])
        if m.get('UserProfileDTO') is not None:
            temp_model = GetBindedUserByDingIdResponseBodyDataUserProfileDTO()
            self.user_profile_dto = temp_model.from_map(m['UserProfileDTO'])
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('MainAccountType') is not None:
            self.main_account_type = m.get('MainAccountType')
        if m.get('AliyunUser') is not None:
            temp_model = GetBindedUserByDingIdResponseBodyDataAliyunUser()
            self.aliyun_user = temp_model.from_map(m['AliyunUser'])
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetBindedUserByDingIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetBindedUserByDingIdResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetBindedUserByDingIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBindedUserByDingIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBindedUserByDingIdResponseBody = None,
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
            temp_model = GetBindedUserByDingIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChangeLogRequest(TeaModel):
    def __init__(
        self,
        target_type: str = None,
        target_ids: Dict[str, Any] = None,
        corp_identifier: str = None,
    ):
        self.target_type = target_type
        self.target_ids = target_ids
        self.corp_identifier = corp_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        return self


class GetChangeLogShrinkRequest(TeaModel):
    def __init__(
        self,
        target_type: str = None,
        target_ids_shrink: str = None,
        corp_identifier: str = None,
    ):
        self.target_type = target_type
        self.target_ids_shrink = target_ids_shrink
        self.corp_identifier = corp_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_ids_shrink is not None:
            result['TargetIds'] = self.target_ids_shrink
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetIds') is not None:
            self.target_ids_shrink = m.get('TargetIds')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        return self


class GetChangeLogResponseBodyData(TeaModel):
    def __init__(
        self,
        old_value: str = None,
        property_type: str = None,
        property_key: str = None,
        target_id: int = None,
        other: str = None,
        new_value: str = None,
        target_type: str = None,
    ):
        self.old_value = old_value
        self.property_type = property_type
        self.property_key = property_key
        self.target_id = target_id
        self.other = other
        self.new_value = new_value
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.property_type is not None:
            result['PropertyType'] = self.property_type
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.other is not None:
            result['Other'] = self.other
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('Other') is not None:
            self.other = m.get('Other')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetChangeLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetChangeLogResponseBodyData] = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChangeLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetChangeLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetChangeLogResponseBody = None,
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
            temp_model = GetChangeLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomFieldsByTemplateIdRequest(TeaModel):
    def __init__(
        self,
        akproject_id: int = None,
        template_id: int = None,
        corp_identifier: str = None,
    ):
        self.akproject_id = akproject_id
        self.template_id = template_id
        self.corp_identifier = corp_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.akproject_id is not None:
            result['AKProjectId'] = self.akproject_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AKProjectId') is not None:
            self.akproject_id = m.get('AKProjectId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        return self


class GetCustomFieldsByTemplateIdResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        editable: bool = None,
        created_at: int = None,
        is_remember: bool = None,
        is_delete: bool = None,
        default_value: str = None,
        max_length: int = None,
        field_format: str = None,
        description: str = None,
        dynamic: bool = None,
        is_required: bool = None,
        name_i18n: str = None,
        possible_values: str = None,
        min_length: int = None,
        updated_at: int = None,
        name: str = None,
        other: str = None,
        id: int = None,
    ):
        self.type = type
        self.editable = editable
        self.created_at = created_at
        self.is_remember = is_remember
        self.is_delete = is_delete
        self.default_value = default_value
        self.max_length = max_length
        self.field_format = field_format
        self.description = description
        self.dynamic = dynamic
        self.is_required = is_required
        self.name_i18n = name_i18n
        self.possible_values = possible_values
        self.min_length = min_length
        self.updated_at = updated_at
        self.name = name
        self.other = other
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.editable is not None:
            result['Editable'] = self.editable
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.is_remember is not None:
            result['IsRemember'] = self.is_remember
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.field_format is not None:
            result['FieldFormat'] = self.field_format
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.is_required is not None:
            result['IsRequired'] = self.is_required
        if self.name_i18n is not None:
            result['NameI18N'] = self.name_i18n
        if self.possible_values is not None:
            result['PossibleValues'] = self.possible_values
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.other is not None:
            result['Other'] = self.other
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Editable') is not None:
            self.editable = m.get('Editable')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('IsRemember') is not None:
            self.is_remember = m.get('IsRemember')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('FieldFormat') is not None:
            self.field_format = m.get('FieldFormat')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('IsRequired') is not None:
            self.is_required = m.get('IsRequired')
        if m.get('NameI18N') is not None:
            self.name_i18n = m.get('NameI18N')
        if m.get('PossibleValues') is not None:
            self.possible_values = m.get('PossibleValues')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Other') is not None:
            self.other = m.get('Other')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetCustomFieldsByTemplateIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetCustomFieldsByTemplateIdResponseBodyData] = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCustomFieldsByTemplateIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomFieldsByTemplateIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCustomFieldsByTemplateIdResponseBody = None,
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
            temp_model = GetCustomFieldsByTemplateIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIssueByIdRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        corp_identifier: str = None,
    ):
        self.id = id
        self.corp_identifier = corp_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        return self


class GetIssueByIdResponseBodyDataCfsList(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        name: str = None,
        id: str = None,
    ):
        self.type = type
        self.value = value
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetIssueByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        skip_collab: bool = None,
        send_wangwang: bool = None,
        version_list: str = None,
        ak_project_id: int = None,
        user_id: int = None,
        id_path: str = None,
        ignore_integrate: bool = None,
        attachment_ids: str = None,
        commit_date: int = None,
        update_status_at: int = None,
        trackers: str = None,
        subject: str = None,
        user_staff_id: str = None,
        attachment_list: str = None,
        verifier_id: int = None,
        ignore_check: bool = None,
        module_list: str = None,
        attachmented: bool = None,
        serious_level_id: int = None,
        tag_id_list: str = None,
        watched: bool = None,
        assigned_to: str = None,
        assigned_to_ids: str = None,
        priority_id: int = None,
        record_change_log: bool = None,
        updated_at: int = None,
        template_id: int = None,
        verifier: str = None,
        status: str = None,
        related_user_ids: str = None,
        related_akproject_ids: str = None,
        related_akproject_guids: str = None,
        created_at: int = None,
        assigned_to_id_list: str = None,
        cfs_list: List[GetIssueByIdResponseBodyDataCfsList] = None,
        priority: str = None,
        status_stage: int = None,
        assigned_to_staff_id: str = None,
        parent_id: int = None,
        description: str = None,
        logical_status: str = None,
        version_ids: str = None,
        serious_level: str = None,
        status_id: int = None,
        stamp: str = None,
        user: str = None,
        tracker_ids: str = None,
        assigned_to_id: int = None,
        change_log_list: str = None,
        issue_type_id: int = None,
        region_id: int = None,
        guid: str = None,
        assigned_to_maps: str = None,
        black_list_notice: str = None,
        module_updated: bool = None,
        project_ids: str = None,
        comment_list: str = None,
        verifier_staff_id: str = None,
        module_ids: str = None,
        id: int = None,
    ):
        self.skip_collab = skip_collab
        self.send_wangwang = send_wangwang
        self.version_list = version_list
        self.ak_project_id = ak_project_id
        self.user_id = user_id
        self.id_path = id_path
        self.ignore_integrate = ignore_integrate
        self.attachment_ids = attachment_ids
        self.commit_date = commit_date
        self.update_status_at = update_status_at
        self.trackers = trackers
        self.subject = subject
        self.user_staff_id = user_staff_id
        self.attachment_list = attachment_list
        self.verifier_id = verifier_id
        self.ignore_check = ignore_check
        self.module_list = module_list
        self.attachmented = attachmented
        self.serious_level_id = serious_level_id
        self.tag_id_list = tag_id_list
        self.watched = watched
        self.assigned_to = assigned_to
        self.assigned_to_ids = assigned_to_ids
        self.priority_id = priority_id
        self.record_change_log = record_change_log
        self.updated_at = updated_at
        self.template_id = template_id
        self.verifier = verifier
        self.status = status
        self.related_user_ids = related_user_ids
        self.related_akproject_ids = related_akproject_ids
        self.related_akproject_guids = related_akproject_guids
        self.created_at = created_at
        self.assigned_to_id_list = assigned_to_id_list
        self.cfs_list = cfs_list
        self.priority = priority
        self.status_stage = status_stage
        self.assigned_to_staff_id = assigned_to_staff_id
        self.parent_id = parent_id
        self.description = description
        self.logical_status = logical_status
        self.version_ids = version_ids
        self.serious_level = serious_level
        self.status_id = status_id
        self.stamp = stamp
        self.user = user
        self.tracker_ids = tracker_ids
        self.assigned_to_id = assigned_to_id
        self.change_log_list = change_log_list
        self.issue_type_id = issue_type_id
        self.region_id = region_id
        self.guid = guid
        self.assigned_to_maps = assigned_to_maps
        self.black_list_notice = black_list_notice
        self.module_updated = module_updated
        self.project_ids = project_ids
        self.comment_list = comment_list
        self.verifier_staff_id = verifier_staff_id
        self.module_ids = module_ids
        self.id = id

    def validate(self):
        if self.cfs_list:
            for k in self.cfs_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.skip_collab is not None:
            result['SkipCollab'] = self.skip_collab
        if self.send_wangwang is not None:
            result['SendWangwang'] = self.send_wangwang
        if self.version_list is not None:
            result['VersionList'] = self.version_list
        if self.ak_project_id is not None:
            result['AkProjectId'] = self.ak_project_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.id_path is not None:
            result['IdPath'] = self.id_path
        if self.ignore_integrate is not None:
            result['IgnoreIntegrate'] = self.ignore_integrate
        if self.attachment_ids is not None:
            result['AttachmentIds'] = self.attachment_ids
        if self.commit_date is not None:
            result['CommitDate'] = self.commit_date
        if self.update_status_at is not None:
            result['UpdateStatusAt'] = self.update_status_at
        if self.trackers is not None:
            result['Trackers'] = self.trackers
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.user_staff_id is not None:
            result['UserStaffId'] = self.user_staff_id
        if self.attachment_list is not None:
            result['AttachmentList'] = self.attachment_list
        if self.verifier_id is not None:
            result['VerifierId'] = self.verifier_id
        if self.ignore_check is not None:
            result['IgnoreCheck'] = self.ignore_check
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.attachmented is not None:
            result['Attachmented'] = self.attachmented
        if self.serious_level_id is not None:
            result['SeriousLevelId'] = self.serious_level_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.watched is not None:
            result['Watched'] = self.watched
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.assigned_to_ids is not None:
            result['AssignedToIds'] = self.assigned_to_ids
        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id
        if self.record_change_log is not None:
            result['RecordChangeLog'] = self.record_change_log
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.status is not None:
            result['Status'] = self.status
        if self.related_user_ids is not None:
            result['RelatedUserIds'] = self.related_user_ids
        if self.related_akproject_ids is not None:
            result['RelatedAKProjectIds'] = self.related_akproject_ids
        if self.related_akproject_guids is not None:
            result['RelatedAKProjectGuids'] = self.related_akproject_guids
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.assigned_to_id_list is not None:
            result['AssignedToIdList'] = self.assigned_to_id_list
        result['CfsList'] = []
        if self.cfs_list is not None:
            for k in self.cfs_list:
                result['CfsList'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status_stage is not None:
            result['StatusStage'] = self.status_stage
        if self.assigned_to_staff_id is not None:
            result['AssignedToStaffId'] = self.assigned_to_staff_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.logical_status is not None:
            result['LogicalStatus'] = self.logical_status
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids
        if self.serious_level is not None:
            result['SeriousLevel'] = self.serious_level
        if self.status_id is not None:
            result['StatusId'] = self.status_id
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.user is not None:
            result['User'] = self.user
        if self.tracker_ids is not None:
            result['TrackerIds'] = self.tracker_ids
        if self.assigned_to_id is not None:
            result['AssignedToId'] = self.assigned_to_id
        if self.change_log_list is not None:
            result['ChangeLogList'] = self.change_log_list
        if self.issue_type_id is not None:
            result['IssueTypeId'] = self.issue_type_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.guid is not None:
            result['Guid'] = self.guid
        if self.assigned_to_maps is not None:
            result['AssignedToMaps'] = self.assigned_to_maps
        if self.black_list_notice is not None:
            result['BlackListNotice'] = self.black_list_notice
        if self.module_updated is not None:
            result['ModuleUpdated'] = self.module_updated
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.comment_list is not None:
            result['CommentList'] = self.comment_list
        if self.verifier_staff_id is not None:
            result['VerifierStaffId'] = self.verifier_staff_id
        if self.module_ids is not None:
            result['ModuleIds'] = self.module_ids
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipCollab') is not None:
            self.skip_collab = m.get('SkipCollab')
        if m.get('SendWangwang') is not None:
            self.send_wangwang = m.get('SendWangwang')
        if m.get('VersionList') is not None:
            self.version_list = m.get('VersionList')
        if m.get('AkProjectId') is not None:
            self.ak_project_id = m.get('AkProjectId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('IdPath') is not None:
            self.id_path = m.get('IdPath')
        if m.get('IgnoreIntegrate') is not None:
            self.ignore_integrate = m.get('IgnoreIntegrate')
        if m.get('AttachmentIds') is not None:
            self.attachment_ids = m.get('AttachmentIds')
        if m.get('CommitDate') is not None:
            self.commit_date = m.get('CommitDate')
        if m.get('UpdateStatusAt') is not None:
            self.update_status_at = m.get('UpdateStatusAt')
        if m.get('Trackers') is not None:
            self.trackers = m.get('Trackers')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('UserStaffId') is not None:
            self.user_staff_id = m.get('UserStaffId')
        if m.get('AttachmentList') is not None:
            self.attachment_list = m.get('AttachmentList')
        if m.get('VerifierId') is not None:
            self.verifier_id = m.get('VerifierId')
        if m.get('IgnoreCheck') is not None:
            self.ignore_check = m.get('IgnoreCheck')
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Attachmented') is not None:
            self.attachmented = m.get('Attachmented')
        if m.get('SeriousLevelId') is not None:
            self.serious_level_id = m.get('SeriousLevelId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Watched') is not None:
            self.watched = m.get('Watched')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('AssignedToIds') is not None:
            self.assigned_to_ids = m.get('AssignedToIds')
        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')
        if m.get('RecordChangeLog') is not None:
            self.record_change_log = m.get('RecordChangeLog')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RelatedUserIds') is not None:
            self.related_user_ids = m.get('RelatedUserIds')
        if m.get('RelatedAKProjectIds') is not None:
            self.related_akproject_ids = m.get('RelatedAKProjectIds')
        if m.get('RelatedAKProjectGuids') is not None:
            self.related_akproject_guids = m.get('RelatedAKProjectGuids')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AssignedToIdList') is not None:
            self.assigned_to_id_list = m.get('AssignedToIdList')
        self.cfs_list = []
        if m.get('CfsList') is not None:
            for k in m.get('CfsList'):
                temp_model = GetIssueByIdResponseBodyDataCfsList()
                self.cfs_list.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('StatusStage') is not None:
            self.status_stage = m.get('StatusStage')
        if m.get('AssignedToStaffId') is not None:
            self.assigned_to_staff_id = m.get('AssignedToStaffId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LogicalStatus') is not None:
            self.logical_status = m.get('LogicalStatus')
        if m.get('VersionIds') is not None:
            self.version_ids = m.get('VersionIds')
        if m.get('SeriousLevel') is not None:
            self.serious_level = m.get('SeriousLevel')
        if m.get('StatusId') is not None:
            self.status_id = m.get('StatusId')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('TrackerIds') is not None:
            self.tracker_ids = m.get('TrackerIds')
        if m.get('AssignedToId') is not None:
            self.assigned_to_id = m.get('AssignedToId')
        if m.get('ChangeLogList') is not None:
            self.change_log_list = m.get('ChangeLogList')
        if m.get('IssueTypeId') is not None:
            self.issue_type_id = m.get('IssueTypeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        if m.get('AssignedToMaps') is not None:
            self.assigned_to_maps = m.get('AssignedToMaps')
        if m.get('BlackListNotice') is not None:
            self.black_list_notice = m.get('BlackListNotice')
        if m.get('ModuleUpdated') is not None:
            self.module_updated = m.get('ModuleUpdated')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('CommentList') is not None:
            self.comment_list = m.get('CommentList')
        if m.get('VerifierStaffId') is not None:
            self.verifier_staff_id = m.get('VerifierStaffId')
        if m.get('ModuleIds') is not None:
            self.module_ids = m.get('ModuleIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetIssueByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetIssueByIdResponseBodyData = None,
        code: int = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetIssueByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIssueByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIssueByIdResponseBody = None,
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
            temp_model = GetIssueByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJoinCodeRequest(TeaModel):
    def __init__(
        self,
        corp_identifier: str = None,
    ):
        self.corp_identifier = corp_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        return self


class GetJoinCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetJoinCodeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetJoinCodeResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetJoinCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJoinCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJoinCodeResponseBody = None,
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
            temp_model = GetJoinCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectMembersRequest(TeaModel):
    def __init__(
        self,
        corp_identifier: str = None,
        project_id: int = None,
        staff_id: str = None,
    ):
        self.corp_identifier = corp_identifier
        self.project_id = project_id
        self.staff_id = staff_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.staff_id is not None:
            result['StaffId'] = self.staff_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StaffId') is not None:
            self.staff_id = m.get('StaffId')
        return self


class GetProjectMembersResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        email: str = None,
        real_name: str = None,
        staff_id: str = None,
        nick_name: str = None,
        id: int = None,
    ):
        self.avatar = avatar
        self.email = email
        self.real_name = real_name
        self.staff_id = staff_id
        self.nick_name = nick_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.email is not None:
            result['Email'] = self.email
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.staff_id is not None:
            result['StaffId'] = self.staff_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('StaffId') is not None:
            self.staff_id = m.get('StaffId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectMembersResponseBodyData(TeaModel):
    def __init__(
        self,
        identifier: str = None,
        users: List[GetProjectMembersResponseBodyDataUsers] = None,
        name: str = None,
        id: int = None,
    ):
        self.identifier = identifier
        self.users = users
        self.name = name
        self.id = id

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = GetProjectMembersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectMembersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetProjectMembersResponseBodyData] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetProjectMembersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class GetUserByAliyunPkRequest(TeaModel):
    def __init__(
        self,
        pk: str = None,
    ):
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class GetUserByAliyunPkResponseBodyDataDingtalkUser(TeaModel):
    def __init__(
        self,
        dingtalk_user_id: int = None,
        ding_id: str = None,
        union_id: str = None,
        nick: str = None,
        code_user_name: str = None,
        id: int = None,
    ):
        self.dingtalk_user_id = dingtalk_user_id
        self.ding_id = ding_id
        self.union_id = union_id
        self.nick = nick
        self.code_user_name = code_user_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dingtalk_user_id is not None:
            result['DingtalkUserId'] = self.dingtalk_user_id
        if self.ding_id is not None:
            result['DingId'] = self.ding_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.code_user_name is not None:
            result['CodeUserName'] = self.code_user_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingtalkUserId') is not None:
            self.dingtalk_user_id = m.get('DingtalkUserId')
        if m.get('DingId') is not None:
            self.ding_id = m.get('DingId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('CodeUserName') is not None:
            self.code_user_name = m.get('CodeUserName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserByAliyunPkResponseBodyDataUserProfileDTO(TeaModel):
    def __init__(
        self,
        data_source: str = None,
        avatar: str = None,
        email: str = None,
        mobile: str = None,
        user_id: int = None,
        created_at: int = None,
        english_name: str = None,
        nick_name: str = None,
        name: str = None,
    ):
        self.data_source = data_source
        self.avatar = avatar
        self.email = email
        self.mobile = mobile
        self.user_id = user_id
        self.created_at = created_at
        self.english_name = english_name
        self.nick_name = nick_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetUserByAliyunPkResponseBodyDataAliyunUser(TeaModel):
    def __init__(
        self,
        email: str = None,
        havana_id: str = None,
        taobao_nick: str = None,
        kp: str = None,
        realname: str = None,
        nick_name: str = None,
        account_structure: int = None,
        aliyun_id: str = None,
        id: int = None,
    ):
        self.email = email
        self.havana_id = havana_id
        self.taobao_nick = taobao_nick
        self.kp = kp
        self.realname = realname
        self.nick_name = nick_name
        self.account_structure = account_structure
        self.aliyun_id = aliyun_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id
        if self.taobao_nick is not None:
            result['TaobaoNick'] = self.taobao_nick
        if self.kp is not None:
            result['Kp'] = self.kp
        if self.realname is not None:
            result['Realname'] = self.realname
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.account_structure is not None:
            result['AccountStructure'] = self.account_structure
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')
        if m.get('TaobaoNick') is not None:
            self.taobao_nick = m.get('TaobaoNick')
        if m.get('Kp') is not None:
            self.kp = m.get('Kp')
        if m.get('Realname') is not None:
            self.realname = m.get('Realname')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('AccountStructure') is not None:
            self.account_structure = m.get('AccountStructure')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserByAliyunPkResponseBodyData(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        guid: str = None,
        dingtalk_user: GetUserByAliyunPkResponseBodyDataDingtalkUser = None,
        user_profile_dto: GetUserByAliyunPkResponseBodyDataUserProfileDTO = None,
        nick_name: str = None,
        main_account_type: str = None,
        aliyun_user: GetUserByAliyunPkResponseBodyDataAliyunUser = None,
        is_valid: bool = None,
        id: int = None,
    ):
        self.uuid = uuid
        self.guid = guid
        self.dingtalk_user = dingtalk_user
        self.user_profile_dto = user_profile_dto
        self.nick_name = nick_name
        self.main_account_type = main_account_type
        self.aliyun_user = aliyun_user
        self.is_valid = is_valid
        self.id = id

    def validate(self):
        if self.dingtalk_user:
            self.dingtalk_user.validate()
        if self.user_profile_dto:
            self.user_profile_dto.validate()
        if self.aliyun_user:
            self.aliyun_user.validate()

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.guid is not None:
            result['Guid'] = self.guid
        if self.dingtalk_user is not None:
            result['DingtalkUser'] = self.dingtalk_user.to_map()
        if self.user_profile_dto is not None:
            result['UserProfileDTO'] = self.user_profile_dto.to_map()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.main_account_type is not None:
            result['MainAccountType'] = self.main_account_type
        if self.aliyun_user is not None:
            result['AliyunUser'] = self.aliyun_user.to_map()
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        if m.get('DingtalkUser') is not None:
            temp_model = GetUserByAliyunPkResponseBodyDataDingtalkUser()
            self.dingtalk_user = temp_model.from_map(m['DingtalkUser'])
        if m.get('UserProfileDTO') is not None:
            temp_model = GetUserByAliyunPkResponseBodyDataUserProfileDTO()
            self.user_profile_dto = temp_model.from_map(m['UserProfileDTO'])
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('MainAccountType') is not None:
            self.main_account_type = m.get('MainAccountType')
        if m.get('AliyunUser') is not None:
            temp_model = GetUserByAliyunPkResponseBodyDataAliyunUser()
            self.aliyun_user = temp_model.from_map(m['AliyunUser'])
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserByAliyunPkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetUserByAliyunPkResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetUserByAliyunPkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserByAliyunPkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserByAliyunPkResponseBody = None,
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
            temp_model = GetUserByAliyunPkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkitemByIdRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        corp_identifier: str = None,
    ):
        self.id = id
        self.corp_identifier = corp_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        return self


class GetWorkitemByIdResponseBodyDataCfsList(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        name: str = None,
        id: str = None,
    ):
        self.type = type
        self.value = value
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetWorkitemByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        skip_collab: bool = None,
        send_wangwang: bool = None,
        version_list: str = None,
        ak_project_id: int = None,
        user_id: int = None,
        id_path: str = None,
        ignore_integrate: bool = None,
        attachment_ids: str = None,
        commit_date: int = None,
        update_status_at: int = None,
        trackers: str = None,
        subject: str = None,
        user_staff_id: str = None,
        attachment_list: str = None,
        verifier_id: int = None,
        ignore_check: bool = None,
        module_list: str = None,
        attachmented: bool = None,
        serious_level_id: int = None,
        tag_id_list: str = None,
        watched: bool = None,
        assigned_to: str = None,
        assigned_to_ids: str = None,
        priority_id: int = None,
        record_change_log: bool = None,
        updated_at: int = None,
        template_id: int = None,
        verifier: str = None,
        status: str = None,
        related_user_ids: str = None,
        related_akproject_ids: str = None,
        related_akproject_guids: str = None,
        created_at: int = None,
        assigned_to_id_list: str = None,
        cfs_list: List[GetWorkitemByIdResponseBodyDataCfsList] = None,
        priority: str = None,
        status_stage: int = None,
        assigned_to_staff_id: str = None,
        parent_id: int = None,
        description: str = None,
        logical_status: str = None,
        version_ids: str = None,
        serious_level: str = None,
        status_id: int = None,
        stamp: str = None,
        user: str = None,
        tracker_ids: str = None,
        assigned_to_id: int = None,
        change_log_list: str = None,
        issue_type_id: int = None,
        region_id: int = None,
        guid: str = None,
        assigned_to_maps: str = None,
        black_list_notice: str = None,
        module_updated: bool = None,
        project_ids: str = None,
        comment_list: str = None,
        verifier_staff_id: str = None,
        module_ids: str = None,
        id: int = None,
    ):
        self.skip_collab = skip_collab
        self.send_wangwang = send_wangwang
        self.version_list = version_list
        self.ak_project_id = ak_project_id
        self.user_id = user_id
        self.id_path = id_path
        self.ignore_integrate = ignore_integrate
        self.attachment_ids = attachment_ids
        self.commit_date = commit_date
        self.update_status_at = update_status_at
        self.trackers = trackers
        self.subject = subject
        self.user_staff_id = user_staff_id
        self.attachment_list = attachment_list
        self.verifier_id = verifier_id
        self.ignore_check = ignore_check
        self.module_list = module_list
        self.attachmented = attachmented
        self.serious_level_id = serious_level_id
        self.tag_id_list = tag_id_list
        self.watched = watched
        self.assigned_to = assigned_to
        self.assigned_to_ids = assigned_to_ids
        self.priority_id = priority_id
        self.record_change_log = record_change_log
        self.updated_at = updated_at
        self.template_id = template_id
        self.verifier = verifier
        self.status = status
        self.related_user_ids = related_user_ids
        self.related_akproject_ids = related_akproject_ids
        self.related_akproject_guids = related_akproject_guids
        self.created_at = created_at
        self.assigned_to_id_list = assigned_to_id_list
        self.cfs_list = cfs_list
        self.priority = priority
        self.status_stage = status_stage
        self.assigned_to_staff_id = assigned_to_staff_id
        self.parent_id = parent_id
        self.description = description
        self.logical_status = logical_status
        self.version_ids = version_ids
        self.serious_level = serious_level
        self.status_id = status_id
        self.stamp = stamp
        self.user = user
        self.tracker_ids = tracker_ids
        self.assigned_to_id = assigned_to_id
        self.change_log_list = change_log_list
        self.issue_type_id = issue_type_id
        self.region_id = region_id
        self.guid = guid
        self.assigned_to_maps = assigned_to_maps
        self.black_list_notice = black_list_notice
        self.module_updated = module_updated
        self.project_ids = project_ids
        self.comment_list = comment_list
        self.verifier_staff_id = verifier_staff_id
        self.module_ids = module_ids
        self.id = id

    def validate(self):
        if self.cfs_list:
            for k in self.cfs_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.skip_collab is not None:
            result['SkipCollab'] = self.skip_collab
        if self.send_wangwang is not None:
            result['SendWangwang'] = self.send_wangwang
        if self.version_list is not None:
            result['VersionList'] = self.version_list
        if self.ak_project_id is not None:
            result['AkProjectId'] = self.ak_project_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.id_path is not None:
            result['IdPath'] = self.id_path
        if self.ignore_integrate is not None:
            result['IgnoreIntegrate'] = self.ignore_integrate
        if self.attachment_ids is not None:
            result['AttachmentIds'] = self.attachment_ids
        if self.commit_date is not None:
            result['CommitDate'] = self.commit_date
        if self.update_status_at is not None:
            result['UpdateStatusAt'] = self.update_status_at
        if self.trackers is not None:
            result['Trackers'] = self.trackers
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.user_staff_id is not None:
            result['UserStaffId'] = self.user_staff_id
        if self.attachment_list is not None:
            result['AttachmentList'] = self.attachment_list
        if self.verifier_id is not None:
            result['VerifierId'] = self.verifier_id
        if self.ignore_check is not None:
            result['IgnoreCheck'] = self.ignore_check
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.attachmented is not None:
            result['Attachmented'] = self.attachmented
        if self.serious_level_id is not None:
            result['SeriousLevelId'] = self.serious_level_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.watched is not None:
            result['Watched'] = self.watched
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.assigned_to_ids is not None:
            result['AssignedToIds'] = self.assigned_to_ids
        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id
        if self.record_change_log is not None:
            result['RecordChangeLog'] = self.record_change_log
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.status is not None:
            result['Status'] = self.status
        if self.related_user_ids is not None:
            result['RelatedUserIds'] = self.related_user_ids
        if self.related_akproject_ids is not None:
            result['RelatedAKProjectIds'] = self.related_akproject_ids
        if self.related_akproject_guids is not None:
            result['RelatedAKProjectGuids'] = self.related_akproject_guids
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.assigned_to_id_list is not None:
            result['AssignedToIdList'] = self.assigned_to_id_list
        result['CfsList'] = []
        if self.cfs_list is not None:
            for k in self.cfs_list:
                result['CfsList'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status_stage is not None:
            result['StatusStage'] = self.status_stage
        if self.assigned_to_staff_id is not None:
            result['AssignedToStaffId'] = self.assigned_to_staff_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.logical_status is not None:
            result['LogicalStatus'] = self.logical_status
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids
        if self.serious_level is not None:
            result['SeriousLevel'] = self.serious_level
        if self.status_id is not None:
            result['StatusId'] = self.status_id
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.user is not None:
            result['User'] = self.user
        if self.tracker_ids is not None:
            result['TrackerIds'] = self.tracker_ids
        if self.assigned_to_id is not None:
            result['AssignedToId'] = self.assigned_to_id
        if self.change_log_list is not None:
            result['ChangeLogList'] = self.change_log_list
        if self.issue_type_id is not None:
            result['IssueTypeId'] = self.issue_type_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.guid is not None:
            result['Guid'] = self.guid
        if self.assigned_to_maps is not None:
            result['AssignedToMaps'] = self.assigned_to_maps
        if self.black_list_notice is not None:
            result['BlackListNotice'] = self.black_list_notice
        if self.module_updated is not None:
            result['ModuleUpdated'] = self.module_updated
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.comment_list is not None:
            result['CommentList'] = self.comment_list
        if self.verifier_staff_id is not None:
            result['VerifierStaffId'] = self.verifier_staff_id
        if self.module_ids is not None:
            result['ModuleIds'] = self.module_ids
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipCollab') is not None:
            self.skip_collab = m.get('SkipCollab')
        if m.get('SendWangwang') is not None:
            self.send_wangwang = m.get('SendWangwang')
        if m.get('VersionList') is not None:
            self.version_list = m.get('VersionList')
        if m.get('AkProjectId') is not None:
            self.ak_project_id = m.get('AkProjectId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('IdPath') is not None:
            self.id_path = m.get('IdPath')
        if m.get('IgnoreIntegrate') is not None:
            self.ignore_integrate = m.get('IgnoreIntegrate')
        if m.get('AttachmentIds') is not None:
            self.attachment_ids = m.get('AttachmentIds')
        if m.get('CommitDate') is not None:
            self.commit_date = m.get('CommitDate')
        if m.get('UpdateStatusAt') is not None:
            self.update_status_at = m.get('UpdateStatusAt')
        if m.get('Trackers') is not None:
            self.trackers = m.get('Trackers')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('UserStaffId') is not None:
            self.user_staff_id = m.get('UserStaffId')
        if m.get('AttachmentList') is not None:
            self.attachment_list = m.get('AttachmentList')
        if m.get('VerifierId') is not None:
            self.verifier_id = m.get('VerifierId')
        if m.get('IgnoreCheck') is not None:
            self.ignore_check = m.get('IgnoreCheck')
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Attachmented') is not None:
            self.attachmented = m.get('Attachmented')
        if m.get('SeriousLevelId') is not None:
            self.serious_level_id = m.get('SeriousLevelId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Watched') is not None:
            self.watched = m.get('Watched')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('AssignedToIds') is not None:
            self.assigned_to_ids = m.get('AssignedToIds')
        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')
        if m.get('RecordChangeLog') is not None:
            self.record_change_log = m.get('RecordChangeLog')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RelatedUserIds') is not None:
            self.related_user_ids = m.get('RelatedUserIds')
        if m.get('RelatedAKProjectIds') is not None:
            self.related_akproject_ids = m.get('RelatedAKProjectIds')
        if m.get('RelatedAKProjectGuids') is not None:
            self.related_akproject_guids = m.get('RelatedAKProjectGuids')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AssignedToIdList') is not None:
            self.assigned_to_id_list = m.get('AssignedToIdList')
        self.cfs_list = []
        if m.get('CfsList') is not None:
            for k in m.get('CfsList'):
                temp_model = GetWorkitemByIdResponseBodyDataCfsList()
                self.cfs_list.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('StatusStage') is not None:
            self.status_stage = m.get('StatusStage')
        if m.get('AssignedToStaffId') is not None:
            self.assigned_to_staff_id = m.get('AssignedToStaffId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LogicalStatus') is not None:
            self.logical_status = m.get('LogicalStatus')
        if m.get('VersionIds') is not None:
            self.version_ids = m.get('VersionIds')
        if m.get('SeriousLevel') is not None:
            self.serious_level = m.get('SeriousLevel')
        if m.get('StatusId') is not None:
            self.status_id = m.get('StatusId')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('TrackerIds') is not None:
            self.tracker_ids = m.get('TrackerIds')
        if m.get('AssignedToId') is not None:
            self.assigned_to_id = m.get('AssignedToId')
        if m.get('ChangeLogList') is not None:
            self.change_log_list = m.get('ChangeLogList')
        if m.get('IssueTypeId') is not None:
            self.issue_type_id = m.get('IssueTypeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        if m.get('AssignedToMaps') is not None:
            self.assigned_to_maps = m.get('AssignedToMaps')
        if m.get('BlackListNotice') is not None:
            self.black_list_notice = m.get('BlackListNotice')
        if m.get('ModuleUpdated') is not None:
            self.module_updated = m.get('ModuleUpdated')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('CommentList') is not None:
            self.comment_list = m.get('CommentList')
        if m.get('VerifierStaffId') is not None:
            self.verifier_staff_id = m.get('VerifierStaffId')
        if m.get('ModuleIds') is not None:
            self.module_ids = m.get('ModuleIds')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetWorkitemByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetWorkitemByIdResponseBodyData = None,
        code: int = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetWorkitemByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorkitemByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWorkitemByIdResponseBody = None,
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
            temp_model = GetWorkitemByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinCompanyRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class JoinCompanyResponseBodyData(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class JoinCompanyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: JoinCompanyResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = JoinCompanyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class JoinCompanyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinCompanyResponseBody = None,
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
            temp_model = JoinCompanyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchProjectsByRegionRequest(TeaModel):
    def __init__(
        self,
        corp_identifier: str = None,
        region: str = None,
        status: str = None,
        to_page: int = None,
        page_size: int = None,
    ):
        self.corp_identifier = corp_identifier
        self.region = region
        self.status = status
        self.to_page = to_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.to_page is not None:
            result['ToPage'] = self.to_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class SearchProjectsByRegionResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        aone_type: str = None,
        stamp: str = None,
        full_name: str = None,
        icons: List[str] = None,
        id_path: str = None,
        mode: str = None,
        aone_id: int = None,
        parent_id: int = None,
        description: str = None,
        custom_field_map: List[str] = None,
        name: str = None,
        id: int = None,
    ):
        self.status = status
        self.type = type
        self.aone_type = aone_type
        self.stamp = stamp
        self.full_name = full_name
        self.icons = icons
        self.id_path = id_path
        self.mode = mode
        self.aone_id = aone_id
        self.parent_id = parent_id
        self.description = description
        self.custom_field_map = custom_field_map
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.aone_type is not None:
            result['AoneType'] = self.aone_type
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.icons is not None:
            result['Icons'] = self.icons
        if self.id_path is not None:
            result['IdPath'] = self.id_path
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.aone_id is not None:
            result['AoneId'] = self.aone_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.custom_field_map is not None:
            result['CustomFieldMap'] = self.custom_field_map
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AoneType') is not None:
            self.aone_type = m.get('AoneType')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('Icons') is not None:
            self.icons = m.get('Icons')
        if m.get('IdPath') is not None:
            self.id_path = m.get('IdPath')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('AoneId') is not None:
            self.aone_id = m.get('AoneId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CustomFieldMap') is not None:
            self.custom_field_map = m.get('CustomFieldMap')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SearchProjectsByRegionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[SearchProjectsByRegionResponseBodyData] = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchProjectsByRegionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchProjectsByRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchProjectsByRegionResponseBody = None,
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
            temp_model = SearchProjectsByRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTestCaseRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        corp_identifier: str = None,
        ak_project_id: str = None,
        case_tag: str = None,
        page_num: str = None,
        create_date_start: str = None,
        create_date_end: str = None,
        update_date_start: str = None,
        update_date_end: str = None,
    ):
        self.page_size = page_size
        self.corp_identifier = corp_identifier
        self.ak_project_id = ak_project_id
        self.case_tag = case_tag
        self.page_num = page_num
        self.create_date_start = create_date_start
        self.create_date_end = create_date_end
        self.update_date_start = update_date_start
        self.update_date_end = update_date_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.ak_project_id is not None:
            result['AkProjectId'] = self.ak_project_id
        if self.case_tag is not None:
            result['CaseTag'] = self.case_tag
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.create_date_start is not None:
            result['CreateDateStart'] = self.create_date_start
        if self.create_date_end is not None:
            result['CreateDateEnd'] = self.create_date_end
        if self.update_date_start is not None:
            result['UpdateDateStart'] = self.update_date_start
        if self.update_date_end is not None:
            result['UpdateDateEnd'] = self.update_date_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('AkProjectId') is not None:
            self.ak_project_id = m.get('AkProjectId')
        if m.get('CaseTag') is not None:
            self.case_tag = m.get('CaseTag')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('CreateDateStart') is not None:
            self.create_date_start = m.get('CreateDateStart')
        if m.get('CreateDateEnd') is not None:
            self.create_date_end = m.get('CreateDateEnd')
        if m.get('UpdateDateStart') is not None:
            self.update_date_start = m.get('UpdateDateStart')
        if m.get('UpdateDateEnd') is not None:
            self.update_date_end = m.get('UpdateDateEnd')
        return self


class SearchTestCaseResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: str = None,
        cases: str = None,
        page_size: str = None,
        page_total: str = None,
        total_count: str = None,
    ):
        self.page_num = page_num
        self.cases = cases
        self.page_size = page_size
        self.page_total = page_total
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.cases is not None:
            result['Cases'] = self.cases
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('Cases') is not None:
            self.cases = m.get('Cases')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchTestCaseResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SearchTestCaseResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SearchTestCaseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchTestCaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTestCaseResponseBody = None,
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
            temp_model = SearchTestCaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchWorkitemRequest(TeaModel):
    def __init__(
        self,
        stamp: str = None,
        akproject_id: int = None,
        to_page: int = None,
        page_size: int = None,
        corp_identifier: str = None,
        sprint_id: int = None,
        created_at_start: str = None,
        created_at_end: str = None,
    ):
        self.stamp = stamp
        self.akproject_id = akproject_id
        self.to_page = to_page
        self.page_size = page_size
        self.corp_identifier = corp_identifier
        self.sprint_id = sprint_id
        self.created_at_start = created_at_start
        self.created_at_end = created_at_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.akproject_id is not None:
            result['AKProjectId'] = self.akproject_id
        if self.to_page is not None:
            result['ToPage'] = self.to_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.created_at_start is not None:
            result['CreatedAtStart'] = self.created_at_start
        if self.created_at_end is not None:
            result['CreatedAtEnd'] = self.created_at_end
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('AKProjectId') is not None:
            self.akproject_id = m.get('AKProjectId')
        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('CreatedAtStart') is not None:
            self.created_at_start = m.get('CreatedAtStart')
        if m.get('CreatedAtEnd') is not None:
            self.created_at_end = m.get('CreatedAtEnd')
        return self


class SearchWorkitemResponseBodyData(TeaModel):
    def __init__(
        self,
        fixed_user_id: int = None,
        send_wangwang: bool = None,
        skip_collab: bool = None,
        version_list: str = None,
        ak_project_id: int = None,
        project_id: int = None,
        user_id: int = None,
        version_id: int = None,
        id_path: str = None,
        ignore_integrate: bool = None,
        attachment_ids: str = None,
        commit_date: int = None,
        ak_version_ids: str = None,
        region: str = None,
        trackers: str = None,
        subject: str = None,
        solution: int = None,
        attachment_list: str = None,
        user_staff_id: str = None,
        ignore_check: bool = None,
        ak_paths: str = None,
        verifier_id: int = None,
        module_list: str = None,
        attachmented: bool = None,
        source_id: int = None,
        serious_level_id: int = None,
        tag_id_list: str = None,
        watched: bool = None,
        assigned_to: str = None,
        assigned_to_ids: str = None,
        closed_duration: int = None,
        priority_id: int = None,
        record_change_log: bool = None,
        issue_relations: str = None,
        updated_at: int = None,
        template_id: int = None,
        verifier: str = None,
        status: str = None,
        related_user_ids: str = None,
        related_akproject_guids: str = None,
        related_akproject_ids: str = None,
        watcher_id_list: str = None,
        created_at: int = None,
        assigned_to_id_list: str = None,
        priority: str = None,
        status_stage: int = None,
        assigned_to_staff_id: str = None,
        parent_id: int = None,
        logical_status: str = None,
        version_ids: str = None,
        scope: int = None,
        serious_level: str = None,
        status_id: int = None,
        stamp: str = None,
        user: str = None,
        source: str = None,
        assigned_to_id: int = None,
        tracker_ids: str = None,
        issue_type_id: int = None,
        change_log_list: str = None,
        fixed_duration: int = None,
        scope_user_ids: str = None,
        dev_duration: int = None,
        line_path: str = None,
        black_list_notice: str = None,
        project_ids: str = None,
        testsuite_id: int = None,
        module_updated: bool = None,
        comment_list: str = None,
        sprint_id: int = None,
        respond_duration: int = None,
        module_ids: str = None,
        verifier_staff_id: str = None,
        id: int = None,
    ):
        self.fixed_user_id = fixed_user_id
        self.send_wangwang = send_wangwang
        self.skip_collab = skip_collab
        self.version_list = version_list
        self.ak_project_id = ak_project_id
        self.project_id = project_id
        self.user_id = user_id
        self.version_id = version_id
        self.id_path = id_path
        self.ignore_integrate = ignore_integrate
        self.attachment_ids = attachment_ids
        self.commit_date = commit_date
        self.ak_version_ids = ak_version_ids
        self.region = region
        self.trackers = trackers
        self.subject = subject
        self.solution = solution
        self.attachment_list = attachment_list
        self.user_staff_id = user_staff_id
        self.ignore_check = ignore_check
        self.ak_paths = ak_paths
        self.verifier_id = verifier_id
        self.module_list = module_list
        self.attachmented = attachmented
        self.source_id = source_id
        self.serious_level_id = serious_level_id
        self.tag_id_list = tag_id_list
        self.watched = watched
        self.assigned_to = assigned_to
        self.assigned_to_ids = assigned_to_ids
        self.closed_duration = closed_duration
        self.priority_id = priority_id
        self.record_change_log = record_change_log
        self.issue_relations = issue_relations
        self.updated_at = updated_at
        self.template_id = template_id
        self.verifier = verifier
        self.status = status
        self.related_user_ids = related_user_ids
        self.related_akproject_guids = related_akproject_guids
        self.related_akproject_ids = related_akproject_ids
        self.watcher_id_list = watcher_id_list
        self.created_at = created_at
        self.assigned_to_id_list = assigned_to_id_list
        self.priority = priority
        self.status_stage = status_stage
        self.assigned_to_staff_id = assigned_to_staff_id
        self.parent_id = parent_id
        self.logical_status = logical_status
        self.version_ids = version_ids
        self.scope = scope
        self.serious_level = serious_level
        self.status_id = status_id
        self.stamp = stamp
        self.user = user
        self.source = source
        self.assigned_to_id = assigned_to_id
        self.tracker_ids = tracker_ids
        self.issue_type_id = issue_type_id
        self.change_log_list = change_log_list
        self.fixed_duration = fixed_duration
        self.scope_user_ids = scope_user_ids
        self.dev_duration = dev_duration
        self.line_path = line_path
        self.black_list_notice = black_list_notice
        self.project_ids = project_ids
        self.testsuite_id = testsuite_id
        self.module_updated = module_updated
        self.comment_list = comment_list
        self.sprint_id = sprint_id
        self.respond_duration = respond_duration
        self.module_ids = module_ids
        self.verifier_staff_id = verifier_staff_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.fixed_user_id is not None:
            result['FixedUserId'] = self.fixed_user_id
        if self.send_wangwang is not None:
            result['SendWangwang'] = self.send_wangwang
        if self.skip_collab is not None:
            result['SkipCollab'] = self.skip_collab
        if self.version_list is not None:
            result['VersionList'] = self.version_list
        if self.ak_project_id is not None:
            result['AkProjectId'] = self.ak_project_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.id_path is not None:
            result['IdPath'] = self.id_path
        if self.ignore_integrate is not None:
            result['IgnoreIntegrate'] = self.ignore_integrate
        if self.attachment_ids is not None:
            result['AttachmentIds'] = self.attachment_ids
        if self.commit_date is not None:
            result['CommitDate'] = self.commit_date
        if self.ak_version_ids is not None:
            result['AkVersionIds'] = self.ak_version_ids
        if self.region is not None:
            result['Region'] = self.region
        if self.trackers is not None:
            result['Trackers'] = self.trackers
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.attachment_list is not None:
            result['AttachmentList'] = self.attachment_list
        if self.user_staff_id is not None:
            result['UserStaffId'] = self.user_staff_id
        if self.ignore_check is not None:
            result['IgnoreCheck'] = self.ignore_check
        if self.ak_paths is not None:
            result['AkPaths'] = self.ak_paths
        if self.verifier_id is not None:
            result['VerifierId'] = self.verifier_id
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.attachmented is not None:
            result['Attachmented'] = self.attachmented
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.serious_level_id is not None:
            result['SeriousLevelId'] = self.serious_level_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.watched is not None:
            result['Watched'] = self.watched
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.assigned_to_ids is not None:
            result['AssignedToIds'] = self.assigned_to_ids
        if self.closed_duration is not None:
            result['ClosedDuration'] = self.closed_duration
        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id
        if self.record_change_log is not None:
            result['RecordChangeLog'] = self.record_change_log
        if self.issue_relations is not None:
            result['IssueRelations'] = self.issue_relations
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.status is not None:
            result['Status'] = self.status
        if self.related_user_ids is not None:
            result['RelatedUserIds'] = self.related_user_ids
        if self.related_akproject_guids is not None:
            result['RelatedAKProjectGuids'] = self.related_akproject_guids
        if self.related_akproject_ids is not None:
            result['RelatedAKProjectIds'] = self.related_akproject_ids
        if self.watcher_id_list is not None:
            result['WatcherIdList'] = self.watcher_id_list
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.assigned_to_id_list is not None:
            result['AssignedToIdList'] = self.assigned_to_id_list
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status_stage is not None:
            result['StatusStage'] = self.status_stage
        if self.assigned_to_staff_id is not None:
            result['AssignedToStaffId'] = self.assigned_to_staff_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.logical_status is not None:
            result['LogicalStatus'] = self.logical_status
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.serious_level is not None:
            result['SeriousLevel'] = self.serious_level
        if self.status_id is not None:
            result['StatusId'] = self.status_id
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.user is not None:
            result['User'] = self.user
        if self.source is not None:
            result['Source'] = self.source
        if self.assigned_to_id is not None:
            result['AssignedToId'] = self.assigned_to_id
        if self.tracker_ids is not None:
            result['TrackerIds'] = self.tracker_ids
        if self.issue_type_id is not None:
            result['IssueTypeId'] = self.issue_type_id
        if self.change_log_list is not None:
            result['ChangeLogList'] = self.change_log_list
        if self.fixed_duration is not None:
            result['FixedDuration'] = self.fixed_duration
        if self.scope_user_ids is not None:
            result['ScopeUserIds'] = self.scope_user_ids
        if self.dev_duration is not None:
            result['DevDuration'] = self.dev_duration
        if self.line_path is not None:
            result['LinePath'] = self.line_path
        if self.black_list_notice is not None:
            result['BlackListNotice'] = self.black_list_notice
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.testsuite_id is not None:
            result['TestsuiteId'] = self.testsuite_id
        if self.module_updated is not None:
            result['ModuleUpdated'] = self.module_updated
        if self.comment_list is not None:
            result['CommentList'] = self.comment_list
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.respond_duration is not None:
            result['RespondDuration'] = self.respond_duration
        if self.module_ids is not None:
            result['ModuleIds'] = self.module_ids
        if self.verifier_staff_id is not None:
            result['VerifierStaffId'] = self.verifier_staff_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedUserId') is not None:
            self.fixed_user_id = m.get('FixedUserId')
        if m.get('SendWangwang') is not None:
            self.send_wangwang = m.get('SendWangwang')
        if m.get('SkipCollab') is not None:
            self.skip_collab = m.get('SkipCollab')
        if m.get('VersionList') is not None:
            self.version_list = m.get('VersionList')
        if m.get('AkProjectId') is not None:
            self.ak_project_id = m.get('AkProjectId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('IdPath') is not None:
            self.id_path = m.get('IdPath')
        if m.get('IgnoreIntegrate') is not None:
            self.ignore_integrate = m.get('IgnoreIntegrate')
        if m.get('AttachmentIds') is not None:
            self.attachment_ids = m.get('AttachmentIds')
        if m.get('CommitDate') is not None:
            self.commit_date = m.get('CommitDate')
        if m.get('AkVersionIds') is not None:
            self.ak_version_ids = m.get('AkVersionIds')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Trackers') is not None:
            self.trackers = m.get('Trackers')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('AttachmentList') is not None:
            self.attachment_list = m.get('AttachmentList')
        if m.get('UserStaffId') is not None:
            self.user_staff_id = m.get('UserStaffId')
        if m.get('IgnoreCheck') is not None:
            self.ignore_check = m.get('IgnoreCheck')
        if m.get('AkPaths') is not None:
            self.ak_paths = m.get('AkPaths')
        if m.get('VerifierId') is not None:
            self.verifier_id = m.get('VerifierId')
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Attachmented') is not None:
            self.attachmented = m.get('Attachmented')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SeriousLevelId') is not None:
            self.serious_level_id = m.get('SeriousLevelId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Watched') is not None:
            self.watched = m.get('Watched')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('AssignedToIds') is not None:
            self.assigned_to_ids = m.get('AssignedToIds')
        if m.get('ClosedDuration') is not None:
            self.closed_duration = m.get('ClosedDuration')
        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')
        if m.get('RecordChangeLog') is not None:
            self.record_change_log = m.get('RecordChangeLog')
        if m.get('IssueRelations') is not None:
            self.issue_relations = m.get('IssueRelations')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RelatedUserIds') is not None:
            self.related_user_ids = m.get('RelatedUserIds')
        if m.get('RelatedAKProjectGuids') is not None:
            self.related_akproject_guids = m.get('RelatedAKProjectGuids')
        if m.get('RelatedAKProjectIds') is not None:
            self.related_akproject_ids = m.get('RelatedAKProjectIds')
        if m.get('WatcherIdList') is not None:
            self.watcher_id_list = m.get('WatcherIdList')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AssignedToIdList') is not None:
            self.assigned_to_id_list = m.get('AssignedToIdList')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('StatusStage') is not None:
            self.status_stage = m.get('StatusStage')
        if m.get('AssignedToStaffId') is not None:
            self.assigned_to_staff_id = m.get('AssignedToStaffId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('LogicalStatus') is not None:
            self.logical_status = m.get('LogicalStatus')
        if m.get('VersionIds') is not None:
            self.version_ids = m.get('VersionIds')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SeriousLevel') is not None:
            self.serious_level = m.get('SeriousLevel')
        if m.get('StatusId') is not None:
            self.status_id = m.get('StatusId')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('AssignedToId') is not None:
            self.assigned_to_id = m.get('AssignedToId')
        if m.get('TrackerIds') is not None:
            self.tracker_ids = m.get('TrackerIds')
        if m.get('IssueTypeId') is not None:
            self.issue_type_id = m.get('IssueTypeId')
        if m.get('ChangeLogList') is not None:
            self.change_log_list = m.get('ChangeLogList')
        if m.get('FixedDuration') is not None:
            self.fixed_duration = m.get('FixedDuration')
        if m.get('ScopeUserIds') is not None:
            self.scope_user_ids = m.get('ScopeUserIds')
        if m.get('DevDuration') is not None:
            self.dev_duration = m.get('DevDuration')
        if m.get('LinePath') is not None:
            self.line_path = m.get('LinePath')
        if m.get('BlackListNotice') is not None:
            self.black_list_notice = m.get('BlackListNotice')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('TestsuiteId') is not None:
            self.testsuite_id = m.get('TestsuiteId')
        if m.get('ModuleUpdated') is not None:
            self.module_updated = m.get('ModuleUpdated')
        if m.get('CommentList') is not None:
            self.comment_list = m.get('CommentList')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('RespondDuration') is not None:
            self.respond_duration = m.get('RespondDuration')
        if m.get('ModuleIds') is not None:
            self.module_ids = m.get('ModuleIds')
        if m.get('VerifierStaffId') is not None:
            self.verifier_staff_id = m.get('VerifierStaffId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SearchWorkitemResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        to_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_pages: int = None,
        data: List[SearchWorkitemResponseBodyData] = None,
        code: int = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.to_page = to_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_pages = total_pages
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.to_page is not None:
            result['ToPage'] = self.to_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchWorkitemResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchWorkitemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchWorkitemResponseBody = None,
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
            temp_model = SearchWorkitemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchWorkitemWithTotalCountRequest(TeaModel):
    def __init__(
        self,
        stamp: str = None,
        akproject_id: int = None,
        to_page: int = None,
        page_size: int = None,
        corp_identifier: str = None,
        sprint_id: int = None,
    ):
        self.stamp = stamp
        self.akproject_id = akproject_id
        self.to_page = to_page
        self.page_size = page_size
        self.corp_identifier = corp_identifier
        self.sprint_id = sprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.akproject_id is not None:
            result['AKProjectId'] = self.akproject_id
        if self.to_page is not None:
            result['ToPage'] = self.to_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('AKProjectId') is not None:
            self.akproject_id = m.get('AKProjectId')
        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        return self


class SearchWorkitemWithTotalCountResponseBodyData(TeaModel):
    def __init__(
        self,
        fixed_user_id: int = None,
        send_wangwang: bool = None,
        skip_collab: bool = None,
        version_list: str = None,
        ak_project_id: int = None,
        project_id: int = None,
        user_id: int = None,
        version_id: int = None,
        id_path: str = None,
        ignore_integrate: bool = None,
        attachment_ids: str = None,
        commit_date: int = None,
        ak_version_ids: str = None,
        region: str = None,
        trackers: str = None,
        subject: str = None,
        solution: int = None,
        attachment_list: str = None,
        user_staff_id: str = None,
        ignore_check: bool = None,
        ak_paths: str = None,
        verifier_id: int = None,
        module_list: str = None,
        attachmented: bool = None,
        source_id: int = None,
        serious_level_id: int = None,
        tag_id_list: str = None,
        watched: bool = None,
        assigned_to: str = None,
        assigned_to_ids: str = None,
        closed_duration: int = None,
        priority_id: int = None,
        record_change_log: bool = None,
        issue_relations: str = None,
        updated_at: int = None,
        template_id: int = None,
        verifier: str = None,
        status: str = None,
        related_user_ids: str = None,
        related_akproject_guids: str = None,
        related_akproject_ids: str = None,
        watcher_id_list: str = None,
        created_at: int = None,
        assigned_to_id_list: str = None,
        priority: str = None,
        status_stage: int = None,
        assigned_to_staff_id: str = None,
        parent_id: int = None,
        logical_status: str = None,
        version_ids: str = None,
        scope: int = None,
        serious_level: str = None,
        status_id: int = None,
        stamp: str = None,
        user: str = None,
        source: str = None,
        assigned_to_id: int = None,
        tracker_ids: str = None,
        issue_type_id: int = None,
        change_log_list: str = None,
        fixed_duration: int = None,
        scope_user_ids: str = None,
        dev_duration: int = None,
        line_path: str = None,
        black_list_notice: str = None,
        project_ids: str = None,
        testsuite_id: int = None,
        module_updated: bool = None,
        comment_list: str = None,
        sprint_id: int = None,
        respond_duration: int = None,
        module_ids: str = None,
        verifier_staff_id: str = None,
        id: int = None,
    ):
        self.fixed_user_id = fixed_user_id
        self.send_wangwang = send_wangwang
        self.skip_collab = skip_collab
        self.version_list = version_list
        self.ak_project_id = ak_project_id
        self.project_id = project_id
        self.user_id = user_id
        self.version_id = version_id
        self.id_path = id_path
        self.ignore_integrate = ignore_integrate
        self.attachment_ids = attachment_ids
        self.commit_date = commit_date
        self.ak_version_ids = ak_version_ids
        self.region = region
        self.trackers = trackers
        self.subject = subject
        self.solution = solution
        self.attachment_list = attachment_list
        self.user_staff_id = user_staff_id
        self.ignore_check = ignore_check
        self.ak_paths = ak_paths
        self.verifier_id = verifier_id
        self.module_list = module_list
        self.attachmented = attachmented
        self.source_id = source_id
        self.serious_level_id = serious_level_id
        self.tag_id_list = tag_id_list
        self.watched = watched
        self.assigned_to = assigned_to
        self.assigned_to_ids = assigned_to_ids
        self.closed_duration = closed_duration
        self.priority_id = priority_id
        self.record_change_log = record_change_log
        self.issue_relations = issue_relations
        self.updated_at = updated_at
        self.template_id = template_id
        self.verifier = verifier
        self.status = status
        self.related_user_ids = related_user_ids
        self.related_akproject_guids = related_akproject_guids
        self.related_akproject_ids = related_akproject_ids
        self.watcher_id_list = watcher_id_list
        self.created_at = created_at
        self.assigned_to_id_list = assigned_to_id_list
        self.priority = priority
        self.status_stage = status_stage
        self.assigned_to_staff_id = assigned_to_staff_id
        self.parent_id = parent_id
        self.logical_status = logical_status
        self.version_ids = version_ids
        self.scope = scope
        self.serious_level = serious_level
        self.status_id = status_id
        self.stamp = stamp
        self.user = user
        self.source = source
        self.assigned_to_id = assigned_to_id
        self.tracker_ids = tracker_ids
        self.issue_type_id = issue_type_id
        self.change_log_list = change_log_list
        self.fixed_duration = fixed_duration
        self.scope_user_ids = scope_user_ids
        self.dev_duration = dev_duration
        self.line_path = line_path
        self.black_list_notice = black_list_notice
        self.project_ids = project_ids
        self.testsuite_id = testsuite_id
        self.module_updated = module_updated
        self.comment_list = comment_list
        self.sprint_id = sprint_id
        self.respond_duration = respond_duration
        self.module_ids = module_ids
        self.verifier_staff_id = verifier_staff_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.fixed_user_id is not None:
            result['FixedUserId'] = self.fixed_user_id
        if self.send_wangwang is not None:
            result['SendWangwang'] = self.send_wangwang
        if self.skip_collab is not None:
            result['SkipCollab'] = self.skip_collab
        if self.version_list is not None:
            result['VersionList'] = self.version_list
        if self.ak_project_id is not None:
            result['AkProjectId'] = self.ak_project_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.id_path is not None:
            result['IdPath'] = self.id_path
        if self.ignore_integrate is not None:
            result['IgnoreIntegrate'] = self.ignore_integrate
        if self.attachment_ids is not None:
            result['AttachmentIds'] = self.attachment_ids
        if self.commit_date is not None:
            result['CommitDate'] = self.commit_date
        if self.ak_version_ids is not None:
            result['AkVersionIds'] = self.ak_version_ids
        if self.region is not None:
            result['Region'] = self.region
        if self.trackers is not None:
            result['Trackers'] = self.trackers
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.attachment_list is not None:
            result['AttachmentList'] = self.attachment_list
        if self.user_staff_id is not None:
            result['UserStaffId'] = self.user_staff_id
        if self.ignore_check is not None:
            result['IgnoreCheck'] = self.ignore_check
        if self.ak_paths is not None:
            result['AkPaths'] = self.ak_paths
        if self.verifier_id is not None:
            result['VerifierId'] = self.verifier_id
        if self.module_list is not None:
            result['ModuleList'] = self.module_list
        if self.attachmented is not None:
            result['Attachmented'] = self.attachmented
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.serious_level_id is not None:
            result['SeriousLevelId'] = self.serious_level_id
        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list
        if self.watched is not None:
            result['Watched'] = self.watched
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.assigned_to_ids is not None:
            result['AssignedToIds'] = self.assigned_to_ids
        if self.closed_duration is not None:
            result['ClosedDuration'] = self.closed_duration
        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id
        if self.record_change_log is not None:
            result['RecordChangeLog'] = self.record_change_log
        if self.issue_relations is not None:
            result['IssueRelations'] = self.issue_relations
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.status is not None:
            result['Status'] = self.status
        if self.related_user_ids is not None:
            result['RelatedUserIds'] = self.related_user_ids
        if self.related_akproject_guids is not None:
            result['RelatedAKProjectGuids'] = self.related_akproject_guids
        if self.related_akproject_ids is not None:
            result['RelatedAKProjectIds'] = self.related_akproject_ids
        if self.watcher_id_list is not None:
            result['WatcherIdList'] = self.watcher_id_list
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.assigned_to_id_list is not None:
            result['AssignedToIdList'] = self.assigned_to_id_list
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status_stage is not None:
            result['StatusStage'] = self.status_stage
        if self.assigned_to_staff_id is not None:
            result['AssignedToStaffId'] = self.assigned_to_staff_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.logical_status is not None:
            result['LogicalStatus'] = self.logical_status
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.serious_level is not None:
            result['SeriousLevel'] = self.serious_level
        if self.status_id is not None:
            result['StatusId'] = self.status_id
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.user is not None:
            result['User'] = self.user
        if self.source is not None:
            result['Source'] = self.source
        if self.assigned_to_id is not None:
            result['AssignedToId'] = self.assigned_to_id
        if self.tracker_ids is not None:
            result['TrackerIds'] = self.tracker_ids
        if self.issue_type_id is not None:
            result['IssueTypeId'] = self.issue_type_id
        if self.change_log_list is not None:
            result['ChangeLogList'] = self.change_log_list
        if self.fixed_duration is not None:
            result['FixedDuration'] = self.fixed_duration
        if self.scope_user_ids is not None:
            result['ScopeUserIds'] = self.scope_user_ids
        if self.dev_duration is not None:
            result['DevDuration'] = self.dev_duration
        if self.line_path is not None:
            result['LinePath'] = self.line_path
        if self.black_list_notice is not None:
            result['BlackListNotice'] = self.black_list_notice
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.testsuite_id is not None:
            result['TestsuiteId'] = self.testsuite_id
        if self.module_updated is not None:
            result['ModuleUpdated'] = self.module_updated
        if self.comment_list is not None:
            result['CommentList'] = self.comment_list
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.respond_duration is not None:
            result['RespondDuration'] = self.respond_duration
        if self.module_ids is not None:
            result['ModuleIds'] = self.module_ids
        if self.verifier_staff_id is not None:
            result['VerifierStaffId'] = self.verifier_staff_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedUserId') is not None:
            self.fixed_user_id = m.get('FixedUserId')
        if m.get('SendWangwang') is not None:
            self.send_wangwang = m.get('SendWangwang')
        if m.get('SkipCollab') is not None:
            self.skip_collab = m.get('SkipCollab')
        if m.get('VersionList') is not None:
            self.version_list = m.get('VersionList')
        if m.get('AkProjectId') is not None:
            self.ak_project_id = m.get('AkProjectId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('IdPath') is not None:
            self.id_path = m.get('IdPath')
        if m.get('IgnoreIntegrate') is not None:
            self.ignore_integrate = m.get('IgnoreIntegrate')
        if m.get('AttachmentIds') is not None:
            self.attachment_ids = m.get('AttachmentIds')
        if m.get('CommitDate') is not None:
            self.commit_date = m.get('CommitDate')
        if m.get('AkVersionIds') is not None:
            self.ak_version_ids = m.get('AkVersionIds')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Trackers') is not None:
            self.trackers = m.get('Trackers')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('AttachmentList') is not None:
            self.attachment_list = m.get('AttachmentList')
        if m.get('UserStaffId') is not None:
            self.user_staff_id = m.get('UserStaffId')
        if m.get('IgnoreCheck') is not None:
            self.ignore_check = m.get('IgnoreCheck')
        if m.get('AkPaths') is not None:
            self.ak_paths = m.get('AkPaths')
        if m.get('VerifierId') is not None:
            self.verifier_id = m.get('VerifierId')
        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')
        if m.get('Attachmented') is not None:
            self.attachmented = m.get('Attachmented')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SeriousLevelId') is not None:
            self.serious_level_id = m.get('SeriousLevelId')
        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')
        if m.get('Watched') is not None:
            self.watched = m.get('Watched')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('AssignedToIds') is not None:
            self.assigned_to_ids = m.get('AssignedToIds')
        if m.get('ClosedDuration') is not None:
            self.closed_duration = m.get('ClosedDuration')
        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')
        if m.get('RecordChangeLog') is not None:
            self.record_change_log = m.get('RecordChangeLog')
        if m.get('IssueRelations') is not None:
            self.issue_relations = m.get('IssueRelations')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RelatedUserIds') is not None:
            self.related_user_ids = m.get('RelatedUserIds')
        if m.get('RelatedAKProjectGuids') is not None:
            self.related_akproject_guids = m.get('RelatedAKProjectGuids')
        if m.get('RelatedAKProjectIds') is not None:
            self.related_akproject_ids = m.get('RelatedAKProjectIds')
        if m.get('WatcherIdList') is not None:
            self.watcher_id_list = m.get('WatcherIdList')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AssignedToIdList') is not None:
            self.assigned_to_id_list = m.get('AssignedToIdList')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('StatusStage') is not None:
            self.status_stage = m.get('StatusStage')
        if m.get('AssignedToStaffId') is not None:
            self.assigned_to_staff_id = m.get('AssignedToStaffId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('LogicalStatus') is not None:
            self.logical_status = m.get('LogicalStatus')
        if m.get('VersionIds') is not None:
            self.version_ids = m.get('VersionIds')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SeriousLevel') is not None:
            self.serious_level = m.get('SeriousLevel')
        if m.get('StatusId') is not None:
            self.status_id = m.get('StatusId')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('AssignedToId') is not None:
            self.assigned_to_id = m.get('AssignedToId')
        if m.get('TrackerIds') is not None:
            self.tracker_ids = m.get('TrackerIds')
        if m.get('IssueTypeId') is not None:
            self.issue_type_id = m.get('IssueTypeId')
        if m.get('ChangeLogList') is not None:
            self.change_log_list = m.get('ChangeLogList')
        if m.get('FixedDuration') is not None:
            self.fixed_duration = m.get('FixedDuration')
        if m.get('ScopeUserIds') is not None:
            self.scope_user_ids = m.get('ScopeUserIds')
        if m.get('DevDuration') is not None:
            self.dev_duration = m.get('DevDuration')
        if m.get('LinePath') is not None:
            self.line_path = m.get('LinePath')
        if m.get('BlackListNotice') is not None:
            self.black_list_notice = m.get('BlackListNotice')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('TestsuiteId') is not None:
            self.testsuite_id = m.get('TestsuiteId')
        if m.get('ModuleUpdated') is not None:
            self.module_updated = m.get('ModuleUpdated')
        if m.get('CommentList') is not None:
            self.comment_list = m.get('CommentList')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('RespondDuration') is not None:
            self.respond_duration = m.get('RespondDuration')
        if m.get('ModuleIds') is not None:
            self.module_ids = m.get('ModuleIds')
        if m.get('VerifierStaffId') is not None:
            self.verifier_staff_id = m.get('VerifierStaffId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SearchWorkitemWithTotalCountResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        to_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_pages: int = None,
        data: List[SearchWorkitemWithTotalCountResponseBodyData] = None,
        code: int = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.to_page = to_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_pages = total_pages
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.to_page is not None:
            result['ToPage'] = self.to_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ToPage') is not None:
            self.to_page = m.get('ToPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchWorkitemWithTotalCountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchWorkitemWithTotalCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchWorkitemWithTotalCountResponseBody = None,
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
            temp_model = SearchWorkitemWithTotalCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncUserToRdcRequest(TeaModel):
    def __init__(
        self,
        login_ticket: str = None,
    ):
        self.login_ticket = login_ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.login_ticket is not None:
            result['LoginTicket'] = self.login_ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginTicket') is not None:
            self.login_ticket = m.get('LoginTicket')
        return self


class SyncUserToRdcResponseBodyData(TeaModel):
    def __init__(
        self,
        is_valid: bool = None,
    ):
        self.is_valid = is_valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_valid is not None:
            result['IsValid'] = self.is_valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsValid') is not None:
            self.is_valid = m.get('IsValid')
        return self


class SyncUserToRdcResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SyncUserToRdcResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SyncUserToRdcResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncUserToRdcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncUserToRdcResponseBody = None,
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
            temp_model = SyncUserToRdcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkitemRequest(TeaModel):
    def __init__(
        self,
        akproject_id: int = None,
        corp_identifier: str = None,
        modifier: str = None,
        assigned_to: str = None,
        template_id: int = None,
        subject: str = None,
        description: str = None,
        stamp: str = None,
        cf_list: Dict[str, Any] = None,
        issue_id: int = None,
        status: str = None,
        priority: str = None,
        serious_level: str = None,
        verifier: str = None,
        sprint_id: int = None,
        ignore_check: bool = None,
        cfs: Dict[str, Any] = None,
    ):
        self.akproject_id = akproject_id
        self.corp_identifier = corp_identifier
        self.modifier = modifier
        self.assigned_to = assigned_to
        self.template_id = template_id
        self.subject = subject
        self.description = description
        self.stamp = stamp
        self.cf_list = cf_list
        self.issue_id = issue_id
        self.status = status
        self.priority = priority
        self.serious_level = serious_level
        self.verifier = verifier
        self.sprint_id = sprint_id
        self.ignore_check = ignore_check
        self.cfs = cfs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.akproject_id is not None:
            result['AKProjectId'] = self.akproject_id
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.description is not None:
            result['Description'] = self.description
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.cf_list is not None:
            result['CfList'] = self.cf_list
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        if self.status is not None:
            result['Status'] = self.status
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.serious_level is not None:
            result['SeriousLevel'] = self.serious_level
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.ignore_check is not None:
            result['IgnoreCheck'] = self.ignore_check
        if self.cfs is not None:
            result['Cfs'] = self.cfs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AKProjectId') is not None:
            self.akproject_id = m.get('AKProjectId')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('CfList') is not None:
            self.cf_list = m.get('CfList')
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SeriousLevel') is not None:
            self.serious_level = m.get('SeriousLevel')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('IgnoreCheck') is not None:
            self.ignore_check = m.get('IgnoreCheck')
        if m.get('Cfs') is not None:
            self.cfs = m.get('Cfs')
        return self


class UpdateWorkitemShrinkRequest(TeaModel):
    def __init__(
        self,
        akproject_id: int = None,
        corp_identifier: str = None,
        modifier: str = None,
        assigned_to: str = None,
        template_id: int = None,
        subject: str = None,
        description: str = None,
        stamp: str = None,
        cf_list_shrink: str = None,
        issue_id: int = None,
        status: str = None,
        priority: str = None,
        serious_level: str = None,
        verifier: str = None,
        sprint_id: int = None,
        ignore_check: bool = None,
        cfs_shrink: str = None,
    ):
        self.akproject_id = akproject_id
        self.corp_identifier = corp_identifier
        self.modifier = modifier
        self.assigned_to = assigned_to
        self.template_id = template_id
        self.subject = subject
        self.description = description
        self.stamp = stamp
        self.cf_list_shrink = cf_list_shrink
        self.issue_id = issue_id
        self.status = status
        self.priority = priority
        self.serious_level = serious_level
        self.verifier = verifier
        self.sprint_id = sprint_id
        self.ignore_check = ignore_check
        self.cfs_shrink = cfs_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.akproject_id is not None:
            result['AKProjectId'] = self.akproject_id
        if self.corp_identifier is not None:
            result['CorpIdentifier'] = self.corp_identifier
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.assigned_to is not None:
            result['AssignedTo'] = self.assigned_to
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.description is not None:
            result['Description'] = self.description
        if self.stamp is not None:
            result['Stamp'] = self.stamp
        if self.cf_list_shrink is not None:
            result['CfList'] = self.cf_list_shrink
        if self.issue_id is not None:
            result['IssueId'] = self.issue_id
        if self.status is not None:
            result['Status'] = self.status
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.serious_level is not None:
            result['SeriousLevel'] = self.serious_level
        if self.verifier is not None:
            result['Verifier'] = self.verifier
        if self.sprint_id is not None:
            result['SprintId'] = self.sprint_id
        if self.ignore_check is not None:
            result['IgnoreCheck'] = self.ignore_check
        if self.cfs_shrink is not None:
            result['Cfs'] = self.cfs_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AKProjectId') is not None:
            self.akproject_id = m.get('AKProjectId')
        if m.get('CorpIdentifier') is not None:
            self.corp_identifier = m.get('CorpIdentifier')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('AssignedTo') is not None:
            self.assigned_to = m.get('AssignedTo')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Stamp') is not None:
            self.stamp = m.get('Stamp')
        if m.get('CfList') is not None:
            self.cf_list_shrink = m.get('CfList')
        if m.get('IssueId') is not None:
            self.issue_id = m.get('IssueId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SeriousLevel') is not None:
            self.serious_level = m.get('SeriousLevel')
        if m.get('Verifier') is not None:
            self.verifier = m.get('Verifier')
        if m.get('SprintId') is not None:
            self.sprint_id = m.get('SprintId')
        if m.get('IgnoreCheck') is not None:
            self.ignore_check = m.get('IgnoreCheck')
        if m.get('Cfs') is not None:
            self.cfs_shrink = m.get('Cfs')
        return self


class UpdateWorkitemResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWorkitemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateWorkitemResponseBody = None,
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
            temp_model = UpdateWorkitemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


