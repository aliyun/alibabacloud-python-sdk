# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddExternalSAMLIdPCertificateRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        x_509certificate: str = None,
    ):
        self.directory_id = directory_id
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class AddExternalSAMLIdPCertificateResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        request_id: str = None,
    ):
        self.certificate_id = certificate_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddExternalSAMLIdPCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddExternalSAMLIdPCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddExternalSAMLIdPCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPermissionPolicyToAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        inline_policy_document: str = None,
        permission_policy_name: str = None,
        permission_policy_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.inline_policy_document = inline_policy_document
        self.permission_policy_name = permission_policy_name
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.inline_policy_document is not None:
            result['InlinePolicyDocument'] = self.inline_policy_document
        if self.permission_policy_name is not None:
            result['PermissionPolicyName'] = self.permission_policy_name
        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('InlinePolicyDocument') is not None:
            self.inline_policy_document = m.get('InlinePolicyDocument')
        if m.get('PermissionPolicyName') is not None:
            self.permission_policy_name = m.get('PermissionPolicyName')
        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')
        return self


class AddPermissionPolicyToAccessConfigurationResponseBody(TeaModel):
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


class AddPermissionPolicyToAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddPermissionPolicyToAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddPermissionPolicyToAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToGroupRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.group_id = group_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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


class AddUserToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserToGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddUserToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearExternalSAMLIdentityProviderRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class ClearExternalSAMLIdentityProviderResponseBody(TeaModel):
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


class ClearExternalSAMLIdentityProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClearExternalSAMLIdentityProviderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ClearExternalSAMLIdentityProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessAssignmentRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.principal_id = principal_id
        self.principal_type = principal_type
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateAccessAssignmentResponseBodyTask(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.principal_id = principal_id
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class CreateAccessAssignmentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: CreateAccessAssignmentResponseBodyTask = None,
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
            result['RequestId'] = self.request_id
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Task') is not None:
            temp_model = CreateAccessAssignmentResponseBodyTask()
            self.task = temp_model.from_map(m['Task'])
        return self


class CreateAccessAssignmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessAssignmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateAccessAssignmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_name: str = None,
        description: str = None,
        directory_id: str = None,
        relay_state: str = None,
        session_duration: int = None,
    ):
        self.access_configuration_name = access_configuration_name
        self.description = description
        self.directory_id = directory_id
        self.relay_state = relay_state
        self.session_duration = session_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.relay_state is not None:
            result['RelayState'] = self.relay_state
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        return self


class CreateAccessConfigurationResponseBodyAccessConfiguration(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        relay_state: str = None,
        session_duration: int = None,
        status_notifications: List[str] = None,
        update_time: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.create_time = create_time
        self.description = description
        self.relay_state = relay_state
        self.session_duration = session_duration
        self.status_notifications = status_notifications
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.relay_state is not None:
            result['RelayState'] = self.relay_state
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateAccessConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        access_configuration: CreateAccessConfigurationResponseBodyAccessConfiguration = None,
        request_id: str = None,
    ):
        self.access_configuration = access_configuration
        self.request_id = request_id

    def validate(self):
        if self.access_configuration:
            self.access_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration is not None:
            result['AccessConfiguration'] = self.access_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfiguration') is not None:
            temp_model = CreateAccessConfigurationResponseBodyAccessConfiguration()
            self.access_configuration = temp_model.from_map(m['AccessConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDirectoryRequest(TeaModel):
    def __init__(
        self,
        directory_name: str = None,
    ):
        self.directory_name = directory_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        return self


class CreateDirectoryResponseBodyDirectory(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_name: str = None,
        region: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.region = region
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.region is not None:
            result['Region'] = self.region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        directory: CreateDirectoryResponseBodyDirectory = None,
        request_id: str = None,
    ):
        self.directory = directory
        self.request_id = request_id

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            temp_model = CreateDirectoryResponseBodyDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        group_name: str = None,
    ):
        self.description = description
        self.directory_id = directory_id
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class CreateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        provision_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.provision_type = provision_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class CreateSCIMServerCredentialRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class CreateSCIMServerCredentialResponseBodySCIMServerCredential(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        credential_id: str = None,
        credential_secret: str = None,
        credential_type: str = None,
        directory_id: str = None,
        expire_time: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.credential_id = credential_id
        self.credential_secret = credential_secret
        self.credential_type = credential_type
        self.directory_id = directory_id
        self.expire_time = expire_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.credential_secret is not None:
            result['CredentialSecret'] = self.credential_secret
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('CredentialSecret') is not None:
            self.credential_secret = m.get('CredentialSecret')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateSCIMServerCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scimserver_credential: CreateSCIMServerCredentialResponseBodySCIMServerCredential = None,
    ):
        self.request_id = request_id
        self.scimserver_credential = scimserver_credential

    def validate(self):
        if self.scimserver_credential:
            self.scimserver_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scimserver_credential is not None:
            result['SCIMServerCredential'] = self.scimserver_credential.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SCIMServerCredential') is not None:
            temp_model = CreateSCIMServerCredentialResponseBodySCIMServerCredential()
            self.scimserver_credential = temp_model.from_map(m['SCIMServerCredential'])
        return self


class CreateSCIMServerCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSCIMServerCredentialResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateSCIMServerCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        status: str = None,
        user_name: str = None,
    ):
        self.description = description
        self.directory_id = directory_id
        self.display_name = display_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.provision_type = provision_type
        self.status = status
        self.update_time = update_time
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: CreateUserResponseBodyUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = CreateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessAssignmentRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        deprovision_strategy: str = None,
        directory_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.deprovision_strategy = deprovision_strategy
        self.directory_id = directory_id
        self.principal_id = principal_id
        self.principal_type = principal_type
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.deprovision_strategy is not None:
            result['DeprovisionStrategy'] = self.deprovision_strategy
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DeprovisionStrategy') is not None:
            self.deprovision_strategy = m.get('DeprovisionStrategy')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DeleteAccessAssignmentResponseBodyTask(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.principal_id = principal_id
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DeleteAccessAssignmentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: DeleteAccessAssignmentResponseBodyTask = None,
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
            result['RequestId'] = self.request_id
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Task') is not None:
            temp_model = DeleteAccessAssignmentResponseBodyTask()
            self.task = temp_model.from_map(m['Task'])
        return self


class DeleteAccessAssignmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessAssignmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAccessAssignmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        force_remove_permission_policies: bool = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.force_remove_permission_policies = force_remove_permission_policies

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.force_remove_permission_policies is not None:
            result['ForceRemovePermissionPolicies'] = self.force_remove_permission_policies
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ForceRemovePermissionPolicies') is not None:
            self.force_remove_permission_policies = m.get('ForceRemovePermissionPolicies')
        return self


class DeleteAccessConfigurationResponseBody(TeaModel):
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


class DeleteAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoryRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DeleteDirectoryResponseBody(TeaModel):
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


class DeleteDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
    ):
        self.directory_id = directory_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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
        status_code: int = None,
        body: DeleteGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class DeleteMFADeviceForUserRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        mfadevice_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.mfadevice_id = mfadevice_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.mfadevice_id is not None:
            result['MFADeviceId'] = self.mfadevice_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MFADeviceId') is not None:
            self.mfadevice_id = m.get('MFADeviceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteMFADeviceForUserResponseBody(TeaModel):
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


class DeleteMFADeviceForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMFADeviceForUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteMFADeviceForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSCIMServerCredentialRequest(TeaModel):
    def __init__(
        self,
        credential_id: str = None,
        directory_id: str = None,
    ):
        self.credential_id = credential_id
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DeleteSCIMServerCredentialResponseBody(TeaModel):
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


class DeleteSCIMServerCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSCIMServerCredentialResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteSCIMServerCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeprovisionAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DeprovisionAccessConfigurationResponseBodyTasks(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DeprovisionAccessConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[DeprovisionAccessConfigurationResponseBodyTasks] = None,
    ):
        self.request_id = request_id
        self.tasks = tasks

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DeprovisionAccessConfigurationResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DeprovisionAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeprovisionAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeprovisionAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableServiceResponseBody(TeaModel):
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


class DisableServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DisableServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableServiceResponseBody(TeaModel):
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


class EnableServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = EnableServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetAccessConfigurationResponseBodyAccessConfiguration(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        relay_state: str = None,
        session_duration: int = None,
        status_notifications: List[str] = None,
        update_time: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.create_time = create_time
        self.description = description
        self.relay_state = relay_state
        self.session_duration = session_duration
        self.status_notifications = status_notifications
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.relay_state is not None:
            result['RelayState'] = self.relay_state
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetAccessConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        access_configuration: GetAccessConfigurationResponseBodyAccessConfiguration = None,
        request_id: str = None,
    ):
        self.access_configuration = access_configuration
        self.request_id = request_id

    def validate(self):
        if self.access_configuration:
            self.access_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration is not None:
            result['AccessConfiguration'] = self.access_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfiguration') is not None:
            temp_model = GetAccessConfigurationResponseBodyAccessConfiguration()
            self.access_configuration = temp_model.from_map(m['AccessConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectoryRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetDirectoryResponseBodyDirectory(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_name: str = None,
        region: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.region = region
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.region is not None:
            result['Region'] = self.region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        directory: GetDirectoryResponseBodyDirectory = None,
        request_id: str = None,
    ):
        self.directory = directory
        self.request_id = request_id

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            temp_model = GetDirectoryResponseBodyDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectorySAMLServiceProviderInfoRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider(TeaModel):
    def __init__(
        self,
        acs_url: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
    ):
        self.acs_url = acs_url
        self.directory_id = directory_id
        self.encoded_metadata_document = encoded_metadata_document
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs_url is not None:
            result['AcsUrl'] = self.acs_url
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsUrl') is not None:
            self.acs_url = m.get('AcsUrl')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        return self


class GetDirectorySAMLServiceProviderInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlservice_provider: GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider = None,
    ):
        self.request_id = request_id
        self.samlservice_provider = samlservice_provider

    def validate(self):
        if self.samlservice_provider:
            self.samlservice_provider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlservice_provider is not None:
            result['SAMLServiceProvider'] = self.samlservice_provider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLServiceProvider') is not None:
            temp_model = GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider()
            self.samlservice_provider = temp_model.from_map(m['SAMLServiceProvider'])
        return self


class GetDirectorySAMLServiceProviderInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDirectorySAMLServiceProviderInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetDirectorySAMLServiceProviderInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectoryStatisticsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetDirectoryStatisticsResponseBodyDirectoryStatistics(TeaModel):
    def __init__(
        self,
        access_assignment_count: int = None,
        access_configuration_count: int = None,
        access_configuration_quota: int = None,
        directory_id: str = None,
        directory_name: str = None,
        group_count: int = None,
        group_quota: int = None,
        in_progress_task_count: int = None,
        region: str = None,
        scimserver_credential_count: int = None,
        scimsync_enabled: bool = None,
        ssoenabled: bool = None,
        user_count: int = None,
        user_quota: int = None,
    ):
        self.access_assignment_count = access_assignment_count
        self.access_configuration_count = access_configuration_count
        self.access_configuration_quota = access_configuration_quota
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.group_count = group_count
        self.group_quota = group_quota
        self.in_progress_task_count = in_progress_task_count
        self.region = region
        self.scimserver_credential_count = scimserver_credential_count
        self.scimsync_enabled = scimsync_enabled
        self.ssoenabled = ssoenabled
        self.user_count = user_count
        self.user_quota = user_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_assignment_count is not None:
            result['AccessAssignmentCount'] = self.access_assignment_count
        if self.access_configuration_count is not None:
            result['AccessConfigurationCount'] = self.access_configuration_count
        if self.access_configuration_quota is not None:
            result['AccessConfigurationQuota'] = self.access_configuration_quota
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.group_count is not None:
            result['GroupCount'] = self.group_count
        if self.group_quota is not None:
            result['GroupQuota'] = self.group_quota
        if self.in_progress_task_count is not None:
            result['InProgressTaskCount'] = self.in_progress_task_count
        if self.region is not None:
            result['Region'] = self.region
        if self.scimserver_credential_count is not None:
            result['SCIMServerCredentialCount'] = self.scimserver_credential_count
        if self.scimsync_enabled is not None:
            result['SCIMSyncEnabled'] = self.scimsync_enabled
        if self.ssoenabled is not None:
            result['SSOEnabled'] = self.ssoenabled
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.user_quota is not None:
            result['UserQuota'] = self.user_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAssignmentCount') is not None:
            self.access_assignment_count = m.get('AccessAssignmentCount')
        if m.get('AccessConfigurationCount') is not None:
            self.access_configuration_count = m.get('AccessConfigurationCount')
        if m.get('AccessConfigurationQuota') is not None:
            self.access_configuration_quota = m.get('AccessConfigurationQuota')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')
        if m.get('GroupQuota') is not None:
            self.group_quota = m.get('GroupQuota')
        if m.get('InProgressTaskCount') is not None:
            self.in_progress_task_count = m.get('InProgressTaskCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SCIMServerCredentialCount') is not None:
            self.scimserver_credential_count = m.get('SCIMServerCredentialCount')
        if m.get('SCIMSyncEnabled') is not None:
            self.scimsync_enabled = m.get('SCIMSyncEnabled')
        if m.get('SSOEnabled') is not None:
            self.ssoenabled = m.get('SSOEnabled')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('UserQuota') is not None:
            self.user_quota = m.get('UserQuota')
        return self


class GetDirectoryStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        directory_statistics: GetDirectoryStatisticsResponseBodyDirectoryStatistics = None,
        request_id: str = None,
    ):
        self.directory_statistics = directory_statistics
        self.request_id = request_id

    def validate(self):
        if self.directory_statistics:
            self.directory_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_statistics is not None:
            result['DirectoryStatistics'] = self.directory_statistics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryStatistics') is not None:
            temp_model = GetDirectoryStatisticsResponseBodyDirectoryStatistics()
            self.directory_statistics = temp_model.from_map(m['DirectoryStatistics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectoryStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDirectoryStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetDirectoryStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExternalSAMLIdentityProviderRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration(TeaModel):
    def __init__(
        self,
        certificate_ids: List[str] = None,
        create_time: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        login_url: str = None,
        ssostatus: str = None,
        update_time: str = None,
        want_request_signed: bool = None,
    ):
        self.certificate_ids = certificate_ids
        self.create_time = create_time
        self.directory_id = directory_id
        self.encoded_metadata_document = encoded_metadata_document
        self.entity_id = entity_id
        self.login_url = login_url
        self.ssostatus = ssostatus
        self.update_time = update_time
        self.want_request_signed = want_request_signed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.want_request_signed is not None:
            result['WantRequestSigned'] = self.want_request_signed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('WantRequestSigned') is not None:
            self.want_request_signed = m.get('WantRequestSigned')
        return self


class GetExternalSAMLIdentityProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlidentity_provider_configuration: GetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration = None,
    ):
        self.request_id = request_id
        self.samlidentity_provider_configuration = samlidentity_provider_configuration

    def validate(self):
        if self.samlidentity_provider_configuration:
            self.samlidentity_provider_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlidentity_provider_configuration is not None:
            result['SAMLIdentityProviderConfiguration'] = self.samlidentity_provider_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLIdentityProviderConfiguration') is not None:
            temp_model = GetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration()
            self.samlidentity_provider_configuration = temp_model.from_map(m['SAMLIdentityProviderConfiguration'])
        return self


class GetExternalSAMLIdentityProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExternalSAMLIdentityProviderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetExternalSAMLIdentityProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
    ):
        self.directory_id = directory_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        provision_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.provision_type = provision_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        status_code: int = None,
        body: GetGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class GetMFAAuthenticationSettingsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetMFAAuthenticationSettingsResponseBody(TeaModel):
    def __init__(
        self,
        mfaauthentication_advance_settings: str = None,
        request_id: str = None,
    ):
        self.mfaauthentication_advance_settings = mfaauthentication_advance_settings
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfaauthentication_advance_settings is not None:
            result['MFAAuthenticationAdvanceSettings'] = self.mfaauthentication_advance_settings
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFAAuthenticationAdvanceSettings') is not None:
            self.mfaauthentication_advance_settings = m.get('MFAAuthenticationAdvanceSettings')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMFAAuthenticationSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMFAAuthenticationSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetMFAAuthenticationSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMFAAuthenticationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetMFAAuthenticationStatusResponseBody(TeaModel):
    def __init__(
        self,
        mfaauthentication_status: str = None,
        request_id: str = None,
    ):
        self.mfaauthentication_status = mfaauthentication_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfaauthentication_status is not None:
            result['MFAAuthenticationStatus'] = self.mfaauthentication_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFAAuthenticationStatus') is not None:
            self.mfaauthentication_status = m.get('MFAAuthenticationStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMFAAuthenticationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMFAAuthenticationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetMFAAuthenticationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSCIMSynchronizationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetSCIMSynchronizationStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scimsynchronization_status: str = None,
    ):
        self.request_id = request_id
        self.scimsynchronization_status = scimsynchronization_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scimsynchronization_status is not None:
            result['SCIMSynchronizationStatus'] = self.scimsynchronization_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SCIMSynchronizationStatus') is not None:
            self.scimsynchronization_status = m.get('SCIMSynchronizationStatus')
        return self


class GetSCIMSynchronizationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSCIMSynchronizationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetSCIMSynchronizationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceStatusResponseBodyServiceStatus(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        prerequisite_check_result: str = None,
        regions_in_use: List[str] = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.prerequisite_check_result = prerequisite_check_result
        self.regions_in_use = regions_in_use
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.prerequisite_check_result is not None:
            result['PrerequisiteCheckResult'] = self.prerequisite_check_result
        if self.regions_in_use is not None:
            result['RegionsInUse'] = self.regions_in_use
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('PrerequisiteCheckResult') is not None:
            self.prerequisite_check_result = m.get('PrerequisiteCheckResult')
        if m.get('RegionsInUse') is not None:
            self.regions_in_use = m.get('RegionsInUse')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_status: GetServiceStatusResponseBodyServiceStatus = None,
    ):
        self.request_id = request_id
        self.service_status = service_status

    def validate(self):
        if self.service_status:
            self.service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            temp_model = GetServiceStatusResponseBodyServiceStatus()
            self.service_status = temp_model.from_map(m['ServiceStatus'])
        return self


class GetServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        task_id: str = None,
    ):
        self.directory_id = directory_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        end_time: str = None,
        failure_reason: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        start_time: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.end_time = end_time
        self.failure_reason = failure_reason
        self.principal_id = principal_id
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.start_time = start_time
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetTaskResponseBodyTask = None,
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
            result['RequestId'] = self.request_id
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['Task'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        task_id: str = None,
    ):
        self.directory_id = directory_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskStatusResponseBodyTaskStatus(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        failure_reason: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.end_time = end_time
        self.failure_reason = failure_reason
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_status: GetTaskStatusResponseBodyTaskStatus = None,
    ):
        self.request_id = request_id
        self.task_status = task_status

    def validate(self):
        if self.task_status:
            self.task_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            temp_model = GetTaskStatusResponseBodyTaskStatus()
            self.task_status = temp_model.from_map(m['TaskStatus'])
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.provision_type = provision_type
        self.status = status
        self.update_time = update_time
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: GetUserResponseBodyUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserMFAAuthenticationSettingsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserMFAAuthenticationSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_mfaauthentication_settings: str = None,
    ):
        self.request_id = request_id
        self.user_mfaauthentication_settings = user_mfaauthentication_settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_mfaauthentication_settings is not None:
            result['UserMFAAuthenticationSettings'] = self.user_mfaauthentication_settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserMFAAuthenticationSettings') is not None:
            self.user_mfaauthentication_settings = m.get('UserMFAAuthenticationSettings')
        return self


class GetUserMFAAuthenticationSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserMFAAuthenticationSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetUserMFAAuthenticationSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessAssignmentsRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.max_results = max_results
        self.next_token = next_token
        self.principal_id = principal_id
        self.principal_type = principal_type
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListAccessAssignmentsResponseBodyAccessAssignments(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.create_time = create_time
        self.principal_id = principal_id
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListAccessAssignmentsResponseBody(TeaModel):
    def __init__(
        self,
        access_assignments: List[ListAccessAssignmentsResponseBodyAccessAssignments] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.access_assignments = access_assignments
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.access_assignments:
            for k in self.access_assignments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessAssignments'] = []
        if self.access_assignments is not None:
            for k in self.access_assignments:
                result['AccessAssignments'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_assignments = []
        if m.get('AccessAssignments') is not None:
            for k in m.get('AccessAssignments'):
                temp_model = ListAccessAssignmentsResponseBodyAccessAssignments()
                self.access_assignments.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListAccessAssignmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessAssignmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAccessAssignmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessConfigurationProvisioningsRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        provisioning_status: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.max_results = max_results
        self.next_token = next_token
        self.provisioning_status = provisioning_status
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.provisioning_status is not None:
            result['ProvisioningStatus'] = self.provisioning_status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProvisioningStatus') is not None:
            self.provisioning_status = m.get('ProvisioningStatus')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListAccessConfigurationProvisioningsResponseBodyAccessConfigurationProvisionings(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        rampolicy_names: List[str] = None,
        ramrole_name: str = None,
        samlprovider_name: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        update_time: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.create_time = create_time
        self.rampolicy_names = rampolicy_names
        self.ramrole_name = ramrole_name
        self.samlprovider_name = samlprovider_name
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rampolicy_names is not None:
            result['RAMPolicyNames'] = self.rampolicy_names
        if self.ramrole_name is not None:
            result['RAMRoleName'] = self.ramrole_name
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RAMPolicyNames') is not None:
            self.rampolicy_names = m.get('RAMPolicyNames')
        if m.get('RAMRoleName') is not None:
            self.ramrole_name = m.get('RAMRoleName')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListAccessConfigurationProvisioningsResponseBody(TeaModel):
    def __init__(
        self,
        access_configuration_provisionings: List[ListAccessConfigurationProvisioningsResponseBodyAccessConfigurationProvisionings] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.access_configuration_provisionings = access_configuration_provisionings
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.access_configuration_provisionings:
            for k in self.access_configuration_provisionings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessConfigurationProvisionings'] = []
        if self.access_configuration_provisionings is not None:
            for k in self.access_configuration_provisionings:
                result['AccessConfigurationProvisionings'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_configuration_provisionings = []
        if m.get('AccessConfigurationProvisionings') is not None:
            for k in m.get('AccessConfigurationProvisionings'):
                temp_model = ListAccessConfigurationProvisioningsResponseBodyAccessConfigurationProvisionings()
                self.access_configuration_provisionings.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListAccessConfigurationProvisioningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessConfigurationProvisioningsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAccessConfigurationProvisioningsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessConfigurationsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        status_notifications: str = None,
    ):
        self.directory_id = directory_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.status_notifications = status_notifications

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')
        return self


class ListAccessConfigurationsResponseBodyAccessConfigurations(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        relay_state: str = None,
        session_duration: int = None,
        status_notifications: List[str] = None,
        update_time: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.create_time = create_time
        self.description = description
        self.relay_state = relay_state
        self.session_duration = session_duration
        self.status_notifications = status_notifications
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.relay_state is not None:
            result['RelayState'] = self.relay_state
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListAccessConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        access_configurations: List[ListAccessConfigurationsResponseBodyAccessConfigurations] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.access_configurations = access_configurations
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.access_configurations:
            for k in self.access_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessConfigurations'] = []
        if self.access_configurations is not None:
            for k in self.access_configurations:
                result['AccessConfigurations'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_configurations = []
        if m.get('AccessConfigurations') is not None:
            for k in m.get('AccessConfigurations'):
                temp_model = ListAccessConfigurationsResponseBodyAccessConfigurations()
                self.access_configurations.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListAccessConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAccessConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_name: str = None,
        region: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.region = region
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.region is not None:
            result['Region'] = self.region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        directories: List[ListDirectoriesResponseBodyDirectories] = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.directories = directories
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = ListDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDirectoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExternalSAMLIdPCertificatesRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class ListExternalSAMLIdPCertificatesResponseBodySAMLIdPCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        issuer: str = None,
        not_after: str = None,
        not_before: str = None,
        public_key: str = None,
        serial_number: str = None,
        signature_algorithm: str = None,
        subject: str = None,
        version: int = None,
        x_509certificate: str = None,
    ):
        self.certificate_id = certificate_id
        self.issuer = issuer
        self.not_after = not_after
        self.not_before = not_before
        self.public_key = public_key
        self.serial_number = serial_number
        self.signature_algorithm = signature_algorithm
        self.subject = subject
        self.version = version
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.version is not None:
            result['Version'] = self.version
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class ListExternalSAMLIdPCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlid_pcertificates: List[ListExternalSAMLIdPCertificatesResponseBodySAMLIdPCertificates] = None,
        total_counts: int = None,
    ):
        self.request_id = request_id
        self.samlid_pcertificates = samlid_pcertificates
        self.total_counts = total_counts

    def validate(self):
        if self.samlid_pcertificates:
            for k in self.samlid_pcertificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SAMLIdPCertificates'] = []
        if self.samlid_pcertificates is not None:
            for k in self.samlid_pcertificates:
                result['SAMLIdPCertificates'].append(k.to_map() if k else None)
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.samlid_pcertificates = []
        if m.get('SAMLIdPCertificates') is not None:
            for k in m.get('SAMLIdPCertificates'):
                temp_model = ListExternalSAMLIdPCertificatesResponseBodySAMLIdPCertificates()
                self.samlid_pcertificates.append(temp_model.from_map(k))
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListExternalSAMLIdPCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExternalSAMLIdPCertificatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListExternalSAMLIdPCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupMembersRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.directory_id = directory_id
        self.group_id = group_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListGroupMembersResponseBodyGroupMembers(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        email: str = None,
        group_id: str = None,
        join_time: str = None,
        provision_type: str = None,
        status: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.email = email
        self.group_id = group_id
        self.join_time = join_time
        self.provision_type = provision_type
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        group_members: List[ListGroupMembersResponseBodyGroupMembers] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.group_members = group_members
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.group_members:
            for k in self.group_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupMembers'] = []
        if self.group_members is not None:
            for k in self.group_members:
                result['GroupMembers'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_members = []
        if m.get('GroupMembers') is not None:
            for k in m.get('GroupMembers'):
                temp_model = ListGroupMembersResponseBodyGroupMembers()
                self.group_members.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        provision_type: str = None,
    ):
        self.directory_id = directory_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.provision_type = provision_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        return self


class ListGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        provision_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.provision_type = provision_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        groups: List[ListGroupsResponseBodyGroups] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.groups = groups
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts

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
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJoinedGroupsForUserRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.max_results = max_results
        self.next_token = next_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListJoinedGroupsForUserResponseBodyJoinedGroups(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        join_time: str = None,
        provision_type: str = None,
        user_id: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.join_time = join_time
        self.provision_type = provision_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListJoinedGroupsForUserResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        joined_groups: List[ListJoinedGroupsForUserResponseBodyJoinedGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.is_truncated = is_truncated
        self.joined_groups = joined_groups
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.joined_groups:
            for k in self.joined_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        result['JoinedGroups'] = []
        if self.joined_groups is not None:
            for k in self.joined_groups:
                result['JoinedGroups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        self.joined_groups = []
        if m.get('JoinedGroups') is not None:
            for k in m.get('JoinedGroups'):
                temp_model = ListJoinedGroupsForUserResponseBodyJoinedGroups()
                self.joined_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListJoinedGroupsForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJoinedGroupsForUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListJoinedGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMFADevicesForUserRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListMFADevicesForUserResponseBodyMFADevices(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_name: str = None,
        device_type: str = None,
        effective_time: str = None,
        user_id: str = None,
    ):
        self.device_id = device_id
        self.device_name = device_name
        self.device_type = device_type
        self.effective_time = effective_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListMFADevicesForUserResponseBody(TeaModel):
    def __init__(
        self,
        mfadevices: List[ListMFADevicesForUserResponseBodyMFADevices] = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.mfadevices = mfadevices
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.mfadevices:
            for k in self.mfadevices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MFADevices'] = []
        if self.mfadevices is not None:
            for k in self.mfadevices:
                result['MFADevices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mfadevices = []
        if m.get('MFADevices') is not None:
            for k in m.get('MFADevices'):
                temp_model = ListMFADevicesForUserResponseBodyMFADevices()
                self.mfadevices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListMFADevicesForUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMFADevicesForUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListMFADevicesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionPoliciesInAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        permission_policy_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')
        return self


class ListPermissionPoliciesInAccessConfigurationResponseBodyPermissionPolicies(TeaModel):
    def __init__(
        self,
        add_time: str = None,
        permission_policy_document: str = None,
        permission_policy_name: str = None,
        permission_policy_type: str = None,
    ):
        self.add_time = add_time
        self.permission_policy_document = permission_policy_document
        self.permission_policy_name = permission_policy_name
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.permission_policy_document is not None:
            result['PermissionPolicyDocument'] = self.permission_policy_document
        if self.permission_policy_name is not None:
            result['PermissionPolicyName'] = self.permission_policy_name
        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('PermissionPolicyDocument') is not None:
            self.permission_policy_document = m.get('PermissionPolicyDocument')
        if m.get('PermissionPolicyName') is not None:
            self.permission_policy_name = m.get('PermissionPolicyName')
        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')
        return self


class ListPermissionPoliciesInAccessConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        permission_policies: List[ListPermissionPoliciesInAccessConfigurationResponseBodyPermissionPolicies] = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.permission_policies = permission_policies
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.permission_policies:
            for k in self.permission_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PermissionPolicies'] = []
        if self.permission_policies is not None:
            for k in self.permission_policies:
                result['PermissionPolicies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permission_policies = []
        if m.get('PermissionPolicies') is not None:
            for k in m.get('PermissionPolicies'):
                temp_model = ListPermissionPoliciesInAccessConfigurationResponseBodyPermissionPolicies()
                self.permission_policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListPermissionPoliciesInAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPermissionPoliciesInAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListPermissionPoliciesInAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSCIMServerCredentialsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class ListSCIMServerCredentialsResponseBodySCIMServerCredentials(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        credential_id: str = None,
        credential_type: str = None,
        directory_id: str = None,
        expire_time: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.credential_id = credential_id
        self.credential_type = credential_type
        self.directory_id = directory_id
        self.expire_time = expire_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSCIMServerCredentialsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scimserver_credentials: List[ListSCIMServerCredentialsResponseBodySCIMServerCredentials] = None,
        total_counts: int = None,
    ):
        self.request_id = request_id
        self.scimserver_credentials = scimserver_credentials
        self.total_counts = total_counts

    def validate(self):
        if self.scimserver_credentials:
            for k in self.scimserver_credentials:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SCIMServerCredentials'] = []
        if self.scimserver_credentials is not None:
            for k in self.scimserver_credentials:
                result['SCIMServerCredentials'].append(k.to_map() if k else None)
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scimserver_credentials = []
        if m.get('SCIMServerCredentials') is not None:
            for k in m.get('SCIMServerCredentials'):
                temp_model = ListSCIMServerCredentialsResponseBodySCIMServerCredentials()
                self.scimserver_credentials.append(temp_model.from_map(k))
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        return self


class ListSCIMServerCredentialsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSCIMServerCredentialsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListSCIMServerCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        principal_id: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_type: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.principal_id = principal_id
        self.principal_type = principal_type
        self.status = status
        self.target_id = target_id
        self.target_type = target_type
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        end_time: str = None,
        failure_reason: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        start_time: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.end_time = end_time
        self.failure_reason = failure_reason
        self.principal_id = principal_id
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.start_time = start_time
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tasks: List[ListTasksResponseBodyTasks] = None,
        total_counts: int = None,
    ):
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.tasks = tasks
        self.total_counts = total_counts

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
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        provision_type: str = None,
        status: str = None,
    ):
        self.directory_id = directory_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.provision_type = provision_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.provision_type = provision_type
        self.status = status
        self.update_time = update_time
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
        users: List[ListUsersResponseBodyUsers] = None,
    ):
        self.is_truncated = is_truncated
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_counts = total_counts
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProvisionAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ProvisionAccessConfigurationResponseBodyTasks(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.status = status
        self.target_id = target_id
        self.target_name = target_name
        self.target_path = target_path
        self.target_path_name = target_path_name
        self.target_type = target_type
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.status is not None:
            result['Status'] = self.status
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ProvisionAccessConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[ProvisionAccessConfigurationResponseBodyTasks] = None,
    ):
        self.request_id = request_id
        self.tasks = tasks

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ProvisionAccessConfigurationResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ProvisionAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProvisionAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ProvisionAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveExternalSAMLIdPCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        directory_id: str = None,
    ):
        self.certificate_id = certificate_id
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class RemoveExternalSAMLIdPCertificateResponseBody(TeaModel):
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


class RemoveExternalSAMLIdPCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveExternalSAMLIdPCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveExternalSAMLIdPCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemovePermissionPolicyFromAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        permission_policy_name: str = None,
        permission_policy_type: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.permission_policy_name = permission_policy_name
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.permission_policy_name is not None:
            result['PermissionPolicyName'] = self.permission_policy_name
        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('PermissionPolicyName') is not None:
            self.permission_policy_name = m.get('PermissionPolicyName')
        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')
        return self


class RemovePermissionPolicyFromAccessConfigurationResponseBody(TeaModel):
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


class RemovePermissionPolicyFromAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemovePermissionPolicyFromAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemovePermissionPolicyFromAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.group_id = group_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserFromGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveUserFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetUserPasswordRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        generate_random_password: bool = None,
        password: str = None,
        require_password_reset_for_next_login: bool = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.generate_random_password = generate_random_password
        self.password = password
        self.require_password_reset_for_next_login = require_password_reset_for_next_login
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.generate_random_password is not None:
            result['GenerateRandomPassword'] = self.generate_random_password
        if self.password is not None:
            result['Password'] = self.password
        if self.require_password_reset_for_next_login is not None:
            result['RequirePasswordResetForNextLogin'] = self.require_password_reset_for_next_login
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GenerateRandomPassword') is not None:
            self.generate_random_password = m.get('GenerateRandomPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RequirePasswordResetForNextLogin') is not None:
            self.require_password_reset_for_next_login = m.get('RequirePasswordResetForNextLogin')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ResetUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        new_password: str = None,
        request_id: str = None,
    ):
        self.new_password = new_password
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetUserPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ResetUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetExternalSAMLIdentityProviderRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        login_url: str = None,
        ssostatus: str = None,
        want_request_signed: bool = None,
        x_509certificate: str = None,
    ):
        self.directory_id = directory_id
        self.encoded_metadata_document = encoded_metadata_document
        self.entity_id = entity_id
        self.login_url = login_url
        self.ssostatus = ssostatus
        self.want_request_signed = want_request_signed
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus
        if self.want_request_signed is not None:
            result['WantRequestSigned'] = self.want_request_signed
        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')
        if m.get('WantRequestSigned') is not None:
            self.want_request_signed = m.get('WantRequestSigned')
        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')
        return self


class SetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration(TeaModel):
    def __init__(
        self,
        certificate_ids: List[str] = None,
        create_time: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        login_url: str = None,
        ssostatus: str = None,
        update_time: str = None,
        want_request_signed: bool = None,
    ):
        self.certificate_ids = certificate_ids
        self.create_time = create_time
        self.directory_id = directory_id
        self.encoded_metadata_document = encoded_metadata_document
        self.entity_id = entity_id
        self.login_url = login_url
        self.ssostatus = ssostatus
        self.update_time = update_time
        self.want_request_signed = want_request_signed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.want_request_signed is not None:
            result['WantRequestSigned'] = self.want_request_signed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('WantRequestSigned') is not None:
            self.want_request_signed = m.get('WantRequestSigned')
        return self


class SetExternalSAMLIdentityProviderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlidentity_provider_configuration: SetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration = None,
    ):
        self.request_id = request_id
        self.samlidentity_provider_configuration = samlidentity_provider_configuration

    def validate(self):
        if self.samlidentity_provider_configuration:
            self.samlidentity_provider_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlidentity_provider_configuration is not None:
            result['SAMLIdentityProviderConfiguration'] = self.samlidentity_provider_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLIdentityProviderConfiguration') is not None:
            temp_model = SetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration()
            self.samlidentity_provider_configuration = temp_model.from_map(m['SAMLIdentityProviderConfiguration'])
        return self


class SetExternalSAMLIdentityProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetExternalSAMLIdentityProviderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetExternalSAMLIdentityProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMFAAuthenticationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        mfaauthentication_status: str = None,
    ):
        self.directory_id = directory_id
        self.mfaauthentication_status = mfaauthentication_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.mfaauthentication_status is not None:
            result['MFAAuthenticationStatus'] = self.mfaauthentication_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MFAAuthenticationStatus') is not None:
            self.mfaauthentication_status = m.get('MFAAuthenticationStatus')
        return self


class SetMFAAuthenticationStatusResponseBody(TeaModel):
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


class SetMFAAuthenticationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetMFAAuthenticationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetMFAAuthenticationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSCIMSynchronizationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        scimsynchronization_status: str = None,
    ):
        self.directory_id = directory_id
        self.scimsynchronization_status = scimsynchronization_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.scimsynchronization_status is not None:
            result['SCIMSynchronizationStatus'] = self.scimsynchronization_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('SCIMSynchronizationStatus') is not None:
            self.scimsynchronization_status = m.get('SCIMSynchronizationStatus')
        return self


class SetSCIMSynchronizationStatusResponseBody(TeaModel):
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


class SetSCIMSynchronizationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSCIMSynchronizationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetSCIMSynchronizationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        new_description: str = None,
        new_relay_state: str = None,
        new_session_duration: int = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.new_description = new_description
        self.new_relay_state = new_relay_state
        self.new_session_duration = new_session_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_relay_state is not None:
            result['NewRelayState'] = self.new_relay_state
        if self.new_session_duration is not None:
            result['NewSessionDuration'] = self.new_session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewRelayState') is not None:
            self.new_relay_state = m.get('NewRelayState')
        if m.get('NewSessionDuration') is not None:
            self.new_session_duration = m.get('NewSessionDuration')
        return self


class UpdateAccessConfigurationResponseBodyAccessConfiguration(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        relay_state: str = None,
        session_duration: int = None,
        status_notifications: List[str] = None,
        update_time: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.access_configuration_name = access_configuration_name
        self.create_time = create_time
        self.description = description
        self.relay_state = relay_state
        self.session_duration = session_duration
        self.status_notifications = status_notifications
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.relay_state is not None:
            result['RelayState'] = self.relay_state
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateAccessConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        access_configuration: UpdateAccessConfigurationResponseBodyAccessConfiguration = None,
        request_id: str = None,
    ):
        self.access_configuration = access_configuration
        self.request_id = request_id

    def validate(self):
        if self.access_configuration:
            self.access_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration is not None:
            result['AccessConfiguration'] = self.access_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfiguration') is not None:
            temp_model = UpdateAccessConfigurationResponseBodyAccessConfiguration()
            self.access_configuration = temp_model.from_map(m['AccessConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDirectoryRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        new_directory_name: str = None,
    ):
        self.directory_id = directory_id
        self.new_directory_name = new_directory_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_directory_name is not None:
            result['NewDirectoryName'] = self.new_directory_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewDirectoryName') is not None:
            self.new_directory_name = m.get('NewDirectoryName')
        return self


class UpdateDirectoryResponseBodyDirectory(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_name: str = None,
        region: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.region = region
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.region is not None:
            result['Region'] = self.region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        directory: UpdateDirectoryResponseBodyDirectory = None,
        request_id: str = None,
    ):
        self.directory = directory
        self.request_id = request_id

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            temp_model = UpdateDirectoryResponseBodyDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
        new_description: str = None,
        new_group_name: str = None,
    ):
        self.directory_id = directory_id
        self.group_id = group_id
        self.new_description = new_description
        self.new_group_name = new_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        return self


class UpdateGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        provision_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.provision_type = provision_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UpdateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class UpdateInlinePolicyForAccessConfigurationRequest(TeaModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        inline_policy_name: str = None,
        new_inline_policy_document: str = None,
    ):
        self.access_configuration_id = access_configuration_id
        self.directory_id = directory_id
        self.inline_policy_name = inline_policy_name
        self.new_inline_policy_document = new_inline_policy_document

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.inline_policy_name is not None:
            result['InlinePolicyName'] = self.inline_policy_name
        if self.new_inline_policy_document is not None:
            result['NewInlinePolicyDocument'] = self.new_inline_policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('InlinePolicyName') is not None:
            self.inline_policy_name = m.get('InlinePolicyName')
        if m.get('NewInlinePolicyDocument') is not None:
            self.new_inline_policy_document = m.get('NewInlinePolicyDocument')
        return self


class UpdateInlinePolicyForAccessConfigurationResponseBody(TeaModel):
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


class UpdateInlinePolicyForAccessConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInlinePolicyForAccessConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateInlinePolicyForAccessConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMFAAuthenticationSettingsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        mfaauthentication_settings: str = None,
        operation_for_risk_login: str = None,
    ):
        self.directory_id = directory_id
        self.mfaauthentication_settings = mfaauthentication_settings
        self.operation_for_risk_login = operation_for_risk_login

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.mfaauthentication_settings is not None:
            result['MFAAuthenticationSettings'] = self.mfaauthentication_settings
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MFAAuthenticationSettings') is not None:
            self.mfaauthentication_settings = m.get('MFAAuthenticationSettings')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        return self


class UpdateMFAAuthenticationSettingsResponseBody(TeaModel):
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


class UpdateMFAAuthenticationSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMFAAuthenticationSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateMFAAuthenticationSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSCIMServerCredentialStatusRequest(TeaModel):
    def __init__(
        self,
        credential_id: str = None,
        directory_id: str = None,
        new_status: str = None,
    ):
        self.credential_id = credential_id
        self.directory_id = directory_id
        self.new_status = new_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_status is not None:
            result['NewStatus'] = self.new_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewStatus') is not None:
            self.new_status = m.get('NewStatus')
        return self


class UpdateSCIMServerCredentialStatusResponseBodySCIMServerCredential(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        credential_id: str = None,
        credential_type: str = None,
        directory_id: str = None,
        expire_time: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.credential_id = credential_id
        self.credential_type = credential_type
        self.directory_id = directory_id
        self.expire_time = expire_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateSCIMServerCredentialStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scimserver_credential: UpdateSCIMServerCredentialStatusResponseBodySCIMServerCredential = None,
    ):
        self.request_id = request_id
        self.scimserver_credential = scimserver_credential

    def validate(self):
        if self.scimserver_credential:
            self.scimserver_credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scimserver_credential is not None:
            result['SCIMServerCredential'] = self.scimserver_credential.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SCIMServerCredential') is not None:
            temp_model = UpdateSCIMServerCredentialStatusResponseBodySCIMServerCredential()
            self.scimserver_credential = temp_model.from_map(m['SCIMServerCredential'])
        return self


class UpdateSCIMServerCredentialStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSCIMServerCredentialStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateSCIMServerCredentialStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        new_description: str = None,
        new_display_name: str = None,
        new_email: str = None,
        new_first_name: str = None,
        new_last_name: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.new_description = new_description
        self.new_display_name = new_display_name
        self.new_email = new_email
        self.new_first_name = new_first_name
        self.new_last_name = new_last_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_email is not None:
            result['NewEmail'] = self.new_email
        if self.new_first_name is not None:
            result['NewFirstName'] = self.new_first_name
        if self.new_last_name is not None:
            result['NewLastName'] = self.new_last_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')
        if m.get('NewFirstName') is not None:
            self.new_first_name = m.get('NewFirstName')
        if m.get('NewLastName') is not None:
            self.new_last_name = m.get('NewLastName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.provision_type = provision_type
        self.status = status
        self.update_time = update_time
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user: UpdateUserResponseBodyUser = None,
    ):
        self.request_id = request_id
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = UpdateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserMFAAuthenticationSettingsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
        user_mfaauthentication_settings: str = None,
    ):
        self.directory_id = directory_id
        self.user_id = user_id
        self.user_mfaauthentication_settings = user_mfaauthentication_settings

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_mfaauthentication_settings is not None:
            result['UserMFAAuthenticationSettings'] = self.user_mfaauthentication_settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserMFAAuthenticationSettings') is not None:
            self.user_mfaauthentication_settings = m.get('UserMFAAuthenticationSettings')
        return self


class UpdateUserMFAAuthenticationSettingsResponseBody(TeaModel):
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


class UpdateUserMFAAuthenticationSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserMFAAuthenticationSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateUserMFAAuthenticationSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        new_status: str = None,
        user_id: str = None,
    ):
        self.directory_id = directory_id
        self.new_status = new_status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_status is not None:
            result['NewStatus'] = self.new_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewStatus') is not None:
            self.new_status = m.get('NewStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserStatusResponseBody(TeaModel):
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


class UpdateUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


