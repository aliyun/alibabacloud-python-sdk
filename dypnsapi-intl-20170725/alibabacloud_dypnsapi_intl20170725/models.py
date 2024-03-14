# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class CheckVerificationRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        service_sid: str = None,
        to: str = None,
        verification_id: str = None,
    ):
        # The verification code.
        self.code = code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service ID that is displayed in the Phone Number Verification Service console.
        self.service_sid = service_sid
        # The mobile phone number of the recipient. You must add the country code to the beginning of the mobile phone number. Example: 6212345\*\*\*\*01.
        self.to = to
        # The unique authentication ID that is returned by calling the StartVerification operation.
        self.verification_id = verification_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_sid is not None:
            result['ServiceSid'] = self.service_sid
        if self.to is not None:
            result['To'] = self.to
        if self.verification_id is not None:
            result['VerificationId'] = self.verification_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceSid') is not None:
            self.service_sid = m.get('ServiceSid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('VerificationId') is not None:
            self.verification_id = m.get('VerificationId')
        return self


class CheckVerificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code that was returned.
        self.code = code
        # The message that was returned.
        self.message = message
        # The data that was returned for the successful request. Example: "Model": { "phoneNumber": "", "channel": "", "verificationId": "", "status": "approved" },
        self.model = model
        # The ID of the request. An ID is a unique identifier that Alibaba Cloud generates for a request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success

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
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class CheckVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchVerificationRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_date: int = None,
        service_sid: str = None,
        to: str = None,
        verification_id: str = None,
    ):
        # The verification code.
        self.code = code
        # The number of the page to return. Pages start from page 1.
        self.current_page = current_page
        self.owner_id = owner_id
        # The number of entries to return on each page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time when a text message is sent, in milliseconds. You can query text messages that were sent within the last 30 days.
        # 
        # Example: 1677600000000.
        self.send_date = send_date
        # The service ID that is displayed in the Phone Number Verification Service console.
        self.service_sid = service_sid
        # The mobile phone number of the recipient. You must add the country code to the beginning of the mobile phone number. Example: 6212345\*\*\*\*01.
        self.to = to
        # The unique authentication ID that is returned by calling the StartVerification operation.
        self.verification_id = verification_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.service_sid is not None:
            result['ServiceSid'] = self.service_sid
        if self.to is not None:
            result['To'] = self.to
        if self.verification_id is not None:
            result['VerificationId'] = self.verification_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('ServiceSid') is not None:
            self.service_sid = m.get('ServiceSid')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('VerificationId') is not None:
            self.verification_id = m.get('VerificationId')
        return self


class SearchVerificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that was returned for the request.
        self.code = code
        # The message that was returned.
        self.message = message
        # The data that was returned for the request. Example: "Model": { "records": \[ { "sendDate":, "channel": "", "serviceSid": "", "to": "", "updatedDate":, "verificationId": "", "status": "" } ], "pageNo": , "totalPage": 1, "pageSize": 20, "totalCount": 1, }
        self.model = model
        # The ID of the request. An ID is a unique identifier that Alibaba Cloud generates for a request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success

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
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class SearchVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVerificationRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        service_sid: str = None,
        to: str = None,
    ):
        # The channels that you can use for verification.
        # 
        # Valid values:
        # 
        # *   Voice
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   SMS
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   WhatsApp
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.channel = channel
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service ID that is displayed in the Phone Number Verification Service console.
        self.service_sid = service_sid
        # The mobile phone number of the recipient. You must add the country code to the beginning of the mobile phone number. Example: 6212345\*\*\*\*01.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_sid is not None:
            result['ServiceSid'] = self.service_sid
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceSid') is not None:
            self.service_sid = m.get('ServiceSid')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class StartVerificationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: Dict[str, Any] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that was returned for the request.
        self.code = code
        # The message that was returned.
        self.message = message
        # The data that was returned only if the request was successful. Example: "Model": { "verifyCode": "", "verificationId": "", "status": "" }
        self.model = model
        # The ID of the request. An ID is a unique identifier that Alibaba Cloud generates for a request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true: The request was successful. false: The request failed.
        self.success = success

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
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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


class StartVerificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartVerificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


