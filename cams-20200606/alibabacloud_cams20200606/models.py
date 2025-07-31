# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddChatGroupRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        description: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.description = description
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class AddChatGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        unique_code: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.unique_code = unique_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class AddChatGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddChatGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddChatGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddChatGroupInviteLinkRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AddChatGroupInviteLinkResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        invite_link: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.invite_link = invite_link
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.invite_link is not None:
            result['InviteLink'] = self.invite_link
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InviteLink') is not None:
            self.invite_link = m.get('InviteLink')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddChatGroupInviteLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddChatGroupInviteLinkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddChatGroupInviteLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddChatappPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        cc: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        pre_validate_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verified_name: str = None,
    ):
        # You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        # 
        # This parameter is required.
        self.cc = cc
        # Adds a phone number for a WhatsApp Business account (WABA).
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # AddChatappPhoneNumber
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # cams:ChatappPhoneNumberRegister
        self.pre_validate_id = pre_validate_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Private
        # 
        # This parameter is required.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.pre_validate_id is not None:
            result['PreValidateId'] = self.pre_validate_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PreValidateId') is not None:
            self.pre_validate_id = m.get('PreValidateId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class AddChatappPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # com.alicom.access.oxs.client.channel.aliyun.flow.AyFlowExecuteService
        self.access_denied_detail = access_denied_detail
        # The phone number.
        self.code = code
        # com.alicom.access.oxs.client.channel.aliyun.flow.dto.AyCommonApiRequest
        self.message = message
        # formData
        self.request_id = request_id
        # 13800000000
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddChatappPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddChatappPhoneNumberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddChatappPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappBindWabaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ChatappBindWabaResponseBodyData(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        waba_id: str = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The ID of the WhatsApp Business Account (WABA).
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ChatappBindWabaResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChatappBindWabaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappBindWabaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappBindWabaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappEmbedSignUpRequest(TeaModel):
    def __init__(
        self,
        input_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.input_token = input_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_token is not None:
            result['InputToken'] = self.input_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputToken') is not None:
            self.input_token = m.get('InputToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChatappEmbedSignUpResponseBodyWabas(TeaModel):
    def __init__(
        self,
        account_review_status: str = None,
        currency: str = None,
        id: str = None,
        message_template_namespace: str = None,
        name: str = None,
    ):
        # The review state of the WABA.
        self.account_review_status = account_review_status
        # The currency.
        self.currency = currency
        # The ID of the WABA.
        self.id = id
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WABA.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ChatappEmbedSignUpResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        wabas: List[ChatappEmbedSignUpResponseBodyWabas] = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The list of the WhatsApp Business accounts.
        self.wabas = wabas

    def validate(self):
        if self.wabas:
            for k in self.wabas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Wabas'] = []
        if self.wabas is not None:
            for k in self.wabas:
                result['Wabas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.wabas = []
        if m.get('Wabas') is not None:
            for k in m.get('Wabas'):
                temp_model = ChatappEmbedSignUpResponseBodyWabas()
                self.wabas.append(temp_model.from_map(k))
        return self


class ChatappEmbedSignUpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappEmbedSignUpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappEmbedSignUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappMigrationRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # None
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChatappMigrationRegisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappMigrationRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappMigrationRegisterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappMigrationRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappMigrationVerifiedRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verify_code: str = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The verification code.
        # 
        # This parameter is required.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappMigrationVerifiedResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
    ):
        # The ID of the phone number.
        self.id = id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class ChatappMigrationVerifiedResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ChatappMigrationVerifiedResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ChatappMigrationVerifiedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappMigrationVerifiedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappMigrationVerifiedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappMigrationVerifiedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappPhoneNumberDeregisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChatappPhoneNumberDeregisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChatappPhoneNumberDeregisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappPhoneNumberDeregisterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappPhoneNumberDeregisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappPhoneNumberRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChatappPhoneNumberRegisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChatappPhoneNumberRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappPhoneNumberRegisterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappPhoneNumberRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappSyncPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ChatappSyncPhoneNumberResponseBodyPhoneNumbers(TeaModel):
    def __init__(
        self,
        code_verification_status: str = None,
        is_official: str = None,
        messaging_limit_tier: str = None,
        name_status: str = None,
        new_name_status: str = None,
        phone_number: str = None,
        quality_rating: str = None,
        status: str = None,
        status_callback_url: str = None,
        status_queue: str = None,
        up_callback_url: str = None,
        up_queue: str = None,
        verified_name: str = None,
    ):
        # The verification state of the phone number.
        # 
        # Valid values:
        # 
        # *   REVOKED: The review application is revoked.
        # *   MORE_INFORMATION_REQUESTED: More information needs to be provided.
        # *   VERIFIED: The phone number passes the verification.
        # *   REJECTED: The phone number fails to pass the verification.
        self.code_verification_status = code_verification_status
        # Indicates whether it is a WhatsApp Official Business Account (OBA).
        self.is_official = is_official
        # The number of phone numbers to which messages can be sent in a day.
        self.messaging_limit_tier = messaging_limit_tier
        # The review status of the business display name.
        self.name_status = name_status
        # The review status of the new business display name.
        self.new_name_status = new_name_status
        # The phone number.
        self.phone_number = phone_number
        # The quality rating of the phone number.
        # 
        # Valid values:
        # 
        # *   RED
        # *   YELLOW
        # *   GREEN
        self.quality_rating = quality_rating
        # The state of the phone number.
        # 
        # Valid values:
        # 
        # *   MIGRATED
        # *   FLAGGED
        # *   DISCONNECTED
        # *   UNVERIFIED
        # *   BANNED
        # *   RATE_LIMITED
        # *   PENDING
        # *   CONNECTED
        # *   UNKNOWN
        # *   DELETED
        # *   RESTRICTED
        self.status = status
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url
        # The status report queue.
        self.status_queue = status_queue
        # The URL that receives the MO messages.
        self.up_callback_url = up_callback_url
        # The mobile originated (MO) message queue.
        self.up_queue = up_queue
        # The display name of the business to which the phone number belongs.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.is_official is not None:
            result['IsOfficial'] = self.is_official
        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier
        if self.name_status is not None:
            result['NameStatus'] = self.name_status
        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating
        if self.status is not None:
            result['Status'] = self.status
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')
        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')
        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')
        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class ChatappSyncPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        phone_numbers: List[ChatappSyncPhoneNumberResponseBodyPhoneNumbers] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The phone numbers.
        self.phone_numbers = phone_numbers
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The call was successful.
        # *   **false**: The call failed.
        self.success = success

    def validate(self):
        if self.phone_numbers:
            for k in self.phone_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k in self.phone_numbers:
                result['PhoneNumbers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k in m.get('PhoneNumbers'):
                temp_model = ChatappSyncPhoneNumberResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChatappSyncPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappSyncPhoneNumberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappSyncPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatappVerifyAndRegisterRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verify_code: str = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class ChatappVerifyAndRegisterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The call was successful.
        # *   **false**: The call failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChatappVerifyAndRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatappVerifyAndRegisterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatappVerifyAndRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatFlowRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_trigger_type: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow trigger type
        self.flow_trigger_type = flow_trigger_type
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateChatFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_trigger_type: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow trigger type
        self.flow_trigger_type = flow_trigger_type
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateChatFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Access denied details, this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Returned data object.
        self.data = data
        # Error message.
        self.message = message
        # Unique request ID.
        self.request_id = request_id
        # Response data
        self.response = response
        # Whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateChatFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatFlowByImportRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_view_model: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Imported flow DSL data
        self.flow_view_model = flow_view_model
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_view_model is not None:
            result['FlowViewModel'] = self.flow_view_model
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowViewModel') is not None:
            self.flow_view_model = m.get('FlowViewModel')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateChatFlowByImportShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_view_model: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Imported flow DSL data
        self.flow_view_model = flow_view_model
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_view_model is not None:
            result['FlowViewModel'] = self.flow_view_model
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowViewModel') is not None:
            self.flow_view_model = m.get('FlowViewModel')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateChatFlowByImportResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # Request status code.
        self.code = code
        # Returned data object.
        self.data = data
        # Error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the request was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateChatFlowByImportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatFlowByImportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatFlowByImportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatFlowLogSettingRequest(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Process code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateChatFlowLogSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Returned data.
        self.data = data
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values: true for success, false for failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateChatFlowLogSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatFlowLogSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatFlowLogSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappMigrationInitiateRequest(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        cust_space_id: str = None,
        mobile_number: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The code of the country or region.
        # 
        # This parameter is required.
        self.country_code = country_code
        # The space ID of the user within the ISV account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The mobile number without the country code or region code.
        # 
        # This parameter is required.
        self.mobile_number = mobile_number
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateChatappMigrationInitiateResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
        status: str = None,
    ):
        # The ID of the mobile number.
        self.id = id
        # The mobile number.
        self.phone_number = phone_number
        # The state of the mobile number. Only MIGRATING may be returned, which indicates that the mobile number is being migrated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateChatappMigrationInitiateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CreateChatappMigrationInitiateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the request denial..
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   A value of OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The response data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateChatappMigrationInitiateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChatappMigrationInitiateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatappMigrationInitiateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatappMigrationInitiateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatappTemplateRequestComponentsButtonsSupportedApps(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        # The name of the Android application package. This parameter is required if you create an Android application.
        self.package_name = package_name
        # WhatsApp template is required when Category is Authoritative and Button Type is ONE_TAP/ZERO-TAP, indicating the signature hash value of the WhatsApp application.
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        return self


class CreateChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[CreateChatappTemplateRequestComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.autofill_text = autofill_text
        # The coupon code. It can contain only letters and digits. You can set this parameter to a variable such as $(couponCode). Specify the value of couponCode when you send a message.
        self.coupon_code = coupon_code
        # The Flow action.
        # 
        # Valid values:
        # 
        # *   DATA_EXCHANGE
        # *   NAVIGATE
        self.flow_action = flow_action
        # The Flow ID.
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. Marketing messages will not be sent to customers if you configure message sending in the Chat App Message Service console and the customers click this button.
        self.is_opt_out = is_opt_out
        # The first screen in the Flow. This parameter is required if FlowAction is set to NAVIGATE.
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.package_name = package_name
        # The phone number. This parameter is valid only when the Type sub-parameter of the Buttons parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.signature_hash = signature_hash
        # List of supported apps.
        self.supported_apps = supported_apps
        # The display name of the button.
        self.text = text
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # *   **COPY_CODE**: copy code button
        # *   **ONE_TAP**: one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   If Category is set to AUTHENTICATION for a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If Type is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If Type is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value of Text indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        # 
        # This parameter is required.
        self.type = type
        # The URL to be accessed when you click the URL button.
        self.url = url
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        if self.supported_apps:
            for k in self.supported_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k in self.supported_apps:
                result['SupportedApps'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k in m.get('SupportedApps'):
                temp_model = CreateChatappTemplateRequestComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The text of the button.
        self.text = text
        # The type of the button. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The type of the URL. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class CreateChatappTemplateRequestComponentsCardsCardComponents(TeaModel):
    def __init__(
        self,
        buttons: List[CreateChatappTemplateRequestComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the CardComponents parameter to BUTTONS. A carousel card can contain up to two buttons.
        self.buttons = buttons
        # The type of the media resource. This parameter is valid if the Type sub-parameter of the CardComponents parameter is set to HEADER. Valid values:
        # 
        # *   **IMAGE**\
        # *   **VIDEO**\
        self.format = format
        # The body content of the carousel card.
        self.text = text
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **BUTTONS**\
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = CreateChatappTemplateRequestComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequestComponentsCards(TeaModel):
    def __init__(
        self,
        card_components: List[CreateChatappTemplateRequestComponentsCardsCardComponents] = None,
    ):
        # The components of the carousel card.
        # 
        # This parameter is required.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = CreateChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class CreateChatappTemplateRequestComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[CreateChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        cards: List[CreateChatappTemplateRequestComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        has_expiration: bool = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the Components parameter to **BUTTONS**.
        # 
        # >  ####
        # 
        # *   A marketing or utility WhatsApp message template can contain up to 10 buttons.
        # 
        # *   A WhatsApp message template can contain only one phone call button.
        # 
        # *   A WhatsApp message template can contain up to two URL buttons.
        # 
        # *   In a WhatsApp message template, a quick reply button cannot be used together with a phone call button or a URL button.
        self.buttons = buttons
        # The description of the document.
        self.caption = caption
        # The carousel cards of the carousel template.
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The type of the media resource. Valid values:
        # 
        # *   **TEXT**\
        # *   **IMAGE**\
        # *   **DOCUMENT**\
        # *   **VIDEO**\
        self.format = format
        # Specifies whether the coupon code has an expiration time. Specify this parameter if the Type sub-parameter of the Components parameter is set to LIMITED_TIME_OFFER.
        self.has_expiration = has_expiration
        # The text of the message that you want to send.
        # 
        # >  If Category is set to AUTHENTICATION, the Text sub-parameter of the Components parameter must be empty.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The type of the component. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # *   **CAROUSEL**\
        # *   **LIMITED_TIME_OFFER**\
        # 
        # > 
        # 
        # *   In a WhatsApp message template, a **Body** component cannot exceed 1,024 characters in length. A **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER**, **CAROUSEL**, and **LIMITED_TIME_OFFER** components are not supported in Viber message templates.
        # 
        # *   In Viber message templates, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed below the text in the message received on a device.
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
        # 
        # >  We recommend that you use 800 × 800 images in Viber message templates.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = CreateChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = CreateChatappTemplateRequestComponentsCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        allow_category_change: bool = None,
        category: str = None,
        category_change_paused: bool = None,
        components: List[CreateChatappTemplateRequestComponents] = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example: Dict[str, str] = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        template_type: str = None,
    ):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # This parameter is required.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter must be empty.
        # 
        # This parameter is required.
        self.components = components
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example = example
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        # 
        # This parameter is required.
        self.name = name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change
        if self.category is not None:
            result['Category'] = self.category
        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = CreateChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        allow_category_change: bool = None,
        category: str = None,
        category_change_paused: bool = None,
        components_shrink: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example_shrink: str = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        template_type: str = None,
    ):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # This parameter is required.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter must be empty.
        # 
        # This parameter is required.
        self.components_shrink = components_shrink
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        # 
        # This parameter is required.
        self.name = name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change
        if self.category is not None:
            result['Category'] = self.category
        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateChatappTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        template_name: str = None,
    ):
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CreateChatappTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateChatappTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatappTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        cust_space_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.categories = categories
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        categories_shrink: str = None,
        cust_space_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.categories_shrink = categories_shrink
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The Flow ID.
        self.flow_id = flow_id
        # The name of the Flow.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CreateFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version_copy_from: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # The flow version to be copied.
        self.flow_version_copy_from = flow_version_copy_from
        self.owner_id = owner_id
        # Version remarks.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version_copy_from is not None:
            result['FlowVersionCopyFrom'] = self.flow_version_copy_from
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersionCopyFrom') is not None:
            self.flow_version_copy_from = m.get('FlowVersionCopyFrom')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version_copy_from: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # The flow version to be copied.
        self.flow_version_copy_from = flow_version_copy_from
        self.owner_id = owner_id
        # Version remarks.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version_copy_from is not None:
            result['FlowVersionCopyFrom'] = self.flow_version_copy_from
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersionCopyFrom') is not None:
            self.flow_version_copy_from = m.get('FlowVersionCopyFrom')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Details of access denial; this field is only returned when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Request status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true for success, false for failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        generate_qr_image: str = None,
        owner_id: int = None,
        phone_number: str = None,
        prefilled_message: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.generate_qr_image = generate_qr_image
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.prefilled_message = prefilled_message
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreatePhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        # The URL of the deep link.
        self.deep_link_url = deep_link_url
        # The format of the generated image.
        self.generate_qr_image = generate_qr_image
        # The phone number.
        self.phone_number = phone_number
        # The message content.
        self.prefilled_message = prefilled_message
        # The URL of the QR code.
        self.qr_image_url = qr_image_url
        # The mode of the quick-response (QR) code.
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class CreatePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: CreatePhoneMessageQrdlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePhoneMessageQrdlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatFlowRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Process code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteChatFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Process code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteChatFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Access denied details, this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Error code
        self.code = code
        # Error message.
        self.message = message
        # Unique request ID.
        self.request_id = request_id
        # Response data
        self.response = response
        # Whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteChatFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChatFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteChatFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatGroupRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteChatGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteChatGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChatGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteChatGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatGroupInviteLinkRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteChatGroupInviteLinkResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteChatGroupInviteLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChatGroupInviteLinkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteChatGroupInviteLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatGroupParticipantsRequestList(TeaModel):
    def __init__(
        self,
        participant_number: str = None,
    ):
        self.participant_number = participant_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.participant_number is not None:
            result['ParticipantNumber'] = self.participant_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParticipantNumber') is not None:
            self.participant_number = m.get('ParticipantNumber')
        return self


class DeleteChatGroupParticipantsRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        list: List[DeleteChatGroupParticipantsRequestList] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.list = list
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DeleteChatGroupParticipantsRequestList()
                self.list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteChatGroupParticipantsShrinkRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        list_shrink: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.list_shrink = list_shrink
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.list_shrink is not None:
            result['List'] = self.list_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('List') is not None:
            self.list_shrink = m.get('List')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteChatGroupParticipantsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteChatGroupParticipantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChatGroupParticipantsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteChatGroupParticipantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business Account (WABA) ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The ISV verification code. This parameter is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The template language.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template code.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name
        # The template type. This parameter is required if you delete a template in a language.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DeleteChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChatappTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        qrdl_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.qrdl_code = qrdl_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeletePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePhoneMessageQrdlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeprecateFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeprecateFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The result returns OK as normal.
        self.code = code
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeprecateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeprecateFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeprecateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWhatsappROIMetricRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The verification code used to verify whether the RAM user is authorized by the independent software vendor (ISV) account.
        self.isv_code = isv_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class EnableWhatsappROIMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableWhatsappROIMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableWhatsappROIMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableWhatsappROIMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlowBindPhoneRequest(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # Message channel Code
        # 
        # This parameter is required.
        self.channel_code = channel_code
        # Message channel Type
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # WABA account ID, or PageId for other channel types, etc.
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class FlowBindPhoneShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # Message channel Code
        # 
        # This parameter is required.
        self.channel_code = channel_code
        # Message channel Type
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers_shrink = phone_numbers_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # WABA account ID, or PageId for other channel types, etc.
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers_shrink is not None:
            result['PhoneNumbers'] = self.phone_numbers_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers_shrink = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class FlowBindPhoneResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of access denial; this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error description message.
        self.message = message
        # Return result.
        self.model = model
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FlowBindPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlowBindPhoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlowBindPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlowRebindPhoneRequest(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # Message channel code
        # 
        # This parameter is required.
        self.channel_code = channel_code
        # Message channel type
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # WABA account ID, or PageId for other channel types, etc.
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class FlowRebindPhoneShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # Message channel code
        # 
        # This parameter is required.
        self.channel_code = channel_code
        # Message channel type
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers_shrink = phone_numbers_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # WABA account ID, or PageId for other channel types, etc.
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers_shrink is not None:
            result['PhoneNumbers'] = self.phone_numbers_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers_shrink = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class FlowRebindPhoneResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request result data.
        self.model = model
        # Request ID.
        self.request_id = request_id
        # Whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FlowRebindPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlowRebindPhoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlowRebindPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlowUnbindPhoneRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Message channel type
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class FlowUnbindPhoneShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Message channel type
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers_shrink = phone_numbers_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_numbers_shrink is not None:
            result['PhoneNumbers'] = self.phone_numbers_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers_shrink = m.get('PhoneNumbers')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class FlowUnbindPhoneResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: bool = None,
        success: bool = None,
    ):
        # Access denied details, this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Request status code.
        self.code = code
        # Error message.
        self.message = message
        # Request result data.
        self.model = model
        # Whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FlowUnbindPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlowUnbindPhoneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlowUnbindPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatFlowMetricRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        from_: int = None,
        metric_name: str = None,
        metric_param: Dict[str, Any] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version.
        self.flow_version = flow_version
        # Start timestamp in seconds.
        self.from_ = from_
        # Metric name.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        self.metric_param = metric_param
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # End timestamp in seconds.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.from_ is not None:
            result['From'] = self.from_
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricParam') is not None:
            self.metric_param = m.get('MetricParam')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetChatFlowMetricShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        from_: int = None,
        metric_name: str = None,
        metric_param_shrink: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # Flow version.
        self.flow_version = flow_version
        # Start timestamp in seconds.
        self.from_ = from_
        # Metric name.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        self.metric_param_shrink = metric_param_shrink
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # End timestamp in seconds.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.from_ is not None:
            result['From'] = self.from_
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_param_shrink is not None:
            result['MetricParam'] = self.metric_param_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricParam') is not None:
            self.metric_param_shrink = m.get('MetricParam')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetChatFlowMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Returned data object.
        self.data = data
        # Error message.
        self.message = message
        # Unique request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetChatFlowMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatFlowMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatFlowMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatFlowTemplateRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        # 
        # This parameter is required.
        self.biz_code = biz_code
        # Template ID
        self.id = id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetChatFlowTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        response: Dict[str, Any] = None,
    ):
        # Content of the returned data.
        self.response = response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response is not None:
            result['Response'] = self.response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Response') is not None:
            self.response = m.get('Response')
        return self


class GetChatFlowTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetChatFlowTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details, this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # System returned error code. For more details on error codes, please refer to the error code documentation.
        self.code = code
        # Returned data.
        self.data = data
        # Error message.
        self.message = message
        # Unique request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatFlowTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetChatFlowTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatFlowTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatFlowTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappPhoneNumberMetricRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        end: int = None,
        granularity: str = None,
        isv_code: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start: int = None,
    ):
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end = end
        # The granularity of the metric.
        # 
        # Valid values:
        # 
        # *   DAILY
        # *   HALF_HOUR
        self.granularity = granularity
        # The independent software vendor (ISV) verification code, which is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        self.owner_id = owner_id
        # The business phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetChatappPhoneNumberMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        delivered_count: int = None,
        end: int = None,
        granularity: str = None,
        phone_number: str = None,
        sent_count: int = None,
        start: int = None,
    ):
        # The number of delivered messages.
        self.delivered_count = delivered_count
        # The end of the time range that you queried.
        self.end = end
        # The granularity of the metric.
        # 
        # Valid values:
        # 
        # *   DAILY
        # *   HALF_HOUR
        self.granularity = granularity
        # The business phone number.
        self.phone_number = phone_number
        # The number of sent messages.
        self.sent_count = sent_count
        # The beginning of the time range that you queried.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetChatappPhoneNumberMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[GetChatappPhoneNumberMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChatappPhoneNumberMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappPhoneNumberMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappPhoneNumberMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappPhoneNumberMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappTemplateDetailRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The independent software vendor (ISV) verification code. This parameter is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The code of the message template.
        self.template_code = template_code
        # Name of a template.
        self.template_name = template_name
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs(TeaModel):
    def __init__(
        self,
        action: str = None,
        intent_code: str = None,
        next_language_code: str = None,
        next_template_code: str = None,
        next_template_name: str = None,
    ):
        # The event type.
        self.action = action
        # The intent code.
        self.intent_code = intent_code
        # The language of the next template.
        self.next_language_code = next_language_code
        # The code of the next template.
        self.next_template_code = next_template_code
        # The name of the next template.
        self.next_template_name = next_template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.intent_code is not None:
            result['IntentCode'] = self.intent_code
        if self.next_language_code is not None:
            result['NextLanguageCode'] = self.next_language_code
        if self.next_template_code is not None:
            result['NextTemplateCode'] = self.next_template_code
        if self.next_template_name is not None:
            result['NextTemplateName'] = self.next_template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('IntentCode') is not None:
            self.intent_code = m.get('IntentCode')
        if m.get('NextLanguageCode') is not None:
            self.next_language_code = m.get('NextLanguageCode')
        if m.get('NextTemplateCode') is not None:
            self.next_template_code = m.get('NextTemplateCode')
        if m.get('NextTemplateName') is not None:
            self.next_template_name = m.get('NextTemplateName')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        # The app package name.
        self.package_name = package_name
        # The app signing key hash.
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        extend_attrs: GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.autofill_text = autofill_text
        # The coupon code.
        self.coupon_code = coupon_code
        # The extended fields.
        self.extend_attrs = extend_attrs
        # The Flow action. Valid values: NAVIGATE and DATA_EXCHANGE.
        self.flow_action = flow_action
        # The Flow ID.
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. Marketing messages will not be sent to customers if you configure message sending in the Chat App Message Service console and the customers click this button.
        self.is_opt_out = is_opt_out
        # The first screen in the Flow. This parameter is returned if FlowAction is set to NAVIGATE.
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.package_name = package_name
        # The phone number. This parameter is valid only if the Type sub-parameter of the Buttons parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.signature_hash = signature_hash
        # The apps that support one-tap authentication and zero-tap authentication.
        self.supported_apps = supported_apps
        # The display name of the button.
        self.text = text
        # The button type. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # *   **COPY_CODE**: copy code button
        # *   **ONE_TAP**: one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   If Category is set to AUTHENTICATION for a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If Type is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If Type is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value of Text indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The URL type. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        if self.extend_attrs:
            self.extend_attrs.validate()
        if self.supported_apps:
            for k in self.supported_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.extend_attrs is not None:
            result['ExtendAttrs'] = self.extend_attrs.to_map()
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k in self.supported_apps:
                result['SupportedApps'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('ExtendAttrs') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs()
            self.extend_attrs = temp_model.from_map(m['ExtendAttrs'])
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k in m.get('SupportedApps'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The button text.
        self.text = text
        # The type of the button in the carousel template. Valid values: URL, PHONE_NUMBER, and QUICK_REQLY.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The type of the URL. Valid values: static and dynamic.
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents(TeaModel):
    def __init__(
        self,
        buttons: List[GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The buttons of the carousel card.
        self.buttons = buttons
        # The type of the header in the carousel template. The header can only be an image or a video. The headers of all carousel cards must be the same. The type of the media resources that are included in the message. Valid values: IMGAGE and VIDEO.
        self.format = format
        # The text of the carousel card.
        self.text = text
        # The component type.
        self.type = type
        # The URL.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetChatappTemplateDetailResponseBodyDataComponentsCards(TeaModel):
    def __init__(
        self,
        card_components: List[GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents] = None,
    ):
        # The components of the carousel card.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class GetChatappTemplateDetailResponseBodyDataComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[GetChatappTemplateDetailResponseBodyDataComponentsButtons] = None,
        caption: str = None,
        cards: List[GetChatappTemplateDetailResponseBodyDataComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        latitude: str = None,
        location_address: str = None,
        location_name: str = None,
        longitude: str = None,
        offer_expiration_time_ms: str = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
        has_expiration: bool = None,
    ):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. This parameter is returned only if the Type sub-parameter of the Components parameter is set to **BUTTONS**.
        # 
        # >  ####
        # 
        # *   A marketing or utility WhatsApp message template can contain up to 10 buttons.
        # 
        # *   A WhatsApp message template can contain only one phone call button.
        # 
        # *   A WhatsApp message template can contain up to two URL buttons.
        # 
        # *   In a WhatsApp message template, a quick reply button cannot be used together with a phone call button or a URL button.
        self.buttons = buttons
        # The description of the document.
        self.caption = caption
        # The carousel cards.
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER for a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The format.
        self.format = format
        # The latitude of the location.
        self.latitude = latitude
        # The address of the location.
        self.location_address = location_address
        # The name of the location.
        self.location_name = location_name
        # The longitude of the location.
        self.longitude = longitude
        # The variable when the coupon code expires in the limited-time offer template.
        self.offer_expiration_time_ms = offer_expiration_time_ms
        # The text of the message that you want to send.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The component type. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # *   **CAROUSEL**\
        # *   **LIMITED_TIME_OFFER**\
        # 
        # > 
        # 
        # *   In a WhatsApp message template, a **Body** component cannot exceed 1,024 characters in length. A **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER**, **CAROUSEL**, and **LIMITED_TIME_OFFER** components are not supported in Viber message templates.
        # 
        # *   In Viber message templates, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed below the text in the message received on a device.
        self.type = type
        # The URL of the media resource.
        self.url = url
        # Indicates whether the coupon code has an expiration time in the limited-time offer template.
        self.has_expiration = has_expiration

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location_address is not None:
            result['LocationAddress'] = self.location_address
        if self.location_name is not None:
            result['LocationName'] = self.location_name
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.offer_expiration_time_ms is not None:
            result['OfferExpirationTimeMs'] = self.offer_expiration_time_ms
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.has_expiration is not None:
            result['hasExpiration'] = self.has_expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponentsCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('LocationAddress') is not None:
            self.location_address = m.get('LocationAddress')
        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('OfferExpirationTimeMs') is not None:
            self.offer_expiration_time_ms = m.get('OfferExpirationTimeMs')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('hasExpiration') is not None:
            self.has_expiration = m.get('hasExpiration')
        return self


class GetChatappTemplateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        allow_send: bool = None,
        audit_status: str = None,
        category: str = None,
        category_change_paused: bool = None,
        components: List[GetChatappTemplateDetailResponseBodyDataComponents] = None,
        example: Dict[str, str] = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        quality_score: str = None,
        reason: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.allow_send = allow_send
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the template when the returned value of TemplateType is WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: a transactional template
        # *   **MARKETING**: a marketing template
        # *   **AUTHENTICATION**: an identity authentication template
        # 
        # The category of the template when the returned value of the TemplateType parameter is VIBER. Valid values:
        # 
        # *   **text**: a template that contains only text
        # *   **image**: a template that contains only images
        # *   **text_image_button**: a template that contains text, images, and buttons
        # *   **text_button**: a template that contains text and buttons
        # *   **document**: a template that contains only files
        # *   **video**: a template that contains only videos
        # *   **text_video**: a template that contains text and videos
        # *   **text_video_button**: a template that contains text, videos, and buttons
        # *   **text_image**: a template that contains text and images
        # 
        # > If Category is set to text_video_button, users cannot open a web page by clicking the button. Users can open only the video in the message. In this case, you do not need to specify the Url parameter for the URL button in the template.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        self.components = components
        # The examples of variables.
        self.example = example
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The validity period of the WhatsApp authentication message.
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        self.name = name
        # The quality of the template.
        self.quality_score = quality_score
        # The reason why the template was rejected.
        self.reason = reason
        # The code of the message template.
        self.template_code = template_code
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE (developing)
        self.template_type = template_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_send is not None:
            result['AllowSend'] = self.allow_send
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.example is not None:
            result['Example'] = self.example
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSend') is not None:
            self.allow_send = m.get('AllowSend')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = GetChatappTemplateDetailResponseBodyDataComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateDetailResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetChatappTemplateDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code.
        # 
        # *   Example: OK. This value indicates that the request is successful.
        # *   Other codes indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatappTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappTemplateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappTemplateDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappTemplateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappTemplateMetricRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        end: int = None,
        granularity: str = None,
        isv_code: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start: int = None,
        template_code: str = None,
        template_type: str = None,
    ):
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end = end
        # The granularity of the metric.
        # 
        # Valid values:
        # 
        # *   DAILY
        # *   HALF_HOUR
        self.granularity = granularity
        # The independent software vendor (ISV) verification code, which is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The template language.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start = start
        # The template code.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The template type. If you do not specify this parameter, the default value WHATSAPP is used.
        # 
        # Valid values:
        # 
        # *   VIBER
        # *   WHATSAPP
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end is not None:
            result['End'] = self.end
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start is not None:
            result['Start'] = self.start
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetChatappTemplateMetricResponseBodyDataCliented(TeaModel):
    def __init__(
        self,
        button_content: str = None,
        count: int = None,
        type: str = None,
    ):
        # The text on the button.
        self.button_content = button_content
        # The number of clicks.
        self.count = count
        # The button type.
        # 
        # Valid values:
        # 
        # *   phone_number_button
        # *   url_button
        # *   quick_relpy_button
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.button_content is not None:
            result['ButtonContent'] = self.button_content
        if self.count is not None:
            result['Count'] = self.count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ButtonContent') is not None:
            self.button_content = m.get('ButtonContent')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetChatappTemplateMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        cliented: List[GetChatappTemplateMetricResponseBodyDataCliented] = None,
        delivered_count: int = None,
        end: int = None,
        language: str = None,
        read_count: int = None,
        sent_count: int = None,
        start: int = None,
        template_code: str = None,
    ):
        # The statistics on button clicks.
        self.cliented = cliented
        # The number of delivered messages.
        self.delivered_count = delivered_count
        # The end of the time range you queried.
        self.end = end
        # The template language.
        self.language = language
        # The number of read messages.
        self.read_count = read_count
        # The number of sent messages.
        self.sent_count = sent_count
        # The beginning of the time range you queried.
        self.start = start
        # The template code.
        self.template_code = template_code

    def validate(self):
        if self.cliented:
            for k in self.cliented:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cliented'] = []
        if self.cliented is not None:
            for k in self.cliented:
                result['Cliented'].append(k.to_map() if k else None)
        if self.delivered_count is not None:
            result['DeliveredCount'] = self.delivered_count
        if self.end is not None:
            result['End'] = self.end
        if self.language is not None:
            result['Language'] = self.language
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.start is not None:
            result['Start'] = self.start
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cliented = []
        if m.get('Cliented') is not None:
            for k in m.get('Cliented'):
                temp_model = GetChatappTemplateMetricResponseBodyDataCliented()
                self.cliented.append(temp_model.from_map(k))
        if m.get('DeliveredCount') is not None:
            self.delivered_count = m.get('DeliveredCount')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class GetChatappTemplateMetricResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[GetChatappTemplateMetricResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The value OK indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetChatappTemplateMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappTemplateMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappTemplateMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappTemplateMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappUploadAuthorizationRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetChatappUploadAuthorizationResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        dir: str = None,
        end_point: str = None,
        expire: int = None,
        security_token: str = None,
    ):
        # The AccessKey ID that is used to authorize a user to upload a file to Object Storage Service (OSS).
        self.access_key_id = access_key_id
        # The AccessKey secret that is used to authorize a user to upload a file to OSS.
        self.access_key_secret = access_key_secret
        # The name of the bucket to which a file is uploaded in OSS.
        self.bucket_name = bucket_name
        # The directory to which the file is uploaded in Object Storage Service (OSS).
        self.dir = dir
        # The address of the OSS server to which a file is uploaded.
        self.end_point = end_point
        # The timeout period.
        self.expire = expire
        # The security token.
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetChatappUploadAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetChatappUploadAuthorizationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Access denied for detailed information.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetChatappUploadAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetChatappUploadAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappUploadAuthorizationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappUploadAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChatappVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        locale: str = None,
        method: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.locale = locale
        # This parameter is required.
        self.method = method
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.method is not None:
            result['Method'] = self.method
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetChatappVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The call was successful.
        # *   **false**: The call failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetChatappVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChatappVerifyCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetChatappVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommerceSettingRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetCommerceSettingResponseBodyData(TeaModel):
    def __init__(
        self,
        cart_enable: bool = None,
        catalog_visible: bool = None,
    ):
        # Indicates whether the shopping cart button is displayed. Valid values:
        # 
        # *   true
        # *   false
        self.cart_enable = cart_enable
        # Indicates whether the catalog button is displayed. Valid values:
        # 
        # *   true
        # *   false
        self.catalog_visible = catalog_visible

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable
        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')
        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')
        return self


class GetCommerceSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetCommerceSettingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied for detailed information.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCommerceSettingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCommerceSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommerceSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCommerceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationalAutomationRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account or the instance ID of the customer of Alibaba Cloud.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number of the enterprise.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetConversationalAutomationResponseBodyDataCommands(TeaModel):
    def __init__(
        self,
        command_description: str = None,
        command_name: str = None,
    ):
        # The description of the command.
        self.command_description = command_description
        # The name of the command.
        self.command_name = command_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        return self


class GetConversationalAutomationResponseBodyData(TeaModel):
    def __init__(
        self,
        commands: List[GetConversationalAutomationResponseBodyDataCommands] = None,
        enable_welcome_message: bool = None,
        phone_number: str = None,
        prompts: List[str] = None,
    ):
        # The commands.
        self.commands = commands
        # Indicates whether the welcoming message is enabled.
        self.enable_welcome_message = enable_welcome_message
        # The phone number of the enterprise.
        self.phone_number = phone_number
        # The opening remarks.
        self.prompts = prompts

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prompts is not None:
            result['Prompts'] = self.prompts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = GetConversationalAutomationResponseBodyDataCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Prompts') is not None:
            self.prompts = m.get('Prompts')
        return self


class GetConversationalAutomationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetConversationalAutomationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetConversationalAutomationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConversationalAutomationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConversationalAutomationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConversationalAutomationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        data_api_version: str = None,
        flow_id: str = None,
        flow_name: str = None,
        jsonversion: str = None,
        preview_url: str = None,
        preview_url_expires: int = None,
        status: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The version number of the API.
        self.data_api_version = data_api_version
        # The Flow ID.
        self.flow_id = flow_id
        # The Flow name.
        self.flow_name = flow_name
        # The JSON version.
        self.jsonversion = jsonversion
        # The temporary preview URL.
        self.preview_url = preview_url
        # The time when the preview URL expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.preview_url_expires = preview_url_expires
        # The state of the Flow.
        # 
        # Valid values:
        # 
        # *   PUBLISHED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DRAFT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DEPRECATED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.data_api_version is not None:
            result['DataApiVersion'] = self.data_api_version
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.jsonversion is not None:
            result['JSONVersion'] = self.jsonversion
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('DataApiVersion') is not None:
            self.data_api_version = m.get('DataApiVersion')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('JSONVersion') is not None:
            self.jsonversion = m.get('JSONVersion')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowJSONAssestRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetFlowJSONAssestResponseBodyData(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        flow_id: str = None,
    ):
        # The file path.
        self.file_path = file_path
        # The Flow ID.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowJSONAssestResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetFlowJSONAssestResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFlowJSONAssestResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowJSONAssestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowJSONAssestResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFlowJSONAssestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowPreviewUrlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetFlowPreviewUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        preview_url: str = None,
        preview_url_expires: int = None,
    ):
        # The Flow ID.
        self.flow_id = flow_id
        # The temporary preview URL.
        self.preview_url = preview_url
        # The time when the preview URL expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.preview_url_expires = preview_url_expires

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.preview_url_expires is not None:
            result['PreviewUrlExpires'] = self.preview_url_expires
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('PreviewUrlExpires') is not None:
            self.preview_url_expires = m.get('PreviewUrlExpires')
        return self


class GetFlowPreviewUrlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetFlowPreviewUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFlowPreviewUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFlowPreviewUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowPreviewUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFlowPreviewUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMigrationVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        locale: str = None,
        method: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user under the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The language.
        # 
        # This parameter is required.
        self.locale = locale
        # The method to obtain the verification code. Valid values: SMS and VOICE.
        # 
        # This parameter is required.
        self.method = method
        self.owner_id = owner_id
        # Phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.method is not None:
            result['Method'] = self.method
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetMigrationVerifyCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
    ):
        # The ID of the number.
        self.id = id
        # Phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetMigrationVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetMigrationVerifyCodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetMigrationVerifyCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMigrationVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMigrationVerifyCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMigrationVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermissionByCodeRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        permissions: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.code = code
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.permissions = permissions
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetPermissionByCodeShrinkRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        permissions_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.code = code
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.permissions_shrink = permissions_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetPermissionByCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPermissionByCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPermissionByCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPermissionByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneEncryptionPublicKeyRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetPhoneEncryptionPublicKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        encryption_public_key: str = None,
        encryption_public_key_status: str = None,
        phone_number: str = None,
    ):
        # The public key.
        self.encryption_public_key = encryption_public_key
        # The validity state of the public key. Valid values:
        # 
        # *   MISMATCH: The public key is invalid.
        # *   VALID: The public key is valid.
        self.encryption_public_key_status = encryption_public_key_status
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key
        if self.encryption_public_key_status is not None:
            result['EncryptionPublicKeyStatus'] = self.encryption_public_key_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')
        if m.get('EncryptionPublicKeyStatus') is not None:
            self.encryption_public_key_status = m.get('EncryptionPublicKeyStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneEncryptionPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetPhoneEncryptionPublicKeyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneEncryptionPublicKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneEncryptionPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneEncryptionPublicKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPhoneEncryptionPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberVerificationStatusRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetPhoneNumberVerificationStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        code_verification_status: str = None,
        id: str = None,
        phone_number: str = None,
    ):
        # The verification status.
        self.code_verification_status = code_verification_status
        # The ID of the number.
        self.id = id
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.id is not None:
            result['Id'] = self.id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class GetPhoneNumberVerificationStatusResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetPhoneNumberVerificationStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberVerificationStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberVerificationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneNumberVerificationStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPhoneNumberVerificationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreValidatePhoneIdRequest(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        verify_code: str = None,
    ):
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The verification code provided when you purchased the pre-registered phone number.
        # 
        # This parameter is required.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class GetPreValidatePhoneIdResponseBodyData(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        phone_number_id: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The ID of the phone number.
        self.phone_number_id = phone_number_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_id is not None:
            result['PhoneNumberId'] = self.phone_number_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberId') is not None:
            self.phone_number_id = m.get('PhoneNumberId')
        return self


class GetPreValidatePhoneIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPreValidatePhoneIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPreValidatePhoneIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPreValidatePhoneIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPreValidatePhoneIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPreValidatePhoneIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWhatsappConnectionCatalogRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The WABA ID.
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappConnectionCatalogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWhatsappConnectionCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWhatsappConnectionCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWhatsappConnectionCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWhatsappHealthStatusRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        language: str = None,
        node_type: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        waba_id: str = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account or the instance ID of the customer of Alibaba Cloud.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The template language.
        self.language = language
        # The node type.
        # 
        # Valid values:
        # 
        # *   template: message template
        # *   phone: phone number
        # *   waba: WhatsApp Business Account (WABA)
        # 
        # This parameter is required.
        self.node_type = node_type
        self.owner_id = owner_id
        # The phone number of the enterprise.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template code.
        self.template_code = template_code
        # WabaId
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.language is not None:
            result['Language'] = self.language
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappHealthStatusResponseBodyDataEntitiesErrors(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_description: str = None,
        possible_solution: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The description of the error.
        self.error_description = error_description
        # The possible solution to the error.
        self.possible_solution = possible_solution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_description is not None:
            result['ErrorDescription'] = self.error_description
        if self.possible_solution is not None:
            result['PossibleSolution'] = self.possible_solution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorDescription') is not None:
            self.error_description = m.get('ErrorDescription')
        if m.get('PossibleSolution') is not None:
            self.possible_solution = m.get('PossibleSolution')
        return self


class GetWhatsappHealthStatusResponseBodyDataEntities(TeaModel):
    def __init__(
        self,
        business_id: str = None,
        can_send_message: str = None,
        entity_type: str = None,
        errors: List[GetWhatsappHealthStatusResponseBodyDataEntitiesErrors] = None,
        language: str = None,
        phone_number: str = None,
        template_code: str = None,
        waba_id: str = None,
    ):
        # The Business Manager ID.
        self.business_id = business_id
        # Indicates whether the messages can be sent.
        self.can_send_message = can_send_message
        # The entity type.
        self.entity_type = entity_type
        # The reasons why the messages failed to be sent.
        self.errors = errors
        # The template language.
        self.language = language
        # The phone number to which the messages are sent.
        self.phone_number = phone_number
        # The template code. This parameter is returned when the NodeType parameter is set to **template**.
        self.template_code = template_code
        # The WABA ID. You can view the WABA ID in the Chat App Message Service console after you create the WABA.
        self.waba_id = waba_id

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.can_send_message is not None:
            result['CanSendMessage'] = self.can_send_message
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        result['Errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['Errors'].append(k.to_map() if k else None)
        if self.language is not None:
            result['Language'] = self.language
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('CanSendMessage') is not None:
            self.can_send_message = m.get('CanSendMessage')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        self.errors = []
        if m.get('Errors') is not None:
            for k in m.get('Errors'):
                temp_model = GetWhatsappHealthStatusResponseBodyDataEntitiesErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class GetWhatsappHealthStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        can_send_message: str = None,
        entities: List[GetWhatsappHealthStatusResponseBodyDataEntities] = None,
    ):
        # Indicates whether the messages can be sent.
        self.can_send_message = can_send_message
        # The queried entities.
        self.entities = entities

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_send_message is not None:
            result['CanSendMessage'] = self.can_send_message
        result['Entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['Entities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSendMessage') is not None:
            self.can_send_message = m.get('CanSendMessage')
        self.entities = []
        if m.get('Entities') is not None:
            for k in m.get('Entities'):
                temp_model = GetWhatsappHealthStatusResponseBodyDataEntities()
                self.entities.append(temp_model.from_map(k))
        return self


class GetWhatsappHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetWhatsappHealthStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetWhatsappHealthStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWhatsappHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWhatsappHealthStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWhatsappHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsvGetAppIdRequest(TeaModel):
    def __init__(
        self,
        intl_version: str = None,
        owner_id: int = None,
        permissions: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
    ):
        self.intl_version = intl_version
        self.owner_id = owner_id
        self.permissions = permissions
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intl_version is not None:
            result['IntlVersion'] = self.intl_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntlVersion') is not None:
            self.intl_version = m.get('IntlVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class IsvGetAppIdResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_id: str = None,
        code: str = None,
        config_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The message ID.
        self.app_id = app_id
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The ID of the configuration item.
        self.config_id = config_id
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IsvGetAppIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IsvGetAppIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IsvGetAppIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingRelationsForFlowVersionRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Channel type. Values:
        # - INSTAGRAM
        # - WHATSAPP
        # - MESSENGER
        # 
        # 
        # <props="intl">- VIBER
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Process code. View the process code in the [Flow Editor](https://chatapp.console.aliyun.com/ChatFlowBuilder) interface.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListBindingRelationsForFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[Dict[str, Any]] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # Error code. For more information, see [Error Codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # Returned data list.
        self.data = data
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values:
        # 
        # - true: Success.
        # 
        # - false: Failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBindingRelationsForFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindingRelationsForFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBindingRelationsForFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatFlowRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_trigger_type: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        return_with_online_version: bool = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow trigger type, enum values:
        # - TriggeredManually
        # - TriggeredByWhatsApp
        # - TriggeredByInstagram
        # - TriggeredByViber
        # - TriggeredByMessenger
        self.flow_trigger_type = flow_trigger_type
        # Search keyword.
        self.keyword = keyword
        self.owner_id = owner_id
        # Page number
        self.page_no = page_no
        # Page size.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Whether to return the online status
        self.return_with_online_version = return_with_online_version
        # Flow status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.return_with_online_version is not None:
            result['ReturnWithOnlineVersion'] = self.return_with_online_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReturnWithOnlineVersion') is not None:
            self.return_with_online_version = m.get('ReturnWithOnlineVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChatFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_trigger_type: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        return_with_online_version: bool = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow trigger type, enum values:
        # - TriggeredManually
        # - TriggeredByWhatsApp
        # - TriggeredByInstagram
        # - TriggeredByViber
        # - TriggeredByMessenger
        self.flow_trigger_type = flow_trigger_type
        # Search keyword.
        self.keyword = keyword
        self.owner_id = owner_id
        # Page number
        self.page_no = page_no
        # Page size.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Whether to return the online status
        self.return_with_online_version = return_with_online_version
        # Flow status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_trigger_type is not None:
            result['FlowTriggerType'] = self.flow_trigger_type
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.return_with_online_version is not None:
            result['ReturnWithOnlineVersion'] = self.return_with_online_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowTriggerType') is not None:
            self.flow_trigger_type = m.get('FlowTriggerType')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReturnWithOnlineVersion') is not None:
            self.return_with_online_version = m.get('ReturnWithOnlineVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChatFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Access denied details, this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # System error code. For more details on error codes, please refer to the error code documentation.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Response data
        self.response = response
        # Whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatFlowTemplateRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        trigger_type: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        # 
        # This parameter is required.
        self.biz_code = biz_code
        # Search keyword.
        self.keyword = keyword
        self.owner_id = owner_id
        # Page number
        self.page_no = page_no
        # Number of records per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Trigger type, with the following enum values:
        # 
        # - TriggeredManually
        # - TriggeredByWhatsApp
        # - TriggeredByInstagram
        # - TriggeredByViber
        # - TriggeredByMessenger
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ListChatFlowTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        response: Dict[str, Any] = None,
    ):
        # Content of the returned data.
        self.response = response

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response is not None:
            result['Response'] = self.response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Response') is not None:
            self.response = m.get('Response')
        return self


class ListChatFlowTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListChatFlowTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Returned data object.
        self.data = data
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChatFlowTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatFlowTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatFlowTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatFlowTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatGroupRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListChatGroupRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_status: str = None,
        owner_id: int = None,
        page: ListChatGroupRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.group_status = group_status
        self.owner_id = owner_id
        # This parameter is required.
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_status is not None:
            result['GroupStatus'] = self.group_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            temp_model = ListChatGroupRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class ListChatGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_status: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.group_status = group_status
        self.owner_id = owner_id
        # This parameter is required.
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_status is not None:
            result['GroupStatus'] = self.group_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class ListChatGroupResponseBodyDataList(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        description: str = None,
        group_id: str = None,
        group_status: str = None,
        invite_link: str = None,
        profile_picture_file: str = None,
        subject: str = None,
    ):
        self.business_number = business_number
        self.description = description
        self.group_id = group_id
        self.group_status = group_status
        self.invite_link = invite_link
        self.profile_picture_file = profile_picture_file
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_status is not None:
            result['GroupStatus'] = self.group_status
        if self.invite_link is not None:
            result['InviteLink'] = self.invite_link
        if self.profile_picture_file is not None:
            result['ProfilePictureFile'] = self.profile_picture_file
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')
        if m.get('InviteLink') is not None:
            self.invite_link = m.get('InviteLink')
        if m.get('ProfilePictureFile') is not None:
            self.profile_picture_file = m.get('ProfilePictureFile')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class ListChatGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListChatGroupResponseBodyDataList] = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListChatGroupResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListChatGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListChatGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChatGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatGroupParticipantsRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        self.index = index
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListChatGroupParticipantsRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        page: ListChatGroupParticipantsRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            temp_model = ListChatGroupParticipantsRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListChatGroupParticipantsShrinkRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListChatGroupParticipantsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        participant_number: str = None,
    ):
        self.participant_number = participant_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.participant_number is not None:
            result['ParticipantNumber'] = self.participant_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParticipantNumber') is not None:
            self.participant_number = m.get('ParticipantNumber')
        return self


class ListChatGroupParticipantsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListChatGroupParticipantsResponseBodyDataList] = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListChatGroupParticipantsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListChatGroupParticipantsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ListChatGroupParticipantsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChatGroupParticipantsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatGroupParticipantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatGroupParticipantsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatGroupParticipantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatappMessageRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListChatappMessageRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        client_accept_status: str = None,
        cust_space_id: str = None,
        end_time: int = None,
        event_action: str = None,
        group_message_id: str = None,
        message_status: str = None,
        owner_id: int = None,
        page: ListChatappMessageRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: int = None,
        template_code: str = None,
        user_number: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        # This parameter is required.
        self.channel_type = channel_type
        self.client_accept_status = client_accept_status
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.end_time = end_time
        self.event_action = event_action
        self.group_message_id = group_message_id
        self.message_status = message_status
        self.owner_id = owner_id
        # This parameter is required.
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.template_code = template_code
        self.user_number = user_number

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.client_accept_status is not None:
            result['ClientAcceptStatus'] = self.client_accept_status
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_action is not None:
            result['EventAction'] = self.event_action
        if self.group_message_id is not None:
            result['GroupMessageId'] = self.group_message_id
        if self.message_status is not None:
            result['MessageStatus'] = self.message_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ClientAcceptStatus') is not None:
            self.client_accept_status = m.get('ClientAcceptStatus')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventAction') is not None:
            self.event_action = m.get('EventAction')
        if m.get('GroupMessageId') is not None:
            self.group_message_id = m.get('GroupMessageId')
        if m.get('MessageStatus') is not None:
            self.message_status = m.get('MessageStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            temp_model = ListChatappMessageRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class ListChatappMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        client_accept_status: str = None,
        cust_space_id: str = None,
        end_time: int = None,
        event_action: str = None,
        group_message_id: str = None,
        message_status: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: int = None,
        template_code: str = None,
        user_number: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        # This parameter is required.
        self.channel_type = channel_type
        self.client_accept_status = client_accept_status
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.end_time = end_time
        self.event_action = event_action
        self.group_message_id = group_message_id
        self.message_status = message_status
        self.owner_id = owner_id
        # This parameter is required.
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time
        self.template_code = template_code
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.client_accept_status is not None:
            result['ClientAcceptStatus'] = self.client_accept_status
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_action is not None:
            result['EventAction'] = self.event_action
        if self.group_message_id is not None:
            result['GroupMessageId'] = self.group_message_id
        if self.message_status is not None:
            result['MessageStatus'] = self.message_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ClientAcceptStatus') is not None:
            self.client_accept_status = m.get('ClientAcceptStatus')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventAction') is not None:
            self.event_action = m.get('EventAction')
        if m.get('GroupMessageId') is not None:
            self.group_message_id = m.get('GroupMessageId')
        if m.get('MessageStatus') is not None:
            self.message_status = m.get('MessageStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class ListChatappMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        client_accept_status_name: str = None,
        client_read_status: str = None,
        client_read_status_name: str = None,
        conversation_id: str = None,
        event_action: str = None,
        event_action_name: str = None,
        fail_back_content: str = None,
        fail_back_flag: str = None,
        fail_reason: str = None,
        language_code: str = None,
        message: str = None,
        message_id: str = None,
        message_source: str = None,
        message_status: str = None,
        message_status_name: str = None,
        message_type: str = None,
        message_type_name: str = None,
        month: str = None,
        send_time: str = None,
        template_code: str = None,
        template_name: str = None,
        type: str = None,
        unique_message_id: str = None,
        user_number: str = None,
    ):
        self.business_number = business_number
        self.channel_type = channel_type
        self.client_accept_status_name = client_accept_status_name
        self.client_read_status = client_read_status
        self.client_read_status_name = client_read_status_name
        self.conversation_id = conversation_id
        self.event_action = event_action
        self.event_action_name = event_action_name
        self.fail_back_content = fail_back_content
        self.fail_back_flag = fail_back_flag
        self.fail_reason = fail_reason
        self.language_code = language_code
        self.message = message
        self.message_id = message_id
        self.message_source = message_source
        self.message_status = message_status
        self.message_status_name = message_status_name
        self.message_type = message_type
        self.message_type_name = message_type_name
        self.month = month
        self.send_time = send_time
        self.template_code = template_code
        self.template_name = template_name
        self.type = type
        self.unique_message_id = unique_message_id
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.client_accept_status_name is not None:
            result['ClientAcceptStatusName'] = self.client_accept_status_name
        if self.client_read_status is not None:
            result['ClientReadStatus'] = self.client_read_status
        if self.client_read_status_name is not None:
            result['ClientReadStatusName'] = self.client_read_status_name
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.event_action is not None:
            result['EventAction'] = self.event_action
        if self.event_action_name is not None:
            result['EventActionName'] = self.event_action_name
        if self.fail_back_content is not None:
            result['FailBackContent'] = self.fail_back_content
        if self.fail_back_flag is not None:
            result['FailBackFlag'] = self.fail_back_flag
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.language_code is not None:
            result['LanguageCode'] = self.language_code
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.message_source is not None:
            result['MessageSource'] = self.message_source
        if self.message_status is not None:
            result['MessageStatus'] = self.message_status
        if self.message_status_name is not None:
            result['MessageStatusName'] = self.message_status_name
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.message_type_name is not None:
            result['MessageTypeName'] = self.message_type_name
        if self.month is not None:
            result['Month'] = self.month
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_message_id is not None:
            result['UniqueMessageId'] = self.unique_message_id
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ClientAcceptStatusName') is not None:
            self.client_accept_status_name = m.get('ClientAcceptStatusName')
        if m.get('ClientReadStatus') is not None:
            self.client_read_status = m.get('ClientReadStatus')
        if m.get('ClientReadStatusName') is not None:
            self.client_read_status_name = m.get('ClientReadStatusName')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('EventAction') is not None:
            self.event_action = m.get('EventAction')
        if m.get('EventActionName') is not None:
            self.event_action_name = m.get('EventActionName')
        if m.get('FailBackContent') is not None:
            self.fail_back_content = m.get('FailBackContent')
        if m.get('FailBackFlag') is not None:
            self.fail_back_flag = m.get('FailBackFlag')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('LanguageCode') is not None:
            self.language_code = m.get('LanguageCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('MessageSource') is not None:
            self.message_source = m.get('MessageSource')
        if m.get('MessageStatus') is not None:
            self.message_status = m.get('MessageStatus')
        if m.get('MessageStatusName') is not None:
            self.message_status_name = m.get('MessageStatusName')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('MessageTypeName') is not None:
            self.message_type_name = m.get('MessageTypeName')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueMessageId') is not None:
            self.unique_message_id = m.get('UniqueMessageId')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class ListChatappMessageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[ListChatappMessageResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListChatappMessageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatappMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatappMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatappMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatappTemplateRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # The page number. Default value: 1.
        # 
        # This parameter is required.
        self.index = index
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        code: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        owner_id: int = None,
        page: ListChatappTemplateRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_type: str = None,
    ):
        # The review state of the template. Valid values:
        # 
        # *   **pass**: The template is approved.
        # *   **fail**: The template is rejected.
        # *   **auditing**: The template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the message template.
        self.category = category
        # The code of the message template.
        self.code = code
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business Account (WABA) ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The ISV verification code. This parameter is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The name of the template.
        self.name = name
        self.owner_id = owner_id
        # The pagination settings.
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        self.template_type = template_type

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            temp_model = ListChatappTemplateRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        code: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_type: str = None,
    ):
        # The review state of the template. Valid values:
        # 
        # *   **pass**: The template is approved.
        # *   **fail**: The template is rejected.
        # *   **auditing**: The template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the message template.
        self.category = category
        # The code of the message template.
        self.code = code
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business Account (WABA) ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The ISV verification code. This parameter is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The name of the template.
        self.name = name
        self.owner_id = owner_id
        # The pagination settings.
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateResponseBodyListTemplate(TeaModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        language: str = None,
        last_update_time: int = None,
        reason: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The review state of the template. Valid values:
        # 
        # *   **pass**: The template is approved.
        # *   **fail**: The template is rejected.
        # *   **auditing**: The template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the WhatsApp message template. Valid values:
        # 
        # *   **UTILITY**\
        # *   **MARKETING**\
        # *   **AUTHENTICATION**\
        # 
        # The category of the Viber template. Valid values:
        # 
        # *   **text**: template that contains only text
        # *   **image**: template that contains only images
        # *   **text_image_button**: template that contains text, images, and buttons
        # *   **text_button**: template that contains text and buttons
        # *   **document**: template that contains only documents
        # *   **video**: template that contains only videos
        # *   **text_video**: template that contains text and videos
        # *   **text_video_button**: template that contains text, videos, and buttons
        # *   **text_image**: template that contains text and images
        self.category = category
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The time when the template was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_update_time = last_update_time
        # The reason why the template was rejected.
        self.reason = reason
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
        self.template_name = template_name
        # The type of the template. Valid values: WHATSAPP and VIBER.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.category is not None:
            result['Category'] = self.category
        if self.language is not None:
            result['Language'] = self.language
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        list_template: List[ListChatappTemplateResponseBodyListTemplate] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The message templates.
        self.list_template = list_template
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.list_template:
            for k in self.list_template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['ListTemplate'] = []
        if self.list_template is not None:
            for k in self.list_template:
                result['ListTemplate'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list_template = []
        if m.get('ListTemplate') is not None:
            for k in m.get('ListTemplate'):
                temp_model = ListChatappTemplateResponseBodyListTemplate()
                self.list_template.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChatappTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRequestPage(TeaModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        self.index = index
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        page: ListFlowRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            temp_model = ListFlowRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flows.
        self.categories = categories
        # The Flow ID.
        self.flow_id = flow_id
        # The Flow name.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ListFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[ListFlowResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFlowResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowNodePrototypeV2Request(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        group_code: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.biz_code = biz_code
        self.group_code = group_code
        self.keyword = keyword
        self.owner_id = owner_id
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListFlowNodePrototypeV2ResponseBodyDataModel(TeaModel):
    def __init__(
        self,
        code: str = None,
        group_code: str = None,
        public_extend: str = None,
        status: str = None,
    ):
        self.code = code
        self.group_code = group_code
        self.public_extend = public_extend
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.public_extend is not None:
            result['PublicExtend'] = self.public_extend
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('PublicExtend') is not None:
            self.public_extend = m.get('PublicExtend')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowNodePrototypeV2ResponseBodyData(TeaModel):
    def __init__(
        self,
        model: List[ListFlowNodePrototypeV2ResponseBodyDataModel] = None,
    ):
        self.model = model

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListFlowNodePrototypeV2ResponseBodyDataModel()
                self.model.append(temp_model.from_map(k))
        return self


class ListFlowNodePrototypeV2ResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        data: ListFlowNodePrototypeV2ResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListFlowNodePrototypeV2ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFlowNodePrototypeV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowNodePrototypeV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowNodePrototypeV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        # Current page number.
        self.page_no = page_no
        # Page size.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow version status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        # Current page number.
        self.page_no = page_no
        # Page size.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow version status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Details of access denied.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListPhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        # The URL of the deep link.
        self.deep_link_url = deep_link_url
        # The format of the generated image.
        self.generate_qr_image = generate_qr_image
        # The phone number.
        self.phone_number = phone_number
        # The message content.
        self.prefilled_message = prefilled_message
        # The URL of the QR code.
        self.qr_image_url = qr_image_url
        # The mode of the quick-response (QR) code.
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class ListPhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[ListPhoneMessageQrdlResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPhoneMessageQrdlResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPhoneMessageQrdlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductRequest(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
        catalog_id: str = None,
        cust_space_id: str = None,
        fields: str = None,
        limit: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before
        # The catalog ID.
        # 
        # This parameter is required.
        self.catalog_id = catalog_id
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The fields. Separate multiple fields with commas (,).
        # 
        #  see [product fields](https://help.aliyun.com/document_detail/2579419.html)
        self.fields = fields
        # The number of products to be queried. Valid values: 1 to 1000.
        self.limit = limit
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the WhatsApp Business account (WABA).
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class ListProductResponseBodyModelPagingCursors(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        return self


class ListProductResponseBodyModelPaging(TeaModel):
    def __init__(
        self,
        cursors: ListProductResponseBodyModelPagingCursors = None,
    ):
        # The cursors for pagination.
        self.cursors = cursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = ListProductResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m['Cursors'])
        return self


class ListProductResponseBodyModel(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        paging: ListProductResponseBodyModelPaging = None,
    ):
        # The returned data.
        self.data = data
        # The pagination details.
        self.paging = paging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Paging') is not None:
            temp_model = ListProductResponseBodyModelPaging()
            self.paging = temp_model.from_map(m['Paging'])
        return self


class ListProductResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: ListProductResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ListProductResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductCatalogRequest(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
        business_id: int = None,
        cust_space_id: str = None,
        fields: str = None,
        limit: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before
        # The Business Manager ID.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The fields. Separate multiple fields with commas (,).
        # see  [catalog fields](https://help.aliyun.com/document_detail/2579419.html)
        self.fields = fields
        # The number of catalogs to be queried. Valid values: 1 to 1000.
        self.limit = limit
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListProductCatalogResponseBodyModelPagingCursors(TeaModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['After'] = self.after
        if self.before is not None:
            result['Before'] = self.before
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')
        if m.get('Before') is not None:
            self.before = m.get('Before')
        return self


class ListProductCatalogResponseBodyModelPaging(TeaModel):
    def __init__(
        self,
        cursors: ListProductCatalogResponseBodyModelPagingCursors = None,
    ):
        # The cursors for pagination.
        self.cursors = cursors

    def validate(self):
        if self.cursors:
            self.cursors.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursors is not None:
            result['Cursors'] = self.cursors.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursors') is not None:
            temp_model = ListProductCatalogResponseBodyModelPagingCursors()
            self.cursors = temp_model.from_map(m['Cursors'])
        return self


class ListProductCatalogResponseBodyModel(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        paging: ListProductCatalogResponseBodyModelPaging = None,
    ):
        # The returned data.
        self.data = data
        # The pagination details.
        self.paging = paging

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Paging') is not None:
            temp_model = ListProductCatalogResponseBodyModelPaging()
            self.paging = temp_model.from_map(m['Paging'])
        return self


class ListProductCatalogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: ListProductCatalogResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ListProductCatalogResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductCatalogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductCatalogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyChatappTemplateRequestComponentsButtonsSupportedApps(TeaModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        # The Whatsapp template is required when the Category is\\" Authorisation \\"and the Button Type is\\" ONE_TAP/ZERO-TAP\\", indicating the signature hash value of the Whatsapp call application.
        self.package_name = package_name
        # The Whatsapp template is required when the Category is\\" Authorisation \\"and the Button Type is\\" ONE_TAP/ZERO-TAP\\", indicating the signature hash value of the Whatsapp call application.
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        return self


class ModifyChatappTemplateRequestComponentsButtons(TeaModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[ModifyChatappTemplateRequestComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.autofill_text = autofill_text
        # The coupon code. It can contain only letters and digits. You can set this parameter to a variable such as $(couponCode). Specify the value of couponCode when you send a message.
        self.coupon_code = coupon_code
        # The Flow action.
        # 
        # Valid values:
        # 
        # *   DATA_EXCHANGE
        # *   NAVIGATE
        self.flow_action = flow_action
        # The Flow ID.
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. Marketing messages will not be sent to customers if you configure message sending in the Chat App Message Service console and the customers click this button.
        self.is_opt_out = is_opt_out
        # The first screen in the Flow. This parameter is required if FlowAction is set to NAVIGATE.
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.package_name = package_name
        # The phone number.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.signature_hash = signature_hash
        # List of supported apps.
        self.supported_apps = supported_apps
        # The text of the button.
        self.text = text
        # The button type. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # *   **COPY_CODE**: copy code button
        # *   **ONE_TAP**: one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   If Category is set to AUTHENTICATION for a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If Type is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If Type is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value of Text indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The URL type. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        if self.supported_apps:
            for k in self.supported_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text
        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out
        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash
        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k in self.supported_apps:
                result['SupportedApps'].append(k.to_map() if k else None)
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')
        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')
        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')
        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')
        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k in m.get('SupportedApps'):
                temp_model = ModifyChatappTemplateRequestComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k))
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The text of the button.
        self.text = text
        # The button type. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The URL type. Valid values:
        # 
        # *   **static**\
        # *   **dynamic**\
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.url_type is not None:
            result['UrlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')
        return self


class ModifyChatappTemplateRequestComponentsCardsCardComponents(TeaModel):
    def __init__(
        self,
        buttons: List[ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the CardComponents parameter to BUTTONS. A carousel card can contain up to two buttons.
        self.buttons = buttons
        # The type of the media resource. This parameter is valid if the Type sub-parameter of the CardComponents parameter is set to HEADER. Valid values:
        # 
        # *   **IMAGE**\
        # *   **VIDEO**\
        self.format = format
        # The body content of the carousel card.
        self.text = text
        # The component type. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **BUTTONS**\
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.format is not None:
            result['Format'] = self.format
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequestComponentsCards(TeaModel):
    def __init__(
        self,
        card_components: List[ModifyChatappTemplateRequestComponentsCardsCardComponents] = None,
    ):
        # The components of the carousel card.
        # 
        # This parameter is required.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for k in self.card_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CardComponents'] = []
        if self.card_components is not None:
            for k in self.card_components:
                result['CardComponents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k in m.get('CardComponents'):
                temp_model = ModifyChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k))
        return self


class ModifyChatappTemplateRequestComponents(TeaModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[ModifyChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        cards: List[ModifyChatappTemplateRequestComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        has_expiration: bool = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the Components parameter to **BUTTONS**.
        # 
        # >  ####
        # 
        # *   A marketing or utility WhatsApp message template can contain up to 10 buttons.
        # 
        # *   A WhatsApp message template can contain only one phone call button.
        # 
        # *   A WhatsApp message template can contain up to two URL buttons.
        # 
        # *   In a WhatsApp message template, a quick reply button cannot be used together with a phone call button or a URL button.
        self.buttons = buttons
        # The description of the media resource.
        # 
        # >  If the Type sub-parameter of the Components parameter is set to **HEADER** and the Format parameter is set to **IMAGE, DOCUMENT, or VIDEO**, you can specify this parameter.
        self.caption = caption
        # The carousel cards of the carousel template.
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        # 
        # >  If the Type sub-parameter of the Components parameter is set to **HEADER** and the Format parameter is set to **DOCUMENT**, you can specify this parameter.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The type of the media resource. Valid values:
        # 
        # *   **TEXT**\
        # *   **IMAGE**\
        # *   **DOCUMENT**\
        # *   **VIDEO**\
        self.format = format
        # Specifies whether the coupon code has an expiration time. Specify this parameter if the Type sub-parameter of the Components parameter is set to LIMITED_TIME_OFFER.
        self.has_expiration = has_expiration
        # The text of the message that you want to send.
        # 
        # >  If Category is set to AUTHENTICATION, do not specify the Text sub-parameter of the Components parameter.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The component type. Valid values:
        # 
        # *   **BODY**\
        # *   **HEADER**\
        # *   **FOOTER**\
        # *   **BUTTONS**\
        # *   **CAROUSEL**\
        # *   **LIMITED_TIME_OFFER**\
        # 
        # > 
        # 
        # *   In a WhatsApp message template, a **Body** component cannot exceed 1,024 characters in length. A **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER**, **CAROUSEL**, and **LIMITED_TIME_OFFER** components are not supported in Viber message templates.
        # 
        # *   In Viber message templates, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed below the text in the message received on a device.
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
        self.url = url

    def validate(self):
        if self.buttons:
            for k in self.buttons:
                if k:
                    k.validate()
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation
        result['Buttons'] = []
        if self.buttons is not None:
            for k in self.buttons:
                result['Buttons'].append(k.to_map() if k else None)
        if self.caption is not None:
            result['Caption'] = self.caption
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.format is not None:
            result['Format'] = self.format
        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration
        if self.text is not None:
            result['Text'] = self.text
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')
        self.buttons = []
        if m.get('Buttons') is not None:
            for k in m.get('Buttons'):
                temp_model = ModifyChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k))
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = ModifyChatappTemplateRequestComponentsCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ModifyChatappTemplateRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        category_change_paused: bool = None,
        components: List[ModifyChatappTemplateRequestComponents] = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example: Dict[str, str] = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, you do not need to set the Text sub-parameter of the Components parameter because the value is automatically generated.
        # 
        # This parameter is required.
        self.components = components
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example = example
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The message template code.
        self.template_code = template_code
        # Template name.
        self.template_name = template_name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example is not None:
            result['Example'] = self.example
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ModifyChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        category_change_paused: bool = None,
        components_shrink: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example_shrink: str = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, you do not need to set the Text sub-parameter of the Components parameter because the value is automatically generated.
        # 
        # This parameter is required.
        self.components_shrink = components_shrink
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The message template code.
        self.template_code = template_code
        # Template name.
        self.template_name = template_name
        # The type of the message template.
        # 
        # *   **WHATSAPP**\
        # *   **VIBER**\
        # *   LINE: the Line message template. This type of message template will be released later.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.example_shrink is not None:
            result['Example'] = self.example_shrink
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.language is not None:
            result['Language'] = self.language
        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        template_name: str = None,
    ):
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ModifyChatappTemplateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ModifyChatappTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyChatappTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyChatappTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyChatappTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyChatappTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyChatappTemplatePropertiesRequest(TeaModel):
    def __init__(
        self,
        allow_send: bool = None,
        category_change_paused: bool = None,
        cust_space_id: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.allow_send = allow_send
        self.category_change_paused = category_change_paused
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.template_code = template_code
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_send is not None:
            result['AllowSend'] = self.allow_send
        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSend') is not None:
            self.allow_send = m.get('AllowSend')
        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ModifyChatappTemplatePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyChatappTemplatePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyChatappTemplatePropertiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyChatappTemplatePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowRequest(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        cust_space_id: str = None,
        flow_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.categories = categories
        self.cust_space_id = cust_space_id
        self.flow_id = flow_id
        # This parameter is required.
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        categories_shrink: str = None,
        cust_space_id: str = None,
        flow_id: str = None,
        flow_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.categories_shrink = categories_shrink
        self.cust_space_id = cust_space_id
        self.flow_id = flow_id
        # This parameter is required.
        self.flow_name = flow_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories_shrink is not None:
            result['Categories'] = self.categories_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories_shrink = m.get('Categories')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        flow_id: str = None,
        flow_name: str = None,
    ):
        # The categories of the Flow.
        self.categories = categories
        # The Flow ID.
        self.flow_id = flow_id
        # The Flow name.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ModifyFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ModifyFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPhoneBusinessProfileRequest(TeaModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        owner_id: int = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        # The business information.
        self.about = about
        # The address.
        self.address = address
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The description of the phone number.
        self.description = description
        # The email address.
        self.email = email
        self.owner_id = owner_id
        # The mobile phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The industry.
        # 
        # >  Valid values: OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, and RESTAURANT.
        self.vertical = vertical
        # The URLs of the websites.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileShrinkRequest(TeaModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        owner_id: int = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vertical: str = None,
        websites_shrink: str = None,
    ):
        # The business information.
        self.about = about
        # The address.
        self.address = address
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The description of the phone number.
        self.description = description
        # The email address.
        self.email = email
        self.owner_id = owner_id
        # The mobile phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The industry.
        # 
        # >  Valid values: OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, and RESTAURANT.
        self.vertical = vertical
        # The URLs of the websites.
        self.websites_shrink = websites_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.address is not None:
            result['Address'] = self.address
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites_shrink is not None:
            result['Websites'] = self.websites_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites_shrink = m.get('Websites')
        return self


class ModifyPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The URL of the website.
        self.code = code
        # The ID of the request.
        self.message = message
        # The websites.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPhoneBusinessProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPhoneBusinessProfileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPhoneBusinessProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OfflineFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Flow remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OfflineFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Access denied details; this field is only returned when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. true means success, false means failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OfflineFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OfflineFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Remark
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OnlineFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Remark
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OnlineFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Details of access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. true means success, false means failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OnlineFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnlineFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFlowRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PublishFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # If OK is returned, the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappBindWabaRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user under the ISV account.
        self.cust_space_id = cust_space_id
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryChatappBindWabaResponseBodyData(TeaModel):
    def __init__(
        self,
        account_review_status: str = None,
        auth_international_rate_eligibility: Dict[str, Any] = None,
        business_id: str = None,
        business_name: str = None,
        currency: str = None,
        id: str = None,
        marketing_message_lite_status: str = None,
        message_template_namespace: str = None,
        name: str = None,
        primary_business_location: str = None,
    ):
        # The review state of the WhatsApp Business account (WABA).
        # 
        # >  Valid values:
        # 
        # *   PENDING: The WABA is to be reviewed.
        # 
        # *   APPROVED: The WABA was approved.
        # 
        # *   REJECTED: The WABA was rejected.
        # 
        # *   DISABLED: The WABA was forbidden.
        self.account_review_status = account_review_status
        # WABA related information.
        self.auth_international_rate_eligibility = auth_international_rate_eligibility
        # The business ID.
        self.business_id = business_id
        # The business name.
        self.business_name = business_name
        # The currency.
        self.currency = currency
        # The ID of the WhatsApp Business account.
        self.id = id
        # The Marketing Messaging Lite status.
        self.marketing_message_lite_status = marketing_message_lite_status
        # The namespace of the message template.
        self.message_template_namespace = message_template_namespace
        # The name of the WhatsApp Business account.
        self.name = name
        # The start time when the authentication-international rate applies.
        self.primary_business_location = primary_business_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_review_status is not None:
            result['AccountReviewStatus'] = self.account_review_status
        if self.auth_international_rate_eligibility is not None:
            result['AuthInternationalRateEligibility'] = self.auth_international_rate_eligibility
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.id is not None:
            result['Id'] = self.id
        if self.marketing_message_lite_status is not None:
            result['MarketingMessageLiteStatus'] = self.marketing_message_lite_status
        if self.message_template_namespace is not None:
            result['MessageTemplateNamespace'] = self.message_template_namespace
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_business_location is not None:
            result['PrimaryBusinessLocation'] = self.primary_business_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountReviewStatus') is not None:
            self.account_review_status = m.get('AccountReviewStatus')
        if m.get('AuthInternationalRateEligibility') is not None:
            self.auth_international_rate_eligibility = m.get('AuthInternationalRateEligibility')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MarketingMessageLiteStatus') is not None:
            self.marketing_message_lite_status = m.get('MarketingMessageLiteStatus')
        if m.get('MessageTemplateNamespace') is not None:
            self.message_template_namespace = m.get('MessageTemplateNamespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryBusinessLocation') is not None:
            self.primary_business_location = m.get('PrimaryBusinessLocation')
        return self


class QueryChatappBindWabaResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QueryChatappBindWabaResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryChatappBindWabaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryChatappBindWabaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChatappBindWabaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryChatappBindWabaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatappPhoneNumbersRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        isv_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The independent software vendor (ISV) verification code, which is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The state of the phone number.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryChatappPhoneNumbersResponseBodyPhoneNumbers(TeaModel):
    def __init__(
        self,
        code_verification_status: str = None,
        is_official: str = None,
        messaging_limit_tier: str = None,
        name_status: str = None,
        new_name_status: str = None,
        phone_number: str = None,
        quality_rating: str = None,
        status: str = None,
        status_callback_url: str = None,
        status_queue: str = None,
        up_callback_url: str = None,
        up_queue: str = None,
        verified_name: str = None,
    ):
        # The verification status of the phone number.
        # 
        # Valid values:
        # 
        # *   REVOKED: The review application is revoked.
        # *   MORE_INFORMATION_REQUESTED: More information needs to be provided.
        # *   VERIFIED: The phone number passes the verification.
        # *   REJECTED: The phone number fails to pass the verification.
        self.code_verification_status = code_verification_status
        # Indicates whether it is a WhatsApp Official Business Account (OBA).
        self.is_official = is_official
        # The number of phone numbers to which messages can be sent in a day.
        # 
        # Valid values:
        # 
        # *   TIER_100K: 100,000
        # *   TIER_UNLIMITED: unlimited
        # *   TIER_250: 250
        # *   TIER_1K: 1,000
        # *   TIER_50: 50
        # *   TIER_10K: 10,000
        self.messaging_limit_tier = messaging_limit_tier
        # The review status of the name.
        self.name_status = name_status
        # The review status of the new display name of the enterprise.
        self.new_name_status = new_name_status
        # The phone number.
        self.phone_number = phone_number
        # The quality rating of the phone number.
        # 
        # Valid values:
        # 
        # *   RED: low
        # *   YELLOW: medium
        # *   UNKNOWN: unknown
        # *   GREEN: high
        self.quality_rating = quality_rating
        # The state of the phone number.
        # 
        # Valid values:
        # 
        # *   MIGRATED
        # *   FLAGGED
        # *   DISCONNECTED
        # *   UNVERIFIED
        # *   BANNED
        # *   RATE_LIMITED
        # *   PENDING
        # *   CONNECTED
        # *   UNKNOWN
        # *   DELETED
        # *   RESTRICTED
        self.status = status
        # The URL that receives the status reports.
        self.status_callback_url = status_callback_url
        # The status report queue.
        self.status_queue = status_queue
        # The URL that receives the MO messages.
        self.up_callback_url = up_callback_url
        # The mobile originated (MO) message queue.
        self.up_queue = up_queue
        # The display name of the enterprise to which the phone number belongs.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_verification_status is not None:
            result['CodeVerificationStatus'] = self.code_verification_status
        if self.is_official is not None:
            result['IsOfficial'] = self.is_official
        if self.messaging_limit_tier is not None:
            result['MessagingLimitTier'] = self.messaging_limit_tier
        if self.name_status is not None:
            result['NameStatus'] = self.name_status
        if self.new_name_status is not None:
            result['NewNameStatus'] = self.new_name_status
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.quality_rating is not None:
            result['QualityRating'] = self.quality_rating
        if self.status is not None:
            result['Status'] = self.status
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue
        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVerificationStatus') is not None:
            self.code_verification_status = m.get('CodeVerificationStatus')
        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')
        if m.get('MessagingLimitTier') is not None:
            self.messaging_limit_tier = m.get('MessagingLimitTier')
        if m.get('NameStatus') is not None:
            self.name_status = m.get('NameStatus')
        if m.get('NewNameStatus') is not None:
            self.new_name_status = m.get('NewNameStatus')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualityRating') is not None:
            self.quality_rating = m.get('QualityRating')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')
        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')
        return self


class QueryChatappPhoneNumbersResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        phone_numbers: List[QueryChatappPhoneNumbersResponseBodyPhoneNumbers] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The message returned.
        self.message = message
        # The phone numbers.
        self.phone_numbers = phone_numbers
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.phone_numbers:
            for k in self.phone_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PhoneNumbers'] = []
        if self.phone_numbers is not None:
            for k in self.phone_numbers:
                result['PhoneNumbers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.phone_numbers = []
        if m.get('PhoneNumbers') is not None:
            for k in m.get('PhoneNumbers'):
                temp_model = QueryChatappPhoneNumbersResponseBodyPhoneNumbers()
                self.phone_numbers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryChatappPhoneNumbersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChatappPhoneNumbersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryChatappPhoneNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhoneBusinessProfileRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPhoneBusinessProfileResponseBodyData(TeaModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        description: str = None,
        email: str = None,
        profile_picture_url: str = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        # Regarding.
        self.about = about
        # The address.
        self.address = address
        # The description.
        self.description = description
        # The email address.
        self.email = email
        # The profile picture.
        self.profile_picture_url = profile_picture_url
        # The industry.
        self.vertical = vertical
        # The website.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.about is not None:
            result['About'] = self.about
        if self.address is not None:
            result['Address'] = self.address
        if self.description is not None:
            result['Description'] = self.description
        if self.email is not None:
            result['Email'] = self.email
        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        if self.websites is not None:
            result['Websites'] = self.websites
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        if m.get('Websites') is not None:
            self.websites = m.get('Websites')
        return self


class QueryPhoneBusinessProfileResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QueryPhoneBusinessProfileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryPhoneBusinessProfileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPhoneBusinessProfileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPhoneBusinessProfileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPhoneBusinessProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWabaBusinessInfoRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the WhatsApp Business Account (WABA).
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.waba_id is not None:
            result['WabaId'] = self.waba_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')
        return self


class QueryWabaBusinessInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        business_id: str = None,
        business_name: str = None,
        verification_status: str = None,
        vertical: str = None,
    ):
        # The Business Manager ID.
        self.business_id = business_id
        # The Business Manager name.
        self.business_name = business_name
        # The verification status.
        self.verification_status = verification_status
        # The industry.
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        return self


class QueryWabaBusinessInfoResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QueryWabaBusinessInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The business information about the WABA.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryWabaBusinessInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWabaBusinessInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWabaBusinessInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWabaBusinessInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadChatFlowRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReadChatFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReadChatFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true for success, false for failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadChatFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadChatFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReadChatFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadChatFlowLogSettingRequest(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Process code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReadChatFlowLogSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Returned data.
        self.data = data
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadChatFlowLogSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadChatFlowLogSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReadChatFlowLogSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow version status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ReadFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Flow version status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ReadFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Access denied details; this field is only returned when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReadFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatappMassMessageRequestSenderListFlowAction(TeaModel):
    def __init__(
        self,
        flow_action_data: Dict[str, Any] = None,
        flow_token: str = None,
    ):
        self.flow_action_data = flow_action_data
        self.flow_token = flow_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data
        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')
        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')
        return self


class SendChatappMassMessageRequestSenderListProductActionSectionsProductItems(TeaModel):
    def __init__(
        self,
        product_retailer_id: str = None,
    ):
        self.product_retailer_id = product_retailer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')
        return self


class SendChatappMassMessageRequestSenderListProductActionSections(TeaModel):
    def __init__(
        self,
        product_items: List[SendChatappMassMessageRequestSenderListProductActionSectionsProductItems] = None,
        title: str = None,
    ):
        self.product_items = product_items
        self.title = title

    def validate(self):
        if self.product_items:
            for k in self.product_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItems'] = []
        if self.product_items is not None:
            for k in self.product_items:
                result['ProductItems'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k in m.get('ProductItems'):
                temp_model = SendChatappMassMessageRequestSenderListProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SendChatappMassMessageRequestSenderListProductAction(TeaModel):
    def __init__(
        self,
        sections: List[SendChatappMassMessageRequestSenderListProductActionSections] = None,
        thumbnail_product_retailer_id: str = None,
    ):
        self.sections = sections
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['Sections'].append(k.to_map() if k else None)
        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k in m.get('Sections'):
                temp_model = SendChatappMassMessageRequestSenderListProductActionSections()
                self.sections.append(temp_model.from_map(k))
        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')
        return self


class SendChatappMassMessageRequestSenderList(TeaModel):
    def __init__(
        self,
        flow_action: SendChatappMassMessageRequestSenderListFlowAction = None,
        payload: List[str] = None,
        product_action: SendChatappMassMessageRequestSenderListProductAction = None,
        template_params: Dict[str, str] = None,
        to: str = None,
    ):
        self.flow_action = flow_action
        self.payload = payload
        self.product_action = product_action
        self.template_params = template_params
        self.to = to

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowAction') is not None:
            temp_model = SendChatappMassMessageRequestSenderListFlowAction()
            self.flow_action = temp_model.from_map(m['FlowAction'])
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ProductAction') is not None:
            temp_model = SendChatappMassMessageRequestSenderListProductAction()
            self.product_action = temp_model.from_map(m['ProductAction'])
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendChatappMassMessageRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        fall_back_rule: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sender_list: List[SendChatappMassMessageRequestSenderList] = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        ttl: int = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        self.fall_back_id = fall_back_id
        self.fall_back_rule = fall_back_rule
        # This parameter is required.
        self.from_ = from_
        self.isv_code = isv_code
        self.label = label
        # This parameter is required.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sender_list = sender_list
        self.tag = tag
        self.task_id = task_id
        self.template_code = template_code
        self.template_name = template_name
        self.ttl = ttl

    def validate(self):
        if self.sender_list:
            for k in self.sender_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SenderList'] = []
        if self.sender_list is not None:
            for k in self.sender_list:
                result['SenderList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.sender_list = []
        if m.get('SenderList') is not None:
            for k in m.get('SenderList'):
                temp_model = SendChatappMassMessageRequestSenderList()
                self.sender_list.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        fall_back_rule: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sender_list_shrink: str = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        ttl: int = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        self.fall_back_id = fall_back_id
        self.fall_back_rule = fall_back_rule
        # This parameter is required.
        self.from_ = from_
        self.isv_code = isv_code
        self.label = label
        # This parameter is required.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sender_list_shrink = sender_list_shrink
        self.tag = tag
        self.task_id = task_id
        self.template_code = template_code
        self.template_name = template_name
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sender_list_shrink is not None:
            result['SenderList'] = self.sender_list_shrink
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SenderList') is not None:
            self.sender_list_shrink = m.get('SenderList')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class SendChatappMassMessageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        group_message_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The ID of the message group.
        self.group_message_id = group_message_id
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.group_message_id is not None:
            result['GroupMessageId'] = self.group_message_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupMessageId') is not None:
            self.group_message_id = m.get('GroupMessageId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendChatappMassMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendChatappMassMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendChatappMassMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendChatappMessageRequestFlowAction(TeaModel):
    def __init__(
        self,
        flow_action_data: Dict[str, Any] = None,
        flow_token: str = None,
    ):
        self.flow_action_data = flow_action_data
        self.flow_token = flow_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_action_data is not None:
            result['FlowActionData'] = self.flow_action_data
        if self.flow_token is not None:
            result['FlowToken'] = self.flow_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowActionData') is not None:
            self.flow_action_data = m.get('FlowActionData')
        if m.get('FlowToken') is not None:
            self.flow_token = m.get('FlowToken')
        return self


class SendChatappMessageRequestProductActionSectionsProductItems(TeaModel):
    def __init__(
        self,
        product_retailer_id: str = None,
    ):
        self.product_retailer_id = product_retailer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_retailer_id is not None:
            result['ProductRetailerId'] = self.product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductRetailerId') is not None:
            self.product_retailer_id = m.get('ProductRetailerId')
        return self


class SendChatappMessageRequestProductActionSections(TeaModel):
    def __init__(
        self,
        product_items: List[SendChatappMessageRequestProductActionSectionsProductItems] = None,
        title: str = None,
    ):
        self.product_items = product_items
        self.title = title

    def validate(self):
        if self.product_items:
            for k in self.product_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductItems'] = []
        if self.product_items is not None:
            for k in self.product_items:
                result['ProductItems'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_items = []
        if m.get('ProductItems') is not None:
            for k in m.get('ProductItems'):
                temp_model = SendChatappMessageRequestProductActionSectionsProductItems()
                self.product_items.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SendChatappMessageRequestProductAction(TeaModel):
    def __init__(
        self,
        sections: List[SendChatappMessageRequestProductActionSections] = None,
        thumbnail_product_retailer_id: str = None,
    ):
        self.sections = sections
        self.thumbnail_product_retailer_id = thumbnail_product_retailer_id

    def validate(self):
        if self.sections:
            for k in self.sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sections'] = []
        if self.sections is not None:
            for k in self.sections:
                result['Sections'].append(k.to_map() if k else None)
        if self.thumbnail_product_retailer_id is not None:
            result['ThumbnailProductRetailerId'] = self.thumbnail_product_retailer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sections = []
        if m.get('Sections') is not None:
            for k in m.get('Sections'):
                temp_model = SendChatappMessageRequestProductActionSections()
                self.sections.append(temp_model.from_map(k))
        if m.get('ThumbnailProductRetailerId') is not None:
            self.thumbnail_product_retailer_id = m.get('ThumbnailProductRetailerId')
        return self


class SendChatappMessageRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        content: str = None,
        context_message_id: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        fall_back_rule: str = None,
        flow_action: SendChatappMessageRequestFlowAction = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_type: str = None,
        owner_id: int = None,
        payload: List[str] = None,
        product_action: SendChatappMessageRequestProductAction = None,
        recipient_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        template_params: Dict[str, str] = None,
        to: str = None,
        tracking_data: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        # The message content.
        # 
        # **Notes on WhatsApp messages:**\
        # 
        # *   If you set **messageType** to **text**, you must specify **text** and must not specify **Caption**.
        # *   If you set **messageType** to **image**, you must specify **Link**.
        # *   If you set **messageType** to **video**, you must specify **Link**.
        # *   If you set **messageType** to **audio**, **Link** is required and **Caption** is invalid.
        # *   If you set **messageType** to **document**, **Link** and **FileName** are required and **Caption** is invalid.
        # *   If you set **messageType** to **interactive**, you must specify **type** and **action**.
        # *   If you set **messageType** to **contacts**, you must specify **name**.
        # *   If you set **messageType** to **location**, you must specify **longitude** and **latitude**.
        # *   If you set **messageType** to **sticker**, you must specify **Link**, and **Caption** and **FileName** are invalid.
        # *   If you set **messageType** to **reaction**, you must specify **messageId** and **emoji**.
        # 
        # **Notes on Viber messages:**\
        # 
        # *   If you set **messageType** to **text**, you must specify **text**.
        # *   If you set **messageType** to **image**, you must specify **link**.
        # *   If you set **messageType** to **video**, you must specify **link**, **thumbnail**, **fileSize**, and **duration**.
        # *   If you set **messageType** to **document**, you must specify **link**, **fileName**, and **fileType**.
        # *   If you set **messageType** to **text_button**, you must specify **text**, **caption**, and **action**.
        # *   If you set **messageType** to **text_image_button**, you must specify **text**, **link**, **caption**, and **action**.
        # *   If you set **messageType** to **text_video**, you must specify **text**, **link**, **thumbnail**, **fileSize**, and **duration**.
        # *   If you set **messageType** to **text_video_button**, you must specify **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption**. In addition, you must not specify **action**.
        self.content = content
        self.context_message_id = context_message_id
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        self.fall_back_id = fall_back_id
        self.fall_back_rule = fall_back_rule
        self.flow_action = flow_action
        # This parameter is required.
        self.from_ = from_
        self.isv_code = isv_code
        self.label = label
        self.language = language
        self.message_type = message_type
        self.owner_id = owner_id
        # The payload of the button.
        self.payload = payload
        self.product_action = product_action
        self.recipient_type = recipient_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag = tag
        self.task_id = task_id
        self.template_code = template_code
        self.template_name = template_name
        self.template_params = template_params
        # This parameter is required.
        self.to = to
        self.tracking_data = tracking_data
        self.ttl = ttl
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.flow_action:
            self.flow_action.validate()
        if self.product_action:
            self.product_action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.content is not None:
            result['Content'] = self.content
        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action.to_map()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.product_action is not None:
            result['ProductAction'] = self.product_action.to_map()
        if self.recipient_type is not None:
            result['RecipientType'] = self.recipient_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_params is not None:
            result['TemplateParams'] = self.template_params
        if self.to is not None:
            result['To'] = self.to
        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('FlowAction') is not None:
            temp_model = SendChatappMessageRequestFlowAction()
            self.flow_action = temp_model.from_map(m['FlowAction'])
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ProductAction') is not None:
            temp_model = SendChatappMessageRequestProductAction()
            self.product_action = temp_model.from_map(m['ProductAction'])
        if m.get('RecipientType') is not None:
            self.recipient_type = m.get('RecipientType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        content: str = None,
        context_message_id: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        fall_back_content: str = None,
        fall_back_duration: int = None,
        fall_back_id: str = None,
        fall_back_rule: str = None,
        flow_action_shrink: str = None,
        from_: str = None,
        isv_code: str = None,
        label: str = None,
        language: str = None,
        message_type: str = None,
        owner_id: int = None,
        payload_shrink: str = None,
        product_action_shrink: str = None,
        recipient_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: str = None,
        task_id: str = None,
        template_code: str = None,
        template_name: str = None,
        template_params_shrink: str = None,
        to: str = None,
        tracking_data: str = None,
        ttl: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        # The message content.
        # 
        # **Notes on WhatsApp messages:**\
        # 
        # *   If you set **messageType** to **text**, you must specify **text** and must not specify **Caption**.
        # *   If you set **messageType** to **image**, you must specify **Link**.
        # *   If you set **messageType** to **video**, you must specify **Link**.
        # *   If you set **messageType** to **audio**, **Link** is required and **Caption** is invalid.
        # *   If you set **messageType** to **document**, **Link** and **FileName** are required and **Caption** is invalid.
        # *   If you set **messageType** to **interactive**, you must specify **type** and **action**.
        # *   If you set **messageType** to **contacts**, you must specify **name**.
        # *   If you set **messageType** to **location**, you must specify **longitude** and **latitude**.
        # *   If you set **messageType** to **sticker**, you must specify **Link**, and **Caption** and **FileName** are invalid.
        # *   If you set **messageType** to **reaction**, you must specify **messageId** and **emoji**.
        # 
        # **Notes on Viber messages:**\
        # 
        # *   If you set **messageType** to **text**, you must specify **text**.
        # *   If you set **messageType** to **image**, you must specify **link**.
        # *   If you set **messageType** to **video**, you must specify **link**, **thumbnail**, **fileSize**, and **duration**.
        # *   If you set **messageType** to **document**, you must specify **link**, **fileName**, and **fileType**.
        # *   If you set **messageType** to **text_button**, you must specify **text**, **caption**, and **action**.
        # *   If you set **messageType** to **text_image_button**, you must specify **text**, **link**, **caption**, and **action**.
        # *   If you set **messageType** to **text_video**, you must specify **text**, **link**, **thumbnail**, **fileSize**, and **duration**.
        # *   If you set **messageType** to **text_video_button**, you must specify **text**, **link**, **thumbnail**, **fileSize**, **duration**, and **caption**. In addition, you must not specify **action**.
        self.content = content
        self.context_message_id = context_message_id
        self.cust_space_id = cust_space_id
        self.cust_waba_id = cust_waba_id
        self.fall_back_content = fall_back_content
        self.fall_back_duration = fall_back_duration
        self.fall_back_id = fall_back_id
        self.fall_back_rule = fall_back_rule
        self.flow_action_shrink = flow_action_shrink
        # This parameter is required.
        self.from_ = from_
        self.isv_code = isv_code
        self.label = label
        self.language = language
        self.message_type = message_type
        self.owner_id = owner_id
        # The payload of the button.
        self.payload_shrink = payload_shrink
        self.product_action_shrink = product_action_shrink
        self.recipient_type = recipient_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tag = tag
        self.task_id = task_id
        self.template_code = template_code
        self.template_name = template_name
        self.template_params_shrink = template_params_shrink
        # This parameter is required.
        self.to = to
        self.tracking_data = tracking_data
        self.ttl = ttl
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.content is not None:
            result['Content'] = self.content
        if self.context_message_id is not None:
            result['ContextMessageId'] = self.context_message_id
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id
        if self.fall_back_content is not None:
            result['FallBackContent'] = self.fall_back_content
        if self.fall_back_duration is not None:
            result['FallBackDuration'] = self.fall_back_duration
        if self.fall_back_id is not None:
            result['FallBackId'] = self.fall_back_id
        if self.fall_back_rule is not None:
            result['FallBackRule'] = self.fall_back_rule
        if self.flow_action_shrink is not None:
            result['FlowAction'] = self.flow_action_shrink
        if self.from_ is not None:
            result['From'] = self.from_
        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code
        if self.label is not None:
            result['Label'] = self.label
        if self.language is not None:
            result['Language'] = self.language
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.product_action_shrink is not None:
            result['ProductAction'] = self.product_action_shrink
        if self.recipient_type is not None:
            result['RecipientType'] = self.recipient_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_params_shrink is not None:
            result['TemplateParams'] = self.template_params_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.tracking_data is not None:
            result['TrackingData'] = self.tracking_data
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContextMessageId') is not None:
            self.context_message_id = m.get('ContextMessageId')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')
        if m.get('FallBackContent') is not None:
            self.fall_back_content = m.get('FallBackContent')
        if m.get('FallBackDuration') is not None:
            self.fall_back_duration = m.get('FallBackDuration')
        if m.get('FallBackId') is not None:
            self.fall_back_id = m.get('FallBackId')
        if m.get('FallBackRule') is not None:
            self.fall_back_rule = m.get('FallBackRule')
        if m.get('FlowAction') is not None:
            self.flow_action_shrink = m.get('FlowAction')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('ProductAction') is not None:
            self.product_action_shrink = m.get('ProductAction')
        if m.get('RecipientType') is not None:
            self.recipient_type = m.get('RecipientType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateParams') is not None:
            self.template_params_shrink = m.get('TemplateParams')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('TrackingData') is not None:
            self.tracking_data = m.get('TrackingData')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendChatappMessageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        message_id: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the message that was sent.
        self.message_id = message_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendChatappMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendChatappMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendChatappMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitIsvCustomerTermsRequest(TeaModel):
    def __init__(
        self,
        business_desc: str = None,
        contact_mail: str = None,
        country_id: str = None,
        cust_name: str = None,
        cust_space_id: str = None,
        isv_terms: str = None,
        office_address: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The business scenario.
        # 
        # This parameter is required.
        self.business_desc = business_desc
        # The enterprise mail.
        # 
        # This parameter is required.
        self.contact_mail = contact_mail
        # The country code.
        # 
        # >  For more information about country codes, see [Country codes](https://help.aliyun.com/document_detail/608210.html).
        # 
        # This parameter is required.
        self.country_id = country_id
        # The enterprise name.
        # 
        # This parameter is required.
        self.cust_name = cust_name
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The ISV or Client agreement.
        # 
        # This parameter is required.
        self.isv_terms = isv_terms
        # The enterprise address.
        # 
        # This parameter is required.
        self.office_address = office_address
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_desc is not None:
            result['BusinessDesc'] = self.business_desc
        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.cust_name is not None:
            result['CustName'] = self.cust_name
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.isv_terms is not None:
            result['IsvTerms'] = self.isv_terms
        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessDesc') is not None:
            self.business_desc = m.get('BusinessDesc')
        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('CustName') is not None:
            self.cust_name = m.get('CustName')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('IsvTerms') is not None:
            self.isv_terms = m.get('IsvTerms')
        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SubmitIsvCustomerTermsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitIsvCustomerTermsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitIsvCustomerTermsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitIsvCustomerTermsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerChatFlowRequest(TeaModel):
    def __init__(
        self,
        claim_time_millis: int = None,
        data: Dict[str, Any] = None,
        discard_time_millis: int = None,
        flow_code: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uuid: str = None,
    ):
        # The declared occurrence time of the event, usually the time when the request was constructed, in milliseconds timestamp.
        self.claim_time_millis = claim_time_millis
        # Input parameters in Key-Value format. The Key must match the input strategy configured at the start node of your flow.
        self.data = data
        # The time when the event should be discarded, i.e., the expiration time. If this field is specified, the message will be discarded if it exceeds this time, in milliseconds timestamp.
        self.discard_time_millis = discard_time_millis
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # External system transaction number, used to associate with external business system transactions. You can retrieve this parameter within the flow after triggering.
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Unique event ID used for idempotent triggers. Do not include any business semantics; you can retrieve this parameter within the flow after triggering.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_time_millis is not None:
            result['ClaimTimeMillis'] = self.claim_time_millis
        if self.data is not None:
            result['Data'] = self.data
        if self.discard_time_millis is not None:
            result['DiscardTimeMillis'] = self.discard_time_millis
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimTimeMillis') is not None:
            self.claim_time_millis = m.get('ClaimTimeMillis')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DiscardTimeMillis') is not None:
            self.discard_time_millis = m.get('DiscardTimeMillis')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class TriggerChatFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        claim_time_millis: int = None,
        data_shrink: str = None,
        discard_time_millis: int = None,
        flow_code: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uuid: str = None,
    ):
        # The declared occurrence time of the event, usually the time when the request was constructed, in milliseconds timestamp.
        self.claim_time_millis = claim_time_millis
        # Input parameters in Key-Value format. The Key must match the input strategy configured at the start node of your flow.
        self.data_shrink = data_shrink
        # The time when the event should be discarded, i.e., the expiration time. If this field is specified, the message will be discarded if it exceeds this time, in milliseconds timestamp.
        self.discard_time_millis = discard_time_millis
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # External system transaction number, used to associate with external business system transactions. You can retrieve this parameter within the flow after triggering.
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Unique event ID used for idempotent triggers. Do not include any business semantics; you can retrieve this parameter within the flow after triggering.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_time_millis is not None:
            result['ClaimTimeMillis'] = self.claim_time_millis
        if self.data_shrink is not None:
            result['Data'] = self.data_shrink
        if self.discard_time_millis is not None:
            result['DiscardTimeMillis'] = self.discard_time_millis
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimTimeMillis') is not None:
            self.claim_time_millis = m.get('ClaimTimeMillis')
        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')
        if m.get('DiscardTimeMillis') is not None:
            self.discard_time_millis = m.get('DiscardTimeMillis')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class TriggerChatFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of access denial
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Returned data.
        self.data = data
        # Error description message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Whether the call was successful.
        # - **true**: Call succeeded.
        # - **false**: Call failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerChatFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerChatFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TriggerChatFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccountWebhookRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        http_flag: str = None,
        owner_id: int = None,
        queue_flag: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status_callback_url: str = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # Specifies whether to use HTTP callbacks to receive message receipts. Valid values:
        # 
        # *   Y: indicates that HTTP callbacks are used to receive receipts.
        # *   N: indicates that HTTP callbacks are not used to receive receipts.
        self.http_flag = http_flag
        self.owner_id = owner_id
        # Specifies whether to use Message Service (MNS) queues to receive receipts. Valid values:
        # 
        # *   Y: indicates that MNS queues are used to receive receipts.
        # *   N: indicates that MNS queues are not used to receive receipts.
        self.queue_flag = queue_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        return self


class UpdateAccountWebhookResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccountWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccountWebhookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAccountWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChatFlowRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Process code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        # Process remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Process title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateChatFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        title: str = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Process code.
        self.flow_code = flow_code
        self.owner_id = owner_id
        # Process remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Process title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateChatFlowResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Details of access denial; this field is only returned when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateChatFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateChatFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateChatFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChatFlowLogSettingRequest(TeaModel):
    def __init__(
        self,
        flow_code: str = None,
        id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # Flow code.
        self.flow_code = flow_code
        # Setting ID.
        self.id = id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Log enable status, enum values:
        # - ENABLED: Enabled, enables log writing
        # - DISABLED: Create or retain related resources, but do not enable log writing
        # - DELETED: Delete, and decide whether to delete related resources based on options
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateChatFlowLogSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Access denied details, this field is returned only when RAM verification fails.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Returned data object.
        self.data = data
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Whether the operation was successful. Values: true: success; false: failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateChatFlowLogSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateChatFlowLogSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateChatFlowLogSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChatGroupRequest(TeaModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        description: str = None,
        group_id: str = None,
        owner_id: int = None,
        profile_picture_file: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.description = description
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.profile_picture_file = profile_picture_file
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.profile_picture_file is not None:
            result['ProfilePictureFile'] = self.profile_picture_file
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProfilePictureFile') is not None:
            self.profile_picture_file = m.get('ProfilePictureFile')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class UpdateChatGroupResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateChatGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateChatGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateChatGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCommerceSettingRequest(TeaModel):
    def __init__(
        self,
        cart_enable: bool = None,
        catalog_visible: bool = None,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to display the shopping cart button. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.cart_enable = cart_enable
        # Specifies whether to display the catalog button. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.catalog_visible = catalog_visible
        # The space ID of the user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cart_enable is not None:
            result['CartEnable'] = self.cart_enable
        if self.catalog_visible is not None:
            result['CatalogVisible'] = self.catalog_visible
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CartEnable') is not None:
            self.cart_enable = m.get('CartEnable')
        if m.get('CatalogVisible') is not None:
            self.catalog_visible = m.get('CatalogVisible')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateCommerceSettingResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCommerceSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCommerceSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCommerceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConversationalAutomationRequestCommands(TeaModel):
    def __init__(
        self,
        command_description: str = None,
        command_name: str = None,
    ):
        # The description of the command.
        self.command_description = command_description
        # The command name.
        self.command_name = command_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        return self


class UpdateConversationalAutomationRequest(TeaModel):
    def __init__(
        self,
        commands: List[UpdateConversationalAutomationRequestCommands] = None,
        cust_space_id: str = None,
        enable_welcome_message: bool = None,
        owner_id: int = None,
        phone_number: str = None,
        prompts: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The commands.
        self.commands = commands
        # The space ID of the RAM user within the independent software vendor (ISV) account or the instance ID of the customer of Alibaba Cloud.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # Specifies whether to enable the welcoming message.
        self.enable_welcome_message = enable_welcome_message
        self.owner_id = owner_id
        # The phone number of the enterprise.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The opening remarks.
        self.prompts = prompts
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prompts is not None:
            result['Prompts'] = self.prompts
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = UpdateConversationalAutomationRequestCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Prompts') is not None:
            self.prompts = m.get('Prompts')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateConversationalAutomationShrinkRequest(TeaModel):
    def __init__(
        self,
        commands_shrink: str = None,
        cust_space_id: str = None,
        enable_welcome_message: bool = None,
        owner_id: int = None,
        phone_number: str = None,
        prompts_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The commands.
        self.commands_shrink = commands_shrink
        # The space ID of the RAM user within the independent software vendor (ISV) account or the instance ID of the customer of Alibaba Cloud.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # Specifies whether to enable the welcoming message.
        self.enable_welcome_message = enable_welcome_message
        self.owner_id = owner_id
        # The phone number of the enterprise.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The opening remarks.
        self.prompts_shrink = prompts_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands_shrink is not None:
            result['Commands'] = self.commands_shrink
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.enable_welcome_message is not None:
            result['EnableWelcomeMessage'] = self.enable_welcome_message
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prompts_shrink is not None:
            result['Prompts'] = self.prompts_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands_shrink = m.get('Commands')
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EnableWelcomeMessage') is not None:
            self.enable_welcome_message = m.get('EnableWelcomeMessage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Prompts') is not None:
            self.prompts_shrink = m.get('Prompts')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateConversationalAutomationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConversationalAutomationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConversationalAutomationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConversationalAutomationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowJSONAssetRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        file_path: str = None,
        flow_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.file_path = file_path
        # This parameter is required.
        self.flow_id = flow_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateFlowJSONAssetResponseBodyData(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        # The Flow ID.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class UpdateFlowJSONAssetResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: UpdateFlowJSONAssetResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The result returns OK as normal.
        self.code = code
        # The returned data.
        self.data = data
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateFlowJSONAssetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFlowJSONAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFlowJSONAssetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFlowJSONAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowVersionRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend: Dict[str, Any] = None,
        flow_code: str = None,
        flow_version: str = None,
        flow_view_model: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend = biz_extend
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        # DSL data of the flow version
        self.flow_view_model = flow_view_model
        self.owner_id = owner_id
        # Version remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend is not None:
            result['BizExtend'] = self.biz_extend
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.flow_view_model is not None:
            result['FlowViewModel'] = self.flow_view_model
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('FlowViewModel') is not None:
            self.flow_view_model = m.get('FlowViewModel')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateFlowVersionShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        biz_extend_shrink: str = None,
        flow_code: str = None,
        flow_version: str = None,
        flow_view_model: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Business tenant code, default is “ALICOM_OPAAS”.
        self.biz_code = biz_code
        # Business extension information, default is “{}”.
        self.biz_extend_shrink = biz_extend_shrink
        # Flow code.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        # DSL data of the flow version
        self.flow_view_model = flow_view_model
        self.owner_id = owner_id
        # Version remarks
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_extend_shrink is not None:
            result['BizExtend'] = self.biz_extend_shrink
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.flow_view_model is not None:
            result['FlowViewModel'] = self.flow_view_model
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizExtend') is not None:
            self.biz_extend_shrink = m.get('BizExtend')
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('FlowViewModel') is not None:
            self.flow_view_model = m.get('FlowViewModel')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Details of access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true for success, false for failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFlowVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneEncryptionPublicKeyRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        encryption_public_key: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.encryption_public_key = encryption_public_key
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdatePhoneEncryptionPublicKeyResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The result returns OK as normal.
        self.code = code
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneEncryptionPublicKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePhoneEncryptionPublicKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePhoneEncryptionPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneMessageQrdlRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        generate_qr_image: str = None,
        owner_id: int = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qrdl_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.generate_qr_image = generate_qr_image
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.prefilled_message = prefilled_message
        # This parameter is required.
        self.qrdl_code = qrdl_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdatePhoneMessageQrdlResponseBodyData(TeaModel):
    def __init__(
        self,
        deep_link_url: str = None,
        generate_qr_image: str = None,
        phone_number: str = None,
        prefilled_message: str = None,
        qr_image_url: str = None,
        qrdl_code: str = None,
    ):
        # Deep link address.
        self.deep_link_url = deep_link_url
        # Generate image types.
        self.generate_qr_image = generate_qr_image
        # Number.
        self.phone_number = phone_number
        # Message content.
        self.prefilled_message = prefilled_message
        # QR code address.
        self.qr_image_url = qr_image_url
        # QR code encoding.
        self.qrdl_code = qrdl_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deep_link_url is not None:
            result['DeepLinkUrl'] = self.deep_link_url
        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message
        if self.qr_image_url is not None:
            result['QrImageUrl'] = self.qr_image_url
        if self.qrdl_code is not None:
            result['QrdlCode'] = self.qrdl_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeepLinkUrl') is not None:
            self.deep_link_url = m.get('DeepLinkUrl')
        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')
        if m.get('QrImageUrl') is not None:
            self.qr_image_url = m.get('QrImageUrl')
        if m.get('QrdlCode') is not None:
            self.qrdl_code = m.get('QrdlCode')
        return self


class UpdatePhoneMessageQrdlResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: UpdatePhoneMessageQrdlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The result returns OK as normal.
        self.code = code
        # The returned data.
        self.data = data
        # Error description information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdatePhoneMessageQrdlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneMessageQrdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePhoneMessageQrdlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePhoneMessageQrdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneWebhookRequest(TeaModel):
    def __init__(
        self,
        cust_space_id: str = None,
        http_flag: str = None,
        owner_id: int = None,
        phone_number: str = None,
        queue_flag: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status_callback_url: str = None,
        up_callback_url: str = None,
    ):
        # SpaceId for ISV sub clients.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # Whether to use HTTP to receive receipts. Value:
        # *   Y: Yes.
        # *   N: No.
        self.http_flag = http_flag
        self.owner_id = owner_id
        # phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # Whether to use queue method to receive receipts. Value:
        # *   Y: Yes.
        # *   N: No.
        self.queue_flag = queue_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # HTTP status report interface callback address.
        self.status_callback_url = status_callback_url
        # HTTP upstream message interface callback address.
        self.up_callback_url = up_callback_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id
        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url
        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')
        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')
        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')
        return self


class UpdatePhoneWebhookResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Access denied for detailed information.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # Prompt message, there is a value when an exception is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhoneWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePhoneWebhookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePhoneWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


