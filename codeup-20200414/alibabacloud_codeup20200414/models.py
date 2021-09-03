# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteRepositoryMemberResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryProtectedBranchRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting(TeaModel):
    def __init__(
        self,
        merge_request_mode: str = None,
        allow_self_approval: bool = None,
        is_require_discussion_processed: bool = None,
        required: bool = None,
        is_reset_approval_when_new_push: bool = None,
        minimual_approval: int = None,
        default_assignees: List[str] = None,
        allow_merge_request_roles: List[int] = None,
    ):
        self.merge_request_mode = merge_request_mode
        self.allow_self_approval = allow_self_approval
        self.is_require_discussion_processed = is_require_discussion_processed
        self.required = required
        self.is_reset_approval_when_new_push = is_reset_approval_when_new_push
        self.minimual_approval = minimual_approval
        self.default_assignees = default_assignees
        self.allow_merge_request_roles = allow_merge_request_roles

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merge_request_mode is not None:
            result['MergeRequestMode'] = self.merge_request_mode
        if self.allow_self_approval is not None:
            result['AllowSelfApproval'] = self.allow_self_approval
        if self.is_require_discussion_processed is not None:
            result['IsRequireDiscussionProcessed'] = self.is_require_discussion_processed
        if self.required is not None:
            result['Required'] = self.required
        if self.is_reset_approval_when_new_push is not None:
            result['IsResetApprovalWhenNewPush'] = self.is_reset_approval_when_new_push
        if self.minimual_approval is not None:
            result['MinimualApproval'] = self.minimual_approval
        if self.default_assignees is not None:
            result['DefaultAssignees'] = self.default_assignees
        if self.allow_merge_request_roles is not None:
            result['AllowMergeRequestRoles'] = self.allow_merge_request_roles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MergeRequestMode') is not None:
            self.merge_request_mode = m.get('MergeRequestMode')
        if m.get('AllowSelfApproval') is not None:
            self.allow_self_approval = m.get('AllowSelfApproval')
        if m.get('IsRequireDiscussionProcessed') is not None:
            self.is_require_discussion_processed = m.get('IsRequireDiscussionProcessed')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('IsResetApprovalWhenNewPush') is not None:
            self.is_reset_approval_when_new_push = m.get('IsResetApprovalWhenNewPush')
        if m.get('MinimualApproval') is not None:
            self.minimual_approval = m.get('MinimualApproval')
        if m.get('DefaultAssignees') is not None:
            self.default_assignees = m.get('DefaultAssignees')
        if m.get('AllowMergeRequestRoles') is not None:
            self.allow_merge_request_roles = m.get('AllowMergeRequestRoles')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection(TeaModel):
    def __init__(
        self,
        message: str = None,
        enabled: bool = None,
    ):
        self.message = message
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection(TeaModel):
    def __init__(
        self,
        message: str = None,
        enabled: bool = None,
    ):
        self.message = message
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
    ):
        self.name = name
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig(TeaModel):
    def __init__(
        self,
        check_items: List[CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems] = None,
    ):
        self.check_items = check_items

    def validate(self):
        if self.check_items:
            for k in self.check_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItems'] = []
        if self.check_items is not None:
            for k in self.check_items:
                result['CheckItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k in m.get('CheckItems'):
                temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems()
                self.check_items.append(temp_model.from_map(k))
        return self


class CreateRepositoryProtectedBranchResponseBodyResultTestSetting(TeaModel):
    def __init__(
        self,
        required: bool = None,
        coding_guidelines_detection: CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection = None,
        sensitive_info_detection: CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection = None,
        check_config: CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig = None,
    ):
        self.required = required
        self.coding_guidelines_detection = coding_guidelines_detection
        self.sensitive_info_detection = sensitive_info_detection
        self.check_config = check_config

    def validate(self):
        if self.coding_guidelines_detection:
            self.coding_guidelines_detection.validate()
        if self.sensitive_info_detection:
            self.sensitive_info_detection.validate()
        if self.check_config:
            self.check_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['Required'] = self.required
        if self.coding_guidelines_detection is not None:
            result['CodingGuidelinesDetection'] = self.coding_guidelines_detection.to_map()
        if self.sensitive_info_detection is not None:
            result['SensitiveInfoDetection'] = self.sensitive_info_detection.to_map()
        if self.check_config is not None:
            result['CheckConfig'] = self.check_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('CodingGuidelinesDetection') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection()
            self.coding_guidelines_detection = temp_model.from_map(m['CodingGuidelinesDetection'])
        if m.get('SensitiveInfoDetection') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection()
            self.sensitive_info_detection = temp_model.from_map(m['SensitiveInfoDetection'])
        if m.get('CheckConfig') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig()
            self.check_config = temp_model.from_map(m['CheckConfig'])
        return self


class CreateRepositoryProtectedBranchResponseBodyResult(TeaModel):
    def __init__(
        self,
        branch: str = None,
        id: int = None,
        allow_push_roles: List[int] = None,
        allow_merge_roles: List[int] = None,
        merge_request_setting: CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting = None,
        test_setting: CreateRepositoryProtectedBranchResponseBodyResultTestSetting = None,
    ):
        self.branch = branch
        self.id = id
        self.allow_push_roles = allow_push_roles
        self.allow_merge_roles = allow_merge_roles
        self.merge_request_setting = merge_request_setting
        self.test_setting = test_setting

    def validate(self):
        if self.merge_request_setting:
            self.merge_request_setting.validate()
        if self.test_setting:
            self.test_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.id is not None:
            result['Id'] = self.id
        if self.allow_push_roles is not None:
            result['AllowPushRoles'] = self.allow_push_roles
        if self.allow_merge_roles is not None:
            result['AllowMergeRoles'] = self.allow_merge_roles
        if self.merge_request_setting is not None:
            result['MergeRequestSetting'] = self.merge_request_setting.to_map()
        if self.test_setting is not None:
            result['TestSetting'] = self.test_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AllowPushRoles') is not None:
            self.allow_push_roles = m.get('AllowPushRoles')
        if m.get('AllowMergeRoles') is not None:
            self.allow_merge_roles = m.get('AllowMergeRoles')
        if m.get('MergeRequestSetting') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultMergeRequestSetting()
            self.merge_request_setting = temp_model.from_map(m['MergeRequestSetting'])
        if m.get('TestSetting') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResultTestSetting()
            self.test_setting = temp_model.from_map(m['TestSetting'])
        return self


class CreateRepositoryProtectedBranchResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: CreateRepositoryProtectedBranchResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = CreateRepositoryProtectedBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateRepositoryProtectedBranchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepositoryProtectedBranchResponseBody = None,
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
            temp_model = CreateRepositoryProtectedBranchResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        name: str = None,
        avatar_url: str = None,
        id: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class CreateMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        satisfied_check_results: List[CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
        unsatisfied_check_results: List[CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.satisfied_check_results = satisfied_check_results
        self.unsatisfied_check_results = unsatisfied_check_results

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = CreateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class CreateMergeRequestResponseBodyResult(TeaModel):
    def __init__(
        self,
        behind_commit_count: int = None,
        state: str = None,
        project_id: int = None,
        created_at: str = None,
        accepted_revision: str = None,
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
        assignee_list: List[CreateMergeRequestResponseBodyResultAssigneeList] = None,
        author: CreateMergeRequestResponseBodyResultAuthor = None,
        approve_check_result: CreateMergeRequestResponseBodyResultApproveCheckResult = None,
    ):
        self.behind_commit_count = behind_commit_count
        self.state = state
        self.project_id = project_id
        self.created_at = created_at
        self.accepted_revision = accepted_revision
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
        self.assignee_list = assignee_list
        self.author = author
        self.approve_check_result = approve_check_result

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.state is not None:
            result['State'] = self.state
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
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
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
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
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = CreateMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = CreateMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('ApproveCheckResult') is not None:
            temp_model = CreateMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        return self


class CreateMergeRequestResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: CreateMergeRequestResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = CreateMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryMemberWithExternUidRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        extern_user_id: str = None,
    ):
        # 个人访问令牌。 使用阿里云AK+SK或使用STS临时授权方式不需要传该字段
        self.access_token = access_token
        # 企业标识，也称企业id，字符串形式，可在云效访问链接中获取，如 https://devops.aliyun.com/organization/\
        self.organization_id = organization_id
        # 云效用户ID
        self.extern_user_id = extern_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        return self


class DeleteRepositoryMemberWithExternUidResponseBodyResult(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        source_type: str = None,
        created_at: str = None,
        access_level: int = None,
        updated_at: str = None,
        source_id: int = None,
        id: int = None,
    ):
        # Codeup用户ID
        self.user_id = user_id
        # 资源类型
        self.source_type = source_type
        # 创建时间
        self.created_at = created_at
        # 权限类型。20-浏览者，30-开发者,40-管理员。
        self.access_level = access_level
        # 更新时间
        self.updated_at = updated_at
        # 代码库ID
        self.source_id = source_id
        # ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.source_id is not None:
            result['SourceId'] = self.source_id
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
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRepositoryMemberWithExternUidResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteRepositoryMemberWithExternUidResponseBodyResult = None,
    ):
        # 错误信息
        self.error_message = error_message
        # 请求ID
        self.request_id = request_id
        # 错误码
        self.error_code = error_code
        # 请求结果
        self.success = success
        # 响应结果
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryMemberWithExternUidResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryMemberWithExternUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryMemberWithExternUidResponseBody = None,
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
            temp_model = DeleteRepositoryMemberWithExternUidResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteRepositoryResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteRepositoryResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetRepositoryTagResponseBodyResultCommitSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class GetRepositoryTagResponseBodyResultCommit(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
        signature: GetRepositoryTagResponseBodyResultCommitSignature = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date
        self.parent_ids = parent_ids
        self.signature = signature

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
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
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
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
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryTagResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class GetRepositoryTagResponseBodyResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        id: str = None,
        commit: GetRepositoryTagResponseBodyResultCommit = None,
        signature: GetRepositoryTagResponseBodyResultSignature = None,
    ):
        self.message = message
        self.name = name
        self.id = id
        self.commit = commit
        self.signature = signature

    def validate(self):
        if self.commit:
            self.commit.validate()
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Commit') is not None:
            temp_model = GetRepositoryTagResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryTagResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetRepositoryTagResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetRepositoryTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMergeRequestRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class UpdateMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        satisfied_check_results: List[UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
        unsatisfied_check_results: List[UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.satisfied_check_results = satisfied_check_results
        self.unsatisfied_check_results = unsatisfied_check_results

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class UpdateMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateMergeRequestResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        behind_commit_count: int = None,
        project_id: int = None,
        created_at: str = None,
        accepted_revision: str = None,
        source_branch: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        merge_type: str = None,
        target_branch: str = None,
        ahead_commit_count: int = None,
        updated_at: str = None,
        title: str = None,
        merge_error: str = None,
        merged_revision: str = None,
        id: int = None,
        merge_status: str = None,
        assignee_list: List[UpdateMergeRequestResponseBodyResultAssigneeList] = None,
        approve_check_result: UpdateMergeRequestResponseBodyResultApproveCheckResult = None,
        author: UpdateMergeRequestResponseBodyResultAuthor = None,
    ):
        self.state = state
        self.behind_commit_count = behind_commit_count
        self.project_id = project_id
        self.created_at = created_at
        self.accepted_revision = accepted_revision
        self.source_branch = source_branch
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.merge_type = merge_type
        self.target_branch = target_branch
        self.ahead_commit_count = ahead_commit_count
        self.updated_at = updated_at
        self.title = title
        self.merge_error = merge_error
        self.merged_revision = merged_revision
        self.id = id
        self.merge_status = merge_status
        self.assignee_list = assignee_list
        self.approve_check_result = approve_check_result
        self.author = author

    def validate(self):
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
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
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        if self.author is not None:
            result['Author'] = self.author.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
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
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = UpdateMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('ApproveCheckResult') is not None:
            temp_model = UpdateMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        if m.get('Author') is not None:
            temp_model = UpdateMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        return self


class UpdateMergeRequestResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: UpdateMergeRequestResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = UpdateMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateMergeRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMergeRequestResponseBody = None,
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
            temp_model = UpdateMergeRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateRepositoryResponseBodyResultNamespace(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        description: str = None,
        public: bool = None,
        visibility_level: str = None,
        path: str = None,
        created_at: str = None,
        updated_at: str = None,
        name: str = None,
        owner_id: int = None,
        id: int = None,
    ):
        self.avatar = avatar
        self.description = description
        self.public = public
        self.visibility_level = visibility_level
        self.path = path
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.owner_id = owner_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.description is not None:
            result['Description'] = self.description
        if self.public is not None:
            result['Public'] = self.public
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.path is not None:
            result['Path'] = self.path
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
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
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateRepositoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        last_activity_at: str = None,
        default_branch: str = None,
        avatar_url: str = None,
        archive: bool = None,
        created_at: str = None,
        creator_id: int = None,
        http_url_to_repo: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        visibility_level: str = None,
        path: str = None,
        ssh_url_to_repo: str = None,
        name: str = None,
        id: int = None,
        namespace: UpdateRepositoryResponseBodyResultNamespace = None,
    ):
        self.last_activity_at = last_activity_at
        self.default_branch = default_branch
        self.avatar_url = avatar_url
        self.archive = archive
        self.created_at = created_at
        self.creator_id = creator_id
        self.http_url_to_repo = http_url_to_repo
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.path = path
        self.ssh_url_to_repo = ssh_url_to_repo
        self.name = name
        self.id = id
        self.namespace = namespace

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
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
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
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
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Namespace') is not None:
            temp_model = UpdateRepositoryResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        return self


class UpdateRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: UpdateRepositoryResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = UpdateRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRepositoryResponseBody = None,
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
            temp_model = UpdateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMergeRequestCommentRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateMergeRequestCommentResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateMergeRequestCommentResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: UpdateMergeRequestCommentResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = UpdateMergeRequestCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateMergeRequestCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMergeRequestCommentResponseBody = None,
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
            temp_model = UpdateMergeRequestCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerRepositoryMirrorSyncRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        account: str = None,
        token: str = None,
    ):
        # 个人访问令牌。 使用阿里云AK+SK或使用STS临时授权方式不需要传该字段
        self.access_token = access_token
        # 企业标识，也称企业id，字符串形式，可在云效访问链接中获取，如 https://devops.aliyun.com/organization/\
        self.organization_id = organization_id
        # 远程同步库克隆账号
        self.account = account
        # 远程同步库克隆令牌
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.account is not None:
            result['Account'] = self.account
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class TriggerRepositoryMirrorSyncResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        # 仓库同步触发结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TriggerRepositoryMirrorSyncResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: TriggerRepositoryMirrorSyncResponseBodyResult = None,
    ):
        # 错误信息
        self.error_message = error_message
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.success = success
        # 错误码
        self.error_code = error_code
        # 响应结果
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = TriggerRepositoryMirrorSyncResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class TriggerRepositoryMirrorSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TriggerRepositoryMirrorSyncResponseBody = None,
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
            temp_model = TriggerRepositoryMirrorSyncResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteBranchResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryCommitDiffRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        context_line: int = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.context_line = context_line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.context_line is not None:
            result['ContextLine'] = self.context_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('ContextLine') is not None:
            self.context_line = m.get('ContextLine')
        return self


class ListRepositoryCommitDiffResponseBodyResult(TeaModel):
    def __init__(
        self,
        deleted_file: bool = None,
        diff: str = None,
        old_path: str = None,
        old_id: str = None,
        bmode: str = None,
        is_old_lfs: bool = None,
        is_new_lfs: bool = None,
        renamed_file: bool = None,
        new_file: bool = None,
        new_id: str = None,
        is_binary: bool = None,
        new_path: str = None,
        amode: str = None,
    ):
        self.deleted_file = deleted_file
        self.diff = diff
        self.old_path = old_path
        self.old_id = old_id
        self.bmode = bmode
        self.is_old_lfs = is_old_lfs
        self.is_new_lfs = is_new_lfs
        self.renamed_file = renamed_file
        self.new_file = new_file
        self.new_id = new_id
        self.is_binary = is_binary
        self.new_path = new_path
        self.amode = amode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_file is not None:
            result['DeletedFile'] = self.deleted_file
        if self.diff is not None:
            result['Diff'] = self.diff
        if self.old_path is not None:
            result['OldPath'] = self.old_path
        if self.old_id is not None:
            result['OldId'] = self.old_id
        if self.bmode is not None:
            result['BMode'] = self.bmode
        if self.is_old_lfs is not None:
            result['IsOldLfs'] = self.is_old_lfs
        if self.is_new_lfs is not None:
            result['IsNewLfs'] = self.is_new_lfs
        if self.renamed_file is not None:
            result['RenamedFile'] = self.renamed_file
        if self.new_file is not None:
            result['NewFile'] = self.new_file
        if self.new_id is not None:
            result['NewId'] = self.new_id
        if self.is_binary is not None:
            result['IsBinary'] = self.is_binary
        if self.new_path is not None:
            result['NewPath'] = self.new_path
        if self.amode is not None:
            result['AMode'] = self.amode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedFile') is not None:
            self.deleted_file = m.get('DeletedFile')
        if m.get('Diff') is not None:
            self.diff = m.get('Diff')
        if m.get('OldPath') is not None:
            self.old_path = m.get('OldPath')
        if m.get('OldId') is not None:
            self.old_id = m.get('OldId')
        if m.get('BMode') is not None:
            self.bmode = m.get('BMode')
        if m.get('IsOldLfs') is not None:
            self.is_old_lfs = m.get('IsOldLfs')
        if m.get('IsNewLfs') is not None:
            self.is_new_lfs = m.get('IsNewLfs')
        if m.get('RenamedFile') is not None:
            self.renamed_file = m.get('RenamedFile')
        if m.get('NewFile') is not None:
            self.new_file = m.get('NewFile')
        if m.get('NewId') is not None:
            self.new_id = m.get('NewId')
        if m.get('IsBinary') is not None:
            self.is_binary = m.get('IsBinary')
        if m.get('NewPath') is not None:
            self.new_path = m.get('NewPath')
        if m.get('AMode') is not None:
            self.amode = m.get('AMode')
        return self


class ListRepositoryCommitDiffResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryCommitDiffResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryCommitDiffResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryCommitDiffResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryCommitDiffResponseBody = None,
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
            temp_model = ListRepositoryCommitDiffResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        last_activity_at: str = None,
        default_branch: str = None,
        avatar_url: str = None,
        archive: bool = None,
        import_url: str = None,
        created_at: str = None,
        demo_project_status: bool = None,
        creator_id: int = None,
        import_status: str = None,
        http_url_to_repo: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        public: bool = None,
        path_with_namespace: str = None,
        path: str = None,
        visibility_level: str = None,
        access_level: int = None,
        import_from_subversion: bool = None,
        ssh_url_to_repo: str = None,
        name: str = None,
        id: int = None,
        tag_list: List[str] = None,
        namespace: GetRepositoryInfoResponseBodyResultNamespace = None,
        permissions: GetRepositoryInfoResponseBodyResultPermissions = None,
    ):
        self.last_activity_at = last_activity_at
        self.default_branch = default_branch
        self.avatar_url = avatar_url
        self.archive = archive
        self.import_url = import_url
        self.created_at = created_at
        self.demo_project_status = demo_project_status
        self.creator_id = creator_id
        self.import_status = import_status
        self.http_url_to_repo = http_url_to_repo
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.public = public
        self.path_with_namespace = path_with_namespace
        self.path = path
        self.visibility_level = visibility_level
        self.access_level = access_level
        self.import_from_subversion = import_from_subversion
        self.ssh_url_to_repo = ssh_url_to_repo
        self.name = name
        self.id = id
        self.tag_list = tag_list
        self.namespace = namespace
        self.permissions = permissions

    def validate(self):
        if self.namespace:
            self.namespace.validate()
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.import_url is not None:
            result['ImportUrl'] = self.import_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.import_status is not None:
            result['ImportStatus'] = self.import_status
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.public is not None:
            result['Public'] = self.public
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.path is not None:
            result['Path'] = self.path
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.import_from_subversion is not None:
            result['ImportFromSubversion'] = self.import_from_subversion
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('ImportUrl') is not None:
            self.import_url = m.get('ImportUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('ImportStatus') is not None:
            self.import_status = m.get('ImportStatus')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('ImportFromSubversion') is not None:
            self.import_from_subversion = m.get('ImportFromSubversion')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Namespace') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        if m.get('Permissions') is not None:
            temp_model = GetRepositoryInfoResponseBodyResultPermissions()
            self.permissions = temp_model.from_map(m['Permissions'])
        return self


class GetRepositoryInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: int = None,
        result: GetRepositoryInfoResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetRepositoryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcceptMergeRequestRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class AcceptMergeRequestResponseBodyResultAssigneeList(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class AcceptMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        satisfied_check_results: List[AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
        unsatisfied_check_results: List[AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.satisfied_check_results = satisfied_check_results
        self.unsatisfied_check_results = unsatisfied_check_results

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class AcceptMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AcceptMergeRequestResponseBodyResult(TeaModel):
    def __init__(
        self,
        state: str = None,
        behind_commit_count: int = None,
        project_id: int = None,
        created_at: str = None,
        accepted_revision: str = None,
        source_branch: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        merge_type: str = None,
        target_branch: str = None,
        ahead_commit_count: int = None,
        updated_at: str = None,
        title: str = None,
        merge_error: str = None,
        merged_revision: str = None,
        id: int = None,
        merge_status: str = None,
        assignee_list: List[AcceptMergeRequestResponseBodyResultAssigneeList] = None,
        approve_check_result: AcceptMergeRequestResponseBodyResultApproveCheckResult = None,
        author: AcceptMergeRequestResponseBodyResultAuthor = None,
    ):
        self.state = state
        self.behind_commit_count = behind_commit_count
        self.project_id = project_id
        self.created_at = created_at
        self.accepted_revision = accepted_revision
        self.source_branch = source_branch
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.merge_type = merge_type
        self.target_branch = target_branch
        self.ahead_commit_count = ahead_commit_count
        self.updated_at = updated_at
        self.title = title
        self.merge_error = merge_error
        self.merged_revision = merged_revision
        self.id = id
        self.merge_status = merge_status
        self.assignee_list = assignee_list
        self.approve_check_result = approve_check_result
        self.author = author

    def validate(self):
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
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
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        if self.author is not None:
            result['Author'] = self.author.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
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
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = AcceptMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('ApproveCheckResult') is not None:
            temp_model = AcceptMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        if m.get('Author') is not None:
            temp_model = AcceptMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        return self


class AcceptMergeRequestResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: AcceptMergeRequestResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = AcceptMergeRequestResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AcceptMergeRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AcceptMergeRequestResponseBody = None,
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
            temp_model = AcceptMergeRequestResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteFileResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryProtectedBranchRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeleteRepositoryProtectedBranchResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteRepositoryProtectedBranchResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: DeleteRepositoryProtectedBranchResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryProtectedBranchResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryProtectedBranchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryProtectedBranchResponseBody = None,
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
            temp_model = DeleteRepositoryProtectedBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryTagV2Request(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        tag_name: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DeleteRepositoryTagV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
    ):
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DeleteRepositoryTagV2ResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: DeleteRepositoryTagV2ResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = DeleteRepositoryTagV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRepositoryTagV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryTagV2ResponseBody = None,
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
            temp_model = DeleteRepositoryTagV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileLastCommitRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        sha: str = None,
        file_path: str = None,
    ):
        # 个人访问令牌
        self.access_token = access_token
        # 云效企业ID
        self.organization_id = organization_id
        # 分支名称、标签名称或Commit ID
        self.sha = sha
        # 文件路径
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.sha is not None:
            result['Sha'] = self.sha
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Sha') is not None:
            self.sha = m.get('Sha')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class GetFileLastCommitResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        # 验证状态
        self.verification_status = verification_status
        # GPG密钥ID
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class GetFileLastCommitResponseBodyResult(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        title: str = None,
        committer_name: str = None,
        author_email: str = None,
        id: str = None,
        committer_email: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
        signature: GetFileLastCommitResponseBodyResultSignature = None,
    ):
        # Commit短ID
        self.short_id = short_id
        # 作者姓名
        self.author_name = author_name
        # 作者提交时间
        self.author_date = author_date
        # 创建时间
        self.created_at = created_at
        # 提交内容
        self.message = message
        # 标题，提交的第一行内容
        self.title = title
        # 提交者姓名
        self.committer_name = committer_name
        # 提交者邮箱
        self.author_email = author_email
        # Commit ID
        self.id = id
        # 提交者邮箱
        self.committer_email = committer_email
        # 提交者提交时间
        self.committed_date = committed_date
        # 父提交ID
        self.parent_ids = parent_ids
        # 签名
        self.signature = signature

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.title is not None:
            result['Title'] = self.title
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('Signature') is not None:
            temp_model = GetFileLastCommitResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetFileLastCommitResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetFileLastCommitResponseBodyResult = None,
    ):
        # 错误信息
        self.error_message = error_message
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.success = success
        # 错误码
        self.error_code = error_code
        # 响应结果
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetFileLastCommitResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetFileLastCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFileLastCommitResponseBody = None,
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
            temp_model = GetFileLastCommitResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: UpdateFileResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = UpdateFileResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: UpdateRepositoryMemberResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = UpdateRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRepositoryMemberRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: List[AddRepositoryMemberResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = AddRepositoryMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSshKeyRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
    ):
        self.access_token = access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class CreateSshKeyResponseBodyResult(TeaModel):
    def __init__(
        self,
        key: str = None,
        finger_print: str = None,
        created_at: str = None,
        title: str = None,
        key_scope: str = None,
        id: int = None,
    ):
        self.key = key
        self.finger_print = finger_print
        self.created_at = created_at
        self.title = title
        self.key_scope = key_scope
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.title is not None:
            result['Title'] = self.title
        if self.key_scope is not None:
            result['KeyScope'] = self.key_scope
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('KeyScope') is not None:
            self.key_scope = m.get('KeyScope')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateSshKeyResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: CreateSshKeyResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = CreateSshKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateSshKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSshKeyResponseBody = None,
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
            temp_model = CreateSshKeyResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListRepositoryTagsResponseBodyResultCommitSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class ListRepositoryTagsResponseBodyResultCommit(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
        signature: ListRepositoryTagsResponseBodyResultCommitSignature = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date
        self.parent_ids = parent_ids
        self.signature = signature

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
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
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
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
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('Signature') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class ListRepositoryTagsResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class ListRepositoryTagsResponseBodyResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        id: str = None,
        commit: ListRepositoryTagsResponseBodyResultCommit = None,
        signature: ListRepositoryTagsResponseBodyResultSignature = None,
    ):
        self.message = message
        self.name = name
        self.id = id
        self.commit = commit
        self.signature = signature

    def validate(self):
        if self.commit:
            self.commit.validate()
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Commit') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Signature') is not None:
            temp_model = ListRepositoryTagsResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class ListRepositoryTagsResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryTagsResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListRepositoryTagsResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        url: str = None,
        issues_events: bool = None,
        tag_push_events: bool = None,
        last_test_result: str = None,
        description: str = None,
        merge_requests_events: bool = None,
        secret_token: str = None,
        note_events: bool = None,
        id: int = None,
        enable_ssl_verification: bool = None,
    ):
        self.push_events = push_events
        self.build_events = build_events
        self.project_id = project_id
        self.created_at = created_at
        self.url = url
        self.issues_events = issues_events
        self.tag_push_events = tag_push_events
        self.last_test_result = last_test_result
        self.description = description
        self.merge_requests_events = merge_requests_events
        self.secret_token = secret_token
        self.note_events = note_events
        self.id = id
        self.enable_ssl_verification = enable_ssl_verification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.build_events is not None:
            result['BuildEvents'] = self.build_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.url is not None:
            result['Url'] = self.url
        if self.issues_events is not None:
            result['IssuesEvents'] = self.issues_events
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
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
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('IssuesEvents') is not None:
            self.issues_events = m.get('IssuesEvents')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
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
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        return self


class AddWebhookResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: AddWebhookResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = AddWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRepositoryDeployKeyRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class EnableRepositoryDeployKeyResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class EnableRepositoryDeployKeyResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: EnableRepositoryDeployKeyResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = EnableRepositoryDeployKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EnableRepositoryDeployKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableRepositoryDeployKeyResponseBody = None,
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
            temp_model = EnableRepositoryDeployKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetUserInfoResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetUserInfoResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: List[ListRepositoryTreeResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListRepositoryTreeResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteRepositoryGroupResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteRepositoryGroupResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        url: str = None,
        tag_push_events: bool = None,
        last_test_result: str = None,
        merge_requests_events: bool = None,
        description: str = None,
        note_events: bool = None,
        secret_token: str = None,
        id: int = None,
        enable_ssl_verification: bool = None,
    ):
        self.push_events = push_events
        self.project_id = project_id
        self.created_at = created_at
        self.url = url
        self.tag_push_events = tag_push_events
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.url is not None:
            result['Url'] = self.url
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
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
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
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


class DeleteRepositoryWebhookResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteRepositoryWebhookResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteRepositoryWebhookResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        name: str = None,
        id: int = None,
        username: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.name = name
        self.id = id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListRepositoryMemberResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryMemberResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListRepositoryMemberResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTagResponseBodyResultCommitInfo(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date
        self.parent_ids = parent_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
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
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
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
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTagResponseBodyResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        message: str = None,
        commit_info: CreateTagResponseBodyResultCommitInfo = None,
        release: CreateTagResponseBodyResultRelease = None,
    ):
        self.name = name
        self.message = message
        self.commit_info = commit_info
        self.release = release

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()
        if self.release:
            self.release.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.message is not None:
            result['Message'] = self.message
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        if self.release is not None:
            result['Release'] = self.release.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('CommitInfo') is not None:
            temp_model = CreateTagResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        if m.get('Release') is not None:
            temp_model = CreateTagResponseBodyResultRelease()
            self.release = temp_model.from_map(m['Release'])
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: CreateTagResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryCommitRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetRepositoryCommitResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class GetRepositoryCommitResponseBodyResult(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        title: str = None,
        committer_name: str = None,
        author_email: str = None,
        id: str = None,
        committer_email: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
        signature: GetRepositoryCommitResponseBodyResultSignature = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.title = title
        self.committer_name = committer_name
        self.author_email = author_email
        self.id = id
        self.committer_email = committer_email
        self.committed_date = committed_date
        self.parent_ids = parent_ids
        self.signature = signature

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.title is not None:
            result['Title'] = self.title
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryCommitResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryCommitResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetRepositoryCommitResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetRepositoryCommitResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRepositoryCommitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepositoryCommitResponseBody = None,
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
            temp_model = GetRepositoryCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupMemberRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: List[AddGroupMemberResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = AddGroupMemberResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        author_name: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date
        self.parent_ids = parent_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
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
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
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
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        return self


class GetBranchInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        protected_branch: bool = None,
        branch_name: str = None,
        commit_info: GetBranchInfoResponseBodyResultCommitInfo = None,
    ):
        self.protected_branch = protected_branch
        self.branch_name = branch_name
        self.commit_info = commit_info

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitInfo') is not None:
            temp_model = GetBranchInfoResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        return self


class GetBranchInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetBranchInfoResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetBranchInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMergeRequestCommentsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        from_commit: str = None,
        to_commit: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.from_commit = from_commit
        self.to_commit = to_commit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.from_commit is not None:
            result['FromCommit'] = self.from_commit
        if self.to_commit is not None:
            result['ToCommit'] = self.to_commit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('FromCommit') is not None:
            self.from_commit = m.get('FromCommit')
        if m.get('ToCommit') is not None:
            self.to_commit = m.get('ToCommit')
        return self


class ListMergeRequestCommentsResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListMergeRequestCommentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        out_dated: bool = None,
        project_id: int = None,
        range_context: str = None,
        created_at: str = None,
        parent_note_id: int = None,
        is_draft: bool = None,
        closed: int = None,
        line: int = None,
        side: str = None,
        path: str = None,
        note: str = None,
        updated_at: str = None,
        id: int = None,
        author: ListMergeRequestCommentsResponseBodyResultAuthor = None,
    ):
        self.out_dated = out_dated
        self.project_id = project_id
        self.range_context = range_context
        self.created_at = created_at
        self.parent_note_id = parent_note_id
        self.is_draft = is_draft
        self.closed = closed
        self.line = line
        self.side = side
        self.path = path
        self.note = note
        self.updated_at = updated_at
        self.id = id
        self.author = author

    def validate(self):
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_dated is not None:
            result['OutDated'] = self.out_dated
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.range_context is not None:
            result['RangeContext'] = self.range_context
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.parent_note_id is not None:
            result['ParentNoteId'] = self.parent_note_id
        if self.is_draft is not None:
            result['IsDraft'] = self.is_draft
        if self.closed is not None:
            result['Closed'] = self.closed
        if self.line is not None:
            result['Line'] = self.line
        if self.side is not None:
            result['Side'] = self.side
        if self.path is not None:
            result['Path'] = self.path
        if self.note is not None:
            result['Note'] = self.note
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        if self.author is not None:
            result['Author'] = self.author.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutDated') is not None:
            self.out_dated = m.get('OutDated')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RangeContext') is not None:
            self.range_context = m.get('RangeContext')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ParentNoteId') is not None:
            self.parent_note_id = m.get('ParentNoteId')
        if m.get('IsDraft') is not None:
            self.is_draft = m.get('IsDraft')
        if m.get('Closed') is not None:
            self.closed = m.get('Closed')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Author') is not None:
            temp_model = ListMergeRequestCommentsResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        return self


class ListMergeRequestCommentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListMergeRequestCommentsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListMergeRequestCommentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListMergeRequestCommentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMergeRequestCommentsResponseBody = None,
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
            temp_model = ListMergeRequestCommentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryGroupRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateRepositoryGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        type: str = None,
        avatar_url: str = None,
        owner_id: int = None,
        web_url: str = None,
        parent_id: int = None,
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
        self.web_url = web_url
        self.parent_id = parent_id
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
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
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
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


class CreateRepositoryGroupResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: int = None,
        result: CreateRepositoryGroupResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = CreateRepositoryGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMergeRequestDetailRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetMergeRequestDetailResponseBodyResultAssigneeList(TeaModel):
    def __init__(
        self,
        status: str = None,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.status = status
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class GetMergeRequestDetailResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        satisfied_check_results: List[GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
        unsatisfied_check_results: List[GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.satisfied_check_results = satisfied_check_results
        self.unsatisfied_check_results = unsatisfied_check_results

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class GetMergeRequestDetailResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMergeRequestDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        is_support_merge: bool = None,
        state: str = None,
        behind_commit_count: int = None,
        project_id: int = None,
        created_at: str = None,
        accepted_revision: str = None,
        source_branch: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        merge_type: str = None,
        target_branch: str = None,
        ahead_commit_count: int = None,
        updated_at: str = None,
        title: str = None,
        merge_error: str = None,
        merged_revision: str = None,
        id: int = None,
        merge_status: str = None,
        assignee_list: List[GetMergeRequestDetailResponseBodyResultAssigneeList] = None,
        approve_check_result: GetMergeRequestDetailResponseBodyResultApproveCheckResult = None,
        author: GetMergeRequestDetailResponseBodyResultAuthor = None,
    ):
        self.is_support_merge = is_support_merge
        self.state = state
        self.behind_commit_count = behind_commit_count
        self.project_id = project_id
        self.created_at = created_at
        self.accepted_revision = accepted_revision
        self.source_branch = source_branch
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.merge_type = merge_type
        self.target_branch = target_branch
        self.ahead_commit_count = ahead_commit_count
        self.updated_at = updated_at
        self.title = title
        self.merge_error = merge_error
        self.merged_revision = merged_revision
        self.id = id
        self.merge_status = merge_status
        self.assignee_list = assignee_list
        self.approve_check_result = approve_check_result
        self.author = author

    def validate(self):
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_support_merge is not None:
            result['IsSupportMerge'] = self.is_support_merge
        if self.state is not None:
            result['State'] = self.state
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
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
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        if self.author is not None:
            result['Author'] = self.author.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSupportMerge') is not None:
            self.is_support_merge = m.get('IsSupportMerge')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
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
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = GetMergeRequestDetailResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('ApproveCheckResult') is not None:
            temp_model = GetMergeRequestDetailResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        if m.get('Author') is not None:
            temp_model = GetMergeRequestDetailResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        return self


class GetMergeRequestDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetMergeRequestDetailResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetMergeRequestDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMergeRequestDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMergeRequestDetailResponseBody = None,
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
            temp_model = GetMergeRequestDetailResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        web_url: str = None,
        parent_id: int = None,
        description: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        visibility_level: str = None,
        path: str = None,
        access_level: int = None,
        updated_at: str = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.created_at = created_at
        self.owner_id = owner_id
        self.web_url = web_url
        self.parent_id = parent_id
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.path = path
        self.access_level = access_level
        self.updated_at = updated_at
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
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
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
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
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListGroupsResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryProtectedBranchRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees(TeaModel):
    def __init__(
        self,
        name: str = None,
        extern_uid: str = None,
        avatar_url: str = None,
        id: int = None,
        email: str = None,
    ):
        # 姓名
        self.name = name
        # 云效用户ID
        self.extern_uid = extern_uid
        # 头像地址
        self.avatar_url = avatar_url
        # 用户ID
        self.id = id
        # 邮箱
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.extern_uid is not None:
            result['ExternUid'] = self.extern_uid
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExternUid') is not None:
            self.extern_uid = m.get('ExternUid')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting(TeaModel):
    def __init__(
        self,
        merge_request_mode: str = None,
        allow_self_approval: bool = None,
        is_require_discussion_processed: bool = None,
        required: bool = None,
        minimum_approval: int = None,
        default_assignees: List[ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees] = None,
        allow_merge_request_roles: List[int] = None,
        white_list: str = None,
    ):
        # 评审模式。  general：普通 codeowner：CodeOwner模式
        self.merge_request_mode = merge_request_mode
        # 是否允许创建者通过代码评审。
        self.allow_self_approval = allow_self_approval
        # 是否要求评论全部已解决。
        self.is_require_discussion_processed = is_require_discussion_processed
        # 是否要求合并前通过代码评审。
        self.required = required
        # 评审通过的最少人数。  注：仅普通模式生效。
        self.minimum_approval = minimum_approval
        # 默认评审者。  注：云效用户 ID 列表。
        self.default_assignees = default_assignees
        # 允许通过代码评审的角色。  40：管理员  30：开发者
        self.allow_merge_request_roles = allow_merge_request_roles
        # 评审文件白名单
        self.white_list = white_list

    def validate(self):
        if self.default_assignees:
            for k in self.default_assignees:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merge_request_mode is not None:
            result['MergeRequestMode'] = self.merge_request_mode
        if self.allow_self_approval is not None:
            result['AllowSelfApproval'] = self.allow_self_approval
        if self.is_require_discussion_processed is not None:
            result['IsRequireDiscussionProcessed'] = self.is_require_discussion_processed
        if self.required is not None:
            result['Required'] = self.required
        if self.minimum_approval is not None:
            result['MinimumApproval'] = self.minimum_approval
        result['DefaultAssignees'] = []
        if self.default_assignees is not None:
            for k in self.default_assignees:
                result['DefaultAssignees'].append(k.to_map() if k else None)
        if self.allow_merge_request_roles is not None:
            result['AllowMergeRequestRoles'] = self.allow_merge_request_roles
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MergeRequestMode') is not None:
            self.merge_request_mode = m.get('MergeRequestMode')
        if m.get('AllowSelfApproval') is not None:
            self.allow_self_approval = m.get('AllowSelfApproval')
        if m.get('IsRequireDiscussionProcessed') is not None:
            self.is_require_discussion_processed = m.get('IsRequireDiscussionProcessed')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('MinimumApproval') is not None:
            self.minimum_approval = m.get('MinimumApproval')
        self.default_assignees = []
        if m.get('DefaultAssignees') is not None:
            for k in m.get('DefaultAssignees'):
                temp_model = ListRepositoryProtectedBranchResponseBodyResultMergeRequestSettingDefaultAssignees()
                self.default_assignees.append(temp_model.from_map(k))
        if m.get('AllowMergeRequestRoles') is not None:
            self.allow_merge_request_roles = m.get('AllowMergeRequestRoles')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection(TeaModel):
    def __init__(
        self,
        message: str = None,
        enabled: bool = None,
    ):
        # 检查信息
        self.message = message
        # 合并前是否需要通过Java 代码规约扫描。
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection(TeaModel):
    def __init__(
        self,
        message: str = None,
        enabled: bool = None,
    ):
        # 检查信息
        self.message = message
        # 合并前是否需要通过敏感信息检查
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
    ):
        # 流水线名称
        self.name = name
        # 是否开启检测
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig(TeaModel):
    def __init__(
        self,
        check_items: List[ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems] = None,
    ):
        # 流水线检测列表
        self.check_items = check_items

    def validate(self):
        if self.check_items:
            for k in self.check_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItems'] = []
        if self.check_items is not None:
            for k in self.check_items:
                result['CheckItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k in m.get('CheckItems'):
                temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfigCheckItems()
                self.check_items.append(temp_model.from_map(k))
        return self


class ListRepositoryProtectedBranchResponseBodyResultTestSetting(TeaModel):
    def __init__(
        self,
        required: bool = None,
        coding_guidelines_detection: ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection = None,
        sensitive_info_detection: ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection = None,
        check_config: ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig = None,
    ):
        # 要求合并前通过自动化执行检查。
        self.required = required
        # Java 代码规约扫描
        self.coding_guidelines_detection = coding_guidelines_detection
        # 敏感信息检查
        self.sensitive_info_detection = sensitive_info_detection
        # 卡点检测
        self.check_config = check_config

    def validate(self):
        if self.coding_guidelines_detection:
            self.coding_guidelines_detection.validate()
        if self.sensitive_info_detection:
            self.sensitive_info_detection.validate()
        if self.check_config:
            self.check_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['Required'] = self.required
        if self.coding_guidelines_detection is not None:
            result['CodingGuidelinesDetection'] = self.coding_guidelines_detection.to_map()
        if self.sensitive_info_detection is not None:
            result['SensitiveInfoDetection'] = self.sensitive_info_detection.to_map()
        if self.check_config is not None:
            result['CheckConfig'] = self.check_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('CodingGuidelinesDetection') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingCodingGuidelinesDetection()
            self.coding_guidelines_detection = temp_model.from_map(m['CodingGuidelinesDetection'])
        if m.get('SensitiveInfoDetection') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingSensitiveInfoDetection()
            self.sensitive_info_detection = temp_model.from_map(m['SensitiveInfoDetection'])
        if m.get('CheckConfig') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSettingCheckConfig()
            self.check_config = temp_model.from_map(m['CheckConfig'])
        return self


class ListRepositoryProtectedBranchResponseBodyResult(TeaModel):
    def __init__(
        self,
        branch: str = None,
        id: int = None,
        allow_push_roles: List[int] = None,
        allow_merge_roles: List[int] = None,
        merge_request_setting: ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting = None,
        test_setting: ListRepositoryProtectedBranchResponseBodyResultTestSetting = None,
    ):
        # 保护分支名称
        self.branch = branch
        # 保护分支 ID
        self.id = id
        # 允许推送代码的角色。  40：管理员  30：开发者
        self.allow_push_roles = allow_push_roles
        # 允许合并的角色。  40：管理员  30：开发者
        self.allow_merge_roles = allow_merge_roles
        # 代码评审设置
        self.merge_request_setting = merge_request_setting
        # 自动化检查设置
        self.test_setting = test_setting

    def validate(self):
        if self.merge_request_setting:
            self.merge_request_setting.validate()
        if self.test_setting:
            self.test_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['Branch'] = self.branch
        if self.id is not None:
            result['Id'] = self.id
        if self.allow_push_roles is not None:
            result['AllowPushRoles'] = self.allow_push_roles
        if self.allow_merge_roles is not None:
            result['AllowMergeRoles'] = self.allow_merge_roles
        if self.merge_request_setting is not None:
            result['MergeRequestSetting'] = self.merge_request_setting.to_map()
        if self.test_setting is not None:
            result['TestSetting'] = self.test_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AllowPushRoles') is not None:
            self.allow_push_roles = m.get('AllowPushRoles')
        if m.get('AllowMergeRoles') is not None:
            self.allow_merge_roles = m.get('AllowMergeRoles')
        if m.get('MergeRequestSetting') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultMergeRequestSetting()
            self.merge_request_setting = temp_model.from_map(m['MergeRequestSetting'])
        if m.get('TestSetting') is not None:
            temp_model = ListRepositoryProtectedBranchResponseBodyResultTestSetting()
            self.test_setting = temp_model.from_map(m['TestSetting'])
        return self


class ListRepositoryProtectedBranchResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryProtectedBranchResponseBodyResult] = None,
    ):
        # 错误信息
        self.error_message = error_message
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.success = success
        # 错误码
        self.error_code = error_code
        # 响应结果
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryProtectedBranchResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryProtectedBranchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryProtectedBranchResponseBody = None,
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
            temp_model = ListRepositoryProtectedBranchResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: List[ListOrganizationsResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListOrganizationsResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        access_level: int = None,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.access_level = access_level
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectMemberResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetProjectMemberResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetProjectMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: CreateFileResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryCommitsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
        search: str = None,
        path: str = None,
        ref_name: str = None,
        show_signature: bool = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size
        self.search = search
        self.path = path
        self.ref_name = ref_name
        self.show_signature = show_signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search is not None:
            result['Search'] = self.search
        if self.path is not None:
            result['Path'] = self.path
        if self.ref_name is not None:
            result['RefName'] = self.ref_name
        if self.show_signature is not None:
            result['ShowSignature'] = self.show_signature
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
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RefName') is not None:
            self.ref_name = m.get('RefName')
        if m.get('ShowSignature') is not None:
            self.show_signature = m.get('ShowSignature')
        return self


class ListRepositoryCommitsResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class ListRepositoryCommitsResponseBodyResult(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        title: str = None,
        committer_name: str = None,
        author_email: str = None,
        id: str = None,
        committer_email: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
        signature: ListRepositoryCommitsResponseBodyResultSignature = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.title = title
        self.committer_name = committer_name
        self.author_email = author_email
        self.id = id
        self.committer_email = committer_email
        self.committed_date = committed_date
        self.parent_ids = parent_ids
        self.signature = signature

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.title is not None:
            result['Title'] = self.title
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('Signature') is not None:
            temp_model = ListRepositoryCommitsResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class ListRepositoryCommitsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryCommitsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryCommitsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryCommitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryCommitsResponseBody = None,
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
            temp_model = ListRepositoryCommitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMergeRequestApproveStatusRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetMergeRequestApproveStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        approve_status: str = None,
    ):
        self.message = message
        self.approve_status = approve_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.approve_status is not None:
            result['ApproveStatus'] = self.approve_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ApproveStatus') is not None:
            self.approve_status = m.get('ApproveStatus')
        return self


class GetMergeRequestApproveStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetMergeRequestApproveStatusResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetMergeRequestApproveStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMergeRequestApproveStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMergeRequestApproveStatusResponseBody = None,
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
            temp_model = GetMergeRequestApproveStatusResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        star: bool = None,
        demo_project_status: bool = None,
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
        self.star = star
        self.demo_project_status = demo_project_status
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.star is not None:
            result['Star'] = self.star
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
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
        if m.get('Star') is not None:
            self.star = m.get('Star')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
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
        error_message: str = None,
        total: int = None,
        success: bool = None,
        error_code: int = None,
        result: List[ListRepositoriesResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMergeRequestSettingRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateMergeRequestSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class UpdateMergeRequestSettingResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: UpdateMergeRequestSettingResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = UpdateMergeRequestSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateMergeRequestSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMergeRequestSettingResponseBody = None,
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
            temp_model = UpdateMergeRequestSettingResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListGroupMemberResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListGroupMemberResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: UpdateGroupMemberResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = UpdateGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMergeRequestCommentRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateMergeRequestCommentResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateMergeRequestCommentResponseBodyResult(TeaModel):
    def __init__(
        self,
        out_dated: bool = None,
        project_id: int = None,
        range_context: str = None,
        created_at: str = None,
        parent_note_id: int = None,
        is_draft: bool = None,
        closed: int = None,
        line: int = None,
        side: str = None,
        path: str = None,
        note: str = None,
        updated_at: str = None,
        id: int = None,
        author: CreateMergeRequestCommentResponseBodyResultAuthor = None,
    ):
        self.out_dated = out_dated
        self.project_id = project_id
        self.range_context = range_context
        self.created_at = created_at
        self.parent_note_id = parent_note_id
        self.is_draft = is_draft
        self.closed = closed
        self.line = line
        self.side = side
        self.path = path
        self.note = note
        self.updated_at = updated_at
        self.id = id
        self.author = author

    def validate(self):
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_dated is not None:
            result['OutDated'] = self.out_dated
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.range_context is not None:
            result['RangeContext'] = self.range_context
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.parent_note_id is not None:
            result['ParentNoteId'] = self.parent_note_id
        if self.is_draft is not None:
            result['IsDraft'] = self.is_draft
        if self.closed is not None:
            result['Closed'] = self.closed
        if self.line is not None:
            result['Line'] = self.line
        if self.side is not None:
            result['Side'] = self.side
        if self.path is not None:
            result['Path'] = self.path
        if self.note is not None:
            result['Note'] = self.note
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.id is not None:
            result['Id'] = self.id
        if self.author is not None:
            result['Author'] = self.author.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutDated') is not None:
            self.out_dated = m.get('OutDated')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RangeContext') is not None:
            self.range_context = m.get('RangeContext')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ParentNoteId') is not None:
            self.parent_note_id = m.get('ParentNoteId')
        if m.get('IsDraft') is not None:
            self.is_draft = m.get('IsDraft')
        if m.get('Closed') is not None:
            self.closed = m.get('Closed')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Side') is not None:
            self.side = m.get('Side')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Author') is not None:
            temp_model = CreateMergeRequestCommentResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        return self


class CreateMergeRequestCommentResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: CreateMergeRequestCommentResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = CreateMergeRequestCommentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateMergeRequestCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMergeRequestCommentResponseBody = None,
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
            temp_model = CreateMergeRequestCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryDeployKeyRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateRepositoryDeployKeyResponseBodyResult(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        key: str = None,
        title: str = None,
        id: int = None,
        finger_print: str = None,
    ):
        self.created_at = created_at
        self.key = key
        self.title = title
        self.id = id
        self.finger_print = finger_print

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        return self


class CreateRepositoryDeployKeyResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: CreateRepositoryDeployKeyResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = CreateRepositoryDeployKeyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateRepositoryDeployKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepositoryDeployKeyResponseBody = None,
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
            temp_model = CreateRepositoryDeployKeyResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteRepositoryTagResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteRepositoryTagResponseBody()
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
    ):
        self.access_token = access_token
        self.sync = sync
        self.create_parent_path = create_parent_path
        self.organization_id = organization_id
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        last_activity_at: str = None,
        default_branch: str = None,
        avatar_url: str = None,
        archive: bool = None,
        snippets_enable_status: bool = None,
        created_at: str = None,
        issues_enable_status: bool = None,
        demo_project_status: bool = None,
        creator_id: int = None,
        builds_enable_status: bool = None,
        http_url_to_repo: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        public: bool = None,
        path_with_namespace: str = None,
        merge_request_enable_status: bool = None,
        path: str = None,
        visibility_level: str = None,
        wiki_enable_status: bool = None,
        ssh_url_to_repo: str = None,
        name: str = None,
        id: int = None,
        tag_list: List[str] = None,
        namespace: CreateRepositoryResponseBodyResultNamespace = None,
    ):
        self.last_activity_at = last_activity_at
        self.default_branch = default_branch
        self.avatar_url = avatar_url
        self.archive = archive
        self.snippets_enable_status = snippets_enable_status
        self.created_at = created_at
        self.issues_enable_status = issues_enable_status
        self.demo_project_status = demo_project_status
        self.creator_id = creator_id
        self.builds_enable_status = builds_enable_status
        self.http_url_to_repo = http_url_to_repo
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.public = public
        self.path_with_namespace = path_with_namespace
        self.merge_request_enable_status = merge_request_enable_status
        self.path = path
        self.visibility_level = visibility_level
        self.wiki_enable_status = wiki_enable_status
        self.ssh_url_to_repo = ssh_url_to_repo
        self.name = name
        self.id = id
        self.tag_list = tag_list
        self.namespace = namespace

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.default_branch is not None:
            result['DefaultBranch'] = self.default_branch
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.snippets_enable_status is not None:
            result['SnippetsEnableStatus'] = self.snippets_enable_status
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.issues_enable_status is not None:
            result['IssuesEnableStatus'] = self.issues_enable_status
        if self.demo_project_status is not None:
            result['DemoProjectStatus'] = self.demo_project_status
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.builds_enable_status is not None:
            result['BuildsEnableStatus'] = self.builds_enable_status
        if self.http_url_to_repo is not None:
            result['HttpUrlToRepo'] = self.http_url_to_repo
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.public is not None:
            result['Public'] = self.public
        if self.path_with_namespace is not None:
            result['PathWithNamespace'] = self.path_with_namespace
        if self.merge_request_enable_status is not None:
            result['MergeRequestEnableStatus'] = self.merge_request_enable_status
        if self.path is not None:
            result['Path'] = self.path
        if self.visibility_level is not None:
            result['VisibilityLevel'] = self.visibility_level
        if self.wiki_enable_status is not None:
            result['WikiEnableStatus'] = self.wiki_enable_status
        if self.ssh_url_to_repo is not None:
            result['SshUrlToRepo'] = self.ssh_url_to_repo
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastActivityAt') is not None:
            self.last_activity_at = m.get('LastActivityAt')
        if m.get('DefaultBranch') is not None:
            self.default_branch = m.get('DefaultBranch')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Archive') is not None:
            self.archive = m.get('Archive')
        if m.get('SnippetsEnableStatus') is not None:
            self.snippets_enable_status = m.get('SnippetsEnableStatus')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('IssuesEnableStatus') is not None:
            self.issues_enable_status = m.get('IssuesEnableStatus')
        if m.get('DemoProjectStatus') is not None:
            self.demo_project_status = m.get('DemoProjectStatus')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('BuildsEnableStatus') is not None:
            self.builds_enable_status = m.get('BuildsEnableStatus')
        if m.get('HttpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('HttpUrlToRepo')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('PathWithNamespace') is not None:
            self.path_with_namespace = m.get('PathWithNamespace')
        if m.get('MergeRequestEnableStatus') is not None:
            self.merge_request_enable_status = m.get('MergeRequestEnableStatus')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('VisibilityLevel') is not None:
            self.visibility_level = m.get('VisibilityLevel')
        if m.get('WikiEnableStatus') is not None:
            self.wiki_enable_status = m.get('WikiEnableStatus')
        if m.get('SshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('SshUrlToRepo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Namespace') is not None:
            temp_model = CreateRepositoryResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['Namespace'])
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: int = None,
        result: CreateRepositoryResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = CreateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeCompletionRequest(TeaModel):
    def __init__(
        self,
        fetch_keys: str = None,
        is_encrypted: bool = None,
    ):
        self.fetch_keys = fetch_keys
        self.is_encrypted = is_encrypted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_keys is not None:
            result['FetchKeys'] = self.fetch_keys
        if self.is_encrypted is not None:
            result['IsEncrypted'] = self.is_encrypted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchKeys') is not None:
            self.fetch_keys = m.get('FetchKeys')
        if m.get('IsEncrypted') is not None:
            self.is_encrypted = m.get('IsEncrypted')
        return self


class GetCodeCompletionResponseBodyResult(TeaModel):
    def __init__(
        self,
        client_timestamp: str = None,
        receive_timestamp: str = None,
        rsp_timestamp: str = None,
        invoke_timestamp: str = None,
        body: str = None,
        fetch_timestamp: str = None,
    ):
        self.client_timestamp = client_timestamp
        self.receive_timestamp = receive_timestamp
        self.rsp_timestamp = rsp_timestamp
        self.invoke_timestamp = invoke_timestamp
        self.body = body
        self.fetch_timestamp = fetch_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_timestamp is not None:
            result['ClientTimestamp'] = self.client_timestamp
        if self.receive_timestamp is not None:
            result['ReceiveTimestamp'] = self.receive_timestamp
        if self.rsp_timestamp is not None:
            result['RspTimestamp'] = self.rsp_timestamp
        if self.invoke_timestamp is not None:
            result['InvokeTimestamp'] = self.invoke_timestamp
        if self.body is not None:
            result['Body'] = self.body
        if self.fetch_timestamp is not None:
            result['FetchTimestamp'] = self.fetch_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientTimestamp') is not None:
            self.client_timestamp = m.get('ClientTimestamp')
        if m.get('ReceiveTimestamp') is not None:
            self.receive_timestamp = m.get('ReceiveTimestamp')
        if m.get('RspTimestamp') is not None:
            self.rsp_timestamp = m.get('RspTimestamp')
        if m.get('InvokeTimestamp') is not None:
            self.invoke_timestamp = m.get('InvokeTimestamp')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('FetchTimestamp') is not None:
            self.fetch_timestamp = m.get('FetchTimestamp')
        return self


class GetCodeCompletionResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetCodeCompletionResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Result') is not None:
            temp_model = GetCodeCompletionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetCodeCompletionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCodeCompletionResponseBody = None,
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
            temp_model = GetCodeCompletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMergeRequestsRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        page: int = None,
        page_size: int = None,
        group_id_list: str = None,
        project_id_list: str = None,
        author_codeup_id_list: str = None,
        author_id_list: str = None,
        assignee_codeup_id_list: str = None,
        assignee_id_list: str = None,
        subscriber_codeup_id_list: str = None,
        state: str = None,
        search: str = None,
        order: str = None,
        after_date: str = None,
        before_date: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.page = page
        self.page_size = page_size
        self.group_id_list = group_id_list
        self.project_id_list = project_id_list
        self.author_codeup_id_list = author_codeup_id_list
        self.author_id_list = author_id_list
        self.assignee_codeup_id_list = assignee_codeup_id_list
        self.assignee_id_list = assignee_id_list
        self.subscriber_codeup_id_list = subscriber_codeup_id_list
        self.state = state
        self.search = search
        self.order = order
        self.after_date = after_date
        self.before_date = before_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.project_id_list is not None:
            result['ProjectIdList'] = self.project_id_list
        if self.author_codeup_id_list is not None:
            result['AuthorCodeupIdList'] = self.author_codeup_id_list
        if self.author_id_list is not None:
            result['AuthorIdList'] = self.author_id_list
        if self.assignee_codeup_id_list is not None:
            result['AssigneeCodeupIdList'] = self.assignee_codeup_id_list
        if self.assignee_id_list is not None:
            result['AssigneeIdList'] = self.assignee_id_list
        if self.subscriber_codeup_id_list is not None:
            result['SubscriberCodeupIdList'] = self.subscriber_codeup_id_list
        if self.state is not None:
            result['State'] = self.state
        if self.search is not None:
            result['Search'] = self.search
        if self.order is not None:
            result['Order'] = self.order
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
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
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('ProjectIdList') is not None:
            self.project_id_list = m.get('ProjectIdList')
        if m.get('AuthorCodeupIdList') is not None:
            self.author_codeup_id_list = m.get('AuthorCodeupIdList')
        if m.get('AuthorIdList') is not None:
            self.author_id_list = m.get('AuthorIdList')
        if m.get('AssigneeCodeupIdList') is not None:
            self.assignee_codeup_id_list = m.get('AssigneeCodeupIdList')
        if m.get('AssigneeIdList') is not None:
            self.assignee_id_list = m.get('AssigneeIdList')
        if m.get('SubscriberCodeupIdList') is not None:
            self.subscriber_codeup_id_list = m.get('SubscriberCodeupIdList')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Search') is not None:
            self.search = m.get('Search')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        return self


class ListMergeRequestsResponseBodyResultAssigneeList(TeaModel):
    def __init__(
        self,
        status: str = None,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        name: str = None,
        id: str = None,
    ):
        self.status = status
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.email is not None:
            result['Email'] = self.email
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class ListMergeRequestsResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        satisfied_check_results: List[ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
        unsatisfied_check_results: List[ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.satisfied_check_results = satisfied_check_results
        self.unsatisfied_check_results = unsatisfied_check_results

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = ListMergeRequestsResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class ListMergeRequestsResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListMergeRequestsResponseBodyResult(TeaModel):
    def __init__(
        self,
        is_support_merge: bool = None,
        state: str = None,
        behind_commit_count: int = None,
        project_id: int = None,
        created_at: str = None,
        accepted_revision: str = None,
        source_branch: str = None,
        web_url: str = None,
        description: str = None,
        name_with_namespace: str = None,
        merge_type: str = None,
        target_branch: str = None,
        ahead_commit_count: int = None,
        updated_at: str = None,
        title: str = None,
        merge_error: str = None,
        merged_revision: str = None,
        id: int = None,
        merge_status: str = None,
        assignee_list: List[ListMergeRequestsResponseBodyResultAssigneeList] = None,
        approve_check_result: ListMergeRequestsResponseBodyResultApproveCheckResult = None,
        author: ListMergeRequestsResponseBodyResultAuthor = None,
    ):
        self.is_support_merge = is_support_merge
        self.state = state
        self.behind_commit_count = behind_commit_count
        self.project_id = project_id
        self.created_at = created_at
        self.accepted_revision = accepted_revision
        self.source_branch = source_branch
        self.web_url = web_url
        self.description = description
        self.name_with_namespace = name_with_namespace
        self.merge_type = merge_type
        self.target_branch = target_branch
        self.ahead_commit_count = ahead_commit_count
        self.updated_at = updated_at
        self.title = title
        self.merge_error = merge_error
        self.merged_revision = merged_revision
        self.id = id
        self.merge_status = merge_status
        self.assignee_list = assignee_list
        self.approve_check_result = approve_check_result
        self.author = author

    def validate(self):
        if self.assignee_list:
            for k in self.assignee_list:
                if k:
                    k.validate()
        if self.approve_check_result:
            self.approve_check_result.validate()
        if self.author:
            self.author.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_support_merge is not None:
            result['IsSupportMerge'] = self.is_support_merge
        if self.state is not None:
            result['State'] = self.state
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
        if self.source_branch is not None:
            result['SourceBranch'] = self.source_branch
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.description is not None:
            result['Description'] = self.description
        if self.name_with_namespace is not None:
            result['NameWithNamespace'] = self.name_with_namespace
        if self.merge_type is not None:
            result['MergeType'] = self.merge_type
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
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        if self.author is not None:
            result['Author'] = self.author.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSupportMerge') is not None:
            self.is_support_merge = m.get('IsSupportMerge')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
        if m.get('SourceBranch') is not None:
            self.source_branch = m.get('SourceBranch')
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NameWithNamespace') is not None:
            self.name_with_namespace = m.get('NameWithNamespace')
        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')
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
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = ListMergeRequestsResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('ApproveCheckResult') is not None:
            temp_model = ListMergeRequestsResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        if m.get('Author') is not None:
            temp_model = ListMergeRequestsResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        return self


class ListMergeRequestsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_message: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListMergeRequestsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.error_message = error_message
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListMergeRequestsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListMergeRequestsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMergeRequestsResponseBody = None,
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
            temp_model = ListMergeRequestsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationSecurityScoresRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
    ):
        self.access_token = access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore(TeaModel):
    def __init__(
        self,
        code_content_score: int = None,
        member_behavior_score: int = None,
        authority_control_score: int = None,
        level: str = None,
    ):
        self.code_content_score = code_content_score
        self.member_behavior_score = member_behavior_score
        self.authority_control_score = authority_control_score
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_content_score is not None:
            result['CodeContentScore'] = self.code_content_score
        if self.member_behavior_score is not None:
            result['MemberBehaviorScore'] = self.member_behavior_score
        if self.authority_control_score is not None:
            result['AuthorityControlScore'] = self.authority_control_score
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeContentScore') is not None:
            self.code_content_score = m.get('CodeContentScore')
        if m.get('MemberBehaviorScore') is not None:
            self.member_behavior_score = m.get('MemberBehaviorScore')
        if m.get('AuthorityControlScore') is not None:
            self.authority_control_score = m.get('AuthorityControlScore')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class ListOrganizationSecurityScoresResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: int = None,
        enable: bool = None,
        organization_id: str = None,
        organization_security_score: ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore = None,
    ):
        self.id = id
        self.enable = enable
        self.organization_id = organization_id
        self.organization_security_score = organization_security_score

    def validate(self):
        if self.organization_security_score:
            self.organization_security_score.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.organization_security_score is not None:
            result['OrganizationSecurityScore'] = self.organization_security_score.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('OrganizationSecurityScore') is not None:
            temp_model = ListOrganizationSecurityScoresResponseBodyResultOrganizationSecurityScore()
            self.organization_security_score = temp_model.from_map(m['OrganizationSecurityScore'])
        return self


class ListOrganizationSecurityScoresResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListOrganizationSecurityScoresResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListOrganizationSecurityScoresResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListOrganizationSecurityScoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrganizationSecurityScoresResponseBody = None,
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
            temp_model = ListOrganizationSecurityScoresResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetFileBlobsResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetFileBlobsResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        name: str = None,
        avatar_url: str = None,
        id: str = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultAuthor(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        name: str = None,
        avatar_url: str = None,
        id: int = None,
    ):
        self.extern_user_id = extern_user_id
        self.name = name
        self.avatar_url = avatar_url
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_user_id is not None:
            result['ExternUserId'] = self.extern_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternUserId') is not None:
            self.extern_user_id = m.get('ExternUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_type: str = None,
        check_name: str = None,
        extra_users: List[MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers] = None,
        unsatisfied_items: List[str] = None,
        satisfied_items: List[str] = None,
    ):
        self.check_status = check_status
        self.check_type = check_type
        self.check_name = check_name
        self.extra_users = extra_users
        self.unsatisfied_items = unsatisfied_items
        self.satisfied_items = satisfied_items

    def validate(self):
        if self.extra_users:
            for k in self.extra_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        result['ExtraUsers'] = []
        if self.extra_users is not None:
            for k in self.extra_users:
                result['ExtraUsers'].append(k.to_map() if k else None)
        if self.unsatisfied_items is not None:
            result['UnsatisfiedItems'] = self.unsatisfied_items
        if self.satisfied_items is not None:
            result['SatisfiedItems'] = self.satisfied_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        self.extra_users = []
        if m.get('ExtraUsers') is not None:
            for k in m.get('ExtraUsers'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResultsExtraUsers()
                self.extra_users.append(temp_model.from_map(k))
        if m.get('UnsatisfiedItems') is not None:
            self.unsatisfied_items = m.get('UnsatisfiedItems')
        if m.get('SatisfiedItems') is not None:
            self.satisfied_items = m.get('SatisfiedItems')
        return self


class MergeMergeRequestResponseBodyResultApproveCheckResult(TeaModel):
    def __init__(
        self,
        total_check_result: str = None,
        satisfied_check_results: List[MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults] = None,
        unsatisfied_check_results: List[MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults] = None,
    ):
        self.total_check_result = total_check_result
        self.satisfied_check_results = satisfied_check_results
        self.unsatisfied_check_results = unsatisfied_check_results

    def validate(self):
        if self.satisfied_check_results:
            for k in self.satisfied_check_results:
                if k:
                    k.validate()
        if self.unsatisfied_check_results:
            for k in self.unsatisfied_check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_check_result is not None:
            result['TotalCheckResult'] = self.total_check_result
        result['SatisfiedCheckResults'] = []
        if self.satisfied_check_results is not None:
            for k in self.satisfied_check_results:
                result['SatisfiedCheckResults'].append(k.to_map() if k else None)
        result['UnsatisfiedCheckResults'] = []
        if self.unsatisfied_check_results is not None:
            for k in self.unsatisfied_check_results:
                result['UnsatisfiedCheckResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCheckResult') is not None:
            self.total_check_result = m.get('TotalCheckResult')
        self.satisfied_check_results = []
        if m.get('SatisfiedCheckResults') is not None:
            for k in m.get('SatisfiedCheckResults'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultSatisfiedCheckResults()
                self.satisfied_check_results.append(temp_model.from_map(k))
        self.unsatisfied_check_results = []
        if m.get('UnsatisfiedCheckResults') is not None:
            for k in m.get('UnsatisfiedCheckResults'):
                temp_model = MergeMergeRequestResponseBodyResultApproveCheckResultUnsatisfiedCheckResults()
                self.unsatisfied_check_results.append(temp_model.from_map(k))
        return self


class MergeMergeRequestResponseBodyResult(TeaModel):
    def __init__(
        self,
        behind_commit_count: int = None,
        state: str = None,
        project_id: int = None,
        created_at: str = None,
        accepted_revision: str = None,
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
        assignee_list: List[MergeMergeRequestResponseBodyResultAssigneeList] = None,
        author: MergeMergeRequestResponseBodyResultAuthor = None,
        approve_check_result: MergeMergeRequestResponseBodyResultApproveCheckResult = None,
    ):
        self.behind_commit_count = behind_commit_count
        self.state = state
        self.project_id = project_id
        self.created_at = created_at
        self.accepted_revision = accepted_revision
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
        self.assignee_list = assignee_list
        self.author = author
        self.approve_check_result = approve_check_result

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behind_commit_count is not None:
            result['BehindCommitCount'] = self.behind_commit_count
        if self.state is not None:
            result['State'] = self.state
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.accepted_revision is not None:
            result['AcceptedRevision'] = self.accepted_revision
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
        result['AssigneeList'] = []
        if self.assignee_list is not None:
            for k in self.assignee_list:
                result['AssigneeList'].append(k.to_map() if k else None)
        if self.author is not None:
            result['Author'] = self.author.to_map()
        if self.approve_check_result is not None:
            result['ApproveCheckResult'] = self.approve_check_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehindCommitCount') is not None:
            self.behind_commit_count = m.get('BehindCommitCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('AcceptedRevision') is not None:
            self.accepted_revision = m.get('AcceptedRevision')
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
        self.assignee_list = []
        if m.get('AssigneeList') is not None:
            for k in m.get('AssigneeList'):
                temp_model = MergeMergeRequestResponseBodyResultAssigneeList()
                self.assignee_list.append(temp_model.from_map(k))
        if m.get('Author') is not None:
            temp_model = MergeMergeRequestResponseBodyResultAuthor()
            self.author = temp_model.from_map(m['Author'])
        if m.get('ApproveCheckResult') is not None:
            temp_model = MergeMergeRequestResponseBodyResultApproveCheckResult()
            self.approve_check_result = temp_model.from_map(m['ApproveCheckResult'])
        return self


class MergeMergeRequestResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: MergeMergeRequestResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = MergeMergeRequestResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: DeleteGroupMemberResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = DeleteGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryMemberWithInheritedRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListRepositoryMemberWithInheritedResponseBodyResultInherited(TeaModel):
    def __init__(
        self,
        type: str = None,
        name_with_namespace: str = None,
        path_with_namespace: str = None,
        visibility_level: str = None,
        path: str = None,
        name: str = None,
        id: int = None,
    ):
        self.type = type
        self.name_with_namespace = name_with_namespace
        self.path_with_namespace = path_with_namespace
        self.visibility_level = visibility_level
        self.path = path
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
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


class ListRepositoryMemberWithInheritedResponseBodyResult(TeaModel):
    def __init__(
        self,
        extern_user_id: str = None,
        email: str = None,
        avatar_url: str = None,
        state: str = None,
        access_level: int = None,
        name: str = None,
        id: int = None,
        username: str = None,
        inherited: ListRepositoryMemberWithInheritedResponseBodyResultInherited = None,
    ):
        self.extern_user_id = extern_user_id
        self.email = email
        self.avatar_url = avatar_url
        self.state = state
        self.access_level = access_level
        self.name = name
        self.id = id
        self.username = username
        self.inherited = inherited

    def validate(self):
        if self.inherited:
            self.inherited.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
        if self.inherited is not None:
            result['Inherited'] = self.inherited.to_map()
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Inherited') is not None:
            temp_model = ListRepositoryMemberWithInheritedResponseBodyResultInherited()
            self.inherited = temp_model.from_map(m['Inherited'])
        return self


class ListRepositoryMemberWithInheritedResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: List[ListRepositoryMemberWithInheritedResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRepositoryMemberWithInheritedResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRepositoryMemberWithInheritedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryMemberWithInheritedResponseBody = None,
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
            temp_model = ListRepositoryMemberWithInheritedResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        web_url: str = None,
        parent_id: int = None,
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
        self.web_url = web_url
        self.parent_id = parent_id
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.web_url is not None:
            result['WebUrl'] = self.web_url
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
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
        if m.get('WebUrl') is not None:
            self.web_url = m.get('WebUrl')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
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


class GetGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetGroupDetailResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetGroupDetailResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: GetCodeupOrganizationResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = GetCodeupOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationSecurityCenterStatusRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
    ):
        self.access_token = access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class GetOrganizationSecurityCenterStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class GetOrganizationSecurityCenterStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetOrganizationSecurityCenterStatusResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetOrganizationSecurityCenterStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetOrganizationSecurityCenterStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrganizationSecurityCenterStatusResponseBody = None,
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
            temp_model = GetOrganizationSecurityCenterStatusResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        author_name: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date
        self.parent_ids = parent_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
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
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
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
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        return self


class ListRepositoryBranchesResponseBodyResult(TeaModel):
    def __init__(
        self,
        protected_branch: bool = None,
        branch_name: str = None,
        commit_info: ListRepositoryBranchesResponseBodyResultCommitInfo = None,
    ):
        self.protected_branch = protected_branch
        self.branch_name = branch_name
        self.commit_info = commit_info

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitInfo') is not None:
            temp_model = ListRepositoryBranchesResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        return self


class ListRepositoryBranchesResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryBranchesResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListRepositoryBranchesResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        author_name: str = None,
        author_date: str = None,
        created_at: str = None,
        message: str = None,
        committer_name: str = None,
        title: str = None,
        author_email: str = None,
        committer_email: str = None,
        id: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.author_date = author_date
        self.created_at = created_at
        self.message = message
        self.committer_name = committer_name
        self.title = title
        self.author_email = author_email
        self.committer_email = committer_email
        self.id = id
        self.committed_date = committed_date
        self.parent_ids = parent_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
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
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
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
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        return self


class CreateBranchResponseBodyResult(TeaModel):
    def __init__(
        self,
        protected_branch: bool = None,
        branch_name: str = None,
        commit_info: CreateBranchResponseBodyResultCommitInfo = None,
    ):
        self.protected_branch = protected_branch
        self.branch_name = branch_name
        self.commit_info = commit_info

    def validate(self):
        if self.commit_info:
            self.commit_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protected_branch is not None:
            result['ProtectedBranch'] = self.protected_branch
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name
        if self.commit_info is not None:
            result['CommitInfo'] = self.commit_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedBranch') is not None:
            self.protected_branch = m.get('ProtectedBranch')
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')
        if m.get('CommitInfo') is not None:
            temp_model = CreateBranchResponseBodyResultCommitInfo()
            self.commit_info = temp_model.from_map(m['CommitInfo'])
        return self


class CreateBranchResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        error_code: str = None,
        success: bool = None,
        result: CreateBranchResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.error_code = error_code
        self.success = success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = CreateBranchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationRepositorySettingRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
    ):
        # 个人访问令牌。 使用阿里云AK+SK或使用STS临时授权方式不需要传该字段
        self.access_token = access_token
        # 企业标识，也称企业id，字符串形式，可在云效访问链接中获取，如 https://devops.aliyun.com/organization/\
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList(TeaModel):
    def __init__(
        self,
        permission_code: str = None,
        allowed: bool = None,
    ):
        # 权限码。ssh-clone：SSH克隆；http-clone：HTTP克隆；download：下载ZIP/TAR
        self.permission_code = permission_code
        # 是否允许
        self.allowed = allowed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code
        if self.allowed is not None:
            result['Allowed'] = self.allowed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')
        if m.get('Allowed') is not None:
            self.allowed = m.get('Allowed')
        return self


class GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList(TeaModel):
    def __init__(
        self,
        role_code: int = None,
        allowed: bool = None,
    ):
        # 角色Code。5：企业外部成员；9999：企业成员（含管理员）
        self.role_code = role_code
        # 是否允许
        self.allowed = allowed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.allowed is not None:
            result['Allowed'] = self.allowed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('Allowed') is not None:
            self.allowed = m.get('Allowed')
        return self


class GetOrganizationRepositorySettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        group_required: bool = None,
        repo_visibility_level: List[int] = None,
        repo_creator_identity: List[int] = None,
        repo_admin_access_visibility_level: List[int] = None,
        repo_admin_operation: List[int] = None,
        open_clone_download_control: bool = None,
        org_clone_download_method_list: List[GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList] = None,
        org_clone_download_role_list: List[GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList] = None,
        force_push_forbidden: bool = None,
    ):
        # 创建库是否必选代码组
        self.group_required = group_required
        # 创建代码库允许使用的可见性选项。0：允许私有；10：允许企业可见
        self.repo_visibility_level = repo_visibility_level
        # 允许创建代码库的角色。5：企业外部成员；15：企业成员；60：企业管理员
        self.repo_creator_identity = repo_creator_identity
        # 库公开性调整设置。0：允许库管理员调整公开性为私有；10：允许库管理员调整公开性为企业可见
        self.repo_admin_access_visibility_level = repo_admin_access_visibility_level
        # 库管理员允许操作。1：允许库管理员删除代码库；2：未使用保留操作
        self.repo_admin_operation = repo_admin_operation
        # 开启克隆下载限制
        self.open_clone_download_control = open_clone_download_control
        # 克隆下载限制方法列表
        self.org_clone_download_method_list = org_clone_download_method_list
        # 克隆下载限制角色列表
        self.org_clone_download_role_list = org_clone_download_role_list
        # 禁止强制推送（Force Push）
        self.force_push_forbidden = force_push_forbidden

    def validate(self):
        if self.org_clone_download_method_list:
            for k in self.org_clone_download_method_list:
                if k:
                    k.validate()
        if self.org_clone_download_role_list:
            for k in self.org_clone_download_role_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_required is not None:
            result['GroupRequired'] = self.group_required
        if self.repo_visibility_level is not None:
            result['RepoVisibilityLevel'] = self.repo_visibility_level
        if self.repo_creator_identity is not None:
            result['RepoCreatorIdentity'] = self.repo_creator_identity
        if self.repo_admin_access_visibility_level is not None:
            result['RepoAdminAccessVisibilityLevel'] = self.repo_admin_access_visibility_level
        if self.repo_admin_operation is not None:
            result['RepoAdminOperation'] = self.repo_admin_operation
        if self.open_clone_download_control is not None:
            result['OpenCloneDownloadControl'] = self.open_clone_download_control
        result['OrgCloneDownloadMethodList'] = []
        if self.org_clone_download_method_list is not None:
            for k in self.org_clone_download_method_list:
                result['OrgCloneDownloadMethodList'].append(k.to_map() if k else None)
        result['OrgCloneDownloadRoleList'] = []
        if self.org_clone_download_role_list is not None:
            for k in self.org_clone_download_role_list:
                result['OrgCloneDownloadRoleList'].append(k.to_map() if k else None)
        if self.force_push_forbidden is not None:
            result['ForcePushForbidden'] = self.force_push_forbidden
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupRequired') is not None:
            self.group_required = m.get('GroupRequired')
        if m.get('RepoVisibilityLevel') is not None:
            self.repo_visibility_level = m.get('RepoVisibilityLevel')
        if m.get('RepoCreatorIdentity') is not None:
            self.repo_creator_identity = m.get('RepoCreatorIdentity')
        if m.get('RepoAdminAccessVisibilityLevel') is not None:
            self.repo_admin_access_visibility_level = m.get('RepoAdminAccessVisibilityLevel')
        if m.get('RepoAdminOperation') is not None:
            self.repo_admin_operation = m.get('RepoAdminOperation')
        if m.get('OpenCloneDownloadControl') is not None:
            self.open_clone_download_control = m.get('OpenCloneDownloadControl')
        self.org_clone_download_method_list = []
        if m.get('OrgCloneDownloadMethodList') is not None:
            for k in m.get('OrgCloneDownloadMethodList'):
                temp_model = GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadMethodList()
                self.org_clone_download_method_list.append(temp_model.from_map(k))
        self.org_clone_download_role_list = []
        if m.get('OrgCloneDownloadRoleList') is not None:
            for k in m.get('OrgCloneDownloadRoleList'):
                temp_model = GetOrganizationRepositorySettingResponseBodyResultOrgCloneDownloadRoleList()
                self.org_clone_download_role_list.append(temp_model.from_map(k))
        if m.get('ForcePushForbidden') is not None:
            self.force_push_forbidden = m.get('ForcePushForbidden')
        return self


class GetOrganizationRepositorySettingResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetOrganizationRepositorySettingResponseBodyResult = None,
    ):
        # 错误信息
        self.error_message = error_message
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.success = success
        # 错误码
        self.error_code = error_code
        # 响应结果
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetOrganizationRepositorySettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetOrganizationRepositorySettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrganizationRepositorySettingResponseBody = None,
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
            temp_model = GetOrganizationRepositorySettingResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        ssh_clone_url: str = None,
        created_at: str = None,
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
        self.ssh_clone_url = ssh_clone_url
        self.created_at = created_at
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_activity_at is not None:
            result['LastActivityAt'] = self.last_activity_at
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.http_clone_url is not None:
            result['HttpCloneUrl'] = self.http_clone_url
        if self.archive is not None:
            result['Archive'] = self.archive
        if self.ssh_clone_url is not None:
            result['SshCloneUrl'] = self.ssh_clone_url
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
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
        if m.get('SshCloneUrl') is not None:
            self.ssh_clone_url = m.get('SshCloneUrl')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
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
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListGroupRepositoriesResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListGroupRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryTagV2Request(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        organization_id: str = None,
        tag_name: str = None,
    ):
        self.access_token = access_token
        self.organization_id = organization_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class GetRepositoryTagV2ResponseBodyResultCommitSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class GetRepositoryTagV2ResponseBodyResultCommit(TeaModel):
    def __init__(
        self,
        short_id: str = None,
        author_name: str = None,
        created_at: str = None,
        message: str = None,
        authored_date: str = None,
        title: str = None,
        committer_name: str = None,
        author_email: str = None,
        id: str = None,
        committer_email: str = None,
        committed_date: str = None,
        parent_ids: List[str] = None,
        signature: GetRepositoryTagV2ResponseBodyResultCommitSignature = None,
    ):
        self.short_id = short_id
        self.author_name = author_name
        self.created_at = created_at
        self.message = message
        self.authored_date = authored_date
        self.title = title
        self.committer_name = committer_name
        self.author_email = author_email
        self.id = id
        self.committer_email = committer_email
        self.committed_date = committed_date
        self.parent_ids = parent_ids
        self.signature = signature

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.message is not None:
            result['Message'] = self.message
        if self.authored_date is not None:
            result['AuthoredDate'] = self.authored_date
        if self.title is not None:
            result['Title'] = self.title
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.id is not None:
            result['Id'] = self.id
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AuthoredDate') is not None:
            self.authored_date = m.get('AuthoredDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResultCommitSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryTagV2ResponseBodyResultSignature(TeaModel):
    def __init__(
        self,
        verification_status: str = None,
        gpg_key_id: str = None,
    ):
        self.verification_status = verification_status
        self.gpg_key_id = gpg_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        return self


class GetRepositoryTagV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        id: str = None,
        commit: GetRepositoryTagV2ResponseBodyResultCommit = None,
        signature: GetRepositoryTagV2ResponseBodyResultSignature = None,
    ):
        self.message = message
        self.name = name
        self.id = id
        self.commit = commit
        self.signature = signature

    def validate(self):
        if self.commit:
            self.commit.validate()
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.commit is not None:
            result['Commit'] = self.commit.to_map()
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Commit') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResultCommit()
            self.commit = temp_model.from_map(m['Commit'])
        if m.get('Signature') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        return self


class GetRepositoryTagV2ResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetRepositoryTagV2ResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetRepositoryTagV2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRepositoryTagV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepositoryTagV2ResponseBody = None,
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
            temp_model = GetRepositoryTagV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMergeRequestSettingRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetMergeRequestSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        is_enable_smart_code_review: bool = None,
        merge_types: List[str] = None,
    ):
        self.is_enable_smart_code_review = is_enable_smart_code_review
        self.merge_types = merge_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enable_smart_code_review is not None:
            result['IsEnableSmartCodeReview'] = self.is_enable_smart_code_review
        if self.merge_types is not None:
            result['MergeTypes'] = self.merge_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnableSmartCodeReview') is not None:
            self.is_enable_smart_code_review = m.get('IsEnableSmartCodeReview')
        if m.get('MergeTypes') is not None:
            self.merge_types = m.get('MergeTypes')
        return self


class GetMergeRequestSettingResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        result: GetMergeRequestSettingResponseBodyResult = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Result') is not None:
            temp_model = GetMergeRequestSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMergeRequestSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMergeRequestSettingResponseBody = None,
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
            temp_model = GetMergeRequestSettingResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        url: str = None,
        tag_push_events: bool = None,
        last_test_result: str = None,
        merge_requests_events: bool = None,
        description: str = None,
        note_events: bool = None,
        secret_token: str = None,
        id: int = None,
        enable_ssl_verification: bool = None,
    ):
        self.push_events = push_events
        self.project_id = project_id
        self.created_at = created_at
        self.url = url
        self.tag_push_events = tag_push_events
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_events is not None:
            result['PushEvents'] = self.push_events
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.url is not None:
            result['Url'] = self.url
        if self.tag_push_events is not None:
            result['TagPushEvents'] = self.tag_push_events
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
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('TagPushEvents') is not None:
            self.tag_push_events = m.get('TagPushEvents')
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


class ListRepositoryWebhookResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
        total: int = None,
        success: bool = None,
        error_code: str = None,
        result: List[ListRepositoryWebhookResponseBodyResult] = None,
    ):
        self.error_message = error_message
        self.request_id = request_id
        self.total = total
        self.success = success
        self.error_code = error_code
        self.result = result

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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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
            temp_model = ListRepositoryWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


