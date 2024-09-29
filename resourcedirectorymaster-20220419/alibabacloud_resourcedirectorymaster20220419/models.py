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
        # You can call the [ListHandshakesForAccount](~~ListHandshakesForAccount~~) operation to obtain the ID.
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
        # The description of the invitation.
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


class AddMessageContactRequest(TeaModel):
    def __init__(
        self,
        email_address: str = None,
        message_types: List[str] = None,
        name: str = None,
        phone_number: str = None,
        title: str = None,
    ):
        # The email address of the contact.
        # 
        # After you specify an email address, you need to call [SendEmailVerificationForMessageContact](~~SendEmailVerificationForMessageContact~~) to send verification information to the email address. After the verification is passed, the email address takes effect.
        # 
        # This parameter is required.
        self.email_address = email_address
        # The types of messages received by the contact.
        # 
        # This parameter is required.
        self.message_types = message_types
        # The name of the contact.
        # 
        # The name must be unique in your resource directory.
        # 
        # The name must be 2 to 12 characters in length and can contain only letters.
        # 
        # This parameter is required.
        self.name = name
        # The mobile phone number of the contact.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # > Only mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are supported.
        # 
        # After you specify a mobile phone number, you need to call [SendPhoneVerificationForMessageContact](~~SendPhoneVerificationForMessageContact~~) to send verification information to the mobile phone number. After the verification is passed, the mobile phone number takes effect.
        self.phone_number = phone_number
        # The job title of the contact.
        # 
        # Valid values:
        # 
        # *   FinanceDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TechnicalDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MaintenanceDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CEO
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ProjectDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Other
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.message_types is not None:
            result['MessageTypes'] = self.message_types
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AddMessageContactResponseBodyContact(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        create_date: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The time when the contact was created.
        self.create_date = create_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class AddMessageContactResponseBody(TeaModel):
    def __init__(
        self,
        contact: AddMessageContactResponseBodyContact = None,
        request_id: str = None,
    ):
        # The information about the contact.
        self.contact = contact
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            temp_model = AddMessageContactResponseBodyContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddMessageContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMessageContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddMessageContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateMembersRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        members: List[str] = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The IDs of objects to which you want to bind the contact.
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class AssociateMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        member_id: str = None,
        modify_date: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The ID of the object. Valid values:
        # 
        # - ID of the resource directory
        # - ID of the folder
        # - ID of the member
        self.member_id = member_id
        # The time when the contact was bound to the object.
        self.modify_date = modify_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.modify_date is not None:
            result['ModifyDate'] = self.modify_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('ModifyDate') is not None:
            self.modify_date = m.get('ModifyDate')
        return self


class AssociateMembersResponseBody(TeaModel):
    def __init__(
        self,
        members: List[AssociateMembersResponseBodyMembers] = None,
        request_id: str = None,
    ):
        # The time when the contact was bound to the object.
        self.members = members
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AssociateMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateMembersResponseBody()
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
        # The mobile phone number you specify must be the same as the mobile phone number that you specify when you call the [SendVerificationCodeForBindSecureMobilePhone](~~SendVerificationCodeForBindSecureMobilePhone~~) operation to obtain a verification code.
        # 
        # Specify the mobile phone number in the \\<Country code>-\\<Mobile phone number> format.
        # 
        # > Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        # 
        # This parameter is required.
        self.secure_mobile_phone = secure_mobile_phone
        # The verification code.
        # 
        # You can call the [SendVerificationCodeForBindSecureMobilePhone](~~SendVerificationCodeForBindSecureMobilePhone~~) operation to obtain the verification code.
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
        # The description of the invitation.
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


class CancelMessageContactUpdateRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        email_address: str = None,
        phone_number: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address of the contact.
        self.email_address = email_address
        # The mobile phone number of the contact.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class CancelMessageContactUpdateResponseBody(TeaModel):
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


class CancelMessageContactUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelMessageContactUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelMessageContactUpdateResponseBody()
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
        # > The system automatically sends a verification email to the email address. After the verification is passed, the email address takes effect, and the system changes both the logon email address and secure email address of the member.
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
        # The Alibaba Cloud account ID of the member that you want to delete.
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


class CreateControlPolicyRequestTag(TeaModel):
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


class CreateControlPolicyRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        effect_scope: str = None,
        policy_document: str = None,
        policy_name: str = None,
        tag: List[CreateControlPolicyRequestTag] = None,
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
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateControlPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
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


class CreateFolderRequestTag(TeaModel):
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


class CreateFolderRequest(TeaModel):
    def __init__(
        self,
        folder_name: str = None,
        parent_folder_id: str = None,
        tag: List[CreateFolderRequestTag] = None,
    ):
        # The name of the folder.
        # 
        # The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.),and hyphens (-).
        # 
        # This parameter is required.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
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
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateFolderRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        # The information about the folder.
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


class CreateResourceAccountRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        dry_run: bool = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
        resell_account_type: str = None,
        tag: List[CreateResourceAccountRequestTag] = None,
    ):
        # The prefix for the Alibaba Cloud account name of the member. If you leave this parameter empty, the system randomly generates a prefix.
        # 
        # The prefix must be 2 to 37 characters in length.
        # 
        # The prefix can contain letters, digits, and special characters but cannot contain consecutive special characters. The prefix must start with a letter or digit and end with a letter or digit. Valid special characters include underscores (`_`), periods (.), and hyphens (`-`).
        # 
        # The complete Alibaba Cloud account name of a member in a resource directory is in the @.aliyunid.com format, such as `alice@rd-3G****.aliyunid.com`.
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
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks whether an identity type can be specified for the member. If the request does not pass the dry run, an error code is returned.
        # *   false (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The ID of the billing account. If you leave this parameter empty, the newly created member is used as its billing account.
        self.payer_account_id = payer_account_id
        # The identity type of the member. Valid values:
        # 
        # *   resell: The member is an account for a reseller. This is the default value. A relationship is automatically established between the member and the reseller. The management account of the resource directory must be used as the billing account of the member.
        # *   non_resell: The member is not an account for a reseller. The member is an account that is not associated with a reseller. You can directly use the account to purchase Alibaba Cloud resources. The member is used as its own billing account.
        # 
        # > This parameter is available only for resellers at the international site (alibabacloud.com).
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
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
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
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
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The Alibaba Cloud account name of the member.
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
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The time when the invitation was modified.
        self.modify_time = modify_time
        # The description of the invitation.
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
        # The IDs of the check items that you can choose to ignore for the member deletion.
        # 
        # You can obtain the IDs from the response of the [GetAccountDeletionCheckResult](~~GetAccountDeletionCheckResult~~) operation.
        self.abandonable_check_id = abandonable_check_id
        # The Alibaba Cloud account ID of the member that you want to delete.
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
        # The IDs of the check items that you can choose to ignore for the member deletion.
        # 
        # You can obtain the IDs from the response of the [GetAccountDeletionCheckResult](~~GetAccountDeletionCheckResult~~) operation.
        self.abandonable_check_id_shrink = abandonable_check_id_shrink
        # The Alibaba Cloud account ID of the member that you want to delete.
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
        # The type of the deletion. Valid values:
        # 
        # *   0: direct deletion. If the member does not have pay-as-you-go resources that are purchased within the previous 30 days, the system directly deletes the member.
        # *   1: deletion with a silence period. If the member has pay-as-you-go resources that are purchased within the previous 30 days, the member enters a silence period. The system starts to delete the member until the silence period ends. For more information about the silence period, see [What is the silence period for member deletion?](https://help.aliyun.com/document_detail/446079.html)
        self.deletion_type = deletion_type
        # The ID of the request.
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


class DeleteControlPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
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


class DeleteMessageContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        retain_contact_in_members: bool = None,
    ):
        # The ID of the contact.
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # Specifies whether to retain the contact for members. Valid values:
        # 
        # *   true (default): retains the contact for members. In this case, the contact can still receive messages for the members.
        # *   false: does not retain the contact for members. In this case, the contact can no longer receive messages for the members. If you set this parameter to false, the response is asynchronously returned. You can call [GetMessageContactDeletionStatus](~~GetMessageContactDeletionStatus~~) to obtain the deletion result.
        self.retain_contact_in_members = retain_contact_in_members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.retain_contact_in_members is not None:
            result['RetainContactInMembers'] = self.retain_contact_in_members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RetainContactInMembers') is not None:
            self.retain_contact_in_members = m.get('RetainContactInMembers')
        return self


class DeleteMessageContactResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The deletion status of the contact. Valid values:
        # 
        # *   Deleting
        # *   Deleted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteMessageContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMessageContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMessageContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterDelegatedAdministratorRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        service_principal: str = None,
    ):
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The identifier of the trusted service.
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


class DisableControlPolicyResponseBody(TeaModel):
    def __init__(
        self,
        enablement_status: str = None,
        request_id: str = None,
    ):
        # The status of the Control Policy feature. Valid values:
        # 
        # *   Enabled: The feature is enabled.
        # *   PendingEnable: The feature is being enabled.
        # *   Disabled: The feature is disabled.
        # *   PendingDisable: The feature is being disabled.
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


class DisassociateMembersRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        members: List[str] = None,
    ):
        # The ID of the contact.
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # The IDs of objects from which you want to unbind the contact.
        # 
        # This parameter is required.
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class DisassociateMembersResponseBodyMembers(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        member_id: str = None,
        modify_date: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The ID of the object. Valid values:
        # 
        # - ID of the resource directory
        # - ID of the folder
        # - ID of the member
        self.member_id = member_id
        # The time when the contact was unbound from the object.
        self.modify_date = modify_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.modify_date is not None:
            result['ModifyDate'] = self.modify_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('ModifyDate') is not None:
            self.modify_date = m.get('ModifyDate')
        return self


class DisassociateMembersResponseBody(TeaModel):
    def __init__(
        self,
        members: List[DisassociateMembersResponseBodyMembers] = None,
        request_id: str = None,
    ):
        # The time when the contact was unbound from the object.
        self.members = members
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DisassociateMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateMembersResponseBody()
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
        # *   Enabled: The feature is enabled.
        # *   PendingEnable: The feature is being enabled.
        # *   Disabled: The feature is disabled.
        # *   PendingDisable: The feature is being disabled.
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
        dry_run: bool = None,
        enable_mode: str = None,
        maname: str = None,
        masecure_mobile_phone: str = None,
        verification_code: str = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The mode in which you enable a resource directory. Valid values:
        # 
        # *   CurrentAccount: The current account is used to enable a resource directory.
        # *   NewManagementAccount: A newly created account is used to enable a resource directory. If you select this mode, you must configure the `MAName`, `MASecureMobilePhone`, and `VerificationCode` parameters.
        # 
        # This parameter is required.
        self.enable_mode = enable_mode
        # The name of the newly created account.
        # 
        # Specify the name in the `<Prefix>@rdadmin.aliyunid.com` format. The prefix can contain letters, digits, and special characters but cannot contain consecutive special characters. The prefix must start and end with a letter or digit. Valid special characters include underscores (`_`), periods (.), and hyphens (-). The prefix must be 2 to 50 characters in length.
        self.maname = maname
        # The mobile phone number that is bound to the newly created account.
        # 
        # If you leave this parameter empty, the mobile phone number that is bound to the current account is used. The mobile phone number you specify must be the same as the mobile phone number that you specify when you call the [SendVerificationCodeForEnableRD](~~SendVerificationCodeForEnableRD~~) operation to obtain a verification code.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # > Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        self.masecure_mobile_phone = masecure_mobile_phone
        # The verification code.
        # 
        # You can call the [SendVerificationCodeForEnableRD](~~SendVerificationCodeForEnableRD~~) operation to obtain the verification code.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
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
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
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
        # The information about the resource directory.
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


class GetAccountResponseBodyAccount(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        email_status: str = None,
        folder_id: str = None,
        has_secure_mobile_phone: bool = None,
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
        # *   If the value of this parameter is empty, no modification is performed for the email address.
        # *   WAIT_MODIFY: The modification is being performed.
        # *   CANCELLED: The modification is canceled.
        # *   EXPIRED: The modification expires.
        self.email_status = email_status
        # The ID of the folder.
        self.folder_id = folder_id
        # Indicates whether a mobile phone number is bound to the member for security purposes. Valid values:
        # 
        # *   true
        # *   false
        self.has_secure_mobile_phone = has_secure_mobile_phone
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
        # The tags of the member.
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
        if self.has_secure_mobile_phone is not None:
            result['HasSecureMobilePhone'] = self.has_secure_mobile_phone
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
        if m.get('HasSecureMobilePhone') is not None:
            self.has_secure_mobile_phone = m.get('HasSecureMobilePhone')
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
        # The information about the member.
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
        # The Alibaba Cloud account ID of the member that you want to delete.
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
        # > This parameter may be returned if the value of AllowDelete is true.
        self.abandonable_checks = abandonable_checks
        # Indicates whether the member can be deleted. Valid values:
        # 
        # *   true: The member can be deleted.
        # *   false: The member cannot be deleted.
        self.allow_delete = allow_delete
        # The reasons why the member cannot be deleted.
        # 
        # > This parameter is returned only if the value of AllowDelete is false.
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
        # *   1: deletion with a silence period. If the member has pay-as-you-go resources that are purchased within the previous 30 days, the member enters a silence period of 45 days. The system starts to delete the member until the silence period ends. For more information about the silence period, see [What is the silence period for member deletion?](https://help.aliyun.com/document_detail/446079.html)
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
        # > This parameter is valid only for system access control policies.
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
        # *   Enabled: The feature is enabled.
        # *   PendingEnable: The feature is being enabled.
        # *   Disabled: The feature is disabled.
        # *   PendingDisable: The feature is being disabled.
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
        # The information about the folder.
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
        # > This parameter is available only when an invitee calls this operation.
        self.invited_account_real_name = invited_account_real_name
        # The ID of the management account of the resource directory.
        self.master_account_id = master_account_id
        # The name of the management account of the resource directory.
        self.master_account_name = master_account_name
        # The real-name verification information of the management account of the resource directory.
        # 
        # > This parameter is available only when an invitee calls this operation.
        self.master_account_real_name = master_account_real_name
        # The time when the invitation was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The description of the invitation.
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


class GetMessageContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
    ):
        # The ID of the contact.
        # 
        # This parameter is required.
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class GetMessageContactResponseBodyContact(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        create_date: str = None,
        email_address: str = None,
        members: List[str] = None,
        message_types: List[str] = None,
        name: str = None,
        phone_number: str = None,
        status: str = None,
        title: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The time when the contact was created.
        self.create_date = create_date
        # The email address of the contact.
        self.email_address = email_address
        # The IDs of objects to which the contact is bound.
        self.members = members
        # The types of messages received by the contact.
        self.message_types = message_types
        # The name of the contact.
        self.name = name
        # The mobile phone number of the contact.
        self.phone_number = phone_number
        # The status of the contact. Valid values:
        # 
        # *   Verifying
        # *   Active
        # *   Deleting
        self.status = status
        # The job title of the contact.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.members is not None:
            result['Members'] = self.members
        if self.message_types is not None:
            result['MessageTypes'] = self.message_types
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetMessageContactResponseBody(TeaModel):
    def __init__(
        self,
        contact: GetMessageContactResponseBodyContact = None,
        request_id: str = None,
    ):
        # The information about the contact.
        self.contact = contact
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            temp_model = GetMessageContactResponseBodyContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMessageContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMessageContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageContactDeletionStatusRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class GetMessageContactDeletionStatusResponseBodyContactDeletionStatusFailReasonList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        message_types: List[str] = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The types of messages received by the contact.
        self.message_types = message_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.message_types is not None:
            result['MessageTypes'] = self.message_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')
        return self


class GetMessageContactDeletionStatusResponseBodyContactDeletionStatus(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        fail_reason_list: List[GetMessageContactDeletionStatusResponseBodyContactDeletionStatusFailReasonList] = None,
        status: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The types of messages received by the contact.
        self.fail_reason_list = fail_reason_list
        # The deletion status of the contact. Valid values:
        # 
        # *   Deleting
        # *   Failed
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
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        result['FailReasonList'] = []
        if self.fail_reason_list is not None:
            for k in self.fail_reason_list:
                result['FailReasonList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        self.fail_reason_list = []
        if m.get('FailReasonList') is not None:
            for k in m.get('FailReasonList'):
                temp_model = GetMessageContactDeletionStatusResponseBodyContactDeletionStatusFailReasonList()
                self.fail_reason_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetMessageContactDeletionStatusResponseBody(TeaModel):
    def __init__(
        self,
        contact_deletion_status: GetMessageContactDeletionStatusResponseBodyContactDeletionStatus = None,
        request_id: str = None,
    ):
        # The deletion information of the contact.
        self.contact_deletion_status = contact_deletion_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.contact_deletion_status:
            self.contact_deletion_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_deletion_status is not None:
            result['ContactDeletionStatus'] = self.contact_deletion_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactDeletionStatus') is not None:
            temp_model = GetMessageContactDeletionStatusResponseBodyContactDeletionStatus()
            self.contact_deletion_status = temp_model.from_map(m['ContactDeletionStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageContactDeletionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMessageContactDeletionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMessageContactDeletionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPayerForAccountRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the billing account.
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
        # The ID of the billing account.
        self.payer_account_id = payer_account_id
        # The name of the billing account.
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
        self.control_policy_status = control_policy_status
        self.create_time = create_time
        self.identity_information = identity_information
        self.master_account_id = master_account_id
        self.master_account_name = master_account_name
        self.member_deletion_status = member_deletion_status
        self.resource_directory_id = resource_directory_id
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
        self.request_id = request_id
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


class InviteAccountToResourceDirectoryRequestTag(TeaModel):
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


class InviteAccountToResourceDirectoryRequest(TeaModel):
    def __init__(
        self,
        note: str = None,
        parent_folder_id: str = None,
        tag: List[InviteAccountToResourceDirectoryRequestTag] = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The description of the invitation.
        # 
        # The description can be up to 1,024 characters in length.
        self.note = note
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The tags.
        self.tag = tag
        # The ID or logon email address of the account that you want to invite.
        # 
        # This parameter is required.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
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
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
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
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
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
        # The description of the invitation.
        self.note = note
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The status of the invitation. Valid values:
        # 
        # *   Pending
        # *   Accepted
        # *   Cancelled
        # *   Declined
        # *   Expired
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
        # The information about the invitation.
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


class ListAccountsRequest(TeaModel):
    def __init__(
        self,
        include_tags: bool = None,
        page_number: int = None,
        page_size: int = None,
        query_keyword: str = None,
        tag: List[ListAccountsRequestTag] = None,
    ):
        # Specifies whether to return information about tags. Valid values:
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
        # The keyword used for the query, such as the display name of a member.
        # 
        # Fuzzy match is supported.
        self.query_keyword = query_keyword
        # The tags. This parameter specifies a filter condition.
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
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        account_name: str = None,
        deletion_status: str = None,
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
        # The Alibaba Cloud account name of the member.
        self.account_name = account_name
        # The deletion status of the member. Valid values:
        # 
        # *   Checking: A deletion check is being performed for the member.
        # *   Deleting: The member is being deleted.
        # *   CheckFailed: The deletion check for the member fails.
        # *   DeleteFailed: The member fails to be deleted.
        # 
        # >  If deletion is not performed for the member, the value of this parameter is empty.
        self.deletion_status = deletion_status
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
        # The RDPath of the member.
        self.resource_directory_path = resource_directory_path
        # The status of the member. Valid values:
        # 
        # *   CreateSuccess: The member is created.
        # *   PromoteVerifying: The upgrade of the member is under confirmation.
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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.deletion_status is not None:
            result['DeletionStatus'] = self.deletion_status
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DeletionStatus') is not None:
            self.deletion_status = m.get('DeletionStatus')
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
        # The information about the members.
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        # Specifies whether to return information about tags. Valid values:
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
        # The ID of the folder.
        self.parent_folder_id = parent_folder_id
        # The keyword used for the query, such as the display name of a member.
        # 
        # Fuzzy match is supported.
        self.query_keyword = query_keyword
        # The tags. This parameter specifies a filter condition.
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        account_name: str = None,
        deletion_status: str = None,
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
        # The Alibaba Cloud account name of the member.
        self.account_name = account_name
        # The deletion status of the member. Valid values:
        # 
        # *   Checking: A deletion check is being performed for the member.
        # *   Deleting: The member is being deleted.
        # *   CheckFailed: The deletion check for the member fails.
        # *   DeleteFailed: The member fails to be deleted.
        # 
        # >  If deletion is not performed for the member, the value of this parameter is empty.
        self.deletion_status = deletion_status
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
        # *   PromoteVerifying: The upgrade of the member is under confirmation.
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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.deletion_status is not None:
            result['DeletionStatus'] = self.deletion_status
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DeletionStatus') is not None:
            self.deletion_status = m.get('DeletionStatus')
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
        # The information about the members.
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
        # The ID of the subfolder.
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
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        # 
        # > This parameter is available only for system access control policies.
        self.language = language
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The type of the access control policies. Valid values:
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
        # The information of the access control policies.
        self.control_policies = control_policies
        # The page number of the returned page.
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
        # > This parameter is valid only for system access control policies.
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
        # The information about the attached access control policies.
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
        # The Alibaba Cloud account ID of the member.
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
        # The information about the delegated administrator accounts.
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


class ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService(TeaModel):
    def __init__(
        self,
        delegation_enabled_time: str = None,
        service_principal: str = None,
        status: str = None,
    ):
        # The time when the member was specified as a delegated administrator account.
        self.delegation_enabled_time = delegation_enabled_time
        # The identifier of the trusted service.
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
        # The information about the trusted services.
        # 
        # > If the value of this parameter is empty, the member is not specified as a delegated administrator account.
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


class ListFoldersForParentRequestTag(TeaModel):
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


class ListFoldersForParentRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
        tag: List[ListFoldersForParentRequestTag] = None,
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
                temp_model = ListFoldersForParentRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListFoldersForParentResponseBodyFoldersFolderTagsTag(TeaModel):
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


class ListFoldersForParentResponseBodyFoldersFolderTags(TeaModel):
    def __init__(
        self,
        tag: List[ListFoldersForParentResponseBodyFoldersFolderTagsTag] = None,
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
                temp_model = ListFoldersForParentResponseBodyFoldersFolderTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListFoldersForParentResponseBodyFoldersFolder(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        tags: ListFoldersForParentResponseBodyFoldersFolderTags = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

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
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('Tags') is not None:
            temp_model = ListFoldersForParentResponseBodyFoldersFolderTags()
            self.tags = temp_model.from_map(m['Tags'])
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
        # The description of the invitation.
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
        # The description of the invitation.
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


class ListMessageContactVerificationsRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMessageContactVerificationsResponseBodyContactVerifications(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        target: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The object that is used for verification. Valid values:
        # 
        # - Mobile phone number
        # - Email address
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ListMessageContactVerificationsResponseBody(TeaModel):
    def __init__(
        self,
        contact_verifications: List[ListMessageContactVerificationsResponseBodyContactVerifications] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The record for the contact to be verified.
        self.contact_verifications = contact_verifications
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.contact_verifications:
            for k in self.contact_verifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactVerifications'] = []
        if self.contact_verifications is not None:
            for k in self.contact_verifications:
                result['ContactVerifications'].append(k.to_map() if k else None)
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
        self.contact_verifications = []
        if m.get('ContactVerifications') is not None:
            for k in m.get('ContactVerifications'):
                temp_model = ListMessageContactVerificationsResponseBodyContactVerifications()
                self.contact_verifications.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageContactVerificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMessageContactVerificationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMessageContactVerificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMessageContactsRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        member: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The ID of the object to which the contact is bound. Valid values:
        # 
        # *   ID of the resource directory
        # *   ID of the folder
        # *   ID of the member
        self.member = member
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.member is not None:
            result['Member'] = self.member
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Member') is not None:
            self.member = m.get('Member')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMessageContactsResponseBodyContacts(TeaModel):
    def __init__(
        self,
        associated_date: str = None,
        contact_id: str = None,
        create_date: str = None,
        email_address: str = None,
        members: List[str] = None,
        message_types: List[str] = None,
        name: str = None,
        phone_number: str = None,
        status: str = None,
        title: str = None,
    ):
        # The time when the contact was bound to the objects.
        self.associated_date = associated_date
        # The ID of the contact.
        self.contact_id = contact_id
        # The time when the contact was added.
        self.create_date = create_date
        # The email address of the contact.
        self.email_address = email_address
        # The IDs of objects to which the contact is bound.
        self.members = members
        # The types of messages received by the contact.
        self.message_types = message_types
        # The name of the contact.
        self.name = name
        # The mobile phone number of the contact.
        self.phone_number = phone_number
        # The status of the contact. Valid values:
        # 
        # - Verifying
        # - Active
        # - Deleting
        self.status = status
        # The job title of the contact.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associated_date is not None:
            result['AssociatedDate'] = self.associated_date
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.members is not None:
            result['Members'] = self.members
        if self.message_types is not None:
            result['MessageTypes'] = self.message_types
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedDate') is not None:
            self.associated_date = m.get('AssociatedDate')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListMessageContactsResponseBody(TeaModel):
    def __init__(
        self,
        contacts: List[ListMessageContactsResponseBodyContacts] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The time when the contact was bound to the objects.
        self.contacts = contacts
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
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
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = ListMessageContactsResponseBodyContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMessageContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMessageContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMessageContactsResponseBody()
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
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
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
        # The request ID.
        self.request_id = request_id
        # The information about the tag keys.
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        # The Alibaba Cloud account IDs of the members. This parameter specifies a filter condition for the query.
        # 
        # > If you want to query the tags that are added to the members in a resource directory, you must configure both the `ResourceId` and `ResourceType` parameters and set the `ResourceType` parameter to `Account` in your request.
        self.resource_id = resource_id
        # The type of the objects whose tags you want to query. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   Account: member
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags. This parameter specifies a filter condition for the query.
        # 
        # You can specify a maximum of 20 tags.
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
        # The Alibaba Cloud account ID of the member.
        self.resource_id = resource_id
        # The type of the object whose tags are queried. Valid values:
        # 
        # *   Account: member
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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
        # Indicates whether the next query is required.```` Valid values:
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the `next query` is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.````
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
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
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
        # The request ID.
        self.request_id = request_id
        # The information about the tag values.
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
        # The time when the access control policy was attached to the object.
        self.attach_date = attach_date
        # The ID of the object.
        self.target_id = target_id
        # The name of the object.
        self.target_name = target_name
        # The type of the object. Valid values:
        # 
        # *   Root: Root folder
        # *   Folder: subfolder of the Root folder
        # *   Account: member
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
        # The information about the objects to which the access control policy is attached.
        self.target_attachments = target_attachments
        # The total number of objects to which the access control policy is attached.
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
        # The ID of the management account or delegated administrator account.
        # 
        # *   If you set this parameter to the ID of a management account, the trusted services that are enabled within the management account are queried. The default value of this parameter is the ID of an management account.
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
        # The identifier of the trusted service.
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
        # The information about the trusted services that are enabled.
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
        # The Alibaba Cloud account ID of the member that you want to move.
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


class PrecheckForConsolidatedBillingAccountRequest(TeaModel):
    def __init__(
        self,
        billing_account_id: str = None,
    ):
        # The ID of the management account or member to be used as a main financial account.
        # 
        # This parameter is required.
        self.billing_account_id = billing_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_account_id is not None:
            result['BillingAccountId'] = self.billing_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingAccountId') is not None:
            self.billing_account_id = m.get('BillingAccountId')
        return self


class PrecheckForConsolidatedBillingAccountResponseBodyReasons(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class PrecheckForConsolidatedBillingAccountResponseBody(TeaModel):
    def __init__(
        self,
        reasons: List[PrecheckForConsolidatedBillingAccountResponseBodyReasons] = None,
        request_id: str = None,
        result: bool = None,
    ):
        # The cause of the check failure.
        self.reasons = reasons
        # The request ID.
        self.request_id = request_id
        # Indicates whether the check was successful. Valid values:
        # 
        # *   true
        # *   false
        self.result = result

    def validate(self):
        if self.reasons:
            for k in self.reasons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Reasons'] = []
        if self.reasons is not None:
            for k in self.reasons:
                result['Reasons'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reasons = []
        if m.get('Reasons') is not None:
            for k in m.get('Reasons'):
                temp_model = PrecheckForConsolidatedBillingAccountResponseBodyReasons()
                self.reasons.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class PrecheckForConsolidatedBillingAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PrecheckForConsolidatedBillingAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PrecheckForConsolidatedBillingAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDelegatedAdministratorRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        service_principal: str = None,
    ):
        # The Alibaba Cloud account ID of the member in the resource directory.
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


class SendEmailVerificationForMessageContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        email_address: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address of the contact.
        # 
        # The specified email address must be the one you specify when you call [AddMessageContact](~~AddMessageContact~~).
        self.email_address = email_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        return self


class SendEmailVerificationForMessageContactResponseBody(TeaModel):
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


class SendEmailVerificationForMessageContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendEmailVerificationForMessageContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendEmailVerificationForMessageContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendPhoneVerificationForMessageContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        phone_number: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The mobile phone number of the contact.
        # 
        # The value must be in the `<Country code>-<Mobile phone number>` format.
        # 
        # The specified mobile phone number must be the one you specify when you call the [AddMessageContact](~~AddMessageContact~~) operation.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class SendPhoneVerificationForMessageContactResponseBody(TeaModel):
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


class SendPhoneVerificationForMessageContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendPhoneVerificationForMessageContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendPhoneVerificationForMessageContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationCodeForBindSecureMobilePhoneRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        secure_mobile_phone: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The mobile phone number that you want to bind to the member for security purposes.
        # 
        # Specify the mobile phone number in the \\<Country code>-\\<Mobile phone number> format.
        # 
        # > Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
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
        # > Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
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


class SetMemberDeletionPermissionRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        # Specifies whether to enable the member deletion feature. Valid values:
        # 
        # *   Enabled: enables the member deletion feature.
        # *   Disabled: disables the member deletion feature.
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
        # The key of the tag.
        # 
        # A tag key can be a maximum of 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of the tag.
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
        # The Alibaba Cloud account IDs of the members.
        # 
        # You can specify a maximum of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the objects to which you want to add tags. Valid values:
        # 
        # *   Account: member
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        # 
        # You can specify a maximum of 20 tags.
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
        # Specifies whether to remove all tags from the specified members. Valid values:
        # 
        # *   false (default value)
        # *   true
        self.all = all
        # The Alibaba Cloud account IDs of the members.
        # 
        # You can specify a maximum of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the objects from which you want to remove tags. Valid values:
        # 
        # *   Account: member
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys.
        # 
        # You can specify a maximum of 20 tag keys.
        # 
        # > If you set the `All` parameter to `true`, you do not need to specify tag keys.
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
        dry_run: bool = None,
        new_account_type: str = None,
        new_display_name: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks items such as whether the member status can be modified and whether security information is configured for the member. If the request does not pass the dry run, an error code is returned.
        # *   false (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The new type of the member. Valid values:
        # 
        # *   ResourceAccount: resource account
        # *   CloudAccount: cloud account
        # 
        # > You can specify either `NewDisplayName` or `NewAccountType`.
        self.new_account_type = new_account_type
        # The new display name of the member.
        # 
        # > You can specify either `NewDisplayName` or `NewAccountType`.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.new_account_type is not None:
            result['NewAccountType'] = self.new_account_type
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
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
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The Alibaba Cloud account name of the member.
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
        # The information about the folder.
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


class UpdateMessageContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        email_address: str = None,
        message_types: List[str] = None,
        name: str = None,
        phone_number: str = None,
        title: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address of the contact.
        # 
        # After you specify an email address, you need to call [SendEmailVerificationForMessageContact](~~SendEmailVerificationForMessageContact~~) to send verification information to the email address. After the verification is passed, the email address takes effect.
        self.email_address = email_address
        # The types of messages received by the contact.
        self.message_types = message_types
        # The name of the contact.
        self.name = name
        # The mobile phone number of the contact.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # After you specify a mobile phone number, you need to call [SendPhoneVerificationForMessageContact](~~SendPhoneVerificationForMessageContact~~) to send verification information to the mobile phone number. After the verification is passed, the mobile phone number takes effect.
        self.phone_number = phone_number
        # The job title of the contact.
        # 
        # Valid values:
        # 
        # *   FinanceDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TechnicalDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MaintenanceDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CEO
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ProjectDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Other
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.message_types is not None:
            result['MessageTypes'] = self.message_types
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateMessageContactResponseBody(TeaModel):
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


class UpdateMessageContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMessageContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateMessageContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


