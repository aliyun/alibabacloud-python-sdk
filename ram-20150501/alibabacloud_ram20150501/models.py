# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddUserToGroupRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        group_name: str = None,
    ):
        self.user_name = user_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AddUserToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserToGroupResponseBody = None,
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
            temp_model = AddUserToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPolicyToGroupRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        group_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class AttachPolicyToGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachPolicyToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachPolicyToGroupResponseBody = None,
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
            temp_model = AttachPolicyToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPolicyToRoleRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        role_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class AttachPolicyToRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachPolicyToRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachPolicyToRoleResponseBody = None,
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
            temp_model = AttachPolicyToRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPolicyToUserRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        user_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class AttachPolicyToUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachPolicyToUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachPolicyToUserResponseBody = None,
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
            temp_model = AttachPolicyToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        user_name: str = None,
        authentication_code_1: str = None,
        authentication_code_2: str = None,
    ):
        self.serial_number = serial_number
        self.user_name = user_name
        self.authentication_code_1 = authentication_code_1
        self.authentication_code_2 = authentication_code_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1
        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = m.get('AuthenticationCode1')
        if m.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = m.get('AuthenticationCode2')
        return self


class BindMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindMFADeviceResponseBody = None,
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
            temp_model = BindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(
        self,
        old_password: str = None,
        new_password: str = None,
    ):
        self.old_password = old_password
        self.new_password = new_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        return self


class ChangePasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangePasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangePasswordResponseBody = None,
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
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearAccountAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClearAccountAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClearAccountAliasResponseBody = None,
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
            temp_model = ClearAccountAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAccessKeyResponseBodyAccessKey(TeaModel):
    def __init__(
        self,
        status: str = None,
        access_key_secret: str = None,
        create_date: str = None,
        access_key_id: str = None,
    ):
        self.status = status
        self.access_key_secret = access_key_secret
        self.create_date = create_date
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class CreateAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_key: CreateAccessKeyResponseBodyAccessKey = None,
    ):
        self.request_id = request_id
        self.access_key = access_key

    def validate(self):
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessKey') is not None:
            temp_model = CreateAccessKeyResponseBodyAccessKey()
            self.access_key = temp_model.from_map(m['AccessKey'])
        return self


class CreateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessKeyResponseBody = None,
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
            temp_model = CreateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        comments: str = None,
    ):
        self.group_name = group_name
        self.comments = comments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        return self


class CreateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: CreateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = CreateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        password: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
    ):
        self.user_name = user_name
        self.password = password
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class CreateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        password_reset_required: bool = None,
        create_date: str = None,
        user_name: str = None,
        mfabind_required: bool = None,
    ):
        self.password_reset_required = password_reset_required
        self.create_date = create_date
        self.user_name = user_name
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class CreateLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: CreateLoginProfileResponseBodyLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginProfile') is not None:
            temp_model = CreateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class CreateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoginProfileResponseBody = None,
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
            temp_model = CreateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        description: str = None,
        policy_document: str = None,
    ):
        self.policy_name = policy_name
        self.description = description
        self.policy_document = policy_document

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        return self


class CreatePolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        create_date: str = None,
        policy_type: str = None,
    ):
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.create_date = create_date
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: CreatePolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = CreatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolicyResponseBody = None,
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_document: str = None,
        set_as_default: bool = None,
        rotate_strategy: str = None,
    ):
        self.policy_name = policy_name
        self.policy_document = policy_document
        self.set_as_default = set_as_default
        self.rotate_strategy = rotate_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default
        if self.rotate_strategy is not None:
            result['RotateStrategy'] = self.rotate_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')
        if m.get('RotateStrategy') is not None:
            self.rotate_strategy = m.get('RotateStrategy')
        return self


class CreatePolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(
        self,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
        create_date: str = None,
    ):
        self.is_default_version = is_default_version
        self.policy_document = policy_document
        self.version_id = version_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreatePolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        policy_version: CreatePolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        self.policy_version = policy_version
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        result = dict()
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = CreatePolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolicyVersionResponseBody = None,
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
            temp_model = CreatePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        description: str = None,
        assume_role_policy_document: str = None,
        max_session_duration: int = None,
    ):
        self.role_name = role_name
        self.description = description
        self.assume_role_policy_document = assume_role_policy_document
        self.max_session_duration = max_session_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.description is not None:
            result['Description'] = self.description
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        return self


class CreateRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        assume_role_policy_document: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
        create_date: str = None,
        role_id: str = None,
        arn: str = None,
    ):
        self.assume_role_policy_document = assume_role_policy_document
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_name = role_name
        self.create_date = create_date
        self.role_id = role_id
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(
        self,
        role: CreateRoleResponseBodyRole = None,
        request_id: str = None,
    ):
        self.role = role
        self.request_id = request_id

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            temp_model = CreateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRoleResponseBody = None,
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
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        display_name: str = None,
        mobile_phone: str = None,
        email: str = None,
        comments: str = None,
    ):
        self.user_name = user_name
        self.display_name = display_name
        self.mobile_phone = mobile_phone
        self.email = email
        self.comments = comments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.email is not None:
            result['Email'] = self.email
        if self.comments is not None:
            result['Comments'] = self.comments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        return self


class CreateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        create_date: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.create_date = create_date
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        user: CreateUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = CreateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUserResponseBody = None,
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        virtual_mfadevice_name: str = None,
    ):
        self.virtual_mfadevice_name = virtual_mfadevice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = m.get('VirtualMFADeviceName')
        return self


class CreateVirtualMFADeviceResponseBodyVirtualMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        qrcode_png: str = None,
        base_32string_seed: str = None,
    ):
        self.serial_number = serial_number
        self.qrcode_png = qrcode_png
        self.base_32string_seed = base_32string_seed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.qrcode_png is not None:
            result['QRCodePNG'] = self.qrcode_png
        if self.base_32string_seed is not None:
            result['Base32StringSeed'] = self.base_32string_seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('QRCodePNG') is not None:
            self.qrcode_png = m.get('QRCodePNG')
        if m.get('Base32StringSeed') is not None:
            self.base_32string_seed = m.get('Base32StringSeed')
        return self


class CreateVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        virtual_mfadevice: CreateVirtualMFADeviceResponseBodyVirtualMFADevice = None,
        request_id: str = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice
        self.request_id = request_id

    def validate(self):
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        result = dict()
        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADevice') is not None:
            temp_model = CreateVirtualMFADeviceResponseBodyVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(m['VirtualMFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVirtualMFADeviceResponseBody = None,
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
            temp_model = CreateVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        user_access_key_id: str = None,
    ):
        self.user_name = user_name
        self.user_access_key_id = user_access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        return self


class DeleteAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessKeyResponseBody = None,
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
            temp_model = DeleteAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupResponseBody = None,
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoginProfileResponseBody = None,
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
            temp_model = DeleteLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePolicyResponseBody = None,
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeletePolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePolicyVersionResponseBody = None,
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
            temp_model = DeletePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRoleResponseBody = None,
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
            temp_model = DeleteRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVirtualMFADeviceResponseBody = None,
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
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyFromGroupRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        group_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DetachPolicyFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachPolicyFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachPolicyFromGroupResponseBody = None,
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
            temp_model = DetachPolicyFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyFromRoleRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        role_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DetachPolicyFromRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachPolicyFromRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachPolicyFromRoleResponseBody = None,
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
            temp_model = DetachPolicyFromRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyFromUserRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        user_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DetachPolicyFromUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachPolicyFromUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachPolicyFromUserResponseBody = None,
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
            temp_model = DetachPolicyFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        user_access_key_id: str = None,
    ):
        self.user_name = user_name
        self.user_access_key_id = user_access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        return self


class GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed(TeaModel):
    def __init__(
        self,
        last_used_date: str = None,
    ):
        self.last_used_date = last_used_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')
        return self


class GetAccessKeyLastUsedResponseBody(TeaModel):
    def __init__(
        self,
        access_key_last_used: GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed = None,
        request_id: str = None,
    ):
        self.access_key_last_used = access_key_last_used
        self.request_id = request_id

    def validate(self):
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        result = dict()
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyLastUsed') is not None:
            temp_model = GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(m['AccessKeyLastUsed'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccessKeyLastUsedResponseBody = None,
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
            temp_model = GetAccessKeyLastUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account_alias: str = None,
    ):
        self.request_id = request_id
        self.account_alias = account_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account_alias is not None:
            result['AccountAlias'] = self.account_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccountAlias') is not None:
            self.account_alias = m.get('AccountAlias')
        return self


class GetAccountAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAccountAliasResponseBody = None,
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
            temp_model = GetAccountAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
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
        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupResponseBody = None,
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
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(
        self,
        password_reset_required: bool = None,
        create_date: str = None,
        user_name: str = None,
        mfabind_required: bool = None,
    ):
        self.password_reset_required = password_reset_required
        self.create_date = create_date
        self.user_name = user_name
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class GetLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_profile: GetLoginProfileResponseBodyLoginProfile = None,
    ):
        self.request_id = request_id
        self.login_profile = login_profile

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginProfile') is not None:
            temp_model = GetLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        return self


class GetLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLoginProfileResponseBody = None,
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
            temp_model = GetLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        require_numbers: bool = None,
        require_lowercase_characters: bool = None,
        hard_expiry: bool = None,
        password_reuse_prevention: int = None,
        require_symbols: bool = None,
        max_password_age: int = None,
        minimum_password_length: int = None,
        require_uppercase_characters: bool = None,
        max_login_attemps: int = None,
    ):
        self.require_numbers = require_numbers
        self.require_lowercase_characters = require_lowercase_characters
        self.hard_expiry = hard_expiry
        self.password_reuse_prevention = password_reuse_prevention
        self.require_symbols = require_symbols
        self.max_password_age = max_password_age
        self.minimum_password_length = minimum_password_length
        self.require_uppercase_characters = require_uppercase_characters
        self.max_login_attemps = max_login_attemps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.hard_expiry is not None:
            result['HardExpiry'] = self.hard_expiry
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('HardExpiry') is not None:
            self.hard_expiry = m.get('HardExpiry')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        return self


class GetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        password_policy: GetPasswordPolicyResponseBodyPasswordPolicy = None,
    ):
        self.request_id = request_id
        self.password_policy = password_policy

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PasswordPolicy') is not None:
            temp_model = GetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPasswordPolicyResponseBody = None,
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
            temp_model = GetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        default_version: str = None,
        update_date: str = None,
        description: str = None,
        policy_document: str = None,
        attachment_count: int = None,
        policy_name: str = None,
        create_date: str = None,
        policy_type: str = None,
    ):
        self.default_version = default_version
        self.update_date = update_date
        self.description = description
        self.policy_document = policy_document
        self.attachment_count = attachment_count
        self.policy_name = policy_name
        self.create_date = create_date
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class GetPolicyResponseBodyDefaultPolicyVersion(TeaModel):
    def __init__(
        self,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
        create_date: str = None,
    ):
        self.is_default_version = is_default_version
        self.policy_document = policy_document
        self.version_id = version_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
        default_policy_version: GetPolicyResponseBodyDefaultPolicyVersion = None,
    ):
        self.policy = policy
        self.request_id = request_id
        self.default_policy_version = default_policy_version

    def validate(self):
        if self.policy:
            self.policy.validate()
        if self.default_policy_version:
            self.default_policy_version.validate()

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.default_policy_version is not None:
            result['DefaultPolicyVersion'] = self.default_policy_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefaultPolicyVersion') is not None:
            temp_model = GetPolicyResponseBodyDefaultPolicyVersion()
            self.default_policy_version = temp_model.from_map(m['DefaultPolicyVersion'])
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolicyResponseBody = None,
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(
        self,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
        create_date: str = None,
    ):
        self.is_default_version = is_default_version
        self.policy_document = policy_document
        self.version_id = version_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetPolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        policy_version: GetPolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        self.policy_version = policy_version
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        result = dict()
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = GetPolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolicyVersionResponseBody = None,
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
            temp_model = GetPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        assume_role_policy_document: str = None,
        update_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
        create_date: str = None,
        role_id: str = None,
        arn: str = None,
    ):
        self.assume_role_policy_document = assume_role_policy_document
        self.update_date = update_date
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_name = role_name
        self.create_date = create_date
        self.role_id = role_id
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetRoleResponseBody(TeaModel):
    def __init__(
        self,
        role: GetRoleResponseBodyRole = None,
        request_id: str = None,
    ):
        self.role = role
        self.request_id = request_id

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            temp_model = GetRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRoleResponseBody = None,
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
            temp_model = GetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        enable_save_mfaticket: bool = None,
        login_session_duration: int = None,
        login_network_masks: str = None,
        allow_user_to_change_password: bool = None,
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.allow_user_to_change_password = allow_user_to_change_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_public_keys: bool = None,
    ):
        self.allow_user_to_manage_public_keys = allow_user_to_manage_public_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_public_keys is not None:
            result['AllowUserToManagePublicKeys'] = self.allow_user_to_manage_public_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManagePublicKeys') is not None:
            self.allow_user_to_manage_public_keys = m.get('AllowUserToManagePublicKeys')
        return self


class GetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(
        self,
        access_key_preference: GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        mfapreference: GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
        login_profile_preference: GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        public_key_preference: GetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference = None,
    ):
        self.access_key_preference = access_key_preference
        self.mfapreference = mfapreference
        self.login_profile_preference = login_profile_preference
        self.public_key_preference = public_key_preference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.public_key_preference:
            self.public_key_preference.validate()

    def to_map(self):
        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.public_key_preference is not None:
            result['PublicKeyPreference'] = self.public_key_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('MFAPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('PublicKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference()
            self.public_key_preference = temp_model.from_map(m['PublicKeyPreference'])
        return self


class GetSecurityPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        security_preference: GetSecurityPreferenceResponseBodySecurityPreference = None,
        request_id: str = None,
    ):
        self.security_preference = security_preference
        self.request_id = request_id

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = dict()
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSecurityPreferenceResponseBody = None,
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
            temp_model = GetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        last_login_date: str = None,
        create_date: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.last_login_date = last_login_date
        self.create_date = create_date
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        user: GetUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetUserMFAInfoRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetUserMFAInfoResponseBodyMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class GetUserMFAInfoResponseBody(TeaModel):
    def __init__(
        self,
        mfadevice: GetUserMFAInfoResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        self.mfadevice = mfadevice
        self.request_id = request_id

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = dict()
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = GetUserMFAInfoResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserMFAInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserMFAInfoResponseBody = None,
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
            temp_model = GetUserMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListAccessKeysResponseBodyAccessKeysAccessKey(TeaModel):
    def __init__(
        self,
        status: str = None,
        access_key_id: str = None,
        create_date: str = None,
    ):
        self.status = status
        self.access_key_id = access_key_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListAccessKeysResponseBodyAccessKeys(TeaModel):
    def __init__(
        self,
        access_key: List[ListAccessKeysResponseBodyAccessKeysAccessKey] = None,
    ):
        self.access_key = access_key

    def validate(self):
        if self.access_key:
            for k in self.access_key:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccessKey'] = []
        if self.access_key is not None:
            for k in self.access_key:
                result['AccessKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_key = []
        if m.get('AccessKey') is not None:
            for k in m.get('AccessKey'):
                temp_model = ListAccessKeysResponseBodyAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k))
        return self


class ListAccessKeysResponseBody(TeaModel):
    def __init__(
        self,
        access_keys: ListAccessKeysResponseBodyAccessKeys = None,
        request_id: str = None,
    ):
        self.access_keys = access_keys
        self.request_id = request_id

    def validate(self):
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        result = dict()
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeys') is not None:
            temp_model = ListAccessKeysResponseBodyAccessKeys()
            self.access_keys = temp_model.from_map(m['AccessKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccessKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAccessKeysResponseBody = None,
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
            temp_model = ListAccessKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEntitiesForPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class ListEntitiesForPolicyResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        comments: str = None,
        attach_date: str = None,
    ):
        self.group_name = group_name
        self.comments = comments
        self.attach_date = attach_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        return self


class ListEntitiesForPolicyResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListEntitiesForPolicyResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListEntitiesForPolicyResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListEntitiesForPolicyResponseBodyRolesRole(TeaModel):
    def __init__(
        self,
        description: str = None,
        role_name: str = None,
        attach_date: str = None,
        arn: str = None,
        role_id: str = None,
    ):
        self.description = description
        self.role_name = role_name
        self.attach_date = attach_date
        self.arn = arn
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class ListEntitiesForPolicyResponseBodyRoles(TeaModel):
    def __init__(
        self,
        role: List[ListEntitiesForPolicyResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListEntitiesForPolicyResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListEntitiesForPolicyResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
        user_name: str = None,
        attach_date: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id
        self.user_name = user_name
        self.attach_date = attach_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        return self


class ListEntitiesForPolicyResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListEntitiesForPolicyResponseBodyUsersUser] = None,
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
                temp_model = ListEntitiesForPolicyResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListEntitiesForPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: ListEntitiesForPolicyResponseBodyGroups = None,
        roles: ListEntitiesForPolicyResponseBodyRoles = None,
        users: ListEntitiesForPolicyResponseBodyUsers = None,
    ):
        self.request_id = request_id
        self.groups = groups
        self.roles = roles
        self.users = users

    def validate(self):
        if self.groups:
            self.groups.validate()
        if self.roles:
            self.roles.validate()
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Groups') is not None:
            temp_model = ListEntitiesForPolicyResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('Roles') is not None:
            temp_model = ListEntitiesForPolicyResponseBodyRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('Users') is not None:
            temp_model = ListEntitiesForPolicyResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListEntitiesForPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEntitiesForPolicyResponseBody = None,
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
            temp_model = ListEntitiesForPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListGroupsResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: ListGroupsResponseBodyGroups = None,
        is_truncated: bool = None,
        marker: str = None,
    ):
        self.request_id = request_id
        self.groups = groups
        self.is_truncated = is_truncated
        self.marker = marker

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Groups') is not None:
            temp_model = ListGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
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


class ListGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListGroupsForUserResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        comments: str = None,
        join_date: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.comments = comments
        self.join_date = join_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        return self


class ListGroupsForUserResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[ListGroupsForUserResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsForUserResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsForUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: ListGroupsForUserResponseBodyGroups = None,
    ):
        self.request_id = request_id
        self.groups = groups

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Groups') is not None:
            temp_model = ListGroupsForUserResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        return self


class ListGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupsForUserResponseBody = None,
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
            temp_model = ListGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        marker: str = None,
        max_items: int = None,
    ):
        self.policy_type = policy_type
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListPoliciesResponseBodyPoliciesPolicy(TeaModel):
    def __init__(
        self,
        default_version: str = None,
        description: str = None,
        update_date: str = None,
        attachment_count: int = None,
        policy_name: str = None,
        create_date: str = None,
        policy_type: str = None,
    ):
        self.default_version = default_version
        self.description = description
        self.update_date = update_date
        self.attachment_count = attachment_count
        self.policy_name = policy_name
        self.create_date = create_date
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        policy: List[ListPoliciesResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        policies: ListPoliciesResponseBodyPolicies = None,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
    ):
        self.policies = policies
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policies') is not None:
            temp_model = ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPoliciesResponseBody = None,
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesForGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ListPoliciesForGroupResponseBodyPoliciesPolicy(TeaModel):
    def __init__(
        self,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        attach_date: str = None,
        policy_type: str = None,
    ):
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.attach_date = attach_date
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesForGroupResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        policy: List[ListPoliciesForGroupResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesForGroupResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesForGroupResponseBody(TeaModel):
    def __init__(
        self,
        policies: ListPoliciesForGroupResponseBodyPolicies = None,
        request_id: str = None,
    ):
        self.policies = policies
        self.request_id = request_id

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policies') is not None:
            temp_model = ListPoliciesForGroupResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesForGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPoliciesForGroupResponseBody = None,
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
            temp_model = ListPoliciesForGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesForRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListPoliciesForRoleResponseBodyPoliciesPolicy(TeaModel):
    def __init__(
        self,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        attach_date: str = None,
        policy_type: str = None,
    ):
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.attach_date = attach_date
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesForRoleResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        policy: List[ListPoliciesForRoleResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesForRoleResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesForRoleResponseBody(TeaModel):
    def __init__(
        self,
        policies: ListPoliciesForRoleResponseBodyPolicies = None,
        request_id: str = None,
    ):
        self.policies = policies
        self.request_id = request_id

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policies') is not None:
            temp_model = ListPoliciesForRoleResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesForRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPoliciesForRoleResponseBody = None,
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
            temp_model = ListPoliciesForRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesForUserRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListPoliciesForUserResponseBodyPoliciesPolicy(TeaModel):
    def __init__(
        self,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        attach_date: str = None,
        policy_type: str = None,
    ):
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.attach_date = attach_date
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesForUserResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        policy: List[ListPoliciesForUserResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesForUserResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesForUserResponseBody(TeaModel):
    def __init__(
        self,
        policies: ListPoliciesForUserResponseBodyPolicies = None,
        request_id: str = None,
    ):
        self.policies = policies
        self.request_id = request_id

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policies') is not None:
            temp_model = ListPoliciesForUserResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPoliciesForUserResponseBody = None,
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
            temp_model = ListPoliciesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyVersionsRequest(TeaModel):
    def __init__(
        self,
        policy_type: str = None,
        policy_name: str = None,
    ):
        self.policy_type = policy_type
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion(TeaModel):
    def __init__(
        self,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
        create_date: str = None,
    ):
        self.is_default_version = is_default_version
        self.policy_document = policy_document
        self.version_id = version_id
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListPolicyVersionsResponseBodyPolicyVersions(TeaModel):
    def __init__(
        self,
        policy_version: List[ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion] = None,
    ):
        self.policy_version = policy_version

    def validate(self):
        if self.policy_version:
            for k in self.policy_version:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PolicyVersion'] = []
        if self.policy_version is not None:
            for k in self.policy_version:
                result['PolicyVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_version = []
        if m.get('PolicyVersion') is not None:
            for k in m.get('PolicyVersion'):
                temp_model = ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion()
                self.policy_version.append(temp_model.from_map(k))
        return self


class ListPolicyVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy_versions: ListPolicyVersionsResponseBodyPolicyVersions = None,
    ):
        self.request_id = request_id
        self.policy_versions = policy_versions

    def validate(self):
        if self.policy_versions:
            self.policy_versions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy_versions is not None:
            result['PolicyVersions'] = self.policy_versions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PolicyVersions') is not None:
            temp_model = ListPolicyVersionsResponseBodyPolicyVersions()
            self.policy_versions = temp_model.from_map(m['PolicyVersions'])
        return self


class ListPolicyVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPolicyVersionsResponseBody = None,
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
            temp_model = ListPolicyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListRolesResponseBodyRolesRole(TeaModel):
    def __init__(
        self,
        description: str = None,
        update_date: str = None,
        max_session_duration: int = None,
        role_name: str = None,
        create_date: str = None,
        role_id: str = None,
        arn: str = None,
    ):
        self.description = description
        self.update_date = update_date
        self.max_session_duration = max_session_duration
        self.role_name = role_name
        self.create_date = create_date
        self.role_id = role_id
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListRolesResponseBodyRoles(TeaModel):
    def __init__(
        self,
        role: List[ListRolesResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListRolesResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        roles: ListRolesResponseBodyRoles = None,
        marker: str = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.roles = roles
        self.marker = marker

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Roles') is not None:
            temp_model = ListRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRolesResponseBody = None,
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        create_date: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.create_date = create_date
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersResponseBodyUsersUser] = None,
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
                temp_model = ListUsersResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        users: ListUsersResponseBodyUsers = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
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


class ListUsersForGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        marker: str = None,
        max_items: int = None,
    ):
        self.group_name = group_name
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersForGroupResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        join_date: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.join_date = join_date
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersForGroupResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListUsersForGroupResponseBodyUsersUser] = None,
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
                temp_model = ListUsersForGroupResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersForGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_truncated: bool = None,
        marker: str = None,
        users: ListUsersForGroupResponseBodyUsers = None,
    ):
        self.request_id = request_id
        self.is_truncated = is_truncated
        self.marker = marker
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Users') is not None:
            temp_model = ListUsersForGroupResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersForGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersForGroupResponseBody = None,
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
            temp_model = ListUsersForGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        user: ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser = None,
        activate_date: str = None,
    ):
        self.serial_number = serial_number
        self.user = user
        self.activate_date = activate_date

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('User') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(
        self,
        virtual_mfadevice: List[ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice] = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        if self.virtual_mfadevice:
            for k in self.virtual_mfadevice:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VirtualMFADevice'] = []
        if self.virtual_mfadevice is not None:
            for k in self.virtual_mfadevice:
                result['VirtualMFADevice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_mfadevice = []
        if m.get('VirtualMFADevice') is not None:
            for k in m.get('VirtualMFADevice'):
                temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k))
        return self


class ListVirtualMFADevicesResponseBody(TeaModel):
    def __init__(
        self,
        virtual_mfadevices: ListVirtualMFADevicesResponseBodyVirtualMFADevices = None,
        request_id: str = None,
    ):
        self.virtual_mfadevices = virtual_mfadevices
        self.request_id = request_id

    def validate(self):
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        result = dict()
        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADevices') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(m['VirtualMFADevices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVirtualMFADevicesResponseBody = None,
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
            temp_model = ListVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        group_name: str = None,
    ):
        self.user_name = user_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class RemoveUserFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserFromGroupResponseBody = None,
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
            temp_model = RemoveUserFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccountAliasRequest(TeaModel):
    def __init__(
        self,
        account_alias: str = None,
    ):
        self.account_alias = account_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_alias is not None:
            result['AccountAlias'] = self.account_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAlias') is not None:
            self.account_alias = m.get('AccountAlias')
        return self


class SetAccountAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAccountAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAccountAliasResponseBody = None,
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
            temp_model = SetAccountAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        self.policy_name = policy_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SetDefaultPolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDefaultPolicyVersionResponseBody = None,
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
            temp_model = SetDefaultPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordPolicyRequest(TeaModel):
    def __init__(
        self,
        minimum_password_length: int = None,
        require_lowercase_characters: bool = None,
        require_uppercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        hard_expiry: bool = None,
        max_password_age: int = None,
        password_reuse_prevention: int = None,
        max_login_attemps: int = None,
    ):
        self.minimum_password_length = minimum_password_length
        self.require_lowercase_characters = require_lowercase_characters
        self.require_uppercase_characters = require_uppercase_characters
        self.require_numbers = require_numbers
        self.require_symbols = require_symbols
        self.hard_expiry = hard_expiry
        self.max_password_age = max_password_age
        self.password_reuse_prevention = password_reuse_prevention
        self.max_login_attemps = max_login_attemps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.hard_expiry is not None:
            result['HardExpiry'] = self.hard_expiry
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('HardExpiry') is not None:
            self.hard_expiry = m.get('HardExpiry')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        return self


class SetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        require_numbers: bool = None,
        require_lowercase_characters: bool = None,
        hard_expiry: bool = None,
        password_reuse_prevention: int = None,
        require_symbols: bool = None,
        max_password_age: int = None,
        minimum_password_length: int = None,
        require_uppercase_characters: bool = None,
        max_login_attemps: int = None,
    ):
        self.require_numbers = require_numbers
        self.require_lowercase_characters = require_lowercase_characters
        self.hard_expiry = hard_expiry
        self.password_reuse_prevention = password_reuse_prevention
        self.require_symbols = require_symbols
        self.max_password_age = max_password_age
        self.minimum_password_length = minimum_password_length
        self.require_uppercase_characters = require_uppercase_characters
        self.max_login_attemps = max_login_attemps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.hard_expiry is not None:
            result['HardExpiry'] = self.hard_expiry
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('HardExpiry') is not None:
            self.hard_expiry = m.get('HardExpiry')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        return self


class SetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        password_policy: SetPasswordPolicyResponseBodyPasswordPolicy = None,
    ):
        self.request_id = request_id
        self.password_policy = password_policy

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PasswordPolicy') is not None:
            temp_model = SetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        return self


class SetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetPasswordPolicyResponseBody = None,
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
            temp_model = SetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSecurityPreferenceRequest(TeaModel):
    def __init__(
        self,
        enable_save_mfaticket: bool = None,
        allow_user_to_change_password: bool = None,
        allow_user_to_manage_access_keys: bool = None,
        allow_user_to_manage_public_keys: bool = None,
        allow_user_to_manage_mfadevices: bool = None,
        login_session_duration: int = None,
        login_network_masks: str = None,
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.allow_user_to_change_password = allow_user_to_change_password
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys
        self.allow_user_to_manage_public_keys = allow_user_to_manage_public_keys
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        if self.allow_user_to_manage_public_keys is not None:
            result['AllowUserToManagePublicKeys'] = self.allow_user_to_manage_public_keys
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        if m.get('AllowUserToManagePublicKeys') is not None:
            self.allow_user_to_manage_public_keys = m.get('AllowUserToManagePublicKeys')
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_access_keys: bool = None,
    ):
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_mfadevices: bool = None,
    ):
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(
        self,
        enable_save_mfaticket: bool = None,
        login_session_duration: int = None,
        login_network_masks: str = None,
        allow_user_to_change_password: bool = None,
    ):
        self.enable_save_mfaticket = enable_save_mfaticket
        self.login_session_duration = login_session_duration
        self.login_network_masks = login_network_masks
        self.allow_user_to_change_password = allow_user_to_change_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_manage_public_keys: bool = None,
    ):
        self.allow_user_to_manage_public_keys = allow_user_to_manage_public_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.allow_user_to_manage_public_keys is not None:
            result['AllowUserToManagePublicKeys'] = self.allow_user_to_manage_public_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToManagePublicKeys') is not None:
            self.allow_user_to_manage_public_keys = m.get('AllowUserToManagePublicKeys')
        return self


class SetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(
        self,
        access_key_preference: SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference = None,
        mfapreference: SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference = None,
        login_profile_preference: SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference = None,
        public_key_preference: SetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference = None,
    ):
        self.access_key_preference = access_key_preference
        self.mfapreference = mfapreference
        self.login_profile_preference = login_profile_preference
        self.public_key_preference = public_key_preference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.public_key_preference:
            self.public_key_preference.validate()

    def to_map(self):
        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.public_key_preference is not None:
            result['PublicKeyPreference'] = self.public_key_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('MFAPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('PublicKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferencePublicKeyPreference()
            self.public_key_preference = temp_model.from_map(m['PublicKeyPreference'])
        return self


class SetSecurityPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        security_preference: SetSecurityPreferenceResponseBodySecurityPreference = None,
        request_id: str = None,
    ):
        self.security_preference = security_preference
        self.request_id = request_id

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        result = dict()
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSecurityPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetSecurityPreferenceResponseBody = None,
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
            temp_model = SetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindMFADeviceRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UnbindMFADeviceResponseBodyMFADevice(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnbindMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        mfadevice: UnbindMFADeviceResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        self.mfadevice = mfadevice
        self.request_id = request_id

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = dict()
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = UnbindMFADeviceResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindMFADeviceResponseBody = None,
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
            temp_model = UnbindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessKeyRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        user_access_key_id: str = None,
        status: str = None,
    ):
        self.user_name = user_name
        self.user_access_key_id = user_access_key_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAccessKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccessKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAccessKeyResponseBody = None,
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
            temp_model = UpdateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        new_group_name: str = None,
        new_comments: str = None,
    ):
        self.group_name = group_name
        self.new_group_name = new_group_name
        self.new_comments = new_comments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        return self


class UpdateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        update_date: str = None,
        group_name: str = None,
        comments: str = None,
        create_date: str = None,
    ):
        self.group_id = group_id
        self.update_date = update_date
        self.group_name = group_name
        self.comments = comments
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: UpdateGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = UpdateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupResponseBody = None,
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
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        password: str = None,
        password_reset_required: bool = None,
        mfabind_required: bool = None,
    ):
        self.user_name = user_name
        self.password = password
        self.password_reset_required = password_reset_required
        self.mfabind_required = mfabind_required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        return self


class UpdateLoginProfileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoginProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLoginProfileResponseBody = None,
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
            temp_model = UpdateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
        new_assume_role_policy_document: str = None,
        new_max_session_duration: int = None,
    ):
        self.role_name = role_name
        self.new_assume_role_policy_document = new_assume_role_policy_document
        self.new_max_session_duration = new_max_session_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.new_assume_role_policy_document is not None:
            result['NewAssumeRolePolicyDocument'] = self.new_assume_role_policy_document
        if self.new_max_session_duration is not None:
            result['NewMaxSessionDuration'] = self.new_max_session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('NewAssumeRolePolicyDocument') is not None:
            self.new_assume_role_policy_document = m.get('NewAssumeRolePolicyDocument')
        if m.get('NewMaxSessionDuration') is not None:
            self.new_max_session_duration = m.get('NewMaxSessionDuration')
        return self


class UpdateRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        assume_role_policy_document: str = None,
        update_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
        create_date: str = None,
        role_id: str = None,
        arn: str = None,
    ):
        self.assume_role_policy_document = assume_role_policy_document
        self.update_date = update_date
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_name = role_name
        self.create_date = create_date
        self.role_id = role_id
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateRoleResponseBody(TeaModel):
    def __init__(
        self,
        role: UpdateRoleResponseBodyRole = None,
        request_id: str = None,
    ):
        self.role = role
        self.request_id = request_id

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            temp_model = UpdateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRoleResponseBody = None,
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
            temp_model = UpdateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        new_user_name: str = None,
        new_display_name: str = None,
        new_mobile_phone: str = None,
        new_email: str = None,
        new_comments: str = None,
    ):
        self.user_name = user_name
        self.new_user_name = new_user_name
        self.new_display_name = new_display_name
        self.new_mobile_phone = new_mobile_phone
        self.new_email = new_email
        self.new_comments = new_comments

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.new_user_name is not None:
            result['NewUserName'] = self.new_user_name
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_mobile_phone is not None:
            result['NewMobilePhone'] = self.new_mobile_phone
        if self.new_email is not None:
            result['NewEmail'] = self.new_email
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('NewUserName') is not None:
            self.new_user_name = m.get('NewUserName')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewMobilePhone') is not None:
            self.new_mobile_phone = m.get('NewMobilePhone')
        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        return self


class UpdateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        update_date: str = None,
        mobile_phone: str = None,
        user_id: str = None,
        comments: str = None,
        create_date: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.update_date = update_date
        self.mobile_phone = mobile_phone
        self.user_id = user_id
        self.comments = comments
        self.create_date = create_date
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        user: UpdateUserResponseBodyUser = None,
        request_id: str = None,
    ):
        self.user = user
        self.request_id = request_id

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = UpdateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


