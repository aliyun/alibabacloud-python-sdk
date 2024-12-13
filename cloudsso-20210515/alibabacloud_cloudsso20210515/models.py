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
        # The ID of the directory.
        self.directory_id = directory_id
        # The X.509 certificate in the PEM format.
        # 
        # The certificate is provided by the SAML IdP.
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
        # The ID of the SAML signing certificate.
        self.certificate_id = certificate_id
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The configurations of the inline policy.
        # 
        # The value can be up to 4,096 characters in length.
        # 
        # If you set `PermissionPolicyType` to `Inline`, you must specify this parameter. For more information about the syntax and structure of RAM policies, see [Policy syntax and structure](https://help.aliyun.com/document_detail/93739.html).
        self.inline_policy_document = inline_policy_document
        # The name of the policy.
        # 
        # *   If you set `PermissionPolicyType` to `System`, you must set this parameter to the name of the system policy. You can obtain the name of the system policy from RAM.
        # *   If you set `PermissionPolicyType` to `Inline`, you must set this parameter to the name of the inline policy. A custom value is supported.
        self.permission_policy_name = permission_policy_name
        # The type of the policy. Valid values:
        # 
        # *   System: system policy. Resource Access Management (RAM) system policies are reused.
        # *   Inline: inline policy. Inline policies are created based on the RAM policy syntax and structure.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the group.
        self.group_id = group_id
        # The ID of the user.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the CloudSSO identity.
        # 
        # *   If you set `PrincipalType` to `User`, set `PrincipalId` to the ID of the CloudSSO user.
        # *   If you set `PrincipalType` to `Group`, set `PrincipalId` to the ID of the CloudSSO group.
        self.principal_id = principal_id
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The ID of the task object.
        self.target_id = target_id
        # The type of the task object. Set the value to RD-Account, which specifies the accounts in the resource directory.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object. The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The ID of the job.
        self.task_id = task_id
        # The task type. The value is fixed as CreateAccessAssignment, which indicates that access permissions on an account in your resource directory are assigned.
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
        # The request ID.
        self.request_id = request_id
        # The queried task.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The name of the access configuration.
        # 
        # The name can contain letters, digits, and hyphens (-).
        # 
        # The name can be up to 32 characters in length.
        self.access_configuration_name = access_configuration_name
        # The description of the access configuration.
        # 
        # The description can be up to 1,024 characters in length.
        self.description = description
        # The ID of the directory.
        self.directory_id = directory_id
        # The initial web page that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # The web page must be a page of the Alibaba Cloud Management Console. By default, this parameter is empty, which indicates that the initial web page is the homepage of the Alibaba Cloud Management Console.
        self.relay_state = relay_state
        # The duration of a session in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        # 
        # Valid values: 900 to 43200. The value 900 indicates 15 minutes. The value 43200 indicates 12 hours.
        # 
        # Default value: 3600. The value indicates 1 hour.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access configuration was created.
        self.create_time = create_time
        # The description of the access configuration.
        self.description = description
        # The initial web page that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        self.relay_state = relay_state
        # The duration of a session in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        self.session_duration = session_duration
        # The status notification.
        self.status_notifications = status_notifications
        # The time when the information about the access configuration was modified.
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
        # The information about the access configuration.
        self.access_configuration = access_configuration
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The name of the directory. The name must be globally unique.
        # 
        # The name can contain lowercase letters, digits, or hyphens (-). The name cannot start or end with a hyphen (-) and cannot contain two consecutive hyphens (-). The name cannot start with d-.
        # 
        # The name must be 2 to 64 characters in length.
        # 
        # >  If you do not specify this parameter, the value of this parameter is automatically generated by the system.
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
        # The time when the directory was created. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The region ID of the directory.
        self.region = region
        # The time when the directory was modified. The time is displayed in UTC.
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
        # The information about the directory.
        self.directory = directory
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The description of the group.
        # 
        # The description can be up to 1,024 characters in length.
        self.description = description
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the group.
        # 
        # The name can contain letters, digits, underscores (_), hyphens (-), and periods (.).
        # 
        # The name can be up to 128 characters in length.
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
        # The time when the group was created.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The type of the group. The value is fixed as Manual, which indicates that the group is manually created.
        self.provision_type = provision_type
        # The time when the information about the group was modified.
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
        # The information about the group.
        self.group = group
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The time when the SCIM credential was created.
        self.create_time = create_time
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The SCIM credential.
        # 
        # >  The SCIM credential is returned only when it is created. After the SCIM credential is created, you cannot query it. Keep the SCIM credential confidential.
        self.credential_secret = credential_secret
        # The type of the SCIM credential.
        self.credential_type = credential_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The time when the SCIM credential expires.
        self.expire_time = expire_time
        # The status of the SCIM credential. The value is fixed as Enabled, which indicates that the SCIM credential is enabled.
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
        # The ID of the request.
        self.request_id = request_id
        # The information about the SCIM credential.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The description of the user.
        # 
        # The description can be up to 1,024 characters in length.
        self.description = description
        # The ID of the directory.
        self.directory_id = directory_id
        # The display name of the user.
        # 
        # The name can be up to 256 characters in length.
        self.display_name = display_name
        # The email address of the user. The email address must be unique within the directory.
        # 
        # The email address can be up to 128 characters in length.
        self.email = email
        # The first name of the user.
        # 
        # The name can be up to 64 characters in length.
        self.first_name = first_name
        # The last name of the user.
        # 
        # The name can be up to 64 characters in length.
        self.last_name = last_name
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled. This is the default value.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The name of the user. The name must be unique within the directory. The name cannot be changed.
        # 
        # The name can contain numbers, letters, and the following special characters: `@_-.`
        # 
        # The name can be up to 64 characters in length.
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
        # The time when the user was created.
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The time when the user was modified.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id
        # The name of the user.
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
        # The ID of the request.
        self.request_id = request_id
        # The information about the user.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class CreateUserProvisioningRequest(TeaModel):
    def __init__(
        self,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If you set the `PrincipalType` parameter to `Group`, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If you set the `PrincipalType` parameter to `User`, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: The identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
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
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateUserProvisioningResponseBodyUserProvisioning(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        owner_pk: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time. The time is displayed in UTC.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: The identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The status of the RAM user provisioning. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.status = status
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The name of the object for which you create the RAM user provisioning. The value is fixed as the name of the member in the resource directory.
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the member.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time. The time is displayed in UTC.
        self.update_time = update_time
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk
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
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')
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
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class CreateUserProvisioningResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning: CreateUserProvisioningResponseBodyUserProvisioning = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user provisioning.
        self.user_provisioning = user_provisioning

    def validate(self):
        if self.user_provisioning:
            self.user_provisioning.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning is not None:
            result['UserProvisioning'] = self.user_provisioning.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioning') is not None:
            temp_model = CreateUserProvisioningResponseBodyUserProvisioning()
            self.user_provisioning = temp_model.from_map(m['UserProvisioning'])
        return self


class CreateUserProvisioningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserProvisioningResponseBody = None,
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
            temp_model = CreateUserProvisioningResponseBody()
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # Specifies whether to de-provision the access configuration when you remove the access permissions from the CloudSSO identity. The access configuration is used to assign the access permissions, and the identity is the only one that uses the access configuration and is associated with the account. Valid values:
        # 
        # *   DeprovisionForLastAccessAssignmentOnAccount: de-provisions the access configuration.
        # *   None: does not de-provision the access configuration. This is the default value.
        self.deprovision_strategy = deprovision_strategy
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the CloudSSO identity.
        # 
        # *   If you set `PrincipalType` to `User`, set `PrincipalId` to the ID of the CloudSSO user.
        # *   If you set `PrincipalType` to `Group`, set `PrincipalId` to the ID of the CloudSSO group.
        self.principal_id = principal_id
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The ID of the task object.
        self.target_id = target_id
        # The type of the task object. Set the value to RD-Account, which specifies the accounts in the resource directory.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object. The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The task ID.
        self.task_id = task_id
        # The task type. The value is fixed as DeleteAccessAssignment, which indicates that access permissions on an account in your resource directory are removed.
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
        # The request ID.
        self.request_id = request_id
        # The task information.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # Specifies whether to forcibly remove system policies and inline policies. Valid values:
        # 
        # *   true: When you delete the access configuration, the associated system policies and inline policies are forcibly removed.
        # *   false: When you delete the access configuration, the associated system policies and inline policies are not forcibly removed. This is the default value. If these policies exist in the access configuration, the deletion fails. Before you delete the access configuration, you must remove the system policies and inline policies. For more information, see [RemovePermissionPolicyFromAccessConfiguration](https://help.aliyun.com/document_detail/336904.html).
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the group.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the MFA device.
        # 
        # You can call the [ListMFADevicesForUser](https://help.aliyun.com/document_detail/333531.html) operation to query the IDs of MFA devices.
        self.mfadevice_id = mfadevice_id
        # The ID of the user.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The ID of the directory.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the user.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class DeleteUserProvisioningRequest(TeaModel):
    def __init__(
        self,
        deletion_strategy: str = None,
        directory_id: str = None,
        user_provisioning_id: str = None,
    ):
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        # 
        # >  If you do not specify this parameter, the deletion policy that is configured when you create the RAM user provisioning is used.
        self.deletion_strategy = deletion_strategy
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class DeleteUserProvisioningResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteUserProvisioningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserProvisioningResponseBody = None,
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
            temp_model = DeleteUserProvisioningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserProvisioningEventRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        event_id: str = None,
        user_provisioning_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning event.
        # 
        # You can call the [ListUserProvisioningEvents](https://help.aliyun.com/document_detail/2636305.html) operation to query the value of `EventId`.
        self.event_id = event_id
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class DeleteUserProvisioningEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteUserProvisioningEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserProvisioningEventResponseBody = None,
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
            temp_model = DeleteUserProvisioningEventResponseBody()
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The directory ID.
        self.directory_id = directory_id
        # The ID of the task object.
        self.target_id = target_id
        # The type of the task object. Set the value to RD-Account, which specifies the accounts in the resource directory.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object. The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The task ID.
        self.task_id = task_id
        # The task type. The value is fixed as DeprovisionAccessConfiguration, which indicates that the access configuration is de-provisioned.
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
        # The request ID.
        self.request_id = request_id
        # The task information.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class DisableDelegateAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the delegated administrator account of CloudSSO.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DisableDelegateAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DisableDelegateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDelegateAccountResponseBody = None,
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
            temp_model = DisableDelegateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class EnableDelegateAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the delegated administrator account of CloudSSO.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class EnableDelegateAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class EnableDelegateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableDelegateAccountResponseBody = None,
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
            temp_model = EnableDelegateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access configuration was created.
        self.create_time = create_time
        # The description of the access configuration.
        self.description = description
        # The initial web page that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        self.relay_state = relay_state
        # The duration of a session in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        self.session_duration = session_duration
        # The status notification.
        self.status_notifications = status_notifications
        # The time when the information about the access configuration was modified.
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
        # The information about the access configuration.
        self.access_configuration = access_configuration
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The time when the directory was created.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The region ID of the directory.
        self.region = region
        # The time when the directory was modified.
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
        # The information about the directory.
        self.directory = directory
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        authn_sign_algo: str = None,
        certificate_type: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        support_encrypted_assertion: bool = None,
    ):
        # The Assertion Consumer Service (ACS) URL of the SP.
        self.acs_url = acs_url
        self.authn_sign_algo = authn_sign_algo
        self.certificate_type = certificate_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the SP. The value of this parameter is Base64-encoded.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the SP.
        self.entity_id = entity_id
        self.support_encrypted_assertion = support_encrypted_assertion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs_url is not None:
            result['AcsUrl'] = self.acs_url
        if self.authn_sign_algo is not None:
            result['AuthnSignAlgo'] = self.authn_sign_algo
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.support_encrypted_assertion is not None:
            result['SupportEncryptedAssertion'] = self.support_encrypted_assertion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsUrl') is not None:
            self.acs_url = m.get('AcsUrl')
        if m.get('AuthnSignAlgo') is not None:
            self.authn_sign_algo = m.get('AuthnSignAlgo')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('SupportEncryptedAssertion') is not None:
            self.support_encrypted_assertion = m.get('SupportEncryptedAssertion')
        return self


class GetDirectorySAMLServiceProviderInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlservice_provider: GetDirectorySAMLServiceProviderInfoResponseBodySAMLServiceProvider = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the SP.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        inline_policy_per_access_configuration_quota: int = None,
        region: str = None,
        scimserver_credential_count: int = None,
        scimsync_enabled: bool = None,
        ssoenabled: bool = None,
        system_policy_per_access_configuration_quota: int = None,
        user_count: int = None,
        user_quota: int = None,
    ):
        # The number of access permissions that are assigned.
        self.access_assignment_count = access_assignment_count
        # The number of access configurations.
        self.access_configuration_count = access_configuration_count
        # The quota for access configurations.
        self.access_configuration_quota = access_configuration_quota
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The number of user groups.
        self.group_count = group_count
        # The quota for user groups.
        self.group_quota = group_quota
        # The number of tasks that are being performed.
        self.in_progress_task_count = in_progress_task_count
        # The number of inline policies that can be configured for an access configuration.
        self.inline_policy_per_access_configuration_quota = inline_policy_per_access_configuration_quota
        # The region ID of the directory.
        self.region = region
        # The number of SCIM credentials.
        self.scimserver_credential_count = scimserver_credential_count
        # Indicates whether SCIM synchronization is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.scimsync_enabled = scimsync_enabled
        # Indicates whether SSO is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.ssoenabled = ssoenabled
        # The quota for system policies that can be configured for an access configuration.
        self.system_policy_per_access_configuration_quota = system_policy_per_access_configuration_quota
        # The number of users.
        self.user_count = user_count
        # The quota for users.
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
        if self.inline_policy_per_access_configuration_quota is not None:
            result['InlinePolicyPerAccessConfigurationQuota'] = self.inline_policy_per_access_configuration_quota
        if self.region is not None:
            result['Region'] = self.region
        if self.scimserver_credential_count is not None:
            result['SCIMServerCredentialCount'] = self.scimserver_credential_count
        if self.scimsync_enabled is not None:
            result['SCIMSyncEnabled'] = self.scimsync_enabled
        if self.ssoenabled is not None:
            result['SSOEnabled'] = self.ssoenabled
        if self.system_policy_per_access_configuration_quota is not None:
            result['SystemPolicyPerAccessConfigurationQuota'] = self.system_policy_per_access_configuration_quota
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
        if m.get('InlinePolicyPerAccessConfigurationQuota') is not None:
            self.inline_policy_per_access_configuration_quota = m.get('InlinePolicyPerAccessConfigurationQuota')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SCIMServerCredentialCount') is not None:
            self.scimserver_credential_count = m.get('SCIMServerCredentialCount')
        if m.get('SCIMSyncEnabled') is not None:
            self.scimsync_enabled = m.get('SCIMSyncEnabled')
        if m.get('SSOEnabled') is not None:
            self.ssoenabled = m.get('SSOEnabled')
        if m.get('SystemPolicyPerAccessConfigurationQuota') is not None:
            self.system_policy_per_access_configuration_quota = m.get('SystemPolicyPerAccessConfigurationQuota')
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
        # The statistics of the directory.
        self.directory_statistics = directory_statistics
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        binding_type: str = None,
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
        # The Binding method for initiating a SAML request. Values:
        # 
        # - Post: Initiate the SAML request using the Post method. 
        # - Redirect: Initiate the SAML request using the Redirect method.
        self.binding_type = binding_type
        # The ID of the SAML signing certificate.
        self.certificate_ids = certificate_ids
        # The time when the IdP was configured for the first time.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the IdP. The value of this parameter is Base64-encoded.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the IdP.
        self.entity_id = entity_id
        # The logon URL of the IdP.
        self.login_url = login_url
        # The status of SSO logon. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.ssostatus = ssostatus
        # The time when the IdP configurations were last modified.
        self.update_time = update_time
        # Indicates whether CloudSSO needs to sign SAML requests. The requests are sent when users log on to the CloudSSO user portal to initiate SAML-based SSO. Valid values:
        # 
        # *   true: yes
        # *   false: no (default)
        self.want_request_signed = want_request_signed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
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
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
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
        # The ID of the request.
        self.request_id = request_id
        # The configurations of the IdP.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the group.
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
        # The time when the group was created.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The type of the group. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The group is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The time when the information about the group was modified.
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
        # The information about the group.
        self.group = group
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetLoginPreferenceRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # The ID of the directory.
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


class GetLoginPreferenceResponseBodyLoginPreference(TeaModel):
    def __init__(
        self,
        allow_user_to_get_credentials: bool = None,
        login_network_masks: str = None,
    ):
        # Whether the user can obtain program access credentials on the portal after logging in. Values: 
        # - True: Yes. 
        # - False (default): No.
        self.allow_user_to_get_credentials = allow_user_to_get_credentials
        # The IP address whitelist. CloudSSO users can log on to the CloudSSO user portal only by using the IP addresses in the whitelist.
        # 
        # The IP address whitelist takes effect only on CloudSSO users who want to log on to the CloudSSO user portal by using the username-password logon or single sign-on (SSO) method. The IP address whitelist does not take effect on CloudSSO users who access accounts in a resource directory from the CloudSSO user portal.
        # 
        # If the return value of this parameter is empty, no IP address whitelists are configured.
        self.login_network_masks = login_network_masks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_get_credentials is not None:
            result['AllowUserToGetCredentials'] = self.allow_user_to_get_credentials
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToGetCredentials') is not None:
            self.allow_user_to_get_credentials = m.get('AllowUserToGetCredentials')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        return self


class GetLoginPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        login_preference: GetLoginPreferenceResponseBodyLoginPreference = None,
        request_id: str = None,
    ):
        # The logon preference.
        self.login_preference = login_preference
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.login_preference:
            self.login_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_preference is not None:
            result['LoginPreference'] = self.login_preference.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginPreference') is not None:
            temp_model = GetLoginPreferenceResponseBodyLoginPreference()
            self.login_preference = temp_model.from_map(m['LoginPreference'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLoginPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLoginPreferenceResponseBody = None,
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
            temp_model = GetLoginPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMFAAuthenticationSettingInfoRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # The ID of the directory.
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


class GetMFAAuthenticationSettingInfoResponseBodyMFAAuthenticationSettingInfo(TeaModel):
    def __init__(
        self,
        mfa_authentication_advance_settings: str = None,
        operation_for_risk_login: str = None,
    ):
        # The MFA policy of all users. Valid values:
        # 
        # *   Enabled: MFA is enabled for all users.
        # *   Byuser: User-specific settings are applied. For more information about how to configure MFA for a single user, see [UpdateUserMFAAuthenticationSettings](https://help.aliyun.com/document_detail/450135.html).
        # *   Disabled: MFA is disabled for all users.
        # *   OnlyRiskyLogin: MFA is required only for unusual logons.
        self.mfa_authentication_advance_settings = mfa_authentication_advance_settings
        # The MFA policy for unusual logons. Valid values:
        # 
        # *   Autonomous: MFA is prompted for users who initiated unusual logons. However, the users are allowed to skip MFA. If an MFA device is bound to a user who initiated an unusual logon, the user must pass MFA.
        # *   EnforceVerify: MFA is required. If no MFA devices are bound to a user who initiated an unusual logon, the user must bind an MFA device. If an MFA device is already bound to a user who initiated an unusual logon, the user must pass MFA.
        # 
        # > This parameter is displayed only when Byuser or OnlyRiskyLogin is returned for the MfaAuthenticationAdvanceSettings parameter.
        self.operation_for_risk_login = operation_for_risk_login

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfa_authentication_advance_settings is not None:
            result['MfaAuthenticationAdvanceSettings'] = self.mfa_authentication_advance_settings
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MfaAuthenticationAdvanceSettings') is not None:
            self.mfa_authentication_advance_settings = m.get('MfaAuthenticationAdvanceSettings')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        return self


class GetMFAAuthenticationSettingInfoResponseBody(TeaModel):
    def __init__(
        self,
        mfaauthentication_setting_info: GetMFAAuthenticationSettingInfoResponseBodyMFAAuthenticationSettingInfo = None,
        request_id: str = None,
    ):
        # The MFA setting of all users.
        self.mfaauthentication_setting_info = mfaauthentication_setting_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.mfaauthentication_setting_info:
            self.mfaauthentication_setting_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfaauthentication_setting_info is not None:
            result['MFAAuthenticationSettingInfo'] = self.mfaauthentication_setting_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFAAuthenticationSettingInfo') is not None:
            temp_model = GetMFAAuthenticationSettingInfoResponseBodyMFAAuthenticationSettingInfo()
            self.mfaauthentication_setting_info = temp_model.from_map(m['MFAAuthenticationSettingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMFAAuthenticationSettingInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMFAAuthenticationSettingInfoResponseBody = None,
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
            temp_model = GetMFAAuthenticationSettingInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMFAAuthenticationSettingsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # The ID of the directory.
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
        # Indicates whether MFA is enabled for all users. Valid values:
        # 
        # *   Enabled: MFA is enabled for all users.
        # *   Byuser: User-specific settings are applied.
        # *   Disabled: MFA is disabled for all users.
        self.mfaauthentication_advance_settings = mfaauthentication_advance_settings
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The status of MFA. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.mfaauthentication_status = mfaauthentication_status
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetPasswordPolicyRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # The ID of the directory.
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


class GetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(
        self,
        hard_expire: bool = None,
        max_login_attempts: int = None,
        max_password_age: int = None,
        max_password_length: int = None,
        min_password_different_chars: int = None,
        min_password_length: int = None,
        password_not_contain_username: bool = None,
        password_reuse_prevention: int = None,
        require_lower_case_chars: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_upper_case_chars: bool = None,
    ):
        # Indicates whether to disable logon after a password expires. Valid values:
        # 
        # *   true: disables logon after a password expires.
        # *   false: does not disable logon after a password expires.
        self.hard_expire = hard_expire
        # The number of password retries.
        # 
        # If wrong passwords are entered for the specified consecutive times, the account is locked for 1 hour.
        # 
        # Valid values: 0 to 32. The value 0 indicates that the number of password retries is not limited.
        self.max_login_attempts = max_login_attempts
        # The validity period of a password.
        # 
        # Valid values: 1 to 120. Unit: days.
        self.max_password_age = max_password_age
        # The maximum password length.
        self.max_password_length = max_password_length
        # The minimum number of different characters in a password.
        # 
        # The minimum value is 0, which indicates that the minimum number of different characters in a password is not limited. The maximum value is the value of the `MinPasswordLength` parameter.
        self.min_password_different_chars = min_password_different_chars
        # The minimum password length.
        # 
        # Valid values: 8 to 32 characters.
        self.min_password_length = min_password_length
        # Indicates whether to exclude the username from the password. Valid values:
        # 
        # *   true: A password cannot contain the username.
        # *   false: A password can contain the username.
        self.password_not_contain_username = password_not_contain_username
        # The policy for password history check.
        # 
        # The previous N passwords cannot be reused. Valid values of N: 0 to 24. The value 0 indicates that all historical passwords can be reused.
        # 
        # >  Passwords that are generated before January 5, 2024 are not counted as historical passwords.
        self.password_reuse_prevention = password_reuse_prevention
        # Indicates whether lowercase letters are required in a password. Valid values:
        # 
        # *   true: Lowercase letters are required in a password.
        # *   false: Lowercase letters are not required in a password.
        self.require_lower_case_chars = require_lower_case_chars
        # Indicates whether digits are required in a password. Valid values:
        # 
        # *   true: Digits are required in a password.
        # *   false: Digits are not required in a password.
        self.require_numbers = require_numbers
        # Indicates whether special characters are required in a password. Valid values:
        # 
        # *   true: Special characters are required in a password.
        # *   false: Special characters are not required in a password.
        self.require_symbols = require_symbols
        # Indicates whether uppercase letters are required in a password. Valid values:
        # 
        # *   true: Uppercase letters are required in a password.
        # *   false: Uppercase letters are not required in a password.
        self.require_upper_case_chars = require_upper_case_chars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attempts is not None:
            result['MaxLoginAttempts'] = self.max_login_attempts
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.max_password_length is not None:
            result['MaxPasswordLength'] = self.max_password_length
        if self.min_password_different_chars is not None:
            result['MinPasswordDifferentChars'] = self.min_password_different_chars
        if self.min_password_length is not None:
            result['MinPasswordLength'] = self.min_password_length
        if self.password_not_contain_username is not None:
            result['PasswordNotContainUsername'] = self.password_not_contain_username
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lower_case_chars is not None:
            result['RequireLowerCaseChars'] = self.require_lower_case_chars
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_upper_case_chars is not None:
            result['RequireUpperCaseChars'] = self.require_upper_case_chars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttempts') is not None:
            self.max_login_attempts = m.get('MaxLoginAttempts')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MaxPasswordLength') is not None:
            self.max_password_length = m.get('MaxPasswordLength')
        if m.get('MinPasswordDifferentChars') is not None:
            self.min_password_different_chars = m.get('MinPasswordDifferentChars')
        if m.get('MinPasswordLength') is not None:
            self.min_password_length = m.get('MinPasswordLength')
        if m.get('PasswordNotContainUsername') is not None:
            self.password_not_contain_username = m.get('PasswordNotContainUsername')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowerCaseChars') is not None:
            self.require_lower_case_chars = m.get('RequireLowerCaseChars')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUpperCaseChars') is not None:
            self.require_upper_case_chars = m.get('RequireUpperCaseChars')
        return self


class GetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        password_policy: GetPasswordPolicyResponseBodyPasswordPolicy = None,
        request_id: str = None,
    ):
        # The password policy.
        self.password_policy = password_policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordPolicy') is not None:
            temp_model = GetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPasswordPolicyResponseBody = None,
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
            temp_model = GetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSCIMSynchronizationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # The ID of the directory.
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
        # The ID of the request.
        self.request_id = request_id
        # The status of SCIM synchronization. Valid values:
        # 
        # *   Enabled
        # *   Disabled
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # Indicates whether you have permissions to enable CloudSSO. Valid values:
        # 
        # *   Success: You have permissions to enable CloudSSO.
        # *   Failed: You do not have permissions to enable CloudSSO.
        # 
        # >  The value of this parameter is returned only if the value of `Status` is `Disabled`.
        self.prerequisite_check_result = prerequisite_check_result
        # The ID of the region.
        self.regions_in_use = regions_in_use
        # Indicates whether CloudSSO is enabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
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
        # The ID of the request.
        self.request_id = request_id
        # The status information of CloudSSO.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The directory ID.
        self.directory_id = directory_id
        # The task ID.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The end time of the task.
        self.end_time = end_time
        # The cause of the task failure.
        # 
        # >  This parameter is returned only when the value of `Status` is `Failed`.
        self.failure_reason = failure_reason
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The start time of the task.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object. The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The task ID.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # *   ProvisionAccessConfiguration: An access configuration is provisioned.
        # *   DeprovisionAccessConfiguration: An access configuration is de-provisioned.
        # *   CreateAccessAssignment: Access permissions on an account in the resource directory are assigned.
        # *   DeleteAccessAssignment: Access permissions on an account in the resource directory are removed.
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
        # The request ID.
        self.request_id = request_id
        # The task information.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The directory ID.
        self.directory_id = directory_id
        # The task ID.
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
        # The end time of the task.
        self.end_time = end_time
        # The cause of the task failure.
        # 
        # >  This parameter is returned only when the value of `Status` is `Failed`.
        self.failure_reason = failure_reason
        # The start time of the task.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # *   ProvisionAccessConfiguration: An access configuration is provisioned.
        # *   DeprovisionAccessConfiguration: An access configuration is de-provisioned.
        # *   CreateAccessAssignment: Access permissions on an account in the resource directory are assigned.
        # *   DeleteAccessAssignment: Access permissions on an account in the resource directory are removed.
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
        # The request ID.
        self.request_id = request_id
        # The status information about the task.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the user.
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


class GetUserResponseBodyUserExternalId(TeaModel):
    def __init__(
        self,
        id: str = None,
        issuer: str = None,
    ):
        # The identifier of the user that is synchronized from an external IdP.
        self.id = id
        # The method for external identity synchronization. Only System for Cross-domain Identity Management (SCIM) synchronization is supported.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        external_id: GetUserResponseBodyUserExternalId = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was created. The value is displayed in UTC.
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The identifier information about the user synchronized from an external IdP.
        self.external_id = external_id
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The time when the information about the user was modified. The value is displayed in UTC.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id
        # The name of the user.
        self.user_name = user_name

    def validate(self):
        if self.external_id:
            self.external_id.validate()

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
        if self.external_id is not None:
            result['ExternalId'] = self.external_id.to_map()
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
        if m.get('ExternalId') is not None:
            temp_model = GetUserResponseBodyUserExternalId()
            self.external_id = temp_model.from_map(m['ExternalId'])
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
        # The request ID.
        self.request_id = request_id
        # The information about the user.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetUserIdRequestExternalId(TeaModel):
    def __init__(
        self,
        id: str = None,
        issuer: str = None,
    ):
        # The identifier of the user that is synchronized from an external IdP.
        self.id = id
        # The method for external identity synchronization. Only System for Cross-domain Identity Management (SCIM) synchronization is supported.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class GetUserIdRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        external_id: GetUserIdRequestExternalId = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The identifier information about the user that is synchronized from an external identity provider (IdP).
        self.external_id = external_id

    def validate(self):
        if self.external_id:
            self.external_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.external_id is not None:
            result['ExternalId'] = self.external_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ExternalId') is not None:
            temp_model = GetUserIdRequestExternalId()
            self.external_id = temp_model.from_map(m['ExternalId'])
        return self


class GetUserIdShrinkRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        external_id_shrink: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The identifier information about the user that is synchronized from an external identity provider (IdP).
        self.external_id_shrink = external_id_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.external_id_shrink is not None:
            result['ExternalId'] = self.external_id_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ExternalId') is not None:
            self.external_id_shrink = m.get('ExternalId')
        return self


class GetUserIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the CloudSSO user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserIdResponseBody = None,
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
            temp_model = GetUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserMFAAuthenticationSettingsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the user.
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
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether MFA is enabled for the user. Valid values:
        # 
        # *   Enabled: MFA is enabled for the user.
        # *   Disabled: MFA is disabled for the user.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetUserProvisioningRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_provisioning_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class GetUserProvisioningResponseBodyUserProvisioning(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        owner_pk: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: indicates that the identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: indicates that the identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The status of the RAM user provisioning. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.status = status
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The name of the object for which you create the RAM user provisioning. The value is fixed as the name of the member in the resource directory.
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the member.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time.
        self.update_time = update_time
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk
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
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')
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
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class GetUserProvisioningResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning: GetUserProvisioningResponseBodyUserProvisioning = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user provisioning.
        self.user_provisioning = user_provisioning

    def validate(self):
        if self.user_provisioning:
            self.user_provisioning.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning is not None:
            result['UserProvisioning'] = self.user_provisioning.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioning') is not None:
            temp_model = GetUserProvisioningResponseBodyUserProvisioning()
            self.user_provisioning = temp_model.from_map(m['UserProvisioning'])
        return self


class GetUserProvisioningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserProvisioningResponseBody = None,
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
            temp_model = GetUserProvisioningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserProvisioningConfigurationRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # The ID of the resource directory.
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


class GetUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_landing_page: str = None,
        directory_id: str = None,
        session_duration: int = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The default URL for a CloudSSO user who logs on to the Alibaba Cloud Management Console.
        # 
        # Default value: https://homenew.console.aliyun.com.
        self.default_landing_page = default_landing_page
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The duration of the logon session.
        # 
        # Unit: hours.
        # 
        # Valid values: 1 to 24.
        # 
        # Default value: 6.
        self.session_duration = session_duration
        # The modification time.
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
        if self.default_landing_page is not None:
            result['DefaultLandingPage'] = self.default_landing_page
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultLandingPage') is not None:
            self.default_landing_page = m.get('DefaultLandingPage')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetUserProvisioningConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_configuration: GetUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The global configurations of the RAM user provisioning.
        self.user_provisioning_configuration = user_provisioning_configuration

    def validate(self):
        if self.user_provisioning_configuration:
            self.user_provisioning_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning_configuration is not None:
            result['UserProvisioningConfiguration'] = self.user_provisioning_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioningConfiguration') is not None:
            temp_model = GetUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration()
            self.user_provisioning_configuration = temp_model.from_map(m['UserProvisioningConfiguration'])
        return self


class GetUserProvisioningConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserProvisioningConfigurationResponseBody = None,
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
            temp_model = GetUserProvisioningConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserProvisioningEventRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        event_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning event.
        # 
        # You can call the [ListUserProvisioningEvents](https://help.aliyun.com/document_detail/2636305.html) operation to query the value of `EventId`.
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class GetUserProvisioningEventResponseBodyUserProvisioningEvent(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        error_count: int = None,
        error_info: str = None,
        event_id: str = None,
        latest_async_time: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        source_type: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time. The time is displayed in UTC.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The number of execution failures.
        self.error_count = error_count
        # The error message that is displayed when the last execution of the RAM user provisioning event failed.
        self.error_info = error_info
        # The ID of the RAM user provisioning event.
        self.event_id = event_id
        # The time at which the RAM user provisioning event was last executed. The time is displayed in UTC.
        self.latest_async_time = latest_async_time
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: The identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The type of the source operation. Valid values:
        # 
        # *   StartProvisioning: enables the RAM user provisioning.
        # *   DeleteProvisioning: deletes the RAM user provisioning.
        # *   AddUserToGroup: adds a user to a user group.
        # *   RemoveUserFromGroup: removes a user from a user group.
        # *   UserProvisioningDeletionClearing: deletes the RAM user provisioning and clears resources in the background.
        self.source_type = source_type
        # The ID of the object for which you create the RAM user provisioning.
        # 
        # The value is fixed as the ID of the member in the resource directory.````
        self.target_id = target_id
        # The name of the object for which you create the RAM user provisioning.
        # 
        # The value is fixed as the name of the member in the resource directory.````
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the object.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time. The time is displayed in UTC.
        self.update_time = update_time
        # The ID of the RAM user provisioning event.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.latest_async_time is not None:
            result['LatestAsyncTime'] = self.latest_async_time
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('LatestAsyncTime') is not None:
            self.latest_async_time = m.get('LatestAsyncTime')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class GetUserProvisioningEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_event: GetUserProvisioningEventResponseBodyUserProvisioningEvent = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The RAM user provisioning event.
        self.user_provisioning_event = user_provisioning_event

    def validate(self):
        if self.user_provisioning_event:
            self.user_provisioning_event.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning_event is not None:
            result['UserProvisioningEvent'] = self.user_provisioning_event.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioningEvent') is not None:
            temp_model = GetUserProvisioningEventResponseBodyUserProvisioningEvent()
            self.user_provisioning_event = temp_model.from_map(m['UserProvisioningEvent'])
        return self


class GetUserProvisioningEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserProvisioningEventResponseBody = None,
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
            temp_model = GetUserProvisioningEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserProvisioningRdAccountStatisticsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        rd_member_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the member in the resource directory.
        self.rd_member_id = rd_member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.rd_member_id is not None:
            result['RdMemberId'] = self.rd_member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RdMemberId') is not None:
            self.rd_member_id = m.get('RdMemberId')
        return self


class GetUserProvisioningRdAccountStatisticsResponseBodyUserProvisioningStatistics(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        entity_id: str = None,
        failed_event_count: int = None,
        latest_async_time: str = None,
        owner_pk: str = None,
        type: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The entity ID, which is the ID of the member in the resource directory.
        self.entity_id = entity_id
        # The number of failed RAM user provisioning events.
        self.failed_event_count = failed_event_count
        # The time when the RAM user provisioning was last performed.
        self.latest_async_time = latest_async_time
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The entity type. The value is fixed as `RD Account`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.failed_event_count is not None:
            result['FailedEventCount'] = self.failed_event_count
        if self.latest_async_time is not None:
            result['LatestAsyncTime'] = self.latest_async_time
        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('FailedEventCount') is not None:
            self.failed_event_count = m.get('FailedEventCount')
        if m.get('LatestAsyncTime') is not None:
            self.latest_async_time = m.get('LatestAsyncTime')
        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUserProvisioningRdAccountStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_statistics: GetUserProvisioningRdAccountStatisticsResponseBodyUserProvisioningStatistics = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics of the RAM user provisioning.
        self.user_provisioning_statistics = user_provisioning_statistics

    def validate(self):
        if self.user_provisioning_statistics:
            self.user_provisioning_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning_statistics is not None:
            result['UserProvisioningStatistics'] = self.user_provisioning_statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioningStatistics') is not None:
            temp_model = GetUserProvisioningRdAccountStatisticsResponseBodyUserProvisioningStatistics()
            self.user_provisioning_statistics = temp_model.from_map(m['UserProvisioningStatistics'])
        return self


class GetUserProvisioningRdAccountStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserProvisioningRdAccountStatisticsResponseBody = None,
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
            temp_model = GetUserProvisioningRdAccountStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserProvisioningStatisticsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        user_provisioning_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class GetUserProvisioningStatisticsResponseBodyUserProvisioningStatistics(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        entity_id: str = None,
        failed_event_count: int = None,
        latest_async_time: str = None,
        owner_pk: str = None,
        type: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The entity ID, which is the ID of the RAM user provisioning.
        self.entity_id = entity_id
        # The number of failed RAM user provisioning events that are associated with the RAM user provisioning.
        self.failed_event_count = failed_event_count
        # The time when the RAM user provisioning was last performed.
        self.latest_async_time = latest_async_time
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The entity type. The value is fixed as `User Provisioning`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.failed_event_count is not None:
            result['FailedEventCount'] = self.failed_event_count
        if self.latest_async_time is not None:
            result['LatestAsyncTime'] = self.latest_async_time
        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('FailedEventCount') is not None:
            self.failed_event_count = m.get('FailedEventCount')
        if m.get('LatestAsyncTime') is not None:
            self.latest_async_time = m.get('LatestAsyncTime')
        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUserProvisioningStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_statistics: GetUserProvisioningStatisticsResponseBodyUserProvisioningStatistics = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics of the RAM user provisioning.
        self.user_provisioning_statistics = user_provisioning_statistics

    def validate(self):
        if self.user_provisioning_statistics:
            self.user_provisioning_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning_statistics is not None:
            result['UserProvisioningStatistics'] = self.user_provisioning_statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioningStatistics') is not None:
            temp_model = GetUserProvisioningStatisticsResponseBodyUserProvisioningStatistics()
            self.user_provisioning_statistics = temp_model.from_map(m['UserProvisioningStatistics'])
        return self


class GetUserProvisioningStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserProvisioningStatisticsResponseBody = None,
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
            temp_model = GetUserProvisioningStatisticsResponseBody()
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
        # The ID of the access configuration. The ID can be used to filter access permissions.
        self.access_configuration_id = access_configuration_id
        # The directory ID.
        self.directory_id = directory_id
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The ID of the CloudSSO identity. The ID can be used to filter access permissions.
        # 
        # *   If you set `PrincipalType` to User, set `PrincipalId` to the ID of the CloudSSO user.
        # *   If you set `PrincipalType` to Group, set `PrincipalId` to the ID of the CloudSSO group.
        # 
        # >  You can use the type to filter access permissions only if you specify both PrincipalId and `PrincipalType`.``
        self.principal_id = principal_id
        # The type of the CloudSSO identity. The type can be used to filter access permissions. Valid values:
        # 
        # *   User
        # *   Group
        # 
        # >  You can use the type to filter access permissions only if you specify both PrincipalId and `PrincipalType`.``
        self.principal_type = principal_type
        # The ID of the task object. The ID can be used to filter access permissions.
        # 
        # >  You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_id = target_id
        # The type of the task object. The type can be used to filter access permissions.
        # 
        # Set the value to RD-Account, which specifies the accounts in the resource directory.
        # 
        # >  You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access permissions were assigned.
        self.create_time = create_time
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object.
        # 
        # The value is fixed as RD-Account, which indicates the accounts in the resource directory.
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
        # The access permissions that are assigned.
        self.access_assignments = access_assignments
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when the value of IsTruncated is `true`.``
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration. The ID can be used to filter access permissions.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The status of the access configuration. The value can be used to filter accounts. Valid values:
        # 
        # *   Provisioned: The access configuration is provisioned.
        # *   ReprovisionRequired: The access configuration needs to be re-provisioned.
        # *   DeprovisionFailed: The access configuration failed to be provisioned.
        self.provisioning_status = provisioning_status
        # The ID of the task object. The ID can be used to filter access permissions.
        # 
        # >  You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_id = target_id
        # The type of the task object. The type can be used to filter access permissions.
        # 
        # Set the value to RD-Account, which specifies the accounts in the resource directory.
        # 
        # >  You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The first time when the access configuration was provisioned.
        self.create_time = create_time
        # The name of the custom policy that is created for an account in the resource directory.
        self.rampolicy_names = rampolicy_names
        # The name of the RAM role that is created for an account in the resource directory.
        self.ramrole_name = ramrole_name
        # The name of the Security Assertion Markup Language (SAML) identity provider (IdP) that is created within an account in the resource directory.
        self.samlprovider_name = samlprovider_name
        # The status of the access configuration. Valid values:
        # 
        # *   Provisioned: The access configuration is provisioned.
        # *   ReprovisionRequired: The access configuration needs to be re-provisioned.
        # *   DeprovisionFailed: The access configuration failed to be provisioned.
        self.status = status
        # The ID of the task object.
        # 
        # If the value of TargetType is `RD-Account`, the value of this parameter is the UID of an account in the resource directory.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object.
        # 
        # Set the value to RD-Account, which specifies the accounts in the resource directory.
        self.target_type = target_type
        # The last time when the access configuration was provisioned.
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
        # The accounts for which the access configuration is provisioned.
        self.access_configuration_provisionings = access_configuration_provisionings
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when the value of `IsTruncated` is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # Specify the value in the \\<Attribute> \\<Operator> \\<Value> format. The value is not case sensitive. You can set \\<Attribute> only to AccessConfigurationName and \\<Operator> only to eq or sw. The value eq indicates Equals. The value sw indicates Starts With.
        # 
        # For example, if you set Filter to AccessConfigurationName sw test, the operation queries all access configurations whose names start with test. If you set Filter to AccessConfigurationName eq TestAccessConfiguration, the operation queries the access configuration whose name is TestAccessConfiguration.
        self.filter = filter
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token to return for the next page. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The status notification. The status notification can be used to filter access configurations.
        # 
        # Set the value to ReprovisionRequired, which indicates that the operation queries all access configurations that need to be re-provisioned.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access configuration was created.
        self.create_time = create_time
        # The description of the access configuration.
        self.description = description
        # The initial web page that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        self.relay_state = relay_state
        # The duration of a session in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        self.session_duration = session_duration
        # The status notification.
        self.status_notifications = status_notifications
        # The time when the information about the access configuration was modified.
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
        # The access configurations.
        self.access_configurations = access_configurations
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true: The queried entries are truncated.
        # *   false: The queried entries are not truncated.
        self.is_truncated = is_truncated
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is returned for the next page.
        # 
        # >  This parameter is returned only when the `IsTruncated` parameter is set to `true`.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The time when the directory was created.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The region ID of the directory.
        self.region = region
        # The time when the directory was modified.
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
        # The directories.
        self.directories = directories
        # The ID of the request.
        self.request_id = request_id
        # The number of directories.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The issuer of the certificate.
        self.issuer = issuer
        # The time when the certificate expires.
        self.not_after = not_after
        # The time when the certificate was created.
        self.not_before = not_before
        # The public key of the certificate. The value of this parameter is in the PEM format and is Base64-encoded.
        self.public_key = public_key
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The signature algorithm of the certificate.
        self.signature_algorithm = signature_algorithm
        # The subject of the certificate.
        self.subject = subject
        # The version of the certificate.
        self.version = version
        # The X.509 certificate in the PEM format.
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
        # The ID of the request.
        self.request_id = request_id
        # The SAML signing certificates.
        self.samlid_pcertificates = samlid_pcertificates
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the group.
        self.group_id = group_id
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token to return for the next page. If this is your first time to call this operation, you do not need to specify `NextToken` .
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
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
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The ID of the group.
        self.group_id = group_id
        # The time when the user was added to the user group.
        self.join_time = join_time
        # The type of the user. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The ID of the user.
        self.user_id = user_id
        # The name of the user.
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
        # The users in the group.
        self.group_members = group_members
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true: The queried entries are truncated.
        # *   false: The queried entries are not truncated.
        self.is_truncated = is_truncated
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is returned for the next page.
        # 
        # >  This parameter is returned only when the value of `IsTruncated` is `true`.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # Specify the value in the `<Attribute> <Operator> <Value>` format. The value is not case sensitive. You can set `<Attribute>` only to `GroupName` and `<Operator>` only to `eq` or `sw`. The value eq indicates Equals. The value sw indicates Starts With.
        # 
        # For example, if you set Filter to GroupName sw test, the operation queries the groups whose names start with test. If you set Filter to GroupName eq testgroup, the operation queries the group whose name is testgroup.
        self.filter = filter
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token to return for the next page. If this is your first time to call this operation, you do not need to specify `NextToken`.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The type of the group. The type can be used to filter groups. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The group is synchronized from an external identity provider (IdP).
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
        # The time when the group was created.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The type of the group. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The group is synchronized from an external IdP.
        self.provision_type = provision_type
        # The time when the information about the group was modified.
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
        # The groups.
        self.groups = groups
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true: The queried entries are truncated.
        # *   false: The queried entries are not truncated.
        self.is_truncated = is_truncated
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is returned for the next page.
        # 
        # >  This parameter is returned only when the `IsTruncated` parameter is set to `true`.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token to return for the next page. If this is your first time to call this operation, you do not need to specify `NextToken` .
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The ID of the user.
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
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The time when the user was added to the user group.
        self.join_time = join_time
        # The type of the group. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The ID of the user.
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
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true: The queried entries are truncated.
        # *   false: The queried entries are not truncated.
        self.is_truncated = is_truncated
        # The groups to which the user is added.
        self.joined_groups = joined_groups
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is returned for the next page.
        # 
        # >  This parameter is returned only when the value of `IsTruncated` is `true`.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the user.
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
        # The ID of the MFA device.
        self.device_id = device_id
        # The name of the MFA device.
        self.device_name = device_name
        # The type of the MFA device. The value is fixed as TOTP, which indicates a virtual MFA device. Virtual MFA devices are based on the Time-based One-time Password (TOTP) algorithm.
        self.device_type = device_type
        # The time when the MFA device was enabled.
        self.effective_time = effective_time
        # The ID of the user.
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
        # The MFA devices.
        self.mfadevices = mfadevices
        # The ID of the request.
        self.request_id = request_id
        # The total number of MFA devices.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The type of the policy. The type can be used to filter policies. Valid values:
        # 
        # *   System: system policy
        # *   Inline: inline policy
        # 
        # If you do not specify this parameter, all types of policies are queried.
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
        # The time when the policy was created for the access configuration.
        self.add_time = add_time
        # The configurations of the inline policy.
        # 
        # >  This parameter is returned only when the value of the PermissionPolicyType parameter is Inline.
        self.permission_policy_document = permission_policy_document
        # The name of the policy.
        self.permission_policy_name = permission_policy_name
        # The type of the policy.
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
        # The policies.
        self.permission_policies = permission_policies
        # The ID of the request.
        self.request_id = request_id
        # The total number of policies.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
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
        # The time when the SCIM credential was created.
        self.create_time = create_time
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The type of the SCIM credential.
        self.credential_type = credential_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The time when the SCIM credential expires.
        self.expire_time = expire_time
        # The status of the SCIM credential. Valid values:
        # 
        # *   Enabled: The SCIM credential is enabled.
        # *   Disabled: The SCIM credential is disabled.
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
        # The ID of the request.
        self.request_id = request_id
        # The SCIM credentials.
        self.scimserver_credentials = scimserver_credentials
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration. The ID can be used to filter access permissions.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # The condition is not case-sensitive. The condition must be in the StartTime ge YYYY-MM-DDTHH:mm:SSZ format. You must set YYYY-MM-DDTHH:mm:SSZ to a value that is no more than 7 days from the current time. ge indicates Greater Than or Equals.
        # 
        # For example, if you set the Filter parameter to StartTime ge 2021-03-15T01:12:23Z, the operation queries the tasks from 2021-03-15T01:12:23 GMT.
        # 
        # >  If you do not specify this parameter, the operation queries the tasks within the previous 24 hours by default.
        self.filter = filter
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 20.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return exceeds the value of `MaxResults`, the entries are truncated. Only the entries that match the value of `MaxResults` are returned, and the excess entries are not returned. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The ID of the CloudSSO identity. The ID can be used to filter access permissions.
        # 
        # *   If you set `PrincipalType` to `User`, set `PrincipalId` to the ID of the CloudSSO user.
        # *   If you set `PrincipalType` to `Group`, set `PrincipalId` to the ID of the CloudSSO group.
        # 
        # >  You can use the type to filter access permissions only if you specify both `PrincipalId` and `PrincipalType`.
        self.principal_id = principal_id
        # The type of the CloudSSO identity. The type can be used to filter access permissions. Valid values:
        # 
        # *   User
        # *   Group
        # 
        # >  You can use the type to filter access permissions only if you specify both `PrincipalId` and `PrincipalType`.
        self.principal_type = principal_type
        # The ID of the task. The ID can be used to filter tasks. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object. The ID can be used to filter access permissions.
        # 
        # >  You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_id = target_id
        # The type of the task object. The type can be used to filter access permissions.
        # 
        # Set the value to RD-Account, which specifies the accounts in the resource directory.
        # 
        # >  You can use the type to filter access permissions only if you specify both `TargetId` and `TargetType`.
        self.target_type = target_type
        # The type of the task. The type can be used to filter tasks. Valid values:
        # 
        # *   ProvisionAccessConfiguration: An access configuration is provisioned.
        # *   DeprovisionAccessConfiguration: An access configuration is de-provisioned.
        # *   CreateAccessAssignment: Access permissions on an account in the resource directory are assigned.
        # *   DeleteAccessAssignment: Access permissions on an account in the resource directory are removed.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The end time of the task.
        self.end_time = end_time
        # The cause of the task failure.
        # 
        # >  This parameter is returned only when the value of `Status` is `Failed`.
        self.failure_reason = failure_reason
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # *   User
        # *   Group
        self.principal_type = principal_type
        # The start time of the task.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object.
        # 
        # The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The ID of the job.
        self.task_id = task_id
        # The task type. Valid values:
        # 
        # *   ProvisionAccessConfiguration: An access configuration is provisioned.
        # *   DeprovisionAccessConfiguration: An access configuration is de-provisioned.
        # *   CreateAccessAssignment: Access permissions on an account in the resource directory are assigned.
        # *   DeleteAccessAssignment: Access permissions on an account in the resource directory are removed.
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
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when the value of `IsTruncated` is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tasks.
        self.tasks = tasks
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class ListUserProvisioningEventsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        user_provisioning_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to initiate the next request. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return is larger than the value of `MaxResults`, the entries are truncated. The system returns entries based on the value of `MaxResults`, and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

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
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class ListUserProvisioningEventsResponseBodyUserProvisioningEvents(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        error_count: int = None,
        error_info: str = None,
        event_id: str = None,
        latest_async_time: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        source_type: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time. The time is displayed in UTC.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The number of execution failures.
        self.error_count = error_count
        # The error message that is displayed when the last execution of the RAM user provisioning event failed.
        self.error_info = error_info
        # The ID of the RAM user provisioning event.
        self.event_id = event_id
        # The time at which the RAM user provisioning event was last executed. The time is displayed in UTC.
        self.latest_async_time = latest_async_time
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If you set the `PrincipalType` parameter to `Group`, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If you set the `PrincipalType` parameter to `User`, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: The identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The type of the source operation. Valid values:
        # 
        # *   StartProvisioning: enables the RAM user provisioning.
        # *   DeleteProvisioning: deletes the RAM user provisioning.
        # *   AddUserToGroup: adds a user to a user group.
        # *   RemoveUserFromGroup: removes a user from a user group.
        # *   UserProvisioningDeletionClearing: deletes the RAM user provisioning and clears resources in the background.
        self.source_type = source_type
        # The ID of the object for which you create the RAM user provisioning.
        # 
        # The value is fixed as the ID of the account in the resource directory.````
        self.target_id = target_id
        # The name of the object for which you create the RAM user provisioning.
        # 
        # If `RD-Account` is returned, the value of this parameter is the name of the account that is used to access the instance.``
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the member.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time. The time is displayed in UTC.
        self.update_time = update_time
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.latest_async_time is not None:
            result['LatestAsyncTime'] = self.latest_async_time
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('LatestAsyncTime') is not None:
            self.latest_async_time = m.get('LatestAsyncTime')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class ListUserProvisioningEventsResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
        user_provisioning_events: List[ListUserProvisioningEventsResponseBodyUserProvisioningEvents] = None,
    ):
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to initiate the next request.
        # 
        # >  This parameter is returned only when the `IsTruncated` parameter is set to `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts
        # The RAM user provisioning events.
        self.user_provisioning_events = user_provisioning_events

    def validate(self):
        if self.user_provisioning_events:
            for k in self.user_provisioning_events:
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
        result['UserProvisioningEvents'] = []
        if self.user_provisioning_events is not None:
            for k in self.user_provisioning_events:
                result['UserProvisioningEvents'].append(k.to_map() if k else None)
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
        self.user_provisioning_events = []
        if m.get('UserProvisioningEvents') is not None:
            for k in m.get('UserProvisioningEvents'):
                temp_model = ListUserProvisioningEventsResponseBodyUserProvisioningEvents()
                self.user_provisioning_events.append(temp_model.from_map(k))
        return self


class ListUserProvisioningEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserProvisioningEventsResponseBody = None,
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
            temp_model = ListUserProvisioningEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserProvisioningsRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to initiate the next request. If this is your first time to call this operation, you do not need to specify the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return is larger than the value of `MaxResults`, the entries are truncated. The system returns entries based on the value of `MaxResults`, and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and `NextToken` is returned. In the next call, you can use the value of `NextToken` and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of `IsTruncated` becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: The identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type

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


class ListUserProvisioningsResponseBodyUserProvisionings(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        owner_pk: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: The identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The status of the RAM user provisioning. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.status = status
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the object.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time.
        self.update_time = update_time
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk
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
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')
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
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class ListUserProvisioningsResponseBody(TeaModel):
    def __init__(
        self,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
        user_provisionings: List[ListUserProvisioningsResponseBodyUserProvisionings] = None,
    ):
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token that is used to initiate the next request.
        # 
        # >  This parameter is returned only when the `IsTruncated` parameter is set to `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts
        # The RAM user provisionings.
        self.user_provisionings = user_provisionings

    def validate(self):
        if self.user_provisionings:
            for k in self.user_provisionings:
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
        result['UserProvisionings'] = []
        if self.user_provisionings is not None:
            for k in self.user_provisionings:
                result['UserProvisionings'].append(k.to_map() if k else None)
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
        self.user_provisionings = []
        if m.get('UserProvisionings') is not None:
            for k in m.get('UserProvisionings'):
                temp_model = ListUserProvisioningsResponseBodyUserProvisionings()
                self.user_provisionings.append(temp_model.from_map(k))
        return self


class ListUserProvisioningsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserProvisioningsResponseBody = None,
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
            temp_model = ListUserProvisioningsResponseBody()
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
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # You must specify the value in the `<Attribute> <Operator> <Value>` format. The value is not case-sensitive. You can set `<Attribute>` only to `UserName` and `Operator` only to `eq` or `sw`. The value eq indicates Equals, and the value sw indicates Start With.
        # 
        # For example, if you set the Filter parameter to UserName sw test, the operation queries the users whose names start with test. If you set the Filter parameter to UserName eq testuser, the operation queries the user whose name is `testuser`.
        self.filter = filter
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of the `NextToken` parameter.
        # 
        # When you call this operation for the first time, if the total number of entries to return is larger than the value of the `MaxResults` parameter, the entries are truncated. The system returns entries based on the value of the `MaxResults` parameter, and does not return the excess entries. In this case, the value of the response parameter `IsTruncated` is `true`, and the `NextToken` parameter is returned. In the next call, you can use the value of the `NextToken` parameter and maintain the settings of the other request parameters to query the excess entries. You can repeat the call until the value of the `IsTruncated` parameter becomes `false`. This way, all entries are returned.
        self.next_token = next_token
        # The type of the user. The parameter can be used to filter users. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. The parameter can be used to filter users. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
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


class ListUsersResponseBodyUsersExternalId(TeaModel):
    def __init__(
        self,
        id: str = None,
        issuer: str = None,
    ):
        # The identifier of the user that is synchronized from an external IdP.
        self.id = id
        # The method for external identity synchronization. Only System for Cross-domain Identity Management (SCIM) synchronization is supported.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        external_id: ListUsersResponseBodyUsersExternalId = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was created. The value is displayed in UTC.
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The identifier information about the user synchronized from an external IdP.
        self.external_id = external_id
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external IdP.
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The time when the information about the user was modified. The value is displayed in UTC.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id
        # The name of the user.
        self.user_name = user_name

    def validate(self):
        if self.external_id:
            self.external_id.validate()

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
        if self.external_id is not None:
            result['ExternalId'] = self.external_id.to_map()
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
        if m.get('ExternalId') is not None:
            temp_model = ListUsersResponseBodyUsersExternalId()
            self.external_id = temp_model.from_map(m['ExternalId'])
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
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when the `IsTruncated` parameter is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts
        # The users.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The directory ID.
        self.directory_id = directory_id
        # The ID of the task object.
        self.target_id = target_id
        # The type of the task object. Set the value to RD-Account, which specifies the accounts in the resource directory.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The task status. Valid values:
        # 
        # *   InProgress: The task is running.
        # *   Success: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object. The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The task ID.
        self.task_id = task_id
        # The task type. The value is fixed as ProvisionAccessConfiguration, which indicates that an access configuration is provisioned.
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
        # The request ID.
        self.request_id = request_id
        # The task information.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the certificate.
        # 
        # You can call the [ListExternalSAMLIdPCertificates](https://help.aliyun.com/document_detail/341629.html) operation to query the IDs of certificates.
        self.certificate_id = certificate_id
        # The ID of the directory.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the policy.
        self.permission_policy_name = permission_policy_name
        # The type of the policy. Valid values:
        # 
        # *   System: system policy
        # *   Inline: inline policy
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the group.
        self.group_id = group_id
        # The ID of the user.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # Specifies whether to enable the system to automatically generate a new password. Valid values:
        # 
        # *   True: The new password is automatically generated by the system.
        # *   False: The new password must be manually specified. This is the default value.
        self.generate_random_password = generate_random_password
        # The new password.
        # 
        # The password must contain the following types of characters: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # The password must be 8 to 32 characters in length.
        # 
        # >  If you set `GenerateRandomPassword` to `False`, you must specify `Password` .
        self.password = password
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # *   True: Password reset is required upon the next logon.
        # *   False: Password reset is not required upon the next logon. This is the default value.
        self.require_password_reset_for_next_login = require_password_reset_for_next_login
        # The ID of the user.
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
        # The new password.
        # 
        # >  This parameter is returned only when the new password is automatically generated by the system.
        self.new_password = new_password
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class RetryUserProvisioningEventRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        duplication_strategy: str = None,
        event_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the RAM user provisioning event.
        # 
        # You can call the [ListUserProvisioningEvents](https://help.aliyun.com/document_detail/2636305.html) operation to query the value of `EventId`.
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class RetryUserProvisioningEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RetryUserProvisioningEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryUserProvisioningEventResponseBody = None,
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
            temp_model = RetryUserProvisioningEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetExternalSAMLIdentityProviderRequest(TeaModel):
    def __init__(
        self,
        binding_type: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        login_url: str = None,
        ssostatus: str = None,
        want_request_signed: bool = None,
        x_509certificate: str = None,
    ):
        # The Binding method for initiating a SAML request. Values:
        # 
        # - Post: Initiate the SAML request using the Post method. 
        # - Redirect: Initiate the SAML request using the Redirect method.
        self.binding_type = binding_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the IdP. The value of this parameter is Base64-encoded.
        # 
        # The file is provided by the IdP that supports SAML 2.0.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the IdP.
        self.entity_id = entity_id
        # The logon URL of the IdP.
        self.login_url = login_url
        # The status of SSO logon. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        self.ssostatus = ssostatus
        # Specifies whether CloudSSO needs to sign SAML requests. The requests are sent when users log on to the CloudSSO user portal to initiate SAML-based SSO. Valid values:
        # 
        # *   true: yes
        # *   false: no (default)
        self.want_request_signed = want_request_signed
        # The X.509 certificate in the PEM format. If you specify this parameter, all existing certificates are replaced.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
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
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
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
        binding_type: str = None,
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
        # The Binding method for initiating a SAML request. Values:
        # 
        # - Post: Initiate the SAML request using the Post method. 
        # - Redirect: Initiate the SAML request using the Redirect method.
        self.binding_type = binding_type
        # The ID of the SAML signing certificate.
        self.certificate_ids = certificate_ids
        # The time when the IdP was configured for the first time.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the IdP. The value of this parameter is Base64-encoded.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the IdP.
        self.entity_id = entity_id
        # The logon URL of the IdP.
        self.login_url = login_url
        # The status of SSO logon. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.ssostatus = ssostatus
        # The time when the IdP configurations were last modified.
        self.update_time = update_time
        # Indicates whether CloudSSO needs to sign SAML requests. The requests are sent when users log on to the CloudSSO user portal to initiate SAML-based SSO. Valid values:
        # 
        # *   true: yes
        # *   false: no (default)
        self.want_request_signed = want_request_signed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
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
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
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
        # The ID of the request.
        self.request_id = request_id
        # The configurations of the IdP.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class SetLoginPreferenceRequest(TeaModel):
    def __init__(
        self,
        allow_user_to_get_credentials: bool = None,
        directory_id: str = None,
        login_network_masks: str = None,
    ):
        self.allow_user_to_get_credentials = allow_user_to_get_credentials
        # The ID of the directory.
        self.directory_id = directory_id
        # The IP address whitelist. CloudSSO users can log on to the CloudSSO user portal only by using the IP addresses in the whitelist. Limits:
        # 
        # *   You can enter IP addresses or CIDR blocks. IPv4 addresses are supported.
        # *   You can enter up to 100 IP addresses or CIDR blocks. Separate multiple IP addresses or CIDR blocks with semicolons `(;)`.
        # *   If you do not specify this parameter, the original settings are retained.
        # *   If you set this parameter to a semicolon (`;`), the value of this parameter is cleared.
        # *   The IP address whitelist takes effect only on CloudSSO users who want to log on to the CloudSSO user portal by using the username-password logon or single sign-on (SSO) method. The IP address whitelist does not take effect on CloudSSO users who access accounts in a resource directory from the CloudSSO user portal.
        self.login_network_masks = login_network_masks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_get_credentials is not None:
            result['AllowUserToGetCredentials'] = self.allow_user_to_get_credentials
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserToGetCredentials') is not None:
            self.allow_user_to_get_credentials = m.get('AllowUserToGetCredentials')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        return self


class SetLoginPreferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class SetLoginPreferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetLoginPreferenceResponseBody = None,
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
            temp_model = SetLoginPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMFAAuthenticationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        mfaauthentication_status: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The status of MFA. Valid values:
        # 
        # *   Enabled
        # *   Disabled
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class SetPasswordPolicyRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        max_login_attempts: int = None,
        max_password_age: int = None,
        min_password_different_chars: int = None,
        min_password_length: int = None,
        password_not_contain_username: bool = None,
        password_reuse_prevention: int = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The number of password retries.
        # 
        # If you enter wrong passwords for the specified consecutive times, the account is locked for 1 hour.
        # 
        # Valid values: 0 to 32. The value 0 specifies that the number of password retries is not limited.
        self.max_login_attempts = max_login_attempts
        # The validity period of a password.
        # 
        # Valid values: 1 to 120. Unit: days.
        self.max_password_age = max_password_age
        # The minimum number of unique characters in a password.
        # 
        # The minimum value is 0, which specifies that the minimum number of unique characters in a password is not limited. The maximum value is the value of the `MinPasswordLength` parameter.
        self.min_password_different_chars = min_password_different_chars
        # The minimum password length.
        # 
        # Valid values: 8 to 32 characters.
        self.min_password_length = min_password_length
        # Specifies whether a password can contain the username. Valid value:
        # 
        # *   true: A password cannot contain the username.
        # *   false: A password can contain the username.
        self.password_not_contain_username = password_not_contain_username
        # The policy for password history check.
        # 
        # The previous N passwords cannot be reused. Valid values of N: 0 to 24. The value 0 specifies that all historical passwords can be reused.
        # 
        # >  Passwords that are generated before January 5, 2024 are not counted as historical passwords.
        self.password_reuse_prevention = password_reuse_prevention

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.max_login_attempts is not None:
            result['MaxLoginAttempts'] = self.max_login_attempts
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.min_password_different_chars is not None:
            result['MinPasswordDifferentChars'] = self.min_password_different_chars
        if self.min_password_length is not None:
            result['MinPasswordLength'] = self.min_password_length
        if self.password_not_contain_username is not None:
            result['PasswordNotContainUsername'] = self.password_not_contain_username
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MaxLoginAttempts') is not None:
            self.max_login_attempts = m.get('MaxLoginAttempts')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinPasswordDifferentChars') is not None:
            self.min_password_different_chars = m.get('MinPasswordDifferentChars')
        if m.get('MinPasswordLength') is not None:
            self.min_password_length = m.get('MinPasswordLength')
        if m.get('PasswordNotContainUsername') is not None:
            self.password_not_contain_username = m.get('PasswordNotContainUsername')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        return self


class SetPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class SetPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPasswordPolicyResponseBody = None,
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
            temp_model = SetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSCIMSynchronizationStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        scimsynchronization_status: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The status of SCIM synchronization. Valid values:
        # 
        # *   Enabled
        # *   Disabled
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The new description of the access configuration.
        # 
        # The description can be up to 1,024 characters in length.
        self.new_description = new_description
        # The new initial web page that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # The web page must be a page of the Alibaba Cloud Management Console.
        self.new_relay_state = new_relay_state
        # The new duration of a session in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        # 
        # Valid values: 900 to 43200. The value 900 indicates 15 minutes. The value 43200 indicates 12 hours.
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access configuration was created.
        self.create_time = create_time
        # The description of the access configuration.
        self.description = description
        # The initial web page that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        self.relay_state = relay_state
        # The duration of a session in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        self.session_duration = session_duration
        # The status notification.
        self.status_notifications = status_notifications
        # The time when the information about the access configuration was modified.
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
        # The information about the access configuration.
        self.access_configuration = access_configuration
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The new name of the directory. The name must be globally unique.
        # 
        # The name can contain lowercase letters, digits, and hyphens (-). The name cannot start or end with a hyphen (-) and cannot have two consecutive hyphens (-). If you want to start the new name of the directory starts with `d-`, you must set this parameter to the ID of the directory.
        # 
        # The name must be 2 to 64 characters in length.
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
        # The time when the directory was created.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The region ID of the directory.
        self.region = region
        # The time when the directory was modified.
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
        # The information about the directory.
        self.directory = directory
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the group.
        self.group_id = group_id
        # The new description of the group.
        self.new_description = new_description
        # The new name of the group.
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
        # The time when the group was created.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The type of the group. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The time when the information about the group was modified.
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
        # The information about the group.
        self.group = group
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the inline policy.
        self.inline_policy_name = inline_policy_name
        # The new configurations of the inline policy.
        # 
        # The value can be up to 4,096 characters in length.
        # 
        # For more information about the syntax and structure of RAM policies, see [Policy syntax and structure](https://help.aliyun.com/document_detail/93739.html).
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # Specifies whether to enable MFA for all users. Valid value:
        # 
        # - Enabled: enables MFA for all users.
        # - Byuser: uses user-specific settings. For more information about how to configure MFA for a single user, see [UpdateUserMFAAuthenticationSettings](https://help.aliyun.com/document_detail/450135.html).
        # - Disabled: disables MFA for all users.
        # - OnlyRiskyLogin: MFA is required only for unusual logons.
        self.mfaauthentication_settings = mfaauthentication_settings
        # Specifies whether MFA is required for users who initiated unusual logons. Valid value:
        # 
        # - Autonomous: MFA is prompted for users who initiated unusual logons. However, the users are allowed to skip MFA. If an MFA device is bound to a user who initiated an unusual logon, the user must pass MFA.
        # 
        # - EnforceVerify: MFA is required. If no MFA devices are bound to a user who initiated an unusual logon, the user must bind an MFA device. If an MFA device is already bound to a user who initiated an unusual logon, the user must pass MFA.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The new status of the SCIM credential. Valid values:
        # 
        # *   Enabled: The SCIM credential is enabled.
        # *   Disabled: The SCIM credential is disabled.
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
        # The time when the SCIM credential was created.
        self.create_time = create_time
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The type of the SCIM credential.
        self.credential_type = credential_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The time when the SCIM credential expires.
        self.expire_time = expire_time
        # The status of the SCIM credential. Valid values:
        # 
        # *   Enabled: The SCIM credential is enabled.
        # *   Disabled: The SCIM credential is disabled.
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
        # The ID of the request.
        self.request_id = request_id
        # The information about the SCIM credential.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The new description of the user.
        self.new_description = new_description
        # The new display name of the user.
        self.new_display_name = new_display_name
        # The new email address of the user.
        self.new_email = new_email
        # The new first name of the user.
        self.new_first_name = new_first_name
        # The new last name of the user.
        self.new_last_name = new_last_name
        # The ID of the user.
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
        # The time when the user was created.
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The time when the information about the user was modified.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id
        # The name of the user.
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
        # The ID of the request.
        self.request_id = request_id
        # The information about the user.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the user.
        self.user_id = user_id
        # Specifies whether to enable MFA for the user. Valid values:
        # 
        # *   Enabled: enables MFA for the user.
        # *   Disabled: disables MFA for the user.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class UpdateUserProvisioningRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        new_deletion_strategy: str = None,
        new_description: str = None,
        new_duplication_strategy: str = None,
        user_provisioning_id: str = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The new deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.new_deletion_strategy = new_deletion_strategy
        # The new description of the RAM user provisioning.
        self.new_description = new_description
        # The new conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.new_duplication_strategy = new_duplication_strategy
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_deletion_strategy is not None:
            result['NewDeletionStrategy'] = self.new_deletion_strategy
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_duplication_strategy is not None:
            result['NewDuplicationStrategy'] = self.new_duplication_strategy
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewDeletionStrategy') is not None:
            self.new_deletion_strategy = m.get('NewDeletionStrategy')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewDuplicationStrategy') is not None:
            self.new_duplication_strategy = m.get('NewDuplicationStrategy')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class UpdateUserProvisioningResponseBodyUserProvisioning(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        owner_pk: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_type: str = None,
        update_time: str = None,
        user_provisioning_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # *   Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # *   Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description for the RAM user provisioning.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # *   KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # *   TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the Alibaba Cloud account to which the resource directory belongs.
        self.owner_pk = owner_pk
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity name of the RAM user provisioning. Valid values:
        # 
        # *   If `Group` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user group.
        # *   If `User` is returned for the `PrincipalType` parameter, the value of this parameter is the name of a CloudSSO user.
        self.principal_name = principal_name
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # *   User: indicates that the identity of the RAM user provisioning is a CloudSSO user.
        # *   Group: indicates that the identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The status of the RAM user provisioning. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.status = status
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the account in the resource directory.
        self.target_id = target_id
        # The name of the object for which you create the RAM user provisioning. The value is fixed as the name of the resource directory.
        self.target_name = target_name
        # The path of the resource directory in which you create the RAM user provisioning for the object.
        self.target_path = target_path
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
        self.target_type = target_type
        # The modification time.
        self.update_time = update_time
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy
        if self.owner_pk is not None:
            result['OwnerPk'] = self.owner_pk
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
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')
        if m.get('OwnerPk') is not None:
            self.owner_pk = m.get('OwnerPk')
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
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')
        return self


class UpdateUserProvisioningResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning: UpdateUserProvisioningResponseBodyUserProvisioning = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the RAM user provisioning.
        self.user_provisioning = user_provisioning

    def validate(self):
        if self.user_provisioning:
            self.user_provisioning.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning is not None:
            result['UserProvisioning'] = self.user_provisioning.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioning') is not None:
            temp_model = UpdateUserProvisioningResponseBodyUserProvisioning()
            self.user_provisioning = temp_model.from_map(m['UserProvisioning'])
        return self


class UpdateUserProvisioningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserProvisioningResponseBody = None,
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
            temp_model = UpdateUserProvisioningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserProvisioningConfigurationRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        new_default_landing_page: str = None,
        new_session_duration: int = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The new default URL for a CloudSSO user who logs on to the Alibaba Cloud Management Console.
        # 
        # Default value: https://homenew.console.aliyun.com.
        self.new_default_landing_page = new_default_landing_page
        # The new duration of the logon session.
        # 
        # Unit: hours.
        # 
        # Valid values: 1 to 24.
        # 
        # Default value: 6.
        self.new_session_duration = new_session_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.new_default_landing_page is not None:
            result['NewDefaultLandingPage'] = self.new_default_landing_page
        if self.new_session_duration is not None:
            result['NewSessionDuration'] = self.new_session_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NewDefaultLandingPage') is not None:
            self.new_default_landing_page = m.get('NewDefaultLandingPage')
        if m.get('NewSessionDuration') is not None:
            self.new_session_duration = m.get('NewSessionDuration')
        return self


class UpdateUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_landing_page: str = None,
        directory_id: str = None,
        session_duration: int = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The default URL for a CloudSSO user who logs on to the Alibaba Cloud Management Console.
        # 
        # Default value: https://homenew.console.aliyun.com.
        self.default_landing_page = default_landing_page
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The duration of the logon session.
        # 
        # Unit: hours.
        # 
        # Valid values: 1 to 24.
        # 
        # Default value: 6.
        self.session_duration = session_duration
        # The modification time.
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
        if self.default_landing_page is not None:
            result['DefaultLandingPage'] = self.default_landing_page
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultLandingPage') is not None:
            self.default_landing_page = m.get('DefaultLandingPage')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateUserProvisioningConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_configuration: UpdateUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The global configurations of the RAM user provisioning.
        self.user_provisioning_configuration = user_provisioning_configuration

    def validate(self):
        if self.user_provisioning_configuration:
            self.user_provisioning_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_provisioning_configuration is not None:
            result['UserProvisioningConfiguration'] = self.user_provisioning_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserProvisioningConfiguration') is not None:
            temp_model = UpdateUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration()
            self.user_provisioning_configuration = temp_model.from_map(m['UserProvisioningConfiguration'])
        return self


class UpdateUserProvisioningConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserProvisioningConfigurationResponseBody = None,
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
            temp_model = UpdateUserProvisioningConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserStatusRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        new_status: str = None,
        user_id: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The new status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.new_status = new_status
        # The ID of the user.
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
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


