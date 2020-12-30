# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddGroupMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
        client_token: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddGroupMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AddGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[AddGroupMemberResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = AddGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class AddGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGroupMemberResponseBody = None,
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
            temp_model = AddGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRepositoryMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
        client_token: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AddRepositoryMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[AddRepositoryMemberResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = AddRepositoryMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class AddRepositoryMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRepositoryMemberResponseBody = None,
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
            temp_model = AddRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWebhookRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AddWebhookResponseBodyResult(TeaModel):
    def __init__(
        self,
        push_events: bool = None,
        build_events: bool = None,
        project_id: int = None,
        created_at: str = None,
        tag_push_events: bool = None,
        issues_events: bool = None,
        url: str = None,
        last_test_result: str = None,
        merge_requests_events: bool = None,
        description: str = None,
        note_events: bool = None,
        secret_token: str = None,
        id: int = None,
        enable_ssl_verification: bool = None,
    ):
        self.push_events = push_events
        self.build_events = build_events
        self.project_id = project_id
        self.created_at = created_at
        self.tag_push_events = tag_push_events
        self.issues_events = issues_events
        self.url = url
        self.last_test_result = last_test_result
        self.merge_requests_events = merge_requests_events
        self.description = description
        self.note_events = note_events
        self.secret_token = secret_token
        self.id = id
        self.enable_ssl_verification = enable_ssl_verification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.build_events is not None:
            result['BuildEvents'] = self.build_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
        if self.issues_events is not None:
            result['IssuesEvents'] = self.issues_events
        if self.url is not None:
            result['Url'] = self.url
        if self.last_test_result is not None:
            result['LastTestResult'] = self.last_test_result
        if self.merge_requests_events is not None:
            result['MergeRequestsEvents'] = self.merge_requests_events
        if self.description is not None:
            result['Description'] = self.description
        if self.note_events is not None:
            result['NoteEvents'] = self.note_events
        if self.secret_token is not None:
            result['SecretToken'] = self.secret_token
        if self.id is not None:
            result['Id'] = self.id
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushEvents') is not None:
            self.push_events = m.get('PushEvents')
        if m.get('BuildEvents') is not None:
            self.build_events = m.get('BuildEvents')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
        if m.get('IssuesEvents') is not None:
            self.issues_events = m.get('IssuesEvents')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('LastTestResult') is not None:
            self.last_test_result = m.get('LastTestResult')
        if m.get('MergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('MergeRequestsEvents')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NoteEvents') is not None:
            self.note_events = m.get('NoteEvents')
        if m.get('SecretToken') is not None:
            self.secret_token = m.get('SecretToken')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        return self


class AddWebhookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: AddWebhookResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = AddWebhookResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AddWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddWebhookResponseBody = None,
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
            temp_model = AddWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBranchRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateBranchResponseBodyResultCommitInfo(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        parent_ids: List[str] = None,
        author_name: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
    ):
        self.short_id = short_id
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.parent_ids = parent_ids
        self.author_name = author_name
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.title is not None:
            result['Title'] = self.title
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        return self


class CreateBranchResponseBodyResult(TeaModel):
    def __init__(
        self,
        protected_branch: bool = None,
        commit_info: CreateBranchResponseBodyResultCommitInfo = None,
        branch_name: str = None,
    ):
        self.protected_branch = protected_branch
        self.commit_info = commit_info
        self.branch_name = branch_name

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        result = dict()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        if m.get('CommitInfo') is not None:
            temp_model = CreateBranchResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class CreateBranchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: CreateBranchResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CreateBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateBranchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBranchResponseBody = None,
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
            temp_model = CreateBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
        client_token: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        branch_name: str = None,
    ):
        self.file_path = file_path
        self.branch_name = branch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class CreateFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: CreateFileResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CreateFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFileResponseBody = None,
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
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMergeRequestRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        satisfied_items: List[str] = None,
        check_status: str = None,
        check_type: str = None,
        unsatisfied_items: List[str] = None,
        extra_users: List[CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        check_name: str = None,
    ):
        self.satisfied_items = satisfied_items
        self.check_status = check_status
        self.check_type = check_type
        self.unsatisfied_items = unsatisfied_items
        self.extra_users = extra_users
        self.check_name = check_name

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        satisfied_items: List[str] = None,
        check_status: str = None,
        check_type: str = None,
        unsatisfied_items: List[str] = None,
        extra_users: List[CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        check_name: str = None,
    ):
        self.satisfied_items = satisfied_items
        self.check_status = check_status
        self.check_type = check_type
        self.unsatisfied_items = unsatisfied_items
        self.extra_users = extra_users
        self.check_name = check_name

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        unsatisfied_check_results: List[CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
        satisfied_check_results: List[CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.unsatisfied_check_results = unsatisfied_check_results
        self.satisfied_check_results = satisfied_check_results

    def validate(self):
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        return self


class CreateMergeRequestResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        behind_commit_count: int = None,
        project_id: int = None,
        assignee_list: List[CreateMergeRequestResponseBodyResultAssigneeList] = None,
        created_at: str = None,
        author: CreateMergeRequestResponseBodyResultAuthor = None,
        accepted_revision: str = None,
        approve_check_result: CreateMergeRequestResponseBodyResultApproveCheckResult = None,
        source_branch: str = None,
        web_url: str = None,
        description: str = None,
        merge_type: str = None,
        name_with_namespace: str = None,
        target_branch: str = None,
        ahead_commit_count: int = None,
        updated_at: str = None,
        title: str = None,
        merge_error: str = None,
        merged_revision: str = None,
        id: int = None,
        merge_status: str = None,
    ):
        self.state = state
        self.behind_commit_count = behind_commit_count
        self.project_id = project_id
        self.assignee_list = assignee_list
        self.created_at = created_at
        self.author = author
        self.accepted_revision = accepted_revision
        self.approve_check_result = approve_check_result
        self.source_branch = source_branch
        self.web_url = web_url
        self.description = description
        self.merge_type = merge_type
        self.name_with_namespace = name_with_namespace
        self.target_branch = target_branch
        self.ahead_commit_count = ahead_commit_count
        self.updated_at = updated_at
        self.title = title
        self.merge_error = merge_error
        self.merged_revision = merged_revision
        self.id = id
        self.merge_status = merge_status

    def validate(self):
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()
        if self.approve_check_result:
            self.approve_check_result.validate()

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.title is not None:
            result['Title'] = self.title
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = CreateMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Author') is not None:
            temp_model = CreateMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('ApproveCheckResult') is not None:
            temp_model = CreateMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        return self


class CreateMergeRequestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: CreateMergeRequestResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CreateMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateMergeRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMergeRequestResponseBody = None,
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
            temp_model = CreateMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        sync: bool = None,
        create_parent_path: bool = None,
        organization_id: str = None,
        sub_user_id: str = None,
        client_token: str = None,
    ):
        self.access_token = access_token
        self.sync = sync
        self.create_parent_path = create_parent_path
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.sync is not None:
            result['Sync'] = self.sync
        if self.create_parent_path is not None:
            result['CreateParentPath'] = self.create_parent_path
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        if m.get('CreateParentPath') is not None:
            self.create_parent_path = m.get('CreateParentPath')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRepositoryResponseBodyResultNamespace(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        description: str = None,
        state: str = None,
        public: bool = None,
        visibility_level: str = None,
        created_at: str = None,
        path: str = None,
        updated_at: str = None,
        name: str = None,
        owner_id: int = None,
        id: int = None,
    ):
        self.avatar = avatar
        self.description = description
        self.state = state
        self.public = public
        self.visibility_level = visibility_level
        self.created_at = created_at
        self.path = path
        self.updated_at = updated_at
        self.name = name
        self.owner_id = owner_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.description is not None:
            result['Description'] = self.description
        if self.state is not None:
            result['State'] = self.state
        if self.public is not None:
            result['Public'] = self.public
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateRepositoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        default_branch: str = None,
        snippets_enable_status: bool = None,
        created_at: str = None,
        builds_enable_status: bool = None,
        web_url: str = None,
        description: str = None,
        tag_list: List[str] = None,
        public: bool = None,
        path_with_namespace: str = None,
        visibility_level: str = None,
        wiki_enable_status: bool = None,
        name: str = None,
        last_activity_at: str = None,
        avatar_url: str = None,
        archive: bool = None,
        namespace: CreateRepositoryResponseBodyResultNamespace = None,
        issues_enable_status: bool = None,
        demo_project_status: bool = None,
        creator_id: int = None,
        http_url_to_repo: str = None,
        name_with_namespace: str = None,
        merge_request_enable_status: bool = None,
        path: str = None,
        ssh_url_to_repo: str = None,
        id: int = None,
    ):
        self.default_branch = default_branch
        self.snippets_enable_status = snippets_enable_status
        self.created_at = created_at
        self.builds_enable_status = builds_enable_status
        self.web_url = web_url
        self.description = description
        self.tag_list = tag_list
        self.public = public
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.wiki_enable_status = wiki_enable_status
        self.name = name
        self.last_activity_at = last_activity_at
        self.avatar_url = avatar_url
        self.archive = archive
        self.namespace = namespace
        self.issues_enable_status = issues_enable_status
        self.demo_project_status = demo_project_status
        self.creator_id = creator_id
        self.http_url_to_repo = http_url_to_repo
        self.name_with_namespace = name_with_namespace
        self.merge_request_enable_status = merge_request_enable_status
        self.path = path
        self.ssh_url_to_repo = ssh_url_to_repo
        self.id = id

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        result = dict()
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.snippets_enable_status is not None:
            result['SnippetsEnableStatus'] = self.snippets_enable_status
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.builds_enable_status is not None:
            result['BuildsEnableStatus'] = self.builds_enable_status
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.public is not None:
            result['Public'] = self.public
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.wiki_enable_status is not None:
            result['WikiEnableStatus'] = self.wiki_enable_status
        if self.name is not None:
            result['Name'] = self.name
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        if self.issues_enable_status is not None:
            result['IssuesEnableStatus'] = self.issues_enable_status
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.merge_request_enable_status is not None:
            result['MergeRequestEnableStatus'] = self.merge_request_enable_status
        if self.path is not None:
            result['Path'] = self.path
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('SnippetsEnableStatus') is not None:
            self.snippets_enable_status = m.get('SnippetsEnableStatus')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('BuildsEnableStatus') is not None:
            self.builds_enable_status = m.get('BuildsEnableStatus')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WikiEnableStatus') is not None:
            self.wiki_enable_status = m.get('WikiEnableStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('Namespace') is not None:
            temp_model = CreateRepositoryResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        if m.get('IssuesEnableStatus') is not None:
            self.issues_enable_status = m.get('IssuesEnableStatus')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('MergeRequestEnableStatus') is not None:
            self.merge_request_enable_status = m.get('MergeRequestEnableStatus')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        error_message: str = None,
        success: bool = None,
        result: CreateRepositoryResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CreateRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepositoryResponseBody = None,
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
            temp_model = CreateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryGroupRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
        client_token: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRepositoryGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        avatar_url: str = None,
        owner_id: int = None,
        parent_id: int = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        path: str = None,
        visibility_level: str = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.avatar_url = avatar_url
        self.owner_id = owner_id
        self.parent_id = parent_id
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.path = path
        self.visibility_level = visibility_level
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.path is not None:
            result['Path'] = self.path
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateRepositoryGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        error_message: str = None,
        success: bool = None,
        result: CreateRepositoryGroupResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CreateRepositoryGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateRepositoryGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepositoryGroupResponseBody = None,
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
            temp_model = CreateRepositoryGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class CreateTagResponseBodyResultRelease(TeaModel):
    def __init__(
        self,
        description: str = None,
        tag_name: str = None,
    ):
        self.description = description
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class CreateTagResponseBodyResultCommitInfo(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        parent_ids: List[str] = None,
        author_name: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
    ):
        self.short_id = short_id
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.parent_ids = parent_ids
        self.author_name = author_name
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.title is not None:
            result['Title'] = self.title
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        return self


class CreateTagResponseBodyResult(TeaModel):
    def __init__(
        self,
        release: CreateTagResponseBodyResultRelease = None,
        message: str = None,
        commit_info: CreateTagResponseBodyResultCommitInfo = None,
        name: str = None,
    ):
        self.release = release
        self.message = message
        self.commit_info = commit_info
        self.name = name

    def validate(self):
        if self.release:
            self.release.validate()
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        result = dict()
        if self.release is not None:
            result['Release'] = self.release.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Release') is not None:
            temp_model = CreateTagResponseBodyResultRelease()
            self.release = temp_model.from_map(m['Release'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('CommitInfo') is not None:
            temp_model = CreateTagResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: CreateTagResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = CreateTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTagResponseBody = None,
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBranchRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        branch_name: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.branch_name = branch_name
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteBranchResponseBodyResult(TeaModel):
    def __init__(
        self,
        branch_name: str = None,
    ):
        self.branch_name = branch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class DeleteBranchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteBranchResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteBranchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBranchResponseBody = None,
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
            temp_model = DeleteBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        branch_name: str = None,
        file_path: str = None,
        commit_message: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.branch_name = branch_name
        self.file_path = file_path
        self.commit_message = commit_message
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.commit_message is not None:
            result['CommitMessage'] = self.commit_message
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('CommitMessage') is not None:
            self.commit_message = m.get('CommitMessage')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        branch_name: str = None,
    ):
        self.file_path = file_path
        self.branch_name = branch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteFileResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileResponseBody = None,
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteGroupMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteGroupMemberResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteGroupMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupMemberResponseBody = None,
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
            temp_model = DeleteGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteRepositoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteRepositoryResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryResponseBody = None,
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
            temp_model = DeleteRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryGroupRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteRepositoryGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteRepositoryGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteRepositoryGroupResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryGroupResponseBody = None,
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
            temp_model = DeleteRepositoryGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class DeleteRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        source_type: str = None,
        created_at: str = None,
        message: str = None,
        access_level: int = None,
        updated_at: str = None,
        source_id: int = None,
        notification_level: int = None,
        id: int = None,
    ):
        self.user_id = user_id
        self.source_type = source_type
        self.created_at = created_at
        self.message = message
        self.access_level = access_level
        self.updated_at = updated_at
        self.source_id = source_id
        self.notification_level = notification_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.notification_level is not None:
            result['NotificationLevel'] = self.notification_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('NotificationLevel') is not None:
            self.notification_level = m.get('NotificationLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRepositoryMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteRepositoryMemberResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryMemberResponseBody = None,
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
            temp_model = DeleteRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryTagRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteRepositoryTagResponseBodyResult(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
    ):
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DeleteRepositoryTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteRepositoryTagResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryTagResponseBody = None,
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
            temp_model = DeleteRepositoryTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryWebhookRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteRepositoryWebhookResponseBodyResult(TeaModel):
    def __init__(
        self,
        push_events: bool = None,
        project_id: int = None,
        created_at: str = None,
        tag_push_events: bool = None,
        url: str = None,
        last_test_result: str = None,
        description: str = None,
        merge_requests_events: bool = None,
        secret_token: str = None,
        note_events: bool = None,
        enable_ssl_verification: bool = None,
        id: int = None,
    ):
        self.push_events = push_events
        self.project_id = project_id
        self.created_at = created_at
        self.tag_push_events = tag_push_events
        self.url = url
        self.last_test_result = last_test_result
        self.description = description
        self.merge_requests_events = merge_requests_events
        self.secret_token = secret_token
        self.note_events = note_events
        self.enable_ssl_verification = enable_ssl_verification
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['Url'] = self.url
        if self.last_test_result is not None:
            result['LastTestResult'] = self.last_test_result
        if self.description is not None:
            result['Description'] = self.description
        if self.merge_requests_events is not None:
            result['MergeRequestsEvents'] = self.merge_requests_events
        if self.secret_token is not None:
            result['SecretToken'] = self.secret_token
        if self.note_events is not None:
            result['NoteEvents'] = self.note_events
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushEvents') is not None:
            self.push_events = m.get('PushEvents')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('LastTestResult') is not None:
            self.last_test_result = m.get('LastTestResult')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('MergeRequestsEvents')
        if m.get('SecretToken') is not None:
            self.secret_token = m.get('SecretToken')
        if m.get('NoteEvents') is not None:
            self.note_events = m.get('NoteEvents')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRepositoryWebhookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: DeleteRepositoryWebhookResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryWebhookResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryWebhookResponseBody = None,
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
            temp_model = DeleteRepositoryWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBranchInfoRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
        branch_name: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.branch_name = branch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class GetBranchInfoResponseBodyResultCommitInfo(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        parent_ids: List[str] = None,
        author_name: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
    ):
        self.short_id = short_id
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.parent_ids = parent_ids
        self.author_name = author_name
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.title is not None:
            result['Title'] = self.title
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        return self


class GetBranchInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        protected_branch: bool = None,
        commit_info: GetBranchInfoResponseBodyResultCommitInfo = None,
        branch_name: str = None,
    ):
        self.protected_branch = protected_branch
        self.commit_info = commit_info
        self.branch_name = branch_name

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        result = dict()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        if m.get('CommitInfo') is not None:
            temp_model = GetBranchInfoResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class GetBranchInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetBranchInfoResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetBranchInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetBranchInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBranchInfoResponseBody = None,
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
            temp_model = GetBranchInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeupOrganizationRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetCodeupOrganizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        namespace_id: int = None,
        user_role: str = None,
        path: str = None,
        created_at: str = None,
        updated_at: str = None,
        id: int = None,
        organization_id: str = None,
    ):
        self.namespace_id = namespace_id
        self.user_role = user_role
        self.path = path
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = id
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.user_role is not None:
            result['UserRole'] = self.user_role
        if self.path is not None:
            result['Path'] = self.path
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetCodeupOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetCodeupOrganizationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetCodeupOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetCodeupOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCodeupOrganizationResponseBody = None,
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
            temp_model = GetCodeupOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileBlobsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        file_path: str = None,
        ref: str = None,
        from_: int = None,
        to: int = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.file_path = file_path
        self.ref = ref
        self.from_ = from_
        self.to = to
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.ref is not None:
            result['Ref'] = self.ref
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Ref') is not None:
            self.ref = m.get('Ref')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetFileBlobsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total_lines: int = None,
        content: str = None,
    ):
        self.total_lines = total_lines
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_lines is not None:
            result['TotalLines'] = self.total_lines
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalLines') is not None:
            self.total_lines = m.get('TotalLines')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetFileBlobsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetFileBlobsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetFileBlobsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetFileBlobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileBlobsResponseBody = None,
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
            temp_model = GetFileBlobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupDetailRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        group_id: int = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.group_id = group_id
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetGroupDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        avatar_url: str = None,
        owner_id: int = None,
        parent_id: int = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        visibility_level: str = None,
        path: str = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.avatar_url = avatar_url
        self.owner_id = owner_id
        self.parent_id = parent_id
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.path = path
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.path is not None:
            result['Path'] = self.path
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetGroupDetailResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetGroupDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupDetailResponseBody = None,
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
            temp_model = GetGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class GetProjectMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        access_level: int = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.access_level = access_level
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetProjectMemberResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetProjectMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetProjectMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectMemberResponseBody = None,
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
            temp_model = GetProjectMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryInfoRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        identity: str = None,
        organization_id: str = None,
    ):
        self.access_token = access_token
        self.identity = identity
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetRepositoryInfoResponseBodyResultNamespace(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        description: str = None,
        state: str = None,
        public: bool = None,
        visibility_level: str = None,
        created_at: str = None,
        path: str = None,
        updated_at: str = None,
        name: str = None,
        owner_id: int = None,
        id: int = None,
    ):
        self.avatar = avatar
        self.description = description
        self.state = state
        self.public = public
        self.visibility_level = visibility_level
        self.created_at = created_at
        self.path = path
        self.updated_at = updated_at
        self.name = name
        self.owner_id = owner_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.description is not None:
            result['Description'] = self.description
        if self.state is not None:
            result['State'] = self.state
        if self.public is not None:
            result['Public'] = self.public
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRepositoryInfoResponseBodyResultPermissionsProjectAccess(TeaModel):
    def __init__(
        self,
        access_level: int = None,
    ):
        self.access_level = access_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        return self


class GetRepositoryInfoResponseBodyResultPermissionsGroupAccess(TeaModel):
    def __init__(
        self,
        access_level: int = None,
    ):
        self.access_level = access_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        return self


class GetRepositoryInfoResponseBodyResultPermissions(TeaModel):
    def __init__(
        self,
        project_access: GetRepositoryInfoResponseBodyResultPermissionsProjectAccess = None,
        group_access: GetRepositoryInfoResponseBodyResultPermissionsGroupAccess = None,
    ):
        self.project_access = project_access
        self.group_access = group_access

    def validate(self):
        if self.project_access:
            self.project_access.validate()
        if self.group_access:
            self.group_access.validate()

    def to_map(self):
        result = dict()
        if self.project_access is not None:
            result['ProjectAccess'] = self.project_access.to_map()
        if self.group_access is not None:
            result['GroupAccess'] = self.group_access.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectAccess') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissionsProjectAccess()
            self.project_access = temp_model.from_map(m['ProjectAccess'])
        if m.get('GroupAccess') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissionsGroupAccess()
            self.group_access = temp_model.from_map(m['GroupAccess'])
        return self


class GetRepositoryInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        default_branch: str = None,
        import_url: str = None,
        created_at: str = None,
        web_url: str = None,
        tag_list: List[str] = None,
        description: str = None,
        public: bool = None,
        path_with_namespace: str = None,
        visibility_level: str = None,
        name: str = None,
        last_activity_at: str = None,
        avatar_url: str = None,
        archive: bool = None,
        namespace: GetRepositoryInfoResponseBodyResultNamespace = None,
        demo_project_status: bool = None,
        creator_id: int = None,
        import_status: str = None,
        http_url_to_repo: str = None,
        permissions: GetRepositoryInfoResponseBodyResultPermissions = None,
        name_with_namespace: str = None,
        path: str = None,
        access_level: int = None,
        import_from_subversion: bool = None,
        ssh_url_to_repo: str = None,
        id: int = None,
    ):
        self.default_branch = default_branch
        self.import_url = import_url
        self.created_at = created_at
        self.web_url = web_url
        self.tag_list = tag_list
        self.description = description
        self.public = public
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.name = name
        self.last_activity_at = last_activity_at
        self.avatar_url = avatar_url
        self.archive = archive
        self.namespace = namespace
        self.demo_project_status = demo_project_status
        self.creator_id = creator_id
        self.import_status = import_status
        self.http_url_to_repo = http_url_to_repo
        self.permissions = permissions
        self.name_with_namespace = name_with_namespace
        self.path = path
        self.access_level = access_level
        self.import_from_subversion = import_from_subversion
        self.ssh_url_to_repo = ssh_url_to_repo
        self.id = id

    def validate(self):
        if self.namespace:
            self.namespace.validate()
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        result = dict()
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.import_url is not None:
            result['ImportUrl'] = self.import_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.description is not None:
            result['Description'] = self.description
        if self.public is not None:
            result['Public'] = self.public
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.name is not None:
            result['Name'] = self.name
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path is not None:
            result['Path'] = self.path
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.import_from_subversion is not None:
            result['ImportFromSubversion'] = self.import_from_subversion
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('ImportUrl') is not None:
            self.import_url = m.get('ImportUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('Namespace') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('Permissions') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissions()
            self.permissions = temp_model.from_map(m['Permissions'])
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('ImportFromSubversion') is not None:
            self.import_from_subversion = m.get('ImportFromSubversion')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRepositoryInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: int = None,
        error_message: str = None,
        success: bool = None,
        result: GetRepositoryInfoResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetRepositoryInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRepositoryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepositoryInfoResponseBody = None,
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
            temp_model = GetRepositoryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryTagRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetRepositoryTagResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        gpg_key_id: str = None,
        verification_status: str = None,
    ):
        self.gpg_key_id = gpg_key_id
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryTagResponseBodyResultCommitSignature(TeaModel):
    def __init__(
        self,
        gpg_key_id: str = None,
        verification_status: str = None,
    ):
        self.gpg_key_id = gpg_key_id
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetRepositoryTagResponseBodyResultCommit(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        signature: GetRepositoryTagResponseBodyResultCommitSignature = None,
        parent_ids: List[str] = None,
        author_name: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
    ):
        self.short_id = short_id
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.signature = signature
        self.parent_ids = parent_ids
        self.author_name = author_name
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.title is not None:
            result['Title'] = self.title
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        return self


class GetRepositoryTagResponseBodyResult(TeaModel):
    def __init__(
        self,
        signature: GetRepositoryTagResponseBodyResultSignature = None,
        commit: GetRepositoryTagResponseBodyResultCommit = None,
        message: str = None,
        name: str = None,
        id: str = None,
    ):
        self.signature = signature
        self.commit = commit
        self.message = message
        self.name = name
        self.id = id

    def validate(self):
        if self.signature:
            self.signature.validate()
        if self.commit:
            self.commit.validate()

    def to_map(self):
        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Commit') is not None:
            temp_model = GetRepositoryTagResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRepositoryTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetRepositoryTagResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetRepositoryTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRepositoryTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepositoryTagResponseBody = None,
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
            temp_model = GetRepositoryTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
    ):
        self.access_token = access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class GetUserInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        email: str = None,
        avatar_url: str = None,
        external_user_id: str = None,
        name: str = None,
        id: int = None,
        username: str = None,
    ):
        self.email = email
        self.avatar_url = avatar_url
        self.external_user_id = external_user_id
        self.name = name
        self.id = id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: GetUserInfoResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserInfoResponseBody = None,
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
            temp_model = GetUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListGroupMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListGroupMemberResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupMemberResponseBody = None,
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
            temp_model = ListGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRepositoriesRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        is_member: bool = None,
        sub_user_id: str = None,
        search: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.is_member = is_member
        self.sub_user_id = sub_user_id
        self.search = search
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.is_member is not None:
            result['IsMember'] = self.is_member
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.search is not None:
            result['Search'] = self.search
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('IsMember') is not None:
            self.is_member = m.get('IsMember')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGroupRepositoriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        last_activity_at: str = None,
        namespace_id: int = None,
        http_clone_url: str = None,
        archive: bool = None,
        created_at: str = None,
        ssh_clone_url: str = None,
        creator_id: int = None,
        import_status: str = None,
        web_url: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        visibility_level: int = None,
        path: str = None,
        updated_at: str = None,
        name: str = None,
        id: int = None,
    ):
        self.last_activity_at = last_activity_at
        self.namespace_id = namespace_id
        self.http_clone_url = http_clone_url
        self.archive = archive
        self.created_at = created_at
        self.ssh_clone_url = ssh_clone_url
        self.creator_id = creator_id
        self.import_status = import_status
        self.web_url = web_url
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.path = path
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.http_clone_url is not None:
            result['HttpCloneUrl'] = self.http_clone_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.ssh_clone_url is not None:
            result['SshCloneUrl'] = self.ssh_clone_url
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('HttpCloneUrl') is not None:
            self.http_clone_url = m.get('HttpCloneUrl')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('SshCloneUrl') is not None:
            self.ssh_clone_url = m.get('SshCloneUrl')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListGroupRepositoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListGroupRepositoriesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGroupRepositoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListGroupRepositoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupRepositoriesResponseBody = None,
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
            temp_model = ListGroupRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        search: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
        sub_user_id: str = None,
        include_personal: bool = None,
    ):
        self.access_token = access_token
        self.search = search
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size
        self.sub_user_id = sub_user_id
        self.include_personal = include_personal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.search is not None:
            result['Search'] = self.search
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.include_personal is not None:
            result['IncludePersonal'] = self.include_personal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('IncludePersonal') is not None:
            self.include_personal = m.get('IncludePersonal')
        return self


class ListGroupsResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        created_at: str = None,
        owner_id: int = None,
        parent_id: int = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        path: str = None,
        visibility_level: str = None,
        access_level: int = None,
        updated_at: str = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.created_at = created_at
        self.owner_id = owner_id
        self.parent_id = parent_id
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.path = path
        self.visibility_level = visibility_level
        self.access_level = access_level
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.path is not None:
            result['Path'] = self.path
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListGroupsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupsResponseBody = None,
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        access_level: int = None,
        min_access_level: int = None,
    ):
        self.access_token = access_token
        self.access_level = access_level
        self.min_access_level = min_access_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.min_access_level is not None:
            result['MinAccessLevel'] = self.min_access_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('MinAccessLevel') is not None:
            self.min_access_level = m.get('MinAccessLevel')
        return self


class ListOrganizationsResponseBodyResult(TeaModel):
    def __init__(
        self,
        organization_role: str = None,
        access_level: int = None,
        organization_name: str = None,
        organization_id: str = None,
    ):
        self.organization_role = organization_role
        self.access_level = access_level
        self.organization_name = organization_name
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organization_role is not None:
            result['OrganizationRole'] = self.organization_role
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationRole') is not None:
            self.organization_role = m.get('OrganizationRole')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListOrganizationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListOrganizationsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListOrganizationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListOrganizationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrganizationsResponseBody = None,
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
            temp_model = ListOrganizationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoriesRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
        order: str = None,
        sort: str = None,
        search: str = None,
        archive: bool = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size
        self.order = order
        self.sort = sort
        self.search = search
        self.archive = archive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.order is not None:
            result['Order'] = self.order
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.search is not None:
            result['Search'] = self.search
        if self.archive is not None:
            result['Archive'] = self.archive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        return self


class ListRepositoriesResponseBodyResult(TeaModel):
    def __init__(
        self,
        last_activity_at: str = None,
        namespace_id: int = None,
        avatar_url: str = None,
        star_count: int = None,
        archive: bool = None,
        created_at: str = None,
        demo_project_status: bool = None,
        star: bool = None,
        import_status: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        path: str = None,
        visibility_level: str = None,
        access_level: int = None,
        updated_at: str = None,
        name: str = None,
        id: int = None,
    ):
        self.last_activity_at = last_activity_at
        self.namespace_id = namespace_id
        self.avatar_url = avatar_url
        self.star_count = star_count
        self.archive = archive
        self.created_at = created_at
        self.demo_project_status = demo_project_status
        self.star = star
        self.import_status = import_status
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.path = path
        self.visibility_level = visibility_level
        self.access_level = access_level
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.star_count is not None:
            result['StarCount'] = self.star_count
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.star is not None:
            result['Star'] = self.star
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.path is not None:
            result['Path'] = self.path
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('StarCount') is not None:
            self.star_count = m.get('StarCount')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('Star') is not None:
            self.star = m.get('Star')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRepositoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: int = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListRepositoriesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoriesResponseBody = None,
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
            temp_model = ListRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryBranchesRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
        page: int = None,
        page_size: int = None,
        search: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id
        self.page = page
        self.page_size = page_size
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        return self


class ListRepositoryBranchesResponseBodyResultCommitInfo(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        parent_ids: List[str] = None,
        author_name: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
    ):
        self.short_id = short_id
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.parent_ids = parent_ids
        self.author_name = author_name
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.title is not None:
            result['Title'] = self.title
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        return self


class ListRepositoryBranchesResponseBodyResult(TeaModel):
    def __init__(
        self,
        protected_branch: bool = None,
        commit_info: ListRepositoryBranchesResponseBodyResultCommitInfo = None,
        branch_name: str = None,
    ):
        self.protected_branch = protected_branch
        self.commit_info = commit_info
        self.branch_name = branch_name

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        result = dict()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        if m.get('CommitInfo') is not None:
            temp_model = ListRepositoryBranchesResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class ListRepositoryBranchesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListRepositoryBranchesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryBranchesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryBranchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryBranchesResponseBody = None,
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
            temp_model = ListRepositoryBranchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        query: str = None,
        page: int = None,
        page_size: int = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.query = query
        self.page = page
        self.page_size = page_size
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.query is not None:
            result['Query'] = self.query
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRepositoryMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListRepositoryMemberResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryMemberResponseBody = None,
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
            temp_model = ListRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryTagsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        search: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
        sort: str = None,
        show_signature: bool = None,
    ):
        self.access_token = access_token
        self.search = search
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size
        self.sort = sort
        self.show_signature = show_signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.search is not None:
            result['Search'] = self.search
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.show_signature is not None:
            result['ShowSignature'] = self.show_signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('ShowSignature') is not None:
            self.show_signature = m.get('ShowSignature')
        return self


class ListRepositoryTagsResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        gpg_key_id: str = None,
        verification_status: str = None,
    ):
        self.gpg_key_id = gpg_key_id
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListRepositoryTagsResponseBodyResultCommitSignature(TeaModel):
    def __init__(
        self,
        gpg_key_id: str = None,
        verification_status: str = None,
    ):
        self.gpg_key_id = gpg_key_id
        self.verification_status = verification_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListRepositoryTagsResponseBodyResultCommit(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        signature: ListRepositoryTagsResponseBodyResultCommitSignature = None,
        parent_ids: List[str] = None,
        author_name: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
    ):
        self.short_id = short_id
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.signature = signature
        self.parent_ids = parent_ids
        self.author_name = author_name
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.title is not None:
            result['Title'] = self.title
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('Signature') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        return self


class ListRepositoryTagsResponseBodyResult(TeaModel):
    def __init__(
        self,
        signature: ListRepositoryTagsResponseBodyResultSignature = None,
        commit: ListRepositoryTagsResponseBodyResultCommit = None,
        message: str = None,
        name: str = None,
        id: str = None,
    ):
        self.signature = signature
        self.commit = commit
        self.message = message
        self.name = name
        self.id = id

    def validate(self):
        if self.signature:
            self.signature.validate()
        if self.commit:
            self.commit.validate()

    def to_map(self):
        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Commit') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRepositoryTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListRepositoryTagsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryTagsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryTagsResponseBody = None,
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
            temp_model = ListRepositoryTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryTreeRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        path: str = None,
        type: str = None,
        ref_name: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.path = path
        self.type = type
        self.ref_name = ref_name
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        if self.ref_name is not None:
            result['RefName'] = self.ref_name
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RefName') is not None:
            self.ref_name = m.get('RefName')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class ListRepositoryTreeResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        path: str = None,
        mode: str = None,
        name: str = None,
        id: str = None,
    ):
        self.type = type
        self.path = path
        self.mode = mode
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.path is not None:
            result['Path'] = self.path
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRepositoryTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListRepositoryTreeResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryTreeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryTreeResponseBody = None,
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
            temp_model = ListRepositoryTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryWebhookRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRepositoryWebhookResponseBodyResult(TeaModel):
    def __init__(
        self,
        push_events: bool = None,
        project_id: int = None,
        created_at: str = None,
        tag_push_events: bool = None,
        url: str = None,
        last_test_result: str = None,
        description: str = None,
        merge_requests_events: bool = None,
        secret_token: str = None,
        note_events: bool = None,
        enable_ssl_verification: bool = None,
        id: int = None,
    ):
        self.push_events = push_events
        self.project_id = project_id
        self.created_at = created_at
        self.tag_push_events = tag_push_events
        self.url = url
        self.last_test_result = last_test_result
        self.description = description
        self.merge_requests_events = merge_requests_events
        self.secret_token = secret_token
        self.note_events = note_events
        self.enable_ssl_verification = enable_ssl_verification
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['Url'] = self.url
        if self.last_test_result is not None:
            result['LastTestResult'] = self.last_test_result
        if self.description is not None:
            result['Description'] = self.description
        if self.merge_requests_events is not None:
            result['MergeRequestsEvents'] = self.merge_requests_events
        if self.secret_token is not None:
            result['SecretToken'] = self.secret_token
        if self.note_events is not None:
            result['NoteEvents'] = self.note_events
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushEvents') is not None:
            self.push_events = m.get('PushEvents')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('LastTestResult') is not None:
            self.last_test_result = m.get('LastTestResult')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('MergeRequestsEvents')
        if m.get('SecretToken') is not None:
            self.secret_token = m.get('SecretToken')
        if m.get('NoteEvents') is not None:
            self.note_events = m.get('NoteEvents')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListRepositoryWebhookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: List[ListRepositoryWebhookResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryWebhookResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryWebhookResponseBody = None,
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
            temp_model = ListRepositoryWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeMergeRequestRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class MergeMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        satisfied_items: List[str] = None,
        check_status: str = None,
        check_type: str = None,
        unsatisfied_items: List[str] = None,
        extra_users: List[MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        check_name: str = None,
    ):
        self.satisfied_items = satisfied_items
        self.check_status = check_status
        self.check_type = check_type
        self.unsatisfied_items = unsatisfied_items
        self.extra_users = extra_users
        self.check_name = check_name

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        avatar_url: str = None,
        name: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        satisfied_items: List[str] = None,
        check_status: str = None,
        check_type: str = None,
        unsatisfied_items: List[str] = None,
        extra_users: List[MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        check_name: str = None,
    ):
        self.satisfied_items = satisfied_items
        self.check_status = check_status
        self.check_type = check_type
        self.unsatisfied_items = unsatisfied_items
        self.extra_users = extra_users
        self.check_name = check_name

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        unsatisfied_check_results: List[MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
        satisfied_check_results: List[MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.unsatisfied_check_results = unsatisfied_check_results
        self.satisfied_check_results = satisfied_check_results

    def validate(self):
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        return self


class MergeMergeRequestResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        behind_commit_count: int = None,
        project_id: int = None,
        assignee_list: List[MergeMergeRequestResponseBodyResultAssigneeList] = None,
        created_at: str = None,
        author: MergeMergeRequestResponseBodyResultAuthor = None,
        accepted_revision: str = None,
        approve_check_result: MergeMergeRequestResponseBodyResultApproveCheckResult = None,
        source_branch: str = None,
        web_url: str = None,
        description: str = None,
        merge_type: str = None,
        name_with_namespace: str = None,
        target_branch: str = None,
        ahead_commit_count: int = None,
        updated_at: str = None,
        title: str = None,
        merge_error: str = None,
        merged_revision: str = None,
        id: int = None,
        merge_status: str = None,
    ):
        self.state = state
        self.behind_commit_count = behind_commit_count
        self.project_id = project_id
        self.assignee_list = assignee_list
        self.created_at = created_at
        self.author = author
        self.accepted_revision = accepted_revision
        self.approve_check_result = approve_check_result
        self.source_branch = source_branch
        self.web_url = web_url
        self.description = description
        self.merge_type = merge_type
        self.name_with_namespace = name_with_namespace
        self.target_branch = target_branch
        self.ahead_commit_count = ahead_commit_count
        self.updated_at = updated_at
        self.title = title
        self.merge_error = merge_error
        self.merged_revision = merged_revision
        self.id = id
        self.merge_status = merge_status

    def validate(self):
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.author:
            self.author.validate()
        if self.approve_check_result:
            self.approve_check_result.validate()

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.target_branch is not None:
            result['TargetBranch'] = self.target_branch
        if self.ahead_commit_count is not None:
            result['AheadCommitCount'] = self.ahead_commit_count
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.title is not None:
            result['Title'] = self.title
        if self.merge_error is not None:
            result['MergeError'] = self.merge_error
        if self.merged_revision is not None:
            result['MergedRevision'] = self.merged_revision
        if self.id is not None:
            result['Id'] = self.id
        if self.merge_status is not None:
            result['MergeStatus'] = self.merge_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = MergeMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Author') is not None:
            temp_model = MergeMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('ApproveCheckResult') is not None:
            temp_model = MergeMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('TargetBranch') is not None:
            self.target_branch = m.get('TargetBranch')
        if m.get('AheadCommitCount') is not None:
            self.ahead_commit_count = m.get('AheadCommitCount')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('MergeError') is not None:
            self.merge_error = m.get('MergeError')
        if m.get('MergedRevision') is not None:
            self.merged_revision = m.get('MergedRevision')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MergeStatus') is not None:
            self.merge_status = m.get('MergeStatus')
        return self


class MergeMergeRequestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: MergeMergeRequestResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = MergeMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class MergeMergeRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MergeMergeRequestResponseBody = None,
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
            temp_model = MergeMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class UpdateFileResponseBodyResult(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        branch_name: str = None,
    ):
        self.file_path = file_path
        self.branch_name = branch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        return self


class UpdateFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: UpdateFileResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = UpdateFileResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFileResponseBody = None,
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
            temp_model = UpdateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class UpdateGroupMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: UpdateGroupMemberResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = UpdateGroupMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupMemberResponseBody = None,
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
            temp_model = UpdateGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryMemberRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sub_user_id: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')
        return self


class UpdateRepositoryMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.state is not None:
            result['State'] = self.state
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateRepositoryMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        result: UpdateRepositoryMemberResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = UpdateRepositoryMemberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateRepositoryMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRepositoryMemberResponseBody = None,
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
            temp_model = UpdateRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


