# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AcceptHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        # The ID of the invitation.
        # 
        # You can call the [ListHandshakesForAccount](https://help.aliyun.com/document_detail/160006.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.handshake_id = handshake_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class AcceptHandshakeResponseBodyHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The comment on the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited Alibaba Cloud account.
        self.target_entity = target_entity
        # The type of the invited Alibaba Cloud account. Valid values:
        # 
        # *   Account: indicates the ID of the Alibaba Cloud account.
        # *   Email: indicates the logon email address of the Alibaba Cloud account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class AcceptHandshakeResponseBody(TeaModel):
    def __init__(
        self,
        handshake: AcceptHandshakeResponseBodyHandshake = None,
        request_id: str = None,
    ):
        # The information of the invitation.
        self.handshake = handshake
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = AcceptHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AcceptHandshakeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptHandshakeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AcceptHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachControlPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        target_id: str = None,
    ):
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The ID of the object to which you want to attach the access control policy. Access control policies can be attached to the following objects:
        # 
        # *   Root folder
        # *   Subfolders of the Root folder
        # *   Members
        # 
        # This parameter is required.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class AttachControlPolicyResponseBody(TeaModel):
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


class AttachControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The name of the object to which you want to attach the policy.
        # 
        # *   If you want to attach the policy to a RAM user, specify the name in the \\<UserName>@\\<AccountAlias>.onaliyun.com format. \\<UserName> indicates the name of the RAM user, and \\<AccountAlias> indicates the alias of the Alibaba Cloud account to which the RAM user belongs.
        # *   If you want to attach the policy to a RAM user group, specify the name in the \\<GroupName>@group.\\<AccountAlias>.onaliyun.com format. \\<GroupName> indicates the name of the RAM user group, and \\<AccountAlias> indicates the alias of the Alibaba Cloud account to which the RAM user group belongs.
        # *   If you want to attach the policy to a RAM role, specify the name in the \\<RoleName>@role.\\<AccountAlias>.onaliyun.com format. \\<RoleName> indicates the name of the RAM role, and \\<AccountAlias> indicates the alias of the Alibaba Cloud account to which the RAM role belongs.
        # 
        # >  The alias of an Alibaba Cloud account is a part of the default domain name. You can call the [GetDefaultDomain](https://help.aliyun.com/document_detail/186720.html) operation to obtain the alias of an Alibaba Cloud account.
        # 
        # This parameter is required.
        self.principal_name = principal_name
        # The type of the object to which you want to attach the policy. Valid values:
        # 
        # *   IMSUser: RAM user
        # *   IMSGroup: RAM user group
        # *   ServiceRole: RAM role
        # 
        # This parameter is required.
        self.principal_type = principal_type
        # The effective scope of the policy. You can set this parameter to one of the following items:
        # 
        # *   ID of a resource group: indicates that the policy takes effect for the resources in the resource group.
        # *   ID of the Alibaba Cloud account to which the authorized object belongs: indicates that the policy takes effect for the resources within the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AttachPolicyResponseBody(TeaModel):
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


class AttachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindSecureMobilePhoneRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        secure_mobile_phone: str = None,
        verification_code: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The mobile phone number that you want to bind to the member for security purposes.
        # 
        # The mobile phone number you specify must be the same as the mobile phone number that you specify when you call the [SendVerificationCodeForBindSecureMobilePhone](https://help.aliyun.com/document_detail/372556.html) operation to obtain a verification code.
        # 
        # Specify the mobile phone number in the \\<Country code>-\\<Mobile phone number> format.
        # 
        # >  Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        # 
        # This parameter is required.
        self.secure_mobile_phone = secure_mobile_phone
        # The verification code.
        # 
        # You can call the [SendVerificationCodeForBindSecureMobilePhone](https://help.aliyun.com/document_detail/372556.html) operation to obtain the verification code.
        # 
        # This parameter is required.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class BindSecureMobilePhoneResponseBody(TeaModel):
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


class BindSecureMobilePhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindSecureMobilePhoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindSecureMobilePhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelChangeAccountEmailRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
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


class CancelChangeAccountEmailResponseBody(TeaModel):
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


class CancelChangeAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelChangeAccountEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelChangeAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCreateCloudAccountRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        # The account record ID.
        # 
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelCreateCloudAccountResponseBody(TeaModel):
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


class CancelCreateCloudAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCreateCloudAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelCreateCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        # The ID of the invitation.
        # 
        # This parameter is required.
        self.handshake_id = handshake_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class CancelHandshakeResponseBodyHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The comment on the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited account.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CancelHandshakeResponseBody(TeaModel):
    def __init__(
        self,
        handshake: CancelHandshakeResponseBodyHandshake = None,
        request_id: str = None,
    ):
        # The information of the invitation.
        self.handshake = handshake
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = CancelHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelHandshakeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelHandshakeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPromoteResourceAccountRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        # The account record ID.
        # 
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelPromoteResourceAccountResponseBody(TeaModel):
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


class CancelPromoteResourceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelPromoteResourceAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelPromoteResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeAccountEmailRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The email address to be bound to the member.
        # 
        # >  The system automatically sends a verification email to the email address. After the verification is passed, the email address takes effect, and the system changes both the logon email address and secure email address of the member.
        # 
        # This parameter is required.
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class ChangeAccountEmailResponseBody(TeaModel):
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


class ChangeAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeAccountEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccountDeleteRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the member that you want to delete.
        # 
        # This parameter is required.
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


class CheckAccountDeleteResponseBody(TeaModel):
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


class CheckAccountDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAccountDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckAccountDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoGroupingRuleRequestRuleContents(TeaModel):
    def __init__(
        self,
        auto_grouping_scope_condition: str = None,
        target_resource_group_condition: str = None,
    ):
        # The condition for the range of resources to be automatically transferred.
        self.auto_grouping_scope_condition = auto_grouping_scope_condition
        # The condition for the destination resource group.
        # 
        # This parameter is required.
        self.target_resource_group_condition = target_resource_group_condition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_grouping_scope_condition is not None:
            result['AutoGroupingScopeCondition'] = self.auto_grouping_scope_condition
        if self.target_resource_group_condition is not None:
            result['TargetResourceGroupCondition'] = self.target_resource_group_condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoGroupingScopeCondition') is not None:
            self.auto_grouping_scope_condition = m.get('AutoGroupingScopeCondition')
        if m.get('TargetResourceGroupCondition') is not None:
            self.target_resource_group_condition = m.get('TargetResourceGroupCondition')
        return self


class CreateAutoGroupingRuleRequest(TeaModel):
    def __init__(
        self,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_resource_types_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_types_scope: str = None,
        rule_contents: List[CreateAutoGroupingRuleRequestRuleContents] = None,
        rule_desc: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        # The IDs of regions to be excluded. Separate multiple IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of resource groups to be excluded. Separate multiple IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of resources to be excluded. Separate multiple IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The resource types to be excluded. Separate multiple resource types with commas (,).
        self.exclude_resource_types_scope = exclude_resource_types_scope
        # The IDs of regions. Separate multiple IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The IDs of resource groups. Separate multiple IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of resources. Separate multiple IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The resource types. Separate multiple resource types with commas (,).
        self.resource_types_scope = resource_types_scope
        # The content records of the rule.
        # 
        # This parameter is required.
        self.rule_contents = rule_contents
        # The description of the rule.
        self.rule_desc = rule_desc
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   custom_condition: custom transfer rule
        # *   associated_transfer: transfer rule for associated resources
        # 
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        if self.rule_contents:
            for k in self.rule_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope
        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.exclude_resource_types_scope is not None:
            result['ExcludeResourceTypesScope'] = self.exclude_resource_types_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        result['RuleContents'] = []
        if self.rule_contents is not None:
            for k in self.rule_contents:
                result['RuleContents'].append(k.to_map() if k else None)
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')
        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ExcludeResourceTypesScope') is not None:
            self.exclude_resource_types_scope = m.get('ExcludeResourceTypesScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        self.rule_contents = []
        if m.get('RuleContents') is not None:
            for k in m.get('RuleContents'):
                temp_model = CreateAutoGroupingRuleRequestRuleContents()
                self.rule_contents.append(temp_model.from_map(k))
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class CreateAutoGroupingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateAutoGroupingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAutoGroupingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAutoGroupingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudAccountRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
    ):
        # The display name of the member account.
        # 
        # The name must be 2 to 50 characters in length and can contain letters, digits, underscores (_), periods (.), and hyphens (-).
        # 
        # The name must be unique in the current resource directory.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The email address used to log on to the cloud account.
        # 
        # This parameter is required.
        self.email = email
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The ID of the settlement account. If you do not specify this parameter, the current account is used for settlement.
        self.payer_account_id = payer_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        return self


class CreateCloudAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the member account.
        self.account_id = account_id
        # The name of the member account.
        self.account_name = account_name
        # The display name of the member account.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member account joined the resource directory. Valid values:
        # 
        # *   invited: The member account is invited to join the resource directory.
        # *   created: The member account is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member account was modified.
        self.modify_time = modify_time
        # The account record ID.
        self.record_id = record_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member account. Valid values:
        # 
        # *   CreateSuccess: The member account is created.
        # *   CreateVerifying: The creation of the member account is under confirmation.
        # *   CreateFailed: The member account failed to be created.
        # *   CreateExpired: The creation of the member account expired.
        # *   CreateCancelled: The creation of the member account is canceled.
        # *   PromoteVerifying: The upgrade of the member account is under confirmation.
        # *   PromoteFailed: The member account failed to be upgraded.
        # *   PromoteExpired: The upgrade of the member account expired.
        # *   PromoteCancelled: The upgrade of the member account is canceled.
        # *   PromoteSuccess: The member account is upgraded.
        # *   InviteSuccess: The owner of the member account accepted the invitation.
        # *   Removed: The member account is removed from the resource directory.
        self.status = status
        # The type of the member account. The value CloudAccount indicates that the member account is a cloud account.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCloudAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: CreateCloudAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member account.
        self.account = account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = CreateCloudAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCloudAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCloudAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateControlPolicyRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        effect_scope: str = None,
        policy_document: str = None,
        policy_name: str = None,
    ):
        # The description of the access control policy.
        # 
        # The description must be 1 to 1,024 characters in length. The description can contain letters, digits, underscores (_), and hyphens (-) and must start with a letter.
        self.description = description
        # The effective scope of the access control policy.
        # 
        # The value RAM indicates that the access control policy takes effect only for RAM users and RAM roles.
        # 
        # This parameter is required.
        self.effect_scope = effect_scope
        # The document of the access control policy.
        # 
        # The document can be a maximum of 4,096 characters in length.
        # 
        # For more information about the languages of access control policies, see [Languages of access control policies](https://help.aliyun.com/document_detail/179096.html).
        # 
        # For more information about the examples of access control policies, see [Examples of custom access control policies](https://help.aliyun.com/document_detail/181474.html).
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # The name of the access control policy.
        # 
        # The name must be 1 to 128 characters in length. The name can contain letters, digits, and hyphens (-) and must start with a letter.
        # 
        # This parameter is required.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class CreateControlPolicyResponseBodyControlPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: str = None,
        create_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times that the access control policy is referenced.
        self.attachment_count = attachment_count
        # The time when the access control policy was created.
        self.create_date = create_date
        # The description of the access control policy.
        self.description = description
        # The effective scope of the access control policy.
        # 
        # The value RAM indicates that the access control policy takes effect only for RAM users and RAM roles.
        self.effect_scope = effect_scope
        # The ID of the access control policy.
        self.policy_id = policy_id
        # The name of the access control policy.
        self.policy_name = policy_name
        # The type of the access control policy. Valid values:
        # 
        # *   System: system access control policy
        # *   Custom: custom access control policy
        self.policy_type = policy_type
        # The time when the access control policy was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        control_policy: CreateControlPolicyResponseBodyControlPolicy = None,
        request_id: str = None,
    ):
        # The details of the access control policy.
        self.control_policy = control_policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = CreateControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m['ControlPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFolderRequest(TeaModel):
    def __init__(
        self,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # The name of the folder.
        # 
        # The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.),and hyphens (-).
        # 
        # This parameter is required.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class CreateFolderResponseBodyFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class CreateFolderResponseBody(TeaModel):
    def __init__(
        self,
        folder: CreateFolderResponseBodyFolder = None,
        request_id: str = None,
    ):
        # The information of the folder.
        self.folder = folder
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = CreateFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
    ):
        # The description of the policy.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The document of the policy.
        # 
        # The document must be 1 to 2,048 characters in length.
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class CreatePolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The time when the policy was created.
        self.create_date = create_date
        # The version number of the policy. Default value: v1.
        self.default_version = default_version
        # The description of the policy.
        self.description = description
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: CreatePolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The information of the policy.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreatePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_document: str = None,
        policy_name: str = None,
        set_as_default: bool = None,
    ):
        # The document of the policy.
        # 
        # The document must be 1 to 2,048 characters in length.
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # Specifies whether to set the policy version as the default version. Valid values:
        # 
        # *   false: The policy version is not set as the default version.
        # *   true: The policy version is set as the default version.
        # 
        # Default value: false.
        self.set_as_default = set_as_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')
        return self


class CreatePolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        version_id: str = None,
    ):
        # The time when the policy version was created.
        self.create_date = create_date
        # Indicates whether the policy version is the default version.
        self.is_default_version = is_default_version
        # The ID of the policy version.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreatePolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        policy_version: CreatePolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        # The information of the policy version.
        self.policy_version = policy_version
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreatePolicyVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceAccountRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateResourceAccountRequest(TeaModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        display_name: str = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
        resell_account_type: str = None,
        tag: List[CreateResourceAccountRequestTag] = None,
    ):
        # The prefix for the Alibaba Cloud account name of the member. If you leave this parameter empty, the system randomly generates a prefix.
        # 
        # The prefix must be 2 to 37 characters in length.
        # 
        # The prefix can contain letters, digits, and special characters but cannot contain consecutive special characters. The prefix must start with a letter or digit and end with a letter or digit. Valid special characters include underscores (`_`), periods (`.`), and hyphens (-).
        # 
        # The complete Alibaba Cloud account name of a member is in the @.aliyunid.com format, such as `alice@rd-3G****.aliyunid.com`.
        # 
        # Each name must be unique in the resource directory.
        self.account_name_prefix = account_name_prefix
        # The display name of the member.
        # 
        # The name must be 2 to 50 characters in length.
        # 
        # The name can contain letters, digits, underscores (_), periods (.), hyphens (-), and spaces.
        # 
        # The name must be unique in the resource directory.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The ID of the billing account. If you leave this parameter empty, the newly created member is used as its billing account.
        self.payer_account_id = payer_account_id
        # The identity type of the member. Valid values:
        # 
        # *   resell (default): The member is an account for a reseller. A relationship is automatically established between the member and the reseller. The management account of the resource directory must be used as the billing account of the member.
        # *   non_resell: The member is not an account for a reseller. The member is an account that is not associated with a reseller. You can directly use the account to purchase Alibaba Cloud resources. The member is used as its own billing account.
        # 
        # >  This parameter is available only for resellers at the international site (alibabacloud.com).
        self.resell_account_type = resell_account_type
        # The tag of the member.
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
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        if self.resell_account_type is not None:
            result['ResellAccountType'] = self.resell_account_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        if m.get('ResellAccountType') is not None:
            self.resell_account_type = m.get('ResellAccountType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateResourceAccountRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateResourceAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the member.
        self.account_id = account_id
        # The Alibaba Cloud account ID of the member.
        self.account_name = account_name
        # The display name of the member.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member joins the resource directory. Valid values:
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member joined the resource directory. The time is displayed in UTC.
        self.join_time = join_time
        # The time when the member was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member. The value CreateSuccess indicates that the member is created.
        self.status = status
        # The type of the member. The value ResourceAccount indicates that the member is a resource account.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateResourceAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: CreateResourceAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information about the member.
        self.account = account
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = CreateResourceAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceGroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. 
        # 
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of the tag. 
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        tag: List[CreateResourceGroupRequestTag] = None,
    ):
        # The display name of the resource group.
        # 
        # The name must be 1 to 50 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The unique identifier of the resource group.
        # 
        # The identifier must be 3 to 50 characters in length and can contain letters, digits, and hyphens (-). The identifier must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        # The tags.
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
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateResourceGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class CreateResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: CreateResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        # The status of the resource group in all regions.
        self.region_statuses = region_statuses
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        self.status = status

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: CreateResourceGroupResponseBodyResourceGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource group.
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        assume_role_policy_document: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
    ):
        # The document of the policy that specifies one or more trusted entities to assume the RAM role. The trusted entities can be Alibaba Cloud accounts, Alibaba Cloud services, or identity providers (IdPs).
        # 
        # >  RAM users cannot assume the RAM roles of trusted Alibaba Cloud services.
        # 
        # This parameter is required.
        self.assume_role_policy_document = assume_role_policy_document
        # The description of the RAM role.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The maximum session duration of the RAM role.
        # 
        # Unit: seconds. Valid values: 3600 to 43200. Default value: 3600.
        # 
        # If you do not specify this parameter, the default value is used.
        self.max_session_duration = max_session_duration
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
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
        return self


class CreateRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.arn = arn
        # The document of the policy that specifies the trusted entity to assume the RAM role.
        self.assume_role_policy_document = assume_role_policy_document
        # The time when the RAM role was created.
        self.create_date = create_date
        # The description of the RAM role.
        self.description = description
        # The maximum session duration of the RAM role.
        self.max_session_duration = max_session_duration
        # The ID of the RAM role.
        self.role_id = role_id
        # The name of the RAM role.
        self.role_name = role_name
        # The name of the RAM role after authorization.
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: CreateRoleResponseBodyRole = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the RAM role.
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        custom_suffix: str = None,
        description: str = None,
        service_name: str = None,
    ):
        # The suffix of the role name.
        # 
        # The role name (including its suffix) must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # For example, if the suffix is `Example`, the role name is `ServiceLinkedRoleName_Example`.
        self.custom_suffix = custom_suffix
        # The description of the service-linked role.
        # 
        # You must configure this parameter for service-linked roles that support custom suffixes. Otherwise, the preset value is used and cannot be modified.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The name of the service.
        # 
        # For more information about the service name, see [Alibaba Cloud services that support service-linked roles](https://help.aliyun.com/document_detail/461722.html).
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_suffix is not None:
            result['CustomSuffix'] = self.custom_suffix
        if self.description is not None:
            result['Description'] = self.description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSuffix') is not None:
            self.custom_suffix = m.get('CustomSuffix')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateServiceLinkedRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the role.
        self.arn = arn
        # The document of the trust policy for the role.
        self.assume_role_policy_document = assume_role_policy_document
        # The time when the role was created. The time is displayed in UTC.
        self.create_date = create_date
        # The description of the role.
        self.description = description
        # Indicates whether the role is a service-linked role. Valid values:
        # 
        # *   true: The role is a service-linked role.
        # *   false: The role is not a service-linked role.
        self.is_service_linked_role = is_service_linked_role
        # The ID of the role.
        self.role_id = role_id
        # The name of the role.
        self.role_name = role_name
        # The role name that uses a domain name as the suffix.
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: CreateServiceLinkedRoleResponseBodyRole = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the role.
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateServiceLinkedRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeclineHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        # The ID of the invitation.
        # 
        # This parameter is required.
        self.handshake_id = handshake_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class DeclineHandshakeResponseBodyHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created.
        self.create_time = create_time
        # The time when the invitation expires.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The ID of the enterprise management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the enterprise management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified.
        self.modify_time = modify_time
        # The invitation note.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expired.
        self.status = status
        # The ID or logon email address of the invited account.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DeclineHandshakeResponseBody(TeaModel):
    def __init__(
        self,
        handshake: DeclineHandshakeResponseBodyHandshake = None,
        request_id: str = None,
    ):
        # The information of the invitation.
        self.handshake = handshake
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = DeclineHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeclineHandshakeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeclineHandshakeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeclineHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        abandonable_check_id: List[str] = None,
        account_id: str = None,
    ):
        self.abandonable_check_id = abandonable_check_id
        # The type of the deletion. Valid values:
        # 
        # *   0: direct deletion. If the member does not have pay-as-you-go resources that are purchased within the previous 30 days, the system directly deletes the member.
        # *   1: deletion with a silence period. If the member has pay-as-you-go resources that are purchased within the previous 30 days, the member enters a silence period of 45 days. The system starts to delete the member until the silence period ends. For more information about the silence period, see [What is the silence period for member deletion?](https://help.aliyun.com/document_detail/446079.html)
        # 
        # This parameter is required.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandonable_check_id is not None:
            result['AbandonableCheckId'] = self.abandonable_check_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonableCheckId') is not None:
            self.abandonable_check_id = m.get('AbandonableCheckId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteAccountShrinkRequest(TeaModel):
    def __init__(
        self,
        abandonable_check_id_shrink: str = None,
        account_id: str = None,
    ):
        self.abandonable_check_id_shrink = abandonable_check_id_shrink
        # The type of the deletion. Valid values:
        # 
        # *   0: direct deletion. If the member does not have pay-as-you-go resources that are purchased within the previous 30 days, the system directly deletes the member.
        # *   1: deletion with a silence period. If the member has pay-as-you-go resources that are purchased within the previous 30 days, the member enters a silence period of 45 days. The system starts to delete the member until the silence period ends. For more information about the silence period, see [What is the silence period for member deletion?](https://help.aliyun.com/document_detail/446079.html)
        # 
        # This parameter is required.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandonable_check_id_shrink is not None:
            result['AbandonableCheckId'] = self.abandonable_check_id_shrink
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonableCheckId') is not None:
            self.abandonable_check_id_shrink = m.get('AbandonableCheckId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        deletion_type: str = None,
        request_id: str = None,
    ):
        self.deletion_type = deletion_type
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_type is not None:
            result['DeletionType'] = self.deletion_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionType') is not None:
            self.deletion_type = m.get('DeletionType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoGroupingRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteAutoGroupingRuleResponseBody(TeaModel):
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


class DeleteAutoGroupingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAutoGroupingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAutoGroupingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteControlPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # The ID of the control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeleteControlPolicyResponseBody(TeaModel):
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


class DeleteControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        # The ID of the folder.
        # 
        # This parameter is required.
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class DeleteFolderResponseBody(TeaModel):
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


class DeleteFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The ID of the policy version.
        # 
        # You can call the [ListPolicyVersions](https://help.aliyun.com/document_detail/159982.html) operation to query the ID.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeletePolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The ID of the resource group.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        # *   Deleting: The resource group is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class DeleteResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: DeleteResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        # The status of the resource group in all regions.
        self.region_statuses = region_statuses
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = DeleteResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: DeleteResourceGroupResponseBodyResourceGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource group.
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = DeleteResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class DeleteResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeleteRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        # The name of the role.
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        deletion_task_id: str = None,
        request_id: str = None,
    ):
        # The ID of the deletion task.
        self.deletion_task_id = deletion_task_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterDelegatedAdministratorRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        service_principal: str = None,
    ):
        # The ID of the member in the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The identifier of the trusted service.
        # 
        # For more information, see the `Trusted service identifier` column in [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        # 
        # This parameter is required.
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class DeregisterDelegatedAdministratorResponseBody(TeaModel):
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


class DeregisterDelegatedAdministratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeregisterDelegatedAdministratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeregisterDelegatedAdministratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyResourceDirectoryResponseBody(TeaModel):
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


class DestroyResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DestroyResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DestroyResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachControlPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        target_id: str = None,
    ):
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The ID of the object from which you want to detach the access control policy. Access control policies can be attached to the following objects:
        # 
        # *   Root folder
        # *   Subfolders of the Root folder
        # *   Members
        # 
        # This parameter is required.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class DetachControlPolicyResponseBody(TeaModel):
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


class DetachControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The name of the object to which the policy is attached.
        # 
        # This parameter is required.
        self.principal_name = principal_name
        # The type of the object to which the policy is attached. Valid values:
        # 
        # *   IMSUser: RAM user
        # *   IMSGroup: RAM user group
        # *   ServiceRole: RAM role
        # 
        # This parameter is required.
        self.principal_type = principal_type
        # The ID of the resource group or the ID of the Alibaba Cloud account to which the resource group belongs.
        # 
        # This parameter specifies the resource group or Alibaba Cloud account for which you want to revoke permissions.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DetachPolicyResponseBody(TeaModel):
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


class DetachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAssociatedTransferResponseBody(TeaModel):
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


class DisableAssociatedTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAssociatedTransferResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAssociatedTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAutoGroupingResponseBody(TeaModel):
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


class DisableAutoGroupingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAutoGroupingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAutoGroupingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        enablement_status: str = None,
        request_id: str = None,
    ):
        # The status of the Control Policy feature. Valid values:
        # 
        # *   Enabled: The Control Policy feature is enabled.
        # *   PendingEnable: The Control Policy feature is being enabled.
        # *   Disabled: The Control Policy feature is disabled.
        # *   PendingDisable: The Control Policy feature is being disabled.
        self.enablement_status = enablement_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enablement_status is not None:
            result['EnablementStatus'] = self.enablement_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablementStatus') is not None:
            self.enablement_status = m.get('EnablementStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAssociatedTransferResponseBody(TeaModel):
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


class EnableAssociatedTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAssociatedTransferResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAssociatedTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAutoGroupingResponseBody(TeaModel):
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


class EnableAutoGroupingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAutoGroupingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAutoGroupingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        enablement_status: str = None,
        request_id: str = None,
    ):
        # The status of the Control Policy feature. Valid values:
        # 
        # *   Enabled: The Control Policy feature is enabled.
        # *   PendingEnable: The Control Policy feature is being enabled.
        # *   Disabled: The Control Policy feature is disabled.
        # *   PendingDisable: The Control Policy feature is being disabled.
        self.enablement_status = enablement_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enablement_status is not None:
            result['EnablementStatus'] = self.enablement_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablementStatus') is not None:
            self.enablement_status = m.get('EnablementStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableResourceDirectoryRequest(TeaModel):
    def __init__(
        self,
        enable_mode: str = None,
        maname: str = None,
        masecure_mobile_phone: str = None,
        verification_code: str = None,
    ):
        # The mode in which you enable a resource directory. Valid values:
        # 
        # *   CurrentAccount: indicates that the current account is used to enable a resource directory.
        # *   NewManagementAccount: indicates that a newly created account is used to enable a resource directory. If you select this mode, you must configure the `MAName`, `MASecureMobilePhone`, and `VerificationCode` parameters.
        # 
        # This parameter is required.
        self.enable_mode = enable_mode
        # The name of the newly created account.
        # 
        # Specify the name in the `<Prefix>@rdadmin.aliyunid.com` format. The prefix can contain letters, digits, and special characters but cannot contain consecutive special characters. The prefix must start with a letter or digit and end with a letter or digit. Valid special characters include underscores (_), periods (.), and hyphens (-). The prefix must be 2 to 50 characters in length.
        self.maname = maname
        # The mobile phone number that is bound to the newly created account.
        # 
        # If you leave this parameter empty, the mobile phone number that is bound to the current account is used. The mobile phone number you specify must be the same as the mobile phone number that you specify when you call the [SendVerificationCodeForEnableRD](https://help.aliyun.com/document_detail/364248.html) operation to obtain a verification code.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # >  Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        self.masecure_mobile_phone = masecure_mobile_phone
        # The verification code.
        # 
        # You can call the [SendVerificationCodeForEnableRD](https://help.aliyun.com/document_detail/364248.html) operation to obtain the verification code.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_mode is not None:
            result['EnableMode'] = self.enable_mode
        if self.maname is not None:
            result['MAName'] = self.maname
        if self.masecure_mobile_phone is not None:
            result['MASecureMobilePhone'] = self.masecure_mobile_phone
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMode') is not None:
            self.enable_mode = m.get('EnableMode')
        if m.get('MAName') is not None:
            self.maname = m.get('MAName')
        if m.get('MASecureMobilePhone') is not None:
            self.masecure_mobile_phone = m.get('MASecureMobilePhone')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class EnableResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        resource_directory_id: str = None,
        root_folder_id: str = None,
    ):
        # The time when the resource directory was enabled.
        self.create_time = create_time
        # The ID of the management account.
        self.master_account_id = master_account_id
        # The name of the management account.
        self.master_account_name = master_account_name
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The ID of the Root folder.
        self.root_folder_id = root_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class EnableResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: EnableResourceDirectoryResponseBodyResourceDirectory = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource directory.
        self.resource_directory = resource_directory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = EnableResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class EnableResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        include_tags: bool = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # Specifies whether to return the information of tags. Valid values:
        # 
        # *   false (default value)
        # *   true
        self.include_tags = include_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        return self


class GetAccountResponseBodyAccountTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        email_status: str = None,
        folder_id: str = None,
        identity_information: str = None,
        join_method: str = None,
        join_time: str = None,
        location: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        resource_directory_path: str = None,
        status: str = None,
        tags: List[GetAccountResponseBodyAccountTags] = None,
        type: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The Alibaba Cloud account name of the member.
        self.account_name = account_name
        # The display name of the member.
        self.display_name = display_name
        # The status of the modification for the email address bound to the member. Valid values:
        # 
        # *   WAIT_MODIFY: in progress
        # *   CANCELLED: canceled
        # *   EXPIRED: expired
        # 
        # If the value of this parameter is empty, no modification is performed for the email address.
        self.email_status = email_status
        # The ID of the folder.
        self.folder_id = folder_id
        # The real-name verification information.
        self.identity_information = identity_information
        # The way in which the member joins the resource directory. Valid values:
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member joined the resource directory.
        self.join_time = join_time
        # The location of the member in the resource directory.
        self.location = location
        # The time when the member was modified.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The path of the member in the resource directory.
        self.resource_directory_path = resource_directory_path
        # The status of the member. Valid values:
        # 
        # *   CreateSuccess: The member is created.
        # *   PromoteVerifying: The upgrade of the member is being confirmed.
        # *   PromoteFailed: The upgrade of the member fails.
        # *   PromoteExpired: The upgrade of the member expires.
        # *   PromoteCancelled: The upgrade of the member is canceled.
        # *   PromoteSuccess: The member is upgraded.
        # *   InviteSuccess: The member accepts the invitation.
        self.status = status
        # The tags that are added to the member.
        self.tags = tags
        # The type of the member. Valid values:
        # 
        # *   CloudAccount: cloud account
        # *   ResourceAccount: resource account
        self.type = type

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
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.location is not None:
            result['Location'] = self.location
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetAccountResponseBodyAccountTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: GetAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member.
        self.account = account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = GetAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountDeletionCheckResultRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the member that you want to delete.
        # 
        # This parameter is required.
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


class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        check_name: str = None,
        description: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The name of the cloud service to which the check item belongs.
        self.check_name = check_name
        # The description of the check item.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        check_name: str = None,
        description: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The name of the cloud service to which the check item belongs.
        self.check_name = check_name
        # The description of the check item.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo(TeaModel):
    def __init__(
        self,
        abandonable_checks: List[GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks] = None,
        allow_delete: str = None,
        not_allow_reason: List[GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason] = None,
        status: str = None,
    ):
        # The check items that you can choose to ignore for the member deletion.
        # 
        # >  This parameter may be returned if the value of AllowDelete is true.
        self.abandonable_checks = abandonable_checks
        # Indicates whether the member can be deleted. Valid values:
        # 
        # *   true: The member can be deleted.
        # *   false: The member cannot be deleted.
        self.allow_delete = allow_delete
        # The reasons why the member cannot be deleted.
        # 
        # >  This parameter is returned only if the value of AllowDelete is false.
        self.not_allow_reason = not_allow_reason
        # The status of the check. Valid values:
        # 
        # *   PreCheckComplete: The check is complete.
        # *   PreChecking: The check is in progress.
        self.status = status

    def validate(self):
        if self.abandonable_checks:
            for k in self.abandonable_checks:
                if k:
                    k.validate()
        if self.not_allow_reason:
            for k in self.not_allow_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AbandonableChecks'] = []
        if self.abandonable_checks is not None:
            for k in self.abandonable_checks:
                result['AbandonableChecks'].append(k.to_map() if k else None)
        if self.allow_delete is not None:
            result['AllowDelete'] = self.allow_delete
        result['NotAllowReason'] = []
        if self.not_allow_reason is not None:
            for k in self.not_allow_reason:
                result['NotAllowReason'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abandonable_checks = []
        if m.get('AbandonableChecks') is not None:
            for k in m.get('AbandonableChecks'):
                temp_model = GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks()
                self.abandonable_checks.append(temp_model.from_map(k))
        if m.get('AllowDelete') is not None:
            self.allow_delete = m.get('AllowDelete')
        self.not_allow_reason = []
        if m.get('NotAllowReason') is not None:
            for k in m.get('NotAllowReason'):
                temp_model = GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason()
                self.not_allow_reason.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAccountDeletionCheckResultResponseBody(TeaModel):
    def __init__(
        self,
        account_deletion_check_result_info: GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo = None,
        request_id: str = None,
    ):
        # The result of the deletion check for the member.
        self.account_deletion_check_result_info = account_deletion_check_result_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account_deletion_check_result_info:
            self.account_deletion_check_result_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_deletion_check_result_info is not None:
            result['AccountDeletionCheckResultInfo'] = self.account_deletion_check_result_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDeletionCheckResultInfo') is not None:
            temp_model = GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo()
            self.account_deletion_check_result_info = temp_model.from_map(m['AccountDeletionCheckResultInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountDeletionCheckResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountDeletionCheckResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccountDeletionCheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountDeletionStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
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


class GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The description of the check item.
        self.description = description
        # The name of the cloud service to which the check item belongs.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        deletion_time: str = None,
        deletion_type: str = None,
        fail_reason_list: List[GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList] = None,
        status: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The start time of the deletion.
        self.create_time = create_time
        # The end time of the deletion.
        # 
        # This parameter is required.
        self.deletion_time = deletion_time
        # The type of the deletion. Valid values:
        # 
        # *   0: direct deletion. If the member does not have pay-as-you-go resources that are purchased within the previous 30 days, the system directly deletes the member.
        # *   1: deletion with a silence period. If the member has pay-as-you-go resources that are purchased within the previous 30 days, the member enters a silence period. The system starts to delete the member until the silence period ends. For more information about the silence period, see [What is the silence period for member deletion?](https://help.aliyun.com/document_detail/446079.html)
        self.deletion_type = deletion_type
        # The reasons why the member fails to be deleted.
        self.fail_reason_list = fail_reason_list
        # The status. Valid values:
        # 
        # *   Success: The member is deleted.
        # *   Checking: A deletion check is being performed for the member.
        # *   Deleting: The member is being deleted.
        # *   CheckFailed: The deletion check for the member fails.
        # *   DeleteFailed: The member fails to be deleted.
        self.status = status

    def validate(self):
        if self.fail_reason_list:
            for k in self.fail_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_time is not None:
            result['DeletionTime'] = self.deletion_time
        if self.deletion_type is not None:
            result['DeletionType'] = self.deletion_type
        result['FailReasonList'] = []
        if self.fail_reason_list is not None:
            for k in self.fail_reason_list:
                result['FailReasonList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionTime') is not None:
            self.deletion_time = m.get('DeletionTime')
        if m.get('DeletionType') is not None:
            self.deletion_type = m.get('DeletionType')
        self.fail_reason_list = []
        if m.get('FailReasonList') is not None:
            for k in m.get('FailReasonList'):
                temp_model = GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList()
                self.fail_reason_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAccountDeletionStatusResponseBody(TeaModel):
    def __init__(
        self,
        rd_account_deletion_status: GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus = None,
        request_id: str = None,
    ):
        # The deletion status of the member.
        self.rd_account_deletion_status = rd_account_deletion_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.rd_account_deletion_status:
            self.rd_account_deletion_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_account_deletion_status is not None:
            result['RdAccountDeletionStatus'] = self.rd_account_deletion_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RdAccountDeletionStatus') is not None:
            temp_model = GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus()
            self.rd_account_deletion_status = temp_model.from_map(m['RdAccountDeletionStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountDeletionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountDeletionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccountDeletionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoGroupingRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetAutoGroupingRuleResponseBodyRuleRuleContents(TeaModel):
    def __init__(
        self,
        auto_grouping_scope_condition: str = None,
        rule_content_id: str = None,
        target_resource_group_condition: str = None,
    ):
        # The condition for the range of resources that are automatically transferred.
        self.auto_grouping_scope_condition = auto_grouping_scope_condition
        # The ID of the content record.
        self.rule_content_id = rule_content_id
        # The condition for the destination resource group.
        self.target_resource_group_condition = target_resource_group_condition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_grouping_scope_condition is not None:
            result['AutoGroupingScopeCondition'] = self.auto_grouping_scope_condition
        if self.rule_content_id is not None:
            result['RuleContentId'] = self.rule_content_id
        if self.target_resource_group_condition is not None:
            result['TargetResourceGroupCondition'] = self.target_resource_group_condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoGroupingScopeCondition') is not None:
            self.auto_grouping_scope_condition = m.get('AutoGroupingScopeCondition')
        if m.get('RuleContentId') is not None:
            self.rule_content_id = m.get('RuleContentId')
        if m.get('TargetResourceGroupCondition') is not None:
            self.target_resource_group_condition = m.get('TargetResourceGroupCondition')
        return self


class GetAutoGroupingRuleResponseBodyRule(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_resource_types_scope: str = None,
        modify_time: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_types_scope: str = None,
        rule_contents: List[GetAutoGroupingRuleResponseBodyRuleRuleContents] = None,
        rule_desc: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        # The time when the rule was created.
        self.create_time = create_time
        # The IDs of excluded regions. Multiple IDs are separated by commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of excluded resource groups. Multiple IDs are separated by commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of excluded resources. Multiple IDs are separated by commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The excluded resource types. Multiple resource types are separated by commas (,).
        self.exclude_resource_types_scope = exclude_resource_types_scope
        # The time when the rule was modified.
        self.modify_time = modify_time
        # The IDs of regions. Multiple IDs are separated by commas (,).
        self.region_ids_scope = region_ids_scope
        # The IDs of resource groups. Multiple IDs are separated by commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of resources. Multiple IDs are separated by commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The resource types. Multiple resource types are separated by commas (,).
        self.resource_types_scope = resource_types_scope
        # The content records of the rule.
        self.rule_contents = rule_contents
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   custom_condition: custom transfer rule
        # *   associated_transfer: transfer rule for associated resources
        self.rule_type = rule_type

    def validate(self):
        if self.rule_contents:
            for k in self.rule_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope
        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.exclude_resource_types_scope is not None:
            result['ExcludeResourceTypesScope'] = self.exclude_resource_types_scope
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        result['RuleContents'] = []
        if self.rule_contents is not None:
            for k in self.rule_contents:
                result['RuleContents'].append(k.to_map() if k else None)
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')
        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ExcludeResourceTypesScope') is not None:
            self.exclude_resource_types_scope = m.get('ExcludeResourceTypesScope')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        self.rule_contents = []
        if m.get('RuleContents') is not None:
            for k in m.get('RuleContents'):
                temp_model = GetAutoGroupingRuleResponseBodyRuleRuleContents()
                self.rule_contents.append(temp_model.from_map(k))
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class GetAutoGroupingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule: GetAutoGroupingRuleResponseBodyRule = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rule.
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule is not None:
            result['Rule'] = self.rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rule') is not None:
            temp_model = GetAutoGroupingRuleResponseBodyRule()
            self.rule = temp_model.from_map(m['Rule'])
        return self


class GetAutoGroupingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoGroupingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAutoGroupingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoGroupingStatusResponseBody(TeaModel):
    def __init__(
        self,
        enable_existed_resources_transfer: bool = None,
        enable_status: str = None,
        request_id: str = None,
    ):
        # Indicates whether the Transfer Existing Associated Resources feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_existed_resources_transfer = enable_existed_resources_transfer
        # The status of the Automatic Resource Transfer feature. Valid values:
        # 
        # *   Enabling: The feature is being enabled.
        # *   Enable: The feature is enabled.
        # *   Partial_Enable: The transfer of associated resources is enabled, but custom transfer rule-based resource transfer is disabled. You can call the [EnableAutoGrouping](https://help.aliyun.com/document_detail/2870380.html) operation to enable custom transfer rule-based resource transfer.
        # *   Disable: The feature is disabled.
        self.enable_status = enable_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_existed_resources_transfer is not None:
            result['EnableExistedResourcesTransfer'] = self.enable_existed_resources_transfer
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExistedResourcesTransfer') is not None:
            self.enable_existed_resources_transfer = m.get('EnableExistedResourcesTransfer')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAutoGroupingStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoGroupingStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAutoGroupingStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetControlPolicyRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        policy_id: str = None,
    ):
        # The language in which you want to return the description of the access control policy. Valid values:
        # 
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        # 
        # >  This parameter is valid only for system access control policies.
        self.language = language
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class GetControlPolicyResponseBodyControlPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: str = None,
        create_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_document: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times that the access control policy is referenced.
        self.attachment_count = attachment_count
        # The time when the access control policy was created.
        self.create_date = create_date
        # The description of the access control policy.
        self.description = description
        # The effective scope of the access control policy. Valid values:
        # 
        # *   All: The access control policy is in effect for Alibaba Cloud accounts, RAM users, and RAM roles.
        # *   RAM: The access control policy is in effect only for RAM users and RAM roles.
        self.effect_scope = effect_scope
        # The document of the access control policy.
        self.policy_document = policy_document
        # The ID of the access control policy.
        self.policy_id = policy_id
        # The name of the access control policy.
        self.policy_name = policy_name
        # The type of the access control policy. Valid values:
        # 
        # *   System: system access control policy
        # *   Custom: custom access control policy
        self.policy_type = policy_type
        # The time when the access control policy was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        control_policy: GetControlPolicyResponseBodyControlPolicy = None,
        request_id: str = None,
    ):
        # The details of the access control policy.
        self.control_policy = control_policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = GetControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m['ControlPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetControlPolicyEnablementStatusResponseBody(TeaModel):
    def __init__(
        self,
        enablement_status: str = None,
        request_id: str = None,
    ):
        # The status of the Control Policy feature. Valid values:
        # 
        # *   Enabled: The Control Policy feature is enabled.
        # *   PendingEnable: The Control Policy feature is being enabled.
        # *   Disabled: The Control Policy feature is disabled.
        # *   PendingDisable: The Control Policy feature is being disabled.
        self.enablement_status = enablement_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enablement_status is not None:
            result['EnablementStatus'] = self.enablement_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablementStatus') is not None:
            self.enablement_status = m.get('EnablementStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetControlPolicyEnablementStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetControlPolicyEnablementStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetControlPolicyEnablementStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        # The ID of the folder.
        # 
        # This parameter is required.
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class GetFolderResponseBodyFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
        resource_directory_path: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The path of the folder in the resource directory.
        self.resource_directory_path = resource_directory_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        return self


class GetFolderResponseBody(TeaModel):
    def __init__(
        self,
        folder: GetFolderResponseBodyFolder = None,
        request_id: str = None,
    ):
        # The information of the folder.
        self.folder = folder
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = GetFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHandshakeRequest(TeaModel):
    def __init__(
        self,
        handshake_id: str = None,
    ):
        # The ID of the invitation.
        # 
        # This parameter is required.
        self.handshake_id = handshake_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class GetHandshakeResponseBodyHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        invited_account_real_name: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        master_account_real_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The real-name verification information of the invitee.
        # 
        # >  This parameter is available only when an invitee calls this operation.
        self.invited_account_real_name = invited_account_real_name
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The real-name verification information of the management account of the resource directory.
        # 
        # >  This parameter is available only when an invitee calls this operation.
        self.master_account_real_name = master_account_real_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The comment on the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited account.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.invited_account_real_name is not None:
            result['InvitedAccountRealName'] = self.invited_account_real_name
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.master_account_real_name is not None:
            result['MasterAccountRealName'] = self.master_account_real_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('InvitedAccountRealName') is not None:
            self.invited_account_real_name = m.get('InvitedAccountRealName')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('MasterAccountRealName') is not None:
            self.master_account_real_name = m.get('MasterAccountRealName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetHandshakeResponseBody(TeaModel):
    def __init__(
        self,
        handshake: GetHandshakeResponseBodyHandshake = None,
        request_id: str = None,
    ):
        # The information of the invitation.
        self.handshake = handshake
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = GetHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHandshakeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHandshakeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPayerForAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the account.
        # 
        # This parameter is required.
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


class GetPayerForAccountResponseBody(TeaModel):
    def __init__(
        self,
        payer_account_id: str = None,
        payer_account_name: str = None,
        request_id: str = None,
    ):
        # The ID of the settlement account.
        self.payer_account_id = payer_account_id
        # The name of the settlement account.
        self.payer_account_name = payer_account_name
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        if self.payer_account_name is not None:
            result['PayerAccountName'] = self.payer_account_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        if m.get('PayerAccountName') is not None:
            self.payer_account_name = m.get('PayerAccountName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPayerForAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPayerForAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPayerForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The language that is used to return the description of the system policy. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        # 
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: int = None,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times the policy is referenced.
        self.attachment_count = attachment_count
        # The time when the policy was created.
        self.create_date = create_date
        # The default version of the policy.
        self.default_version = default_version
        # The description of the policy.
        self.description = description
        # The document of the policy.
        self.policy_document = policy_document
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type
        # The time when the policy was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The information of the policy.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        version_id: str = None,
    ):
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The ID of the policy version.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        policy_document: str = None,
        version_id: str = None,
    ):
        # The time when the policy version was created.
        self.create_date = create_date
        # Indicates whether the policy version is the default version.
        self.is_default_version = is_default_version
        # The document of the policy.
        self.policy_document = policy_document
        # The ID of the policy version.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBody(TeaModel):
    def __init__(
        self,
        policy_version: GetPolicyVersionResponseBodyPolicyVersion = None,
        request_id: str = None,
    ):
        # The information of the policy version.
        self.policy_version = policy_version
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: GetPolicyVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(
        self,
        control_policy_status: str = None,
        create_time: str = None,
        identity_information: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        member_deletion_status: str = None,
        resource_directory_id: str = None,
        root_folder_id: str = None,
    ):
        # The status of the Control Policy feature. Valid values:
        # 
        # *   Enabled: The feature is enabled.
        # *   PendingEnable: The feature is being enabled.
        # *   Disabled: The feature is disabled.
        # *   PendingDisable: The feature is being disabled.
        self.control_policy_status = control_policy_status
        # The time when the resource directory was enabled.
        self.create_time = create_time
        # The real-name verification information.
        self.identity_information = identity_information
        # The ID of the management account.
        self.master_account_id = master_account_id
        # The name of the management account.
        self.master_account_name = master_account_name
        # The status of the member deletion feature. Valid values:
        # 
        # *   Enabled: The feature is enabled. You can call the [DeleteAccount](https://help.aliyun.com/document_detail/311546.html) operation to delete members of the resource account type.
        # *   Disabled: The feature is disabled. You cannot delete members of the resource account type.
        self.member_deletion_status = member_deletion_status
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The ID of the Root folder.
        self.root_folder_id = root_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy_status is not None:
            result['ControlPolicyStatus'] = self.control_policy_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.member_deletion_status is not None:
            result['MemberDeletionStatus'] = self.member_deletion_status
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicyStatus') is not None:
            self.control_policy_status = m.get('ControlPolicyStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('MemberDeletionStatus') is not None:
            self.member_deletion_status = m.get('MemberDeletionStatus')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class GetResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: GetResourceDirectoryResponseBodyResourceDirectory = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource directory.
        self.resource_directory = resource_directory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = GetResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class GetResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupRequest(TeaModel):
    def __init__(
        self,
        include_tags: bool = None,
        resource_group_id: str = None,
    ):
        # The ID of the request.
        self.include_tags = include_tags
        # Specifies whether to return the information of tags. Valid values:
        # 
        # *   false (default value)
        # *   true
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.region_id = region_id
        # The region ID.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(
        self,
        region_status: List[GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus] = None,
    ):
        self.region_status = region_status

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class GetResourceGroupResponseBodyResourceGroupTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag value.
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
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetResourceGroupResponseBodyResourceGroupTags(TeaModel):
    def __init__(
        self,
        tag: List[GetResourceGroupResponseBodyResourceGroupTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetResourceGroupResponseBodyResourceGroupTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        region_statuses: GetResourceGroupResponseBodyResourceGroupRegionStatuses = None,
        status: str = None,
        tags: GetResourceGroupResponseBodyResourceGroupTags = None,
    ):
        # The identifier of the resource group.
        self.account_id = account_id
        # The ID of the resource group.
        self.create_date = create_date
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.display_name = display_name
        # The tags that are added to the resource group.
        self.id = id
        # The time when the resource group was created. The time is displayed in UTC.
        self.name = name
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        # *   Deleting: The resource group is being deleted.
        self.region_statuses = region_statuses
        # The status of the resource group in all regions.
        self.status = status
        # The tag key.
        self.tags = tags

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroupTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class GetResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: GetResourceGroupResponseBodyResourceGroup = None,
    ):
        # The information of the resource group.
        self.request_id = request_id
        # The display name of the resource group.
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class GetResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        role_name: str = None,
    ):
        # The language that is used to return the description of the RAM role. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetRoleResponseBodyRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        # The time when the deletion task was created.
        self.create_date = create_date
        # The ID of the deletion task.
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: GetRoleResponseBodyRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.arn = arn
        # The document of the policy that specifies the trusted entity to assume the RAM role.
        self.assume_role_policy_document = assume_role_policy_document
        # The time when the RAM role was created.
        self.create_date = create_date
        # The description of the RAM role.
        self.description = description
        # Indicates whether the RAM role is a service linked role.
        self.is_service_linked_role = is_service_linked_role
        # The information of the most recent deletion task.
        self.latest_deletion_task = latest_deletion_task
        # The maximum session duration of the RAM role.
        self.max_session_duration = max_session_duration
        # The ID of the RAM role.
        self.role_id = role_id
        # The name of the RAM role.
        self.role_name = role_name
        # The name of the RAM role after authorization.
        self.role_principal_name = role_principal_name
        # The time when the RAM role was updated.
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = GetRoleResponseBodyRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: GetRoleResponseBodyRole = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the RAM role.
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = GetRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class GetRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLinkedRoleDeletionStatusRequest(TeaModel):
    def __init__(
        self,
        deletion_task_id: str = None,
    ):
        # The ID of the deletion task.
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources(TeaModel):
    def __init__(
        self,
        resource: List[str] = None,
    ):
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources = None,
    ):
        # The IDs of the regions in which the resources are to be queried.
        self.region = region
        # The returned resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources()
            self.resources = temp_model.from_map(m['Resources'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages(TeaModel):
    def __init__(
        self,
        role_usage: List[GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage] = None,
    ):
        self.role_usage = role_usage

    def validate(self):
        if self.role_usage:
            for k in self.role_usage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoleUsage'] = []
        if self.role_usage is not None:
            for k in self.role_usage:
                result['RoleUsage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_usage = []
        if m.get('RoleUsage') is not None:
            for k in m.get('RoleUsage'):
                temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage()
                self.role_usage.append(temp_model.from_map(k))
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReason(TeaModel):
    def __init__(
        self,
        message: str = None,
        role_usages: GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages = None,
    ):
        # Failure information.
        self.message = message
        # Use resource information of the service linked role.
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            self.role_usages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.role_usages is not None:
            result['RoleUsages'] = self.role_usages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RoleUsages') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages()
            self.role_usages = temp_model.from_map(m['RoleUsages'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseBody(TeaModel):
    def __init__(
        self,
        reason: GetServiceLinkedRoleDeletionStatusResponseBodyReason = None,
        request_id: str = None,
        status: str = None,
    ):
        # The reason why the deletion task failed.
        self.reason = reason
        # The ID of the request.
        self.request_id = request_id
        # The status of the task.
        # 
        # - SUCCEEDED
        # - IN_PROGRESS
        # - FAILED
        # - NOT_STARTED
        # - INTERNAL_ERROR
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceLinkedRoleDeletionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceLinkedRoleDeletionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        resource_directory_id: str = None,
        root_folder_id: str = None,
    ):
        # The time when the resource directory was enabled.
        self.create_time = create_time
        # The ID of the enterprise management account.
        self.master_account_id = master_account_id
        # The name of the enterprise management account.
        self.master_account_name = master_account_name
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The ID of the root folder.
        self.root_folder_id = root_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class InitResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_directory: InitResourceDirectoryResponseBodyResourceDirectory = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource directory.
        self.resource_directory = resource_directory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = InitResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class InitResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InviteAccountToResourceDirectoryRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class InviteAccountToResourceDirectoryRequest(TeaModel):
    def __init__(
        self,
        note: str = None,
        tag: List[InviteAccountToResourceDirectoryRequestTag] = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The comment on the invitation.
        # 
        # The comment can be up to 1,024 characters in length.
        self.note = note
        # The tag key and value.
        self.tag = tag
        # The ID or logon email address of the account that you want to invite.
        # 
        # This parameter is required.
        self.target_entity = target_entity
        # The type of the account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        # 
        # This parameter is required.
        self.target_type = target_type

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
        if self.note is not None:
            result['Note'] = self.note
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = InviteAccountToResourceDirectoryRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class InviteAccountToResourceDirectoryResponseBodyHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The comment on the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation.
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited account.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class InviteAccountToResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        handshake: InviteAccountToResourceDirectoryResponseBodyHandshake = None,
        request_id: str = None,
    ):
        # The information of the invitation.
        self.handshake = handshake
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = InviteAccountToResourceDirectoryResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InviteAccountToResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InviteAccountToResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InviteAccountToResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAccountsRequest(TeaModel):
    def __init__(
        self,
        include_tags: bool = None,
        page_number: int = None,
        page_size: int = None,
        tag: List[ListAccountsRequestTag] = None,
    ):
        # Specifies whether to return the information of tags. Valid values:
        # 
        # *   false (default value)
        # *   true
        self.include_tags = include_tags
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The tag key and value.
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
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBodyAccountsAccountTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAccountsResponseBodyAccountsAccountTags(TeaModel):
    def __init__(
        self,
        tag: List[ListAccountsResponseBodyAccountsAccountTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsResponseBodyAccountsAccountTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        resource_directory_path: str = None,
        status: str = None,
        tags: ListAccountsResponseBodyAccountsAccountTags = None,
        type: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The display name of the member.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member joins the resource directory. Valid values:
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member joined the resource directory. The time is displayed in UTC.
        self.join_time = join_time
        # The time when the member was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The path of the member in the resource directory.
        self.resource_directory_path = resource_directory_path
        # The status of the member. Valid values:
        # 
        # *   CreateSuccess: The member is created.
        # *   PromoteVerifying: The upgrade of the member is being confirmed.
        # *   PromoteFailed: The upgrade of the member fails.
        # *   PromoteExpired: The upgrade of the member expires.
        # *   PromoteCancelled: The upgrade of the member is canceled.
        # *   PromoteSuccess: The member is upgraded.
        # *   InviteSuccess: The member accepts the invitation.
        self.status = status
        # The tags that are added to the member.
        self.tags = tags
        # The type of the member. Valid values:
        # 
        # *   CloudAccount: cloud account
        # *   ResourceAccount: resource account
        self.type = type

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListAccountsResponseBodyAccountsAccountTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountsResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListAccountsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBody(TeaModel):
    def __init__(
        self,
        accounts: ListAccountsResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The members returned.
        self.accounts = accounts
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsForParentRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAccountsForParentRequest(TeaModel):
    def __init__(
        self,
        include_tags: bool = None,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
        tag: List[ListAccountsForParentRequestTag] = None,
    ):
        # Specifies whether to return the information of tags. Valid values:
        # 
        # false (default value)
        # 
        # true
        self.include_tags = include_tags
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The ID of the folder.
        self.parent_folder_id = parent_folder_id
        # The keyword used for the query, such as the display name of a member.
        # 
        # Fuzzy match is supported.
        self.query_keyword = query_keyword
        # The tag key and value.
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
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsForParentRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBodyAccountsAccountTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAccountsForParentResponseBodyAccountsAccountTags(TeaModel):
    def __init__(
        self,
        tag: List[ListAccountsForParentResponseBodyAccountsAccountTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsForParentResponseBodyAccountsAccountTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        tags: ListAccountsForParentResponseBodyAccountsAccountTags = None,
        type: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The display name of the member.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member joins the resource directory.
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member joined the resource directory. The time is displayed in UTC.
        self.join_time = join_time
        # The time when the member was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member. Valid values:
        # 
        # *   CreateSuccess: The member is created.
        # *   PromoteVerifying: The upgrade of the member is being confirmed.
        # *   PromoteFailed: The upgrade of the member fails.
        # *   PromoteExpired: The upgrade of the member expires.
        # *   PromoteCancelled: The upgrade of the member is canceled.
        # *   PromoteSuccess: The member is upgraded.
        # *   InviteSuccess: The member accepts the invitation.
        self.status = status
        # The tags that are added to the member.
        self.tags = tags
        # The type of the member.
        # 
        # *   CloudAccount: cloud account
        # *   ResourceAccount: resource account
        self.type = type

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListAccountsForParentResponseBodyAccountsAccountTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountsForParentResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListAccountsForParentResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsForParentResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBody(TeaModel):
    def __init__(
        self,
        accounts: ListAccountsForParentResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of the members.
        self.accounts = accounts
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListAccountsForParentResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountsForParentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsForParentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountsForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAncestorsRequest(TeaModel):
    def __init__(
        self,
        child_id: str = None,
    ):
        # The ID of the child folder.
        # 
        # This parameter is required.
        self.child_id = child_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_id is not None:
            result['ChildId'] = self.child_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildId') is not None:
            self.child_id = m.get('ChildId')
        return self


class ListAncestorsResponseBodyFoldersFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class ListAncestorsResponseBodyFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListAncestorsResponseBodyFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListAncestorsResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListAncestorsResponseBody(TeaModel):
    def __init__(
        self,
        folders: ListAncestorsResponseBodyFolders = None,
        request_id: str = None,
    ):
        # The information of the folders.
        self.folders = folders
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = ListAncestorsResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAncestorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAncestorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAncestorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssociatedTransferSettingResponseBodyAssociatedTransferSettingRuleSettings(TeaModel):
    def __init__(
        self,
        associated_resource_type: str = None,
        associated_service: str = None,
        master_resource_type: str = None,
        master_service: str = None,
        status: str = None,
    ):
        # The type of the associated resource.
        self.associated_resource_type = associated_resource_type
        # The service code of the associated resource.
        self.associated_service = associated_service
        # The type of the primary resource.
        self.master_resource_type = master_resource_type
        # The service code of the primary resource.
        self.master_service = master_service
        # The status of the Transfer Associated Resources feature. Valid values:
        # 
        # *   Enable: enabled
        # *   Disable: disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associated_resource_type is not None:
            result['AssociatedResourceType'] = self.associated_resource_type
        if self.associated_service is not None:
            result['AssociatedService'] = self.associated_service
        if self.master_resource_type is not None:
            result['MasterResourceType'] = self.master_resource_type
        if self.master_service is not None:
            result['MasterService'] = self.master_service
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedResourceType') is not None:
            self.associated_resource_type = m.get('AssociatedResourceType')
        if m.get('AssociatedService') is not None:
            self.associated_service = m.get('AssociatedService')
        if m.get('MasterResourceType') is not None:
            self.master_resource_type = m.get('MasterResourceType')
        if m.get('MasterService') is not None:
            self.master_service = m.get('MasterService')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAssociatedTransferSettingResponseBodyAssociatedTransferSetting(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        enable_existing_resources_transfer: str = None,
        rule_settings: List[ListAssociatedTransferSettingResponseBodyAssociatedTransferSettingRuleSettings] = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # Indicates whether the Transfer Existing Associated Resources feature is enabled. Valid values:
        # 
        # *   false
        # *   true
        self.enable_existing_resources_transfer = enable_existing_resources_transfer
        # The settings of transfer rules.
        self.rule_settings = rule_settings
        # The status of the Transfer Associated Resources feature. Valid values:
        # 
        # *   Enable: enabled
        # *   Disable: disabled
        self.status = status

    def validate(self):
        if self.rule_settings:
            for k in self.rule_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.enable_existing_resources_transfer is not None:
            result['EnableExistingResourcesTransfer'] = self.enable_existing_resources_transfer
        result['RuleSettings'] = []
        if self.rule_settings is not None:
            for k in self.rule_settings:
                result['RuleSettings'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('EnableExistingResourcesTransfer') is not None:
            self.enable_existing_resources_transfer = m.get('EnableExistingResourcesTransfer')
        self.rule_settings = []
        if m.get('RuleSettings') is not None:
            for k in m.get('RuleSettings'):
                temp_model = ListAssociatedTransferSettingResponseBodyAssociatedTransferSettingRuleSettings()
                self.rule_settings.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAssociatedTransferSettingResponseBody(TeaModel):
    def __init__(
        self,
        associated_transfer_setting: ListAssociatedTransferSettingResponseBodyAssociatedTransferSetting = None,
        request_id: str = None,
    ):
        # The settings of the Transfer Associated Resources feature.
        self.associated_transfer_setting = associated_transfer_setting
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.associated_transfer_setting:
            self.associated_transfer_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associated_transfer_setting is not None:
            result['AssociatedTransferSetting'] = self.associated_transfer_setting.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedTransferSetting') is not None:
            temp_model = ListAssociatedTransferSettingResponseBodyAssociatedTransferSetting()
            self.associated_transfer_setting = temp_model.from_map(m['AssociatedTransferSetting'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAssociatedTransferSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAssociatedTransferSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAssociatedTransferSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoGroupingRulesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        # The maximum number of entries to return for a single request. Valid values: 1 to 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   custom_condition: custom transfer rule
        # *   associated_transfer: transfer rule for associated resources
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListAutoGroupingRulesResponseBodyRulesRuleContents(TeaModel):
    def __init__(
        self,
        auto_grouping_scope_condition: str = None,
        rule_content_id: str = None,
        target_resource_group_condition: str = None,
    ):
        # The condition for the range of resources that are automatically transferred.
        self.auto_grouping_scope_condition = auto_grouping_scope_condition
        # The ID of the content record.
        self.rule_content_id = rule_content_id
        # The condition for the destination resource group.
        self.target_resource_group_condition = target_resource_group_condition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_grouping_scope_condition is not None:
            result['AutoGroupingScopeCondition'] = self.auto_grouping_scope_condition
        if self.rule_content_id is not None:
            result['RuleContentId'] = self.rule_content_id
        if self.target_resource_group_condition is not None:
            result['TargetResourceGroupCondition'] = self.target_resource_group_condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoGroupingScopeCondition') is not None:
            self.auto_grouping_scope_condition = m.get('AutoGroupingScopeCondition')
        if m.get('RuleContentId') is not None:
            self.rule_content_id = m.get('RuleContentId')
        if m.get('TargetResourceGroupCondition') is not None:
            self.target_resource_group_condition = m.get('TargetResourceGroupCondition')
        return self


class ListAutoGroupingRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_resource_types_scope: str = None,
        modify_time: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_types_scope: str = None,
        rule_contents: List[ListAutoGroupingRulesResponseBodyRulesRuleContents] = None,
        rule_desc: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        # The time when the rule was created.
        self.create_time = create_time
        # The IDs of excluded regions. Multiple IDs are separated by commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of excluded resource groups. Multiple IDs are separated by commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of excluded resources. Multiple IDs are separated by commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The excluded resource types. Multiple resource types are separated by commas (,).
        self.exclude_resource_types_scope = exclude_resource_types_scope
        # The time when the rule was updated.
        self.modify_time = modify_time
        # The IDs of regions. Multiple IDs are separated by commas (,).
        self.region_ids_scope = region_ids_scope
        # The IDs of resource groups. Multiple IDs are separated by commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of resources. Multiple IDs are separated by commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The resource types. Multiple resource types are separated by commas (,).
        self.resource_types_scope = resource_types_scope
        # The content records of the rule.
        self.rule_contents = rule_contents
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   custom_condition: custom transfer rule
        # *   associated_transfer: transfer rule for associated resources
        self.rule_type = rule_type

    def validate(self):
        if self.rule_contents:
            for k in self.rule_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope
        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.exclude_resource_types_scope is not None:
            result['ExcludeResourceTypesScope'] = self.exclude_resource_types_scope
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        result['RuleContents'] = []
        if self.rule_contents is not None:
            for k in self.rule_contents:
                result['RuleContents'].append(k.to_map() if k else None)
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')
        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ExcludeResourceTypesScope') is not None:
            self.exclude_resource_types_scope = m.get('ExcludeResourceTypesScope')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        self.rule_contents = []
        if m.get('RuleContents') is not None:
            for k in m.get('RuleContents'):
                temp_model = ListAutoGroupingRulesResponseBodyRulesRuleContents()
                self.rule_contents.append(temp_model.from_map(k))
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListAutoGroupingRulesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rules: List[ListAutoGroupingRulesResponseBodyRules] = None,
    ):
        # The maximum number of entries returned for a single request. Valid values: 1 to 50.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The queried rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListAutoGroupingRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class ListAutoGroupingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAutoGroupingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAutoGroupingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListControlPoliciesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_type: str = None,
    ):
        # The language in which you want to return the descriptions of the access control policies. Valid values:
        # 
        # - zh-CN (default value): Chinese
        # - en: English
        # - ja: Japanese
        # 
        # >  This parameter is valid only for system access control policies.
        self.language = language
        # The number of the page to return. 
        # 
        # Page start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. 
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The type of the access control policy. Valid values:
        # 
        # - System: system access control policy
        # - Custom: custom access control policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListControlPoliciesResponseBodyControlPoliciesControlPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: str = None,
        create_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times that the access control policy is referenced.
        self.attachment_count = attachment_count
        # The time when the access control policy was created.
        self.create_date = create_date
        # The description of the access control policy.
        self.description = description
        # The effective scope of the access control policy. Valid values:
        # 
        # - All: The access control policy is in effect for Alibaba Cloud accounts, RAM users, and RAM roles.
        # - RAM: The access control policy is in effect only for RAM users and RAM roles.
        self.effect_scope = effect_scope
        # The ID of the access control policy.
        self.policy_id = policy_id
        # The name of the access control policy.
        self.policy_name = policy_name
        # The type of the access control policy. Valid values:
        # 
        # - System: system access control policy
        # - Custom: custom access control policy
        self.policy_type = policy_type
        # The time when the access control policy was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListControlPoliciesResponseBodyControlPolicies(TeaModel):
    def __init__(
        self,
        control_policy: List[ListControlPoliciesResponseBodyControlPoliciesControlPolicy] = None,
    ):
        self.control_policy = control_policy

    def validate(self):
        if self.control_policy:
            for k in self.control_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ControlPolicy'] = []
        if self.control_policy is not None:
            for k in self.control_policy:
                result['ControlPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_policy = []
        if m.get('ControlPolicy') is not None:
            for k in m.get('ControlPolicy'):
                temp_model = ListControlPoliciesResponseBodyControlPoliciesControlPolicy()
                self.control_policy.append(temp_model.from_map(k))
        return self


class ListControlPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        control_policies: ListControlPoliciesResponseBodyControlPolicies = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The access control policies.
        self.control_policies = control_policies
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of access control policies.
        self.total_count = total_count

    def validate(self):
        if self.control_policies:
            self.control_policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policies is not None:
            result['ControlPolicies'] = self.control_policies.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicies') is not None:
            temp_model = ListControlPoliciesResponseBodyControlPolicies()
            self.control_policies = temp_model.from_map(m['ControlPolicies'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListControlPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListControlPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListControlPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListControlPolicyAttachmentsForTargetRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        target_id: str = None,
    ):
        # The language in which you want to return the descriptions of the access control policies. Valid values:
        # 
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        # 
        # >  This parameter is valid only for system access control policies.
        self.language = language
        # The ID of the object whose access control policies you want to query. Access control policies can be attached to the following objects:
        # 
        # *   Root folder
        # *   Subfolders of the Root folder
        # *   Members
        # 
        # This parameter is required.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment(TeaModel):
    def __init__(
        self,
        attach_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The time when the access control policy was attached.
        self.attach_date = attach_date
        # The description of the access control policy.
        self.description = description
        # The effective scope of the access control policy. Valid values:
        # 
        # *   All: The access control policy is in effect for Alibaba Cloud accounts, RAM users, and RAM roles.
        # *   RAM: The access control policy is in effect only for RAM users and RAM roles.
        self.effect_scope = effect_scope
        # The ID of the access control policy.
        self.policy_id = policy_id
        # The name of the access control policy.
        self.policy_name = policy_name
        # The type of the access control policy. Valid values:
        # 
        # *   System: system access control policy
        # *   Custom: custom access control policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments(TeaModel):
    def __init__(
        self,
        control_policy_attachment: List[ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment] = None,
    ):
        self.control_policy_attachment = control_policy_attachment

    def validate(self):
        if self.control_policy_attachment:
            for k in self.control_policy_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ControlPolicyAttachment'] = []
        if self.control_policy_attachment is not None:
            for k in self.control_policy_attachment:
                result['ControlPolicyAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.control_policy_attachment = []
        if m.get('ControlPolicyAttachment') is not None:
            for k in m.get('ControlPolicyAttachment'):
                temp_model = ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment()
                self.control_policy_attachment.append(temp_model.from_map(k))
        return self


class ListControlPolicyAttachmentsForTargetResponseBody(TeaModel):
    def __init__(
        self,
        control_policy_attachments: ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments = None,
        request_id: str = None,
    ):
        # The attached access control policies.
        self.control_policy_attachments = control_policy_attachments
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.control_policy_attachments:
            self.control_policy_attachments.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy_attachments is not None:
            result['ControlPolicyAttachments'] = self.control_policy_attachments.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicyAttachments') is not None:
            temp_model = ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments()
            self.control_policy_attachments = temp_model.from_map(m['ControlPolicyAttachments'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListControlPolicyAttachmentsForTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListControlPolicyAttachmentsForTargetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListControlPolicyAttachmentsForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDelegatedAdministratorsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        service_principal: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The identifier of the trusted service.
        # 
        # For more information, see the `Trusted service identifier` column in [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListDelegatedAdministratorsResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        delegation_enabled_time: str = None,
        display_name: str = None,
        join_method: str = None,
        service_principal: str = None,
    ):
        # The ID of the member.
        self.account_id = account_id
        # The time when the member was specified as a delegated administrator account.
        self.delegation_enabled_time = delegation_enabled_time
        # The display name of the member.
        self.display_name = display_name
        # The way in which the member joins the resource directory. Valid values:
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The identifier of the trusted service.
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delegation_enabled_time is not None:
            result['DelegationEnabledTime'] = self.delegation_enabled_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DelegationEnabledTime') is not None:
            self.delegation_enabled_time = m.get('DelegationEnabledTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListDelegatedAdministratorsResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[ListDelegatedAdministratorsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListDelegatedAdministratorsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListDelegatedAdministratorsResponseBody(TeaModel):
    def __init__(
        self,
        accounts: ListDelegatedAdministratorsResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of the delegated administrator accounts.
        self.accounts = accounts
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListDelegatedAdministratorsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDelegatedAdministratorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDelegatedAdministratorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDelegatedAdministratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDelegatedServicesForAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the member.
        # 
        # This parameter is required.
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


class ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService(TeaModel):
    def __init__(
        self,
        delegation_enabled_time: str = None,
        service_principal: str = None,
        status: str = None,
    ):
        # The time when the member was specified as a delegated administrator account of the trusted service.
        self.delegation_enabled_time = delegation_enabled_time
        # The identification of the trusted service.
        self.service_principal = service_principal
        # The status of the trusted service. Valid values:
        # 
        # *   ENABLED: enabled
        # *   DISABLED: disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegation_enabled_time is not None:
            result['DelegationEnabledTime'] = self.delegation_enabled_time
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegationEnabledTime') is not None:
            self.delegation_enabled_time = m.get('DelegationEnabledTime')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDelegatedServicesForAccountResponseBodyDelegatedServices(TeaModel):
    def __init__(
        self,
        delegated_service: List[ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService] = None,
    ):
        self.delegated_service = delegated_service

    def validate(self):
        if self.delegated_service:
            for k in self.delegated_service:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DelegatedService'] = []
        if self.delegated_service is not None:
            for k in self.delegated_service:
                result['DelegatedService'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delegated_service = []
        if m.get('DelegatedService') is not None:
            for k in m.get('DelegatedService'):
                temp_model = ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService()
                self.delegated_service.append(temp_model.from_map(k))
        return self


class ListDelegatedServicesForAccountResponseBody(TeaModel):
    def __init__(
        self,
        delegated_services: ListDelegatedServicesForAccountResponseBodyDelegatedServices = None,
        request_id: str = None,
    ):
        # The trusted services.
        # 
        # >  If the value of this parameter is empty, the member is not specified as a delegated administrator account.
        self.delegated_services = delegated_services
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.delegated_services:
            self.delegated_services.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegated_services is not None:
            result['DelegatedServices'] = self.delegated_services.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegatedServices') is not None:
            temp_model = ListDelegatedServicesForAccountResponseBodyDelegatedServices()
            self.delegated_services = temp_model.from_map(m['DelegatedServices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDelegatedServicesForAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDelegatedServicesForAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDelegatedServicesForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoldersForParentRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The ID of the parent folder.
        # 
        # If you leave this parameter empty, the information of the first-level subfolders of the Root folder is queried.
        self.parent_folder_id = parent_folder_id
        # The keyword used for the query, such as a folder name.
        # 
        # Fuzzy match is supported.
        self.query_keyword = query_keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        return self


class ListFoldersForParentResponseBodyFoldersFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class ListFoldersForParentResponseBodyFolders(TeaModel):
    def __init__(
        self,
        folder: List[ListFoldersForParentResponseBodyFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListFoldersForParentResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListFoldersForParentResponseBody(TeaModel):
    def __init__(
        self,
        folders: ListFoldersForParentResponseBodyFolders = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of the folders.
        self.folders = folders
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = ListFoldersForParentResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFoldersForParentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFoldersForParentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFoldersForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHandshakesForAccountRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHandshakesForAccountResponseBodyHandshakesHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The comment on the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited Alibaba Cloud account.
        self.target_entity = target_entity
        # The type of the invited Alibaba Cloud account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListHandshakesForAccountResponseBodyHandshakes(TeaModel):
    def __init__(
        self,
        handshake: List[ListHandshakesForAccountResponseBodyHandshakesHandshake] = None,
    ):
        self.handshake = handshake

    def validate(self):
        if self.handshake:
            for k in self.handshake:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Handshake'] = []
        if self.handshake is not None:
            for k in self.handshake:
                result['Handshake'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.handshake = []
        if m.get('Handshake') is not None:
            for k in m.get('Handshake'):
                temp_model = ListHandshakesForAccountResponseBodyHandshakesHandshake()
                self.handshake.append(temp_model.from_map(k))
        return self


class ListHandshakesForAccountResponseBody(TeaModel):
    def __init__(
        self,
        handshakes: ListHandshakesForAccountResponseBodyHandshakes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of the invitations.
        self.handshakes = handshakes
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of invitations.
        self.total_count = total_count

    def validate(self):
        if self.handshakes:
            self.handshakes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshakes is not None:
            result['Handshakes'] = self.handshakes.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshakes') is not None:
            temp_model = ListHandshakesForAccountResponseBodyHandshakes()
            self.handshakes = temp_model.from_map(m['Handshakes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHandshakesForAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHandshakesForAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHandshakesForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHandshakesForResourceDirectoryRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        handshake_id: str = None,
        master_account_id: str = None,
        master_account_name: str = None,
        modify_time: str = None,
        note: str = None,
        resource_directory_id: str = None,
        status: str = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the invitation expires. The time is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the invitation.
        self.handshake_id = handshake_id
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The comment on the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Declined: The invitation is rejected.
        # *   Expired: The invitation expires.
        self.status = status
        # The ID or logon email address of the invited account.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListHandshakesForResourceDirectoryResponseBodyHandshakes(TeaModel):
    def __init__(
        self,
        handshake: List[ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake] = None,
    ):
        self.handshake = handshake

    def validate(self):
        if self.handshake:
            for k in self.handshake:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Handshake'] = []
        if self.handshake is not None:
            for k in self.handshake:
                result['Handshake'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.handshake = []
        if m.get('Handshake') is not None:
            for k in m.get('Handshake'):
                temp_model = ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake()
                self.handshake.append(temp_model.from_map(k))
        return self


class ListHandshakesForResourceDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        handshakes: ListHandshakesForResourceDirectoryResponseBodyHandshakes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of the invitations.
        self.handshakes = handshakes
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.handshakes:
            self.handshakes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshakes is not None:
            result['Handshakes'] = self.handshakes.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handshakes') is not None:
            temp_model = ListHandshakesForResourceDirectoryResponseBodyHandshakes()
            self.handshakes = temp_model.from_map(m['Handshakes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHandshakesForResourceDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHandshakesForResourceDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListHandshakesForResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_type: str = None,
    ):
        # The language that is used to return the description of the system policy. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The type of the policy. If you do not specify this parameter, the system lists all types of policies. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesResponseBodyPoliciesPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: int = None,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times the policy is referenced.
        self.attachment_count = attachment_count
        # The time when the policy was created.
        self.create_date = create_date
        # The default version of the policy.
        self.default_version = default_version
        # The description of the policy.
        self.description = description
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type
        # The time when the policy was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        page_number: int = None,
        page_size: int = None,
        policies: ListPoliciesResponseBodyPolicies = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The information of the policies.
        self.policies = policies
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Policies') is not None:
            temp_model = ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyAttachmentsRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        # The language that is used to return the description of the system policy. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        self.policy_name = policy_name
        # The type of the policy. If you do not specify this parameter, the system lists all types of policies. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type
        # The name of the object to which the policy is attached.
        self.principal_name = principal_name
        # The type of the object to which the policy is attached. If you do not specify this parameter, the system lists all types of objects. Valid values:
        # 
        # *   IMSUser: RAM user
        # *   IMSGroup: RAM user group
        # *   ServiceRole: RAM role
        self.principal_type = principal_type
        # The ID of the resource group or the ID of the Alibaba Cloud account to which the resource group belongs. If you do not specify this parameter, the system lists all policy attachment records under the current account.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment(TeaModel):
    def __init__(
        self,
        attach_date: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        # The time when the policy was attached.
        self.attach_date = attach_date
        # The description of the policy.
        self.description = description
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        self.policy_type = policy_type
        # The name of the object to which the policy is attached.
        self.principal_name = principal_name
        # The type of the object to which the policy is attached. Valid values:
        # 
        # *   IMSUser: RAM user
        # *   IMSGroup: RAM user group
        # *   ServiceRole: RAM role
        self.principal_type = principal_type
        # The ID of the resource group or the ID of the Alibaba Cloud account to which the resource group belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListPolicyAttachmentsResponseBodyPolicyAttachments(TeaModel):
    def __init__(
        self,
        policy_attachment: List[ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment] = None,
    ):
        self.policy_attachment = policy_attachment

    def validate(self):
        if self.policy_attachment:
            for k in self.policy_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyAttachment'] = []
        if self.policy_attachment is not None:
            for k in self.policy_attachment:
                result['PolicyAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_attachment = []
        if m.get('PolicyAttachment') is not None:
            for k in m.get('PolicyAttachment'):
                temp_model = ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment()
                self.policy_attachment.append(temp_model.from_map(k))
        return self


class ListPolicyAttachmentsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policy_attachments: ListPolicyAttachmentsResponseBodyPolicyAttachments = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The policy attachment records.
        self.policy_attachments = policy_attachments
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.policy_attachments:
            self.policy_attachments.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_attachments is not None:
            result['PolicyAttachments'] = self.policy_attachments.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyAttachments') is not None:
            temp_model = ListPolicyAttachmentsResponseBodyPolicyAttachments()
            self.policy_attachments = temp_model.from_map(m['PolicyAttachments'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPolicyAttachmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyAttachmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPolicyAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyVersionsRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   Custom: custom policy
        # *   System: system policy
        # 
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        is_default_version: bool = None,
        version_id: str = None,
    ):
        # The time when the policy version was created.
        self.create_date = create_date
        # Indicates whether the policy version is the default version.
        self.is_default_version = is_default_version
        # The ID of the policy version.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        policy_versions: ListPolicyVersionsResponseBodyPolicyVersions = None,
        request_id: str = None,
    ):
        # The information of the policy versions.
        self.policy_versions = policy_versions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy_versions:
            self.policy_versions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_versions is not None:
            result['PolicyVersions'] = self.policy_versions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersions') is not None:
            temp_model = ListPolicyVersionsResponseBodyPolicyVersions()
            self.policy_versions = temp_model.from_map(m['PolicyVersions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPolicyVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPolicyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        include_tags: bool = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_group_ids: List[str] = None,
        status: str = None,
        tag: List[ListResourceGroupsRequestTag] = None,
    ):
        # The display name of the resource group. This parameter specifies a filter condition for the query. Fuzzy match is supported.
        # 
        # The display name can be a maximum of 50 characters in length.
        self.display_name = display_name
        # Specifies whether to return the information of tags. Valid values:
        # 
        # *   false (default value)
        # *   true
        # 
        # >  If you configure the Tag parameter, the system returns the information of tags regardless of the setting of the `IncludeTags` parameter.
        self.include_tags = include_tags
        # The identifier of the resource group. This parameter specifies a filter condition for the query. Fuzzy match is supported.
        # 
        # The identifier can be a maximum of 50 characters in length and can contain letters, digits, and hyphens (-).
        self.name = name
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group. This parameter specifies a filter condition for the query.
        # 
        # The ID can be a maximum of 18 characters in length and must start with `rg-`.
        # 
        # >  This parameter is incorporated into the `ResourceGroupIds` parameter. If you configure both the `ResourceGroupId` and `ResourceGroupIds` parameters, the value of the `ResourceGroupIds` parameter prevails.
        self.resource_group_id = resource_group_id
        # The IDs of the resource groups. This parameter specifies a filter condition for the query.
        # 
        # You can specify a maximum of 100 resource group IDs.
        # 
        # >  If you configure both the `ResourceGroupId` and `ResourceGroupIds` parameters, the value of the `ResourceGroupIds` parameter prevails.
        self.resource_group_ids = resource_group_ids
        # The status of the resource group. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status
        # The tag. This parameter specifies a filter condition for the query.
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
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListResourceGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags(TeaModel):
    def __init__(
        self,
        tag: List[ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
        tags: ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The identifier of the resource group.
        self.name = name
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status
        # The tags that are added to the resource group.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListResourceGroupsResponseBodyResourceGroups(TeaModel):
    def __init__(
        self,
        resource_group: List[ListResourceGroupsResponseBodyResourceGroupsResourceGroup] = None,
    ):
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            for k in self.resource_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k in self.resource_group:
                result['ResourceGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k in m.get('ResourceGroup'):
                temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroup()
                self.resource_group.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resource_groups: ListResourceGroupsResponseBodyResourceGroups = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource groups.
        self.resource_groups = resource_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resource_groups:
            self.resource_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroups') is not None:
            temp_model = ListResourceGroupsResponseBodyResourceGroups()
            self.resource_groups = temp_model.from_map(m['ResourceGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequestResourceTypes(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        service: str = None,
    ):
        # The resource type.
        # 
        # Valid values of N: 1 to 50.
        # 
        # For more information about the supported resource types, see the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        # 
        # >  You must configure both `Service` and `ResourceType` in `ResourceTypes`. Otherwise, the two parameters do not take effect.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        # 
        # Valid values of N: 1 to 50.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        # 
        # >  You must configure both `Service` and `ResourceType` in `ResourceTypes`. Otherwise, the two parameters do not take effect.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_types: List[ListResourcesRequestResourceTypes] = None,
        service: str = None,
    ):
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type.
        # 
        # For more information about the supported resource types, see the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.resource_type = resource_type
        # The resource types. A maximum of 50 resource types are supported.
        # 
        # >  If you configure `ResourceTypes`, you must configure both `Service` and `ResourceType`. Otherwise, the configured Service or ResourceType does not take effect.
        self.resource_types = resource_types
        # The ID of the Alibaba Cloud service.
        # 
        # You can obtain the ID from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.service = service

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['ResourceTypes'].append(k.to_map() if k else None)
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k in m.get('ResourceTypes'):
                temp_model = ListResourcesRequestResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ListResourcesResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
    ):
        # The time when the resource was created. The time is displayed in UTC.
        self.create_date = create_date
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[ListResourcesResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListResourcesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: ListResourcesResponseBodyResources = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the resources.
        self.resources = resources
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = ListResourcesResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListRolesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language that is used to return the descriptions of the RAM roles. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRolesResponseBodyRolesRoleLatestDeletionTask(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        # The time when the deletion task was created.
        self.create_date = create_date
        # The ID of the deletion task.
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class ListRolesResponseBodyRolesRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: ListRolesResponseBodyRolesRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.arn = arn
        # The time when the RAM role was created.
        self.create_date = create_date
        # The description of the RAM role.
        self.description = description
        # Indicates whether the RAM role is a service linked role.
        self.is_service_linked_role = is_service_linked_role
        # The information of the most recent deletion task.
        self.latest_deletion_task = latest_deletion_task
        # The maximum session duration of the RAM role.
        self.max_session_duration = max_session_duration
        # The ID of the RAM role.
        self.role_id = role_id
        # The name of the RAM role.
        self.role_name = role_name
        # The name of the RAM role after authorization.
        self.role_principal_name = role_principal_name
        # The time when the RAM role was updated.
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = ListRolesResponseBodyRolesRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        roles: ListRolesResponseBodyRoles = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The information of the RAM roles.
        self.roles = roles
        # The total number of RAM roles.
        self.total_count = total_count

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Roles') is not None:
            temp_model = ListRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRolesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        key_filter: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
    ):
        # The tag key for a fuzzy query.
        self.key_filter = key_filter
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The resource type.
        # 
        # The value Account indicates the members of the resource directory.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_filter is not None:
            result['KeyFilter'] = self.key_filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyFilter') is not None:
            self.key_filter = m.get('KeyFilter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
    ):
        # The tag key.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tags: List[ListTagKeysResponseBodyTags] = None,
    ):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the tag keys.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagKeysResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        self.key = key
        # A tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The resource ID.
        self.resource_id = resource_id
        # The type of the objects whose tags you want to query. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   ResourceGroup: resource group. This is the default value.
        # *   Account: member.
        self.resource_type = resource_type
        # The tag key and value.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource group or member.
        self.resource_id = resource_id
        # The type of the object whose tags are queried. Valid values:
        # 
        # *   resourcegroup: resource group
        # *   Account: member
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tags.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
        tag_key: str = None,
        value_filter: str = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The resource type.
        # 
        # The value Account indicates the members of the resource directory.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag key. This parameter specifies a filter condition for the query.
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The tag value for a fuzzy query.
        self.value_filter = value_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.value_filter is not None:
            result['ValueFilter'] = self.value_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('ValueFilter') is not None:
            self.value_filter = m.get('ValueFilter')
        return self


class ListTagValuesResponseBodyTags(TeaModel):
    def __init__(
        self,
        value: str = None,
    ):
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tags: List[ListTagValuesResponseBodyTags] = None,
    ):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information of the tag values.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagValuesResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetAttachmentsForControlPolicyRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policy_id: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The ID of the control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment(TeaModel):
    def __init__(
        self,
        attach_date: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The time when the control policy was attached to the object.
        self.attach_date = attach_date
        # The ID of the object.
        self.target_id = target_id
        # The name of the object.
        self.target_name = target_name
        # The type of the object. Valid values:
        # 
        # *   Root: Root folder
        # *   Folder: child folder of the Root folder
        # *   Account: member account
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments(TeaModel):
    def __init__(
        self,
        target_attachment: List[ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment] = None,
    ):
        self.target_attachment = target_attachment

    def validate(self):
        if self.target_attachment:
            for k in self.target_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TargetAttachment'] = []
        if self.target_attachment is not None:
            for k in self.target_attachment:
                result['TargetAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_attachment = []
        if m.get('TargetAttachment') is not None:
            for k in m.get('TargetAttachment'):
                temp_model = ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment()
                self.target_attachment.append(temp_model.from_map(k))
        return self


class ListTargetAttachmentsForControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        target_attachments: ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The list of objects to which the control policy is attached.
        self.target_attachments = target_attachments
        # The total number of objects to which the control policy is attached.
        self.total_count = total_count

    def validate(self):
        if self.target_attachments:
            self.target_attachments.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_attachments is not None:
            result['TargetAttachments'] = self.target_attachments.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetAttachments') is not None:
            temp_model = ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments()
            self.target_attachments = temp_model.from_map(m['TargetAttachments'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTargetAttachmentsForControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTargetAttachmentsForControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTargetAttachmentsForControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrustedServiceStatusRequest(TeaModel):
    def __init__(
        self,
        admin_account_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the enterprise management account or delegated administrator account.
        # 
        # *   If you set this parameter to the ID of an enterprise management account, the trusted services that are enabled within the enterprise management account are queried. The default value of this parameter is the ID of an enterprise management account.
        # *   If you set this parameter to the ID of a delegated administrator account, the trusted services that are enabled within the delegated administrator account are queried.
        # 
        # For more information about trusted services and delegated administrator accounts, see [Overview of trusted services](https://help.aliyun.com/document_detail/208133.html) and [Delegated administrator accounts](https://help.aliyun.com/document_detail/208117.html).
        self.admin_account_id = admin_account_id
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_account_id is not None:
            result['AdminAccountId'] = self.admin_account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminAccountId') is not None:
            self.admin_account_id = m.get('AdminAccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal(TeaModel):
    def __init__(
        self,
        enable_time: str = None,
        service_principal: str = None,
    ):
        # The time when the trusted service was enabled.
        self.enable_time = enable_time
        # The identification of the trusted service.
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListTrustedServiceStatusResponseBodyEnabledServicePrincipals(TeaModel):
    def __init__(
        self,
        enabled_service_principal: List[ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal] = None,
    ):
        self.enabled_service_principal = enabled_service_principal

    def validate(self):
        if self.enabled_service_principal:
            for k in self.enabled_service_principal:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnabledServicePrincipal'] = []
        if self.enabled_service_principal is not None:
            for k in self.enabled_service_principal:
                result['EnabledServicePrincipal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enabled_service_principal = []
        if m.get('EnabledServicePrincipal') is not None:
            for k in m.get('EnabledServicePrincipal'):
                temp_model = ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal()
                self.enabled_service_principal.append(temp_model.from_map(k))
        return self


class ListTrustedServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        enabled_service_principals: ListTrustedServiceStatusResponseBodyEnabledServicePrincipals = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The trusted services that are enabled.
        self.enabled_service_principals = enabled_service_principals
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.enabled_service_principals:
            self.enabled_service_principals.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_service_principals is not None:
            result['EnabledServicePrincipals'] = self.enabled_service_principals.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnabledServicePrincipals') is not None:
            temp_model = ListTrustedServiceStatusResponseBodyEnabledServicePrincipals()
            self.enabled_service_principals = temp_model.from_map(m['EnabledServicePrincipals'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTrustedServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTrustedServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTrustedServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        destination_folder_id: str = None,
    ):
        # The ID of the account you want to move.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The ID of the destination folder.
        # 
        # This parameter is required.
        self.destination_folder_id = destination_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.destination_folder_id is not None:
            result['DestinationFolderId'] = self.destination_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DestinationFolderId') is not None:
            self.destination_folder_id = m.get('DestinationFolderId')
        return self


class MoveAccountResponseBody(TeaModel):
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


class MoveAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourcesRequestResources(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
    ):
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service to which the resource belongs.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class MoveResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resources: List[MoveResourcesRequestResources] = None,
    ):
        # The ID of the resource group to which you want to move the resources.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resources that you want to move.
        # 
        # >  You can move a maximum of 10 resources at a time. If you want to move more than 10 resources, move them in batches.
        # 
        # This parameter is required.
        self.resources = resources

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = MoveResourcesRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class MoveResourcesResponseBodyResponses(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
        status: str = None,
    ):
        # The error code returned.
        # 
        # >  This parameter is returned if the resource failed to be moved.
        self.error_code = error_code
        # The error message returned.
        # 
        # >  This parameter is returned if the resource failed to be moved.
        self.error_msg = error_msg
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The ID of the Alibaba Cloud service.
        self.service = service
        # The status of the move task. Valid values:
        # 
        # *   SUCCESS
        # *   FAIL
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MoveResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        responses: List[MoveResourcesResponseBodyResponses] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned results.
        self.responses = responses

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['Responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.responses = []
        if m.get('Responses') is not None:
            for k in m.get('Responses'):
                temp_model = MoveResourcesResponseBodyResponses()
                self.responses.append(temp_model.from_map(k))
        return self


class MoveResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PromoteResourceAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
    ):
        # The ID of the resource account you want to upgrade.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The email address used to log on to the cloud account after the upgrade.
        # 
        # This parameter is required.
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class PromoteResourceAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the member account.
        self.account_id = account_id
        # The name of the member account.
        self.account_name = account_name
        # The display name of the member account.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member account joined the resource directory. Valid values:
        # 
        # *   invited: The member account is invited to join the resource directory.
        # *   created: The member account is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member account joined the resource directory.
        self.join_time = join_time
        # The time when the member account was modified.
        self.modify_time = modify_time
        # The account record ID.
        self.record_id = record_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member account. Valid values:
        # 
        # *   CreateSuccess: The member account is created.
        # *   CreateVerifying: The creation of the member account is under confirmation.
        # *   CreateFailed: The member account failed to be created.
        # *   CreateExpired: The creation of the member account expired.
        # *   CreateCancelled: The creation of the member account is canceled.
        # *   PromoteVerifying: The upgrade of the member account is under confirmation.
        # *   PromoteFailed: The member account failed to be upgraded.
        # *   PromoteExpired: The upgrade of the member account expired.
        # *   PromoteCancelled: The upgrade of the member account is canceled.
        # *   PromoteSuccess: The member account is upgraded.
        # *   InviteSuccess: The owner of the member account accepted the invitation.
        # *   Removed: The member account is removed from the resource directory.
        self.status = status
        # The type of the member account. Valid values:
        # 
        # *   CloudAccount
        # *   ResourceAccount
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PromoteResourceAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: PromoteResourceAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member account.
        self.account = account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = PromoteResourceAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PromoteResourceAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PromoteResourceAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PromoteResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDelegatedAdministratorRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        service_principal: str = None,
    ):
        # The ID of the member in the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The identifier of the trusted service.
        # 
        # For more information, see the `Trusted service identifier` column in [Supported trusted services](https://help.aliyun.com/document_detail/208133.html).
        # 
        # This parameter is required.
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class RegisterDelegatedAdministratorResponseBody(TeaModel):
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


class RegisterDelegatedAdministratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterDelegatedAdministratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegisterDelegatedAdministratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveCloudAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the member.
        # 
        # This parameter is required.
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


class RemoveCloudAccountResponseBody(TeaModel):
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


class RemoveCloudAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveCloudAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendCreateCloudAccountEmailRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        # The account record ID.
        # 
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendCreateCloudAccountEmailResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the account.
        self.account_id = account_id
        # The name of the account.
        self.account_name = account_name
        # The display name of the member account.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member account joined the resource directory. Valid values:
        # 
        # *   invited: The member account is invited to join the resource directory.
        # *   created: The member account is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member account joined the resource directory.
        self.join_time = join_time
        # The time when the member account was modified.
        self.modify_time = modify_time
        # The account record ID.
        self.record_id = record_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member account. Valid values:
        # 
        # *   CreateSuccess: The member account is created.
        # *   CreateVerifying: The creation of the member account is under confirmation.
        # *   CreateFailed: The member account failed to be created.
        # *   CreateExpired: The creation of the member account expired.
        # *   CreateCancelled: The creation of the member account is canceled.
        # *   PromoteVerifying: The upgrade of the member account is under confirmation.
        # *   PromoteFailed: The member account failed to be upgraded.
        # *   PromoteExpired: The upgrade of the member account expired.
        # *   PromoteCancelled: The upgrade of the member account is canceled.
        # *   PromoteSuccess: The member account is upgraded.
        # *   InviteSuccess: The owner of the member account accepted the invitation.
        # *   Removed: The member account is removed from the resource directory.
        self.status = status
        # The type of the member account. The value CloudAccount indicates that the member account is a cloud account.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ResendCreateCloudAccountEmailResponseBody(TeaModel):
    def __init__(
        self,
        account: ResendCreateCloudAccountEmailResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member account.
        self.account = account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = ResendCreateCloudAccountEmailResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResendCreateCloudAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResendCreateCloudAccountEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResendCreateCloudAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendPromoteResourceAccountEmailRequest(TeaModel):
    def __init__(
        self,
        record_id: str = None,
    ):
        # The account record ID.
        # 
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendPromoteResourceAccountEmailResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        record_id: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the account.
        self.account_id = account_id
        # The name of the account.
        self.account_name = account_name
        # The display name of the member account.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member account joined the resource directory. Valid values:
        # 
        # *   invited: The member account is invited to join the resource directory.
        # *   created: The member account is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member account joined the resource directory.
        self.join_time = join_time
        # The time when the member account was modified.
        self.modify_time = modify_time
        # The account record ID.
        self.record_id = record_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member account. Valid values:
        # 
        # *   CreateSuccess: The member account is created.
        # *   CreateVerifying: The creation of the member account is under confirmation.
        # *   CreateFailed: The member account failed to be created.
        # *   CreateExpired: The creation of the member account expired.
        # *   CreateCancelled: The creation of the member account is canceled.
        # *   PromoteVerifying: The upgrade of the member account is under confirmation.
        # *   PromoteFailed: The member account failed to be upgraded.
        # *   PromoteExpired: The upgrade of the member account expired.
        # *   PromoteCancelled: The upgrade of the member account is canceled.
        # *   PromoteSuccess: The member account is upgraded.
        # *   InviteSuccess: The owner of the member account accepted the invitation.
        # *   Removed: The member account is removed from the resource directory.
        self.status = status
        # The type of the member account. Valid values:
        # 
        # *   CloudAccount: cloud account
        # *   ResourceAccount: resource account
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ResendPromoteResourceAccountEmailResponseBody(TeaModel):
    def __init__(
        self,
        account: ResendPromoteResourceAccountEmailResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member account.
        self.account = account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = ResendPromoteResourceAccountEmailResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResendPromoteResourceAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResendPromoteResourceAccountEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResendPromoteResourceAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryChangeAccountEmailRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
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


class RetryChangeAccountEmailResponseBody(TeaModel):
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


class RetryChangeAccountEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryChangeAccountEmailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RetryChangeAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationCodeForBindSecureMobilePhoneRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        secure_mobile_phone: str = None,
    ):
        # The ID of the resource account.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The mobile phone number that you want to bind to the resource account.
        # 
        # Specify the mobile phone number in the \\<Country code>-\\<Mobile phone number> format.
        # 
        # >  Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        # 
        # This parameter is required.
        self.secure_mobile_phone = secure_mobile_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')
        return self


class SendVerificationCodeForBindSecureMobilePhoneResponseBody(TeaModel):
    def __init__(
        self,
        expiration_date: str = None,
        request_id: str = None,
    ):
        # The time when the verification code expires.
        self.expiration_date = expiration_date
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerificationCodeForBindSecureMobilePhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerificationCodeForBindSecureMobilePhoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendVerificationCodeForBindSecureMobilePhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationCodeForEnableRDRequest(TeaModel):
    def __init__(
        self,
        secure_mobile_phone: str = None,
    ):
        # The mobile phone number that is bound to the newly created account. If you leave this parameter empty, the mobile phone number that is bound to the current account is used.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # >  Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        self.secure_mobile_phone = secure_mobile_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')
        return self


class SendVerificationCodeForEnableRDResponseBody(TeaModel):
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


class SendVerificationCodeForEnableRDResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerificationCodeForEnableRDResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendVerificationCodeForEnableRDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultPolicyVersionRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The ID of the policy version.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class SetDefaultPolicyVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDefaultPolicyVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDefaultPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMemberDeletionPermissionRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        # Specifies whether to enable the member deletion feature. Valid values:
        # 
        # *   Enabled: enables the member deletion feature
        # *   Disabled: disables the member deletion feature
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetMemberDeletionPermissionResponseBody(TeaModel):
    def __init__(
        self,
        management_account_id: str = None,
        member_deletion_status: str = None,
        request_id: str = None,
        resource_directory_id: str = None,
    ):
        # The ID of the management account of the resource directory.
        self.management_account_id = management_account_id
        # The status of the member deletion feature. Valid values:
        # 
        # *   Enabled: The feature is enabled.
        # *   Disabled: The feature is disabled.
        self.member_deletion_status = member_deletion_status
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.management_account_id is not None:
            result['ManagementAccountId'] = self.management_account_id
        if self.member_deletion_status is not None:
            result['MemberDeletionStatus'] = self.member_deletion_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagementAccountId') is not None:
            self.management_account_id = m.get('ManagementAccountId')
        if m.get('MemberDeletionStatus') is not None:
            self.member_deletion_status = m.get('MemberDeletionStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        return self


class SetMemberDeletionPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetMemberDeletionPermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetMemberDeletionPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A tag key.
        # 
        # A tag key can be a maximum of 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.key = key
        # A tag value.
        # 
        # A tag value can be a maximum of 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The ID of a resource group or member.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the objects to which you want to add tags. Valid values:
        # 
        # *   ResourceGroup : resource group. This is the default value.
        # *   Account: member.
        # 
        # >  This parameter is required if you add tags to members in a resource directory.
        self.resource_type = resource_type
        # The tags.
        # 
        # This parameter is required.
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the specified resource groups or members. Valid values:
        # 
        # *   false (default value)
        # *   true
        self.all = all
        # The ID of a resource group or member.
        # 
        # You can specify a maximum of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the objects from which you want to remove tags. Valid values:
        # 
        # *   ResourceGroup: resource group. This is the default value.
        # *   Account: member.
        # 
        # >  This parameter is required if you remove tags from members in a resource directory.
        self.resource_type = resource_type
        # A tag key.
        # 
        # You can specify a maximum of 20 tag keys.
        # 
        # >  If you set the `All` parameter to `true`, you do not need to configure this parameter.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        new_account_type: str = None,
        new_display_name: str = None,
    ):
        # The ID of the Alibaba Cloud account that corresponds to the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The new type of the member. Valid values:
        # 
        # *   ResourceAccount: resource account
        # *   CloudAccount: cloud account
        # 
        # >  You can configure either the `NewDisplayName` or `NewAccountType` parameter.
        self.new_account_type = new_account_type
        # The new display name of the member.
        # 
        # >  You can configure either the `NewDisplayName` or `NewAccountType` parameter.
        self.new_display_name = new_display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.new_account_type is not None:
            result['NewAccountType'] = self.new_account_type
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('NewAccountType') is not None:
            self.new_account_type = m.get('NewAccountType')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        return self


class UpdateAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        folder_id: str = None,
        join_method: str = None,
        join_time: str = None,
        modify_time: str = None,
        resource_directory_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the Alibaba Cloud account that corresponds to the member.
        self.account_id = account_id
        # The name of the Alibaba Cloud account that corresponds to the member.
        self.account_name = account_name
        # The display name of the member.
        self.display_name = display_name
        # The ID of the folder.
        self.folder_id = folder_id
        # The way in which the member joins the resource directory. Valid values:
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The time when the member joined the resource directory. The time is displayed in UTC.
        self.join_time = join_time
        # The time when the member was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the member. Valid values:
        # 
        # *   CreateSuccess: The member is created.
        # *   InviteSuccess: The member accepts the invitation.
        # *   Removed: The member is removed.
        # *   SwitchSuccess: The type of the member is switched.
        self.status = status
        # The type of the member. Valid values:
        # 
        # *   CloudAccount: cloud account
        # *   ResourceAccount: resource account
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateAccountResponseBody(TeaModel):
    def __init__(
        self,
        account: UpdateAccountResponseBodyAccount = None,
        request_id: str = None,
    ):
        # The information of the member.
        self.account = account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = UpdateAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAssociatedTransferSettingRequestRuleSettings(TeaModel):
    def __init__(
        self,
        associated_resource_type: str = None,
        associated_service: str = None,
        master_resource_type: str = None,
        master_service: str = None,
        status: str = None,
    ):
        # The type of the associated resource.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.associated_resource_type = associated_resource_type
        # The service code of the associated resource.
        # 
        # You can obtain the service code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.associated_service = associated_service
        # The type of the primary resource.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.master_resource_type = master_resource_type
        # The service code of the primary resource.
        # 
        # You can obtain the service code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.master_service = master_service
        # The status of the Transfer Associated Resources feature. Valid values:
        # 
        # *   Enable: enabled
        # *   Disable: disabled
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associated_resource_type is not None:
            result['AssociatedResourceType'] = self.associated_resource_type
        if self.associated_service is not None:
            result['AssociatedService'] = self.associated_service
        if self.master_resource_type is not None:
            result['MasterResourceType'] = self.master_resource_type
        if self.master_service is not None:
            result['MasterService'] = self.master_service
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedResourceType') is not None:
            self.associated_resource_type = m.get('AssociatedResourceType')
        if m.get('AssociatedService') is not None:
            self.associated_service = m.get('AssociatedService')
        if m.get('MasterResourceType') is not None:
            self.master_resource_type = m.get('MasterResourceType')
        if m.get('MasterService') is not None:
            self.master_service = m.get('MasterService')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAssociatedTransferSettingRequest(TeaModel):
    def __init__(
        self,
        enable_existing_resources_transfer: str = None,
        rule_settings: List[UpdateAssociatedTransferSettingRequestRuleSettings] = None,
    ):
        # Specifies whether to enable the Transfer Existing Associated Resources feature. Valid values:
        # 
        # *   false
        # *   true
        self.enable_existing_resources_transfer = enable_existing_resources_transfer
        # The settings of transfer rules.
        self.rule_settings = rule_settings

    def validate(self):
        if self.rule_settings:
            for k in self.rule_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_existing_resources_transfer is not None:
            result['EnableExistingResourcesTransfer'] = self.enable_existing_resources_transfer
        result['RuleSettings'] = []
        if self.rule_settings is not None:
            for k in self.rule_settings:
                result['RuleSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExistingResourcesTransfer') is not None:
            self.enable_existing_resources_transfer = m.get('EnableExistingResourcesTransfer')
        self.rule_settings = []
        if m.get('RuleSettings') is not None:
            for k in m.get('RuleSettings'):
                temp_model = UpdateAssociatedTransferSettingRequestRuleSettings()
                self.rule_settings.append(temp_model.from_map(k))
        return self


class UpdateAssociatedTransferSettingResponseBody(TeaModel):
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


class UpdateAssociatedTransferSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAssociatedTransferSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAssociatedTransferSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoGroupingConfigRequest(TeaModel):
    def __init__(
        self,
        enable_existing_resources_transfer: bool = None,
    ):
        # Specifies whether to enable the Transfer Existing Associated Resources feature. Valid values:
        # 
        # *   false
        # *   true
        self.enable_existing_resources_transfer = enable_existing_resources_transfer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_existing_resources_transfer is not None:
            result['EnableExistingResourcesTransfer'] = self.enable_existing_resources_transfer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExistingResourcesTransfer') is not None:
            self.enable_existing_resources_transfer = m.get('EnableExistingResourcesTransfer')
        return self


class UpdateAutoGroupingConfigResponseBody(TeaModel):
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


class UpdateAutoGroupingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutoGroupingConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAutoGroupingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoGroupingRuleRequestRuleContents(TeaModel):
    def __init__(
        self,
        auto_grouping_scope_condition: str = None,
        rule_content_id: str = None,
        target_resource_group_condition: str = None,
    ):
        # The condition for the range of resources that are automatically transferred.
        self.auto_grouping_scope_condition = auto_grouping_scope_condition
        # The ID of the content record.
        self.rule_content_id = rule_content_id
        # The condition for the destination resource group.
        # 
        # This parameter is required.
        self.target_resource_group_condition = target_resource_group_condition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_grouping_scope_condition is not None:
            result['AutoGroupingScopeCondition'] = self.auto_grouping_scope_condition
        if self.rule_content_id is not None:
            result['RuleContentId'] = self.rule_content_id
        if self.target_resource_group_condition is not None:
            result['TargetResourceGroupCondition'] = self.target_resource_group_condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoGroupingScopeCondition') is not None:
            self.auto_grouping_scope_condition = m.get('AutoGroupingScopeCondition')
        if m.get('RuleContentId') is not None:
            self.rule_content_id = m.get('RuleContentId')
        if m.get('TargetResourceGroupCondition') is not None:
            self.target_resource_group_condition = m.get('TargetResourceGroupCondition')
        return self


class UpdateAutoGroupingRuleRequest(TeaModel):
    def __init__(
        self,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_resource_types_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_types_scope: str = None,
        rule_contents: List[UpdateAutoGroupingRuleRequestRuleContents] = None,
        rule_desc: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The IDs of regions to be excluded. Separate multiple IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of resource groups to be excluded. Separate multiple IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of resources to be excluded. Separate multiple IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The resource types to be excluded. Separate multiple resource types with commas (,).
        self.exclude_resource_types_scope = exclude_resource_types_scope
        # The IDs of regions. Separate multiple IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The IDs of resource groups. Separate multiple IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of resources. Separate multiple IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The resource types. Separate multiple resource types with commas (,).
        self.resource_types_scope = resource_types_scope
        # The content records of the rule.
        # 
        # This parameter is required.
        self.rule_contents = rule_contents
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        if self.rule_contents:
            for k in self.rule_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope
        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope
        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope
        if self.exclude_resource_types_scope is not None:
            result['ExcludeResourceTypesScope'] = self.exclude_resource_types_scope
        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope
        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope
        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope
        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope
        result['RuleContents'] = []
        if self.rule_contents is not None:
            for k in self.rule_contents:
                result['RuleContents'].append(k.to_map() if k else None)
        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')
        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')
        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')
        if m.get('ExcludeResourceTypesScope') is not None:
            self.exclude_resource_types_scope = m.get('ExcludeResourceTypesScope')
        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')
        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')
        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')
        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')
        self.rule_contents = []
        if m.get('RuleContents') is not None:
            for k in m.get('RuleContents'):
                temp_model = UpdateAutoGroupingRuleRequestRuleContents()
                self.rule_contents.append(temp_model.from_map(k))
        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateAutoGroupingRuleResponseBody(TeaModel):
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


class UpdateAutoGroupingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutoGroupingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAutoGroupingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateControlPolicyRequest(TeaModel):
    def __init__(
        self,
        new_description: str = None,
        new_policy_document: str = None,
        new_policy_name: str = None,
        policy_id: str = None,
    ):
        # The new description of the access control policy.
        # 
        # The description must be 1 to 1,024 characters in length. The description can contain letters, digits, underscores (_), and hyphens (-) and must start with a letter.
        self.new_description = new_description
        # The new document of the access control policy.
        # 
        # The document can be a maximum of 4,096 characters in length.
        # 
        # For more information about the languages of access control policies, see [Languages of access control policies](https://help.aliyun.com/document_detail/179096.html).
        # 
        # For more information about the examples of access control policies, see [Examples of custom access control policies](https://help.aliyun.com/document_detail/181474.html).
        self.new_policy_document = new_policy_document
        # The new name of the access control policy.
        # 
        # The name must be 1 to 128 characters in length. The name can contain letters, digits, and hyphens (-) and must start with a letter.
        self.new_policy_name = new_policy_name
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_policy_document is not None:
            result['NewPolicyDocument'] = self.new_policy_document
        if self.new_policy_name is not None:
            result['NewPolicyName'] = self.new_policy_name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewPolicyDocument') is not None:
            self.new_policy_document = m.get('NewPolicyDocument')
        if m.get('NewPolicyName') is not None:
            self.new_policy_name = m.get('NewPolicyName')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class UpdateControlPolicyResponseBodyControlPolicy(TeaModel):
    def __init__(
        self,
        attachment_count: str = None,
        create_date: str = None,
        description: str = None,
        effect_scope: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        update_date: str = None,
    ):
        # The number of times that the access control policy is referenced.
        self.attachment_count = attachment_count
        # The time when the access control policy was created.
        self.create_date = create_date
        # The description of the access control policy.
        self.description = description
        # The effective scope of the access control policy. Valid values:
        # 
        # *   All: The access control policy is in effect for Alibaba Cloud accounts, RAM users, and RAM roles.
        # *   RAM: The access control policy is in effect only for RAM users and RAM roles.
        self.effect_scope = effect_scope
        # The ID of the access control policy.
        self.policy_id = policy_id
        # The name of the access control policy.
        self.policy_name = policy_name
        # The type of the access control policy. Valid values:
        # 
        # *   System: system access control policy
        # *   Custom: custom access control policy
        self.policy_type = policy_type
        # The time when the access control policy was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        control_policy: UpdateControlPolicyResponseBodyControlPolicy = None,
        request_id: str = None,
    ):
        # The details of the access control policy.
        self.control_policy = control_policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = UpdateControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m['ControlPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateControlPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateControlPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        new_folder_name: str = None,
    ):
        # The ID of the folder.
        # 
        # This parameter is required.
        self.folder_id = folder_id
        # The new name of the folder.
        # 
        # The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.new_folder_name = new_folder_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.new_folder_name is not None:
            result['NewFolderName'] = self.new_folder_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('NewFolderName') is not None:
            self.new_folder_name = m.get('NewFolderName')
        return self


class UpdateFolderResponseBodyFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class UpdateFolderResponseBody(TeaModel):
    def __init__(
        self,
        folder: UpdateFolderResponseBodyFolder = None,
        request_id: str = None,
    ):
        # The information of the folder.
        self.folder = folder
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = UpdateFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFolderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_display_name: str = None,
        resource_group_id: str = None,
    ):
        # The display name of the resource group.
        # 
        # The name must be 1 to 50 characters in length.
        # 
        # This parameter is required.
        self.new_display_name = new_display_name
        # The ID of the resource group.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class UpdateResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource group belongs.
        self.account_id = account_id
        # The time when the resource group was created. The time is displayed in UTC.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: UpdateResourceGroupResponseBodyResourceGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource group.
        self.resource_group = resource_group

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = UpdateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class UpdateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        new_assume_role_policy_document: str = None,
        new_description: str = None,
        new_max_session_duration: int = None,
        role_name: str = None,
    ):
        # The document of the policy that specifies the trusted entity to assume the RAM role.
        self.new_assume_role_policy_document = new_assume_role_policy_document
        # The description of the RAM role.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.new_description = new_description
        # The maximum session duration of the RAM role.
        # 
        # Unit: seconds. Valid values: 3600 to 43200. Default value: 3600.
        # 
        # If you do not specify this parameter, the default value is used.
        self.new_max_session_duration = new_max_session_duration
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.),and hyphens (-).
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_assume_role_policy_document is not None:
            result['NewAssumeRolePolicyDocument'] = self.new_assume_role_policy_document
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_max_session_duration is not None:
            result['NewMaxSessionDuration'] = self.new_max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewAssumeRolePolicyDocument') is not None:
            self.new_assume_role_policy_document = m.get('NewAssumeRolePolicyDocument')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewMaxSessionDuration') is not None:
            self.new_max_session_duration = m.get('NewMaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateRoleResponseBodyRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.arn = arn
        # The document of the policy that specifies the trusted entity to assume the RAM role.
        self.assume_role_policy_document = assume_role_policy_document
        # The time when the RAM role was created.
        self.create_date = create_date
        # The description of the RAM role.
        self.description = description
        # The maximum session duration of the RAM role.
        self.max_session_duration = max_session_duration
        # The ID of the RAM role.
        self.role_id = role_id
        # The name of the RAM role.
        self.role_name = role_name
        # The name of the RAM role after authorization.
        self.role_principal_name = role_principal_name
        # The time when the RAM role was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: UpdateRoleResponseBodyRole = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the RAM role.
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = UpdateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


