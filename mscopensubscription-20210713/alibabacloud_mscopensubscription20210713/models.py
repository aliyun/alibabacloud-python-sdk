# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateContactRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        contact_name: str = None,
        email: str = None,
        locale: str = None,
        mobile: str = None,
        position: str = None,
    ):
        self.client_token = client_token
        self.contact_name = contact_name
        self.email = email
        self.locale = locale
        self.mobile = mobile
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class CreateContactResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        contact_id: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.contact_id = contact_id
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
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateContactResponseBody = None,
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
            temp_model = CreateContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscriptionItemRequest(TeaModel):
    def __init__(
        self,
        item_name: str = None,
        locale: str = None,
    ):
        self.item_name = item_name
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.locale is not None:
            result['Locale'] = self.locale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        return self


class CreateSubscriptionItemResponseBodySubscriptionItem(TeaModel):
    def __init__(
        self,
        channel: str = None,
        contact_ids: List[int] = None,
        description: str = None,
        email_status: int = None,
        item_id: int = None,
        item_name: str = None,
        pmsg_status: int = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_ids: List[int] = None,
        webhook_status: int = None,
    ):
        self.channel = channel
        self.contact_ids = contact_ids
        self.description = description
        self.email_status = email_status
        self.item_id = item_id
        self.item_name = item_name
        self.pmsg_status = pmsg_status
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_ids = webhook_ids
        self.webhook_status = webhook_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_ids is not None:
            result['WebhookIds'] = self.webhook_ids
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookIds') is not None:
            self.webhook_ids = m.get('WebhookIds')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        return self


class CreateSubscriptionItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        subscription_item: CreateSubscriptionItemResponseBodySubscriptionItem = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.subscription_item = subscription_item
        self.success = success

    def validate(self):
        if self.subscription_item:
            self.subscription_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_item is not None:
            result['SubscriptionItem'] = self.subscription_item.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionItem') is not None:
            temp_model = CreateSubscriptionItemResponseBodySubscriptionItem()
            self.subscription_item = temp_model.from_map(m['SubscriptionItem'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSubscriptionItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubscriptionItemResponseBody = None,
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
            temp_model = CreateSubscriptionItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebhookRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        locale: str = None,
        server_url: str = None,
        webhook_name: str = None,
    ):
        self.client_token = client_token
        self.locale = locale
        self.server_url = server_url
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class CreateWebhookResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        webhook_id: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.webhook_id = webhook_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class CreateWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWebhookResponseBody = None,
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
            temp_model = CreateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        locale: str = None,
    ):
        self.contact_id = contact_id
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.locale is not None:
            result['Locale'] = self.locale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        return self


class DeleteContactResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
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


class DeleteContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteContactResponseBody = None,
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
            temp_model = DeleteContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebhookRequest(TeaModel):
    def __init__(
        self,
        locale: str = None,
        webhook_id: int = None,
    ):
        self.locale = locale
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class DeleteWebhookResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
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


class DeleteWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWebhookResponseBody = None,
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
            temp_model = DeleteWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        locale: str = None,
    ):
        self.contact_id = contact_id
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.locale is not None:
            result['Locale'] = self.locale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        return self


class GetContactResponseBodyContact(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        contact_id: int = None,
        contact_name: str = None,
        email: str = None,
        is_account: bool = None,
        is_obsolete: bool = None,
        is_verified_email: bool = None,
        is_verified_mobile: bool = None,
        last_email_verification_time_stamp: int = None,
        last_mobile_verification_time_stamp: int = None,
        mobile: str = None,
        position: str = None,
    ):
        self.account_uid = account_uid
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.email = email
        self.is_account = is_account
        self.is_obsolete = is_obsolete
        self.is_verified_email = is_verified_email
        self.is_verified_mobile = is_verified_mobile
        self.last_email_verification_time_stamp = last_email_verification_time_stamp
        self.last_mobile_verification_time_stamp = last_mobile_verification_time_stamp
        self.mobile = mobile
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.is_account is not None:
            result['IsAccount'] = self.is_account
        if self.is_obsolete is not None:
            result['IsObsolete'] = self.is_obsolete
        if self.is_verified_email is not None:
            result['IsVerifiedEmail'] = self.is_verified_email
        if self.is_verified_mobile is not None:
            result['IsVerifiedMobile'] = self.is_verified_mobile
        if self.last_email_verification_time_stamp is not None:
            result['LastEmailVerificationTimeStamp'] = self.last_email_verification_time_stamp
        if self.last_mobile_verification_time_stamp is not None:
            result['LastMobileVerificationTimeStamp'] = self.last_mobile_verification_time_stamp
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsAccount') is not None:
            self.is_account = m.get('IsAccount')
        if m.get('IsObsolete') is not None:
            self.is_obsolete = m.get('IsObsolete')
        if m.get('IsVerifiedEmail') is not None:
            self.is_verified_email = m.get('IsVerifiedEmail')
        if m.get('IsVerifiedMobile') is not None:
            self.is_verified_mobile = m.get('IsVerifiedMobile')
        if m.get('LastEmailVerificationTimeStamp') is not None:
            self.last_email_verification_time_stamp = m.get('LastEmailVerificationTimeStamp')
        if m.get('LastMobileVerificationTimeStamp') is not None:
            self.last_mobile_verification_time_stamp = m.get('LastMobileVerificationTimeStamp')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetContactResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        contact: GetContactResponseBodyContact = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.contact = contact
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Contact') is not None:
            temp_model = GetContactResponseBodyContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetContactResponseBody = None,
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
            temp_model = GetContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionItemRequest(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        locale: str = None,
    ):
        self.item_id = item_id
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.locale is not None:
            result['Locale'] = self.locale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        return self


class GetSubscriptionItemResponseBodySubscriptionItem(TeaModel):
    def __init__(
        self,
        channel: str = None,
        contact_ids: List[int] = None,
        description: str = None,
        email_status: int = None,
        item_id: int = None,
        item_name: str = None,
        pmsg_status: int = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_ids: List[int] = None,
        webhook_status: int = None,
    ):
        self.channel = channel
        self.contact_ids = contact_ids
        self.description = description
        self.email_status = email_status
        self.item_id = item_id
        self.item_name = item_name
        self.pmsg_status = pmsg_status
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_ids = webhook_ids
        self.webhook_status = webhook_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_ids is not None:
            result['WebhookIds'] = self.webhook_ids
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookIds') is not None:
            self.webhook_ids = m.get('WebhookIds')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        return self


class GetSubscriptionItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        subscription_item: GetSubscriptionItemResponseBodySubscriptionItem = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.subscription_item = subscription_item
        self.success = success

    def validate(self):
        if self.subscription_item:
            self.subscription_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_item is not None:
            result['SubscriptionItem'] = self.subscription_item.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionItem') is not None:
            temp_model = GetSubscriptionItemResponseBodySubscriptionItem()
            self.subscription_item = temp_model.from_map(m['SubscriptionItem'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubscriptionItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubscriptionItemResponseBody = None,
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
            temp_model = GetSubscriptionItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionItemDetailRequest(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        locale: str = None,
    ):
        self.item_id = item_id
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.locale is not None:
            result['Locale'] = self.locale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        return self


class GetSubscriptionItemDetailResponseBodySubscriptionItemDetailContacts(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        contact_id: int = None,
        email: str = None,
        is_account: bool = None,
        is_obsolete: bool = None,
        is_verified_email: bool = None,
        is_verified_mobile: bool = None,
        last_email_verification_time_stamp: int = None,
        last_mobile_verification_time_stamp: int = None,
        mobile: str = None,
        name: str = None,
        position: str = None,
    ):
        self.account_uid = account_uid
        self.contact_id = contact_id
        self.email = email
        self.is_account = is_account
        self.is_obsolete = is_obsolete
        self.is_verified_email = is_verified_email
        self.is_verified_mobile = is_verified_mobile
        self.last_email_verification_time_stamp = last_email_verification_time_stamp
        self.last_mobile_verification_time_stamp = last_mobile_verification_time_stamp
        self.mobile = mobile
        self.name = name
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUID'] = self.account_uid
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.email is not None:
            result['Email'] = self.email
        if self.is_account is not None:
            result['IsAccount'] = self.is_account
        if self.is_obsolete is not None:
            result['IsObsolete'] = self.is_obsolete
        if self.is_verified_email is not None:
            result['IsVerifiedEmail'] = self.is_verified_email
        if self.is_verified_mobile is not None:
            result['IsVerifiedMobile'] = self.is_verified_mobile
        if self.last_email_verification_time_stamp is not None:
            result['LastEmailVerificationTimeStamp'] = self.last_email_verification_time_stamp
        if self.last_mobile_verification_time_stamp is not None:
            result['LastMobileVerificationTimeStamp'] = self.last_mobile_verification_time_stamp
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUID') is not None:
            self.account_uid = m.get('AccountUID')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsAccount') is not None:
            self.is_account = m.get('IsAccount')
        if m.get('IsObsolete') is not None:
            self.is_obsolete = m.get('IsObsolete')
        if m.get('IsVerifiedEmail') is not None:
            self.is_verified_email = m.get('IsVerifiedEmail')
        if m.get('IsVerifiedMobile') is not None:
            self.is_verified_mobile = m.get('IsVerifiedMobile')
        if m.get('LastEmailVerificationTimeStamp') is not None:
            self.last_email_verification_time_stamp = m.get('LastEmailVerificationTimeStamp')
        if m.get('LastMobileVerificationTimeStamp') is not None:
            self.last_mobile_verification_time_stamp = m.get('LastMobileVerificationTimeStamp')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetSubscriptionItemDetailResponseBodySubscriptionItemDetailWebhooks(TeaModel):
    def __init__(
        self,
        name: str = None,
        server_url: str = None,
        webhook_id: int = None,
    ):
        self.name = name
        self.server_url = server_url
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class GetSubscriptionItemDetailResponseBodySubscriptionItemDetail(TeaModel):
    def __init__(
        self,
        channel: str = None,
        contacts: List[GetSubscriptionItemDetailResponseBodySubscriptionItemDetailContacts] = None,
        description: str = None,
        email_status: int = None,
        item_id: int = None,
        item_name: str = None,
        pmsg_status: int = None,
        region_id: str = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_status: int = None,
        webhooks: List[GetSubscriptionItemDetailResponseBodySubscriptionItemDetailWebhooks] = None,
    ):
        self.channel = channel
        self.contacts = contacts
        self.description = description
        self.email_status = email_status
        self.item_id = item_id
        self.item_name = item_name
        self.pmsg_status = pmsg_status
        self.region_id = region_id
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_status = webhook_status
        self.webhooks = webhooks

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.webhooks:
            for k in self.webhooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        result['Webhooks'] = []
        if self.webhooks is not None:
            for k in self.webhooks:
                result['Webhooks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = GetSubscriptionItemDetailResponseBodySubscriptionItemDetailContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        self.webhooks = []
        if m.get('Webhooks') is not None:
            for k in m.get('Webhooks'):
                temp_model = GetSubscriptionItemDetailResponseBodySubscriptionItemDetailWebhooks()
                self.webhooks.append(temp_model.from_map(k))
        return self


class GetSubscriptionItemDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        subscription_item_detail: GetSubscriptionItemDetailResponseBodySubscriptionItemDetail = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.subscription_item_detail = subscription_item_detail
        self.success = success

    def validate(self):
        if self.subscription_item_detail:
            self.subscription_item_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_item_detail is not None:
            result['SubscriptionItemDetail'] = self.subscription_item_detail.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionItemDetail') is not None:
            temp_model = GetSubscriptionItemDetailResponseBodySubscriptionItemDetail()
            self.subscription_item_detail = temp_model.from_map(m['SubscriptionItemDetail'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubscriptionItemDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubscriptionItemDetailResponseBody = None,
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
            temp_model = GetSubscriptionItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebhookRequest(TeaModel):
    def __init__(
        self,
        locale: str = None,
        webhook_id: int = None,
    ):
        self.locale = locale
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class GetWebhookResponseBodyWebhook(TeaModel):
    def __init__(
        self,
        server_url: str = None,
        webhook_id: int = None,
        webhook_name: str = None,
    ):
        self.server_url = server_url
        self.webhook_id = webhook_id
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class GetWebhookResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        webhook: GetWebhookResponseBodyWebhook = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.webhook = webhook

    def validate(self):
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.webhook is not None:
            result['Webhook'] = self.webhook.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Webhook') is not None:
            temp_model = GetWebhookResponseBodyWebhook()
            self.webhook = temp_model.from_map(m['Webhook'])
        return self


class GetWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebhookResponseBody = None,
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
            temp_model = GetWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContactsRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        filter: str = None,
        locale: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.contact_id = contact_id
        self.filter = filter
        self.locale = locale
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListContactsResponseBodyContacts(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        contact_id: int = None,
        contact_name: str = None,
        email: str = None,
        is_account: bool = None,
        is_obsolete: bool = None,
        is_verified_email: bool = None,
        is_verified_mobile: bool = None,
        last_email_verification_time_stamp: int = None,
        last_mobile_verification_time_stamp: int = None,
        mobile: str = None,
        position: str = None,
    ):
        self.account_uid = account_uid
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.email = email
        self.is_account = is_account
        self.is_obsolete = is_obsolete
        self.is_verified_email = is_verified_email
        self.is_verified_mobile = is_verified_mobile
        self.last_email_verification_time_stamp = last_email_verification_time_stamp
        self.last_mobile_verification_time_stamp = last_mobile_verification_time_stamp
        self.mobile = mobile
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.is_account is not None:
            result['IsAccount'] = self.is_account
        if self.is_obsolete is not None:
            result['IsObsolete'] = self.is_obsolete
        if self.is_verified_email is not None:
            result['IsVerifiedEmail'] = self.is_verified_email
        if self.is_verified_mobile is not None:
            result['IsVerifiedMobile'] = self.is_verified_mobile
        if self.last_email_verification_time_stamp is not None:
            result['LastEmailVerificationTimeStamp'] = self.last_email_verification_time_stamp
        if self.last_mobile_verification_time_stamp is not None:
            result['LastMobileVerificationTimeStamp'] = self.last_mobile_verification_time_stamp
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsAccount') is not None:
            self.is_account = m.get('IsAccount')
        if m.get('IsObsolete') is not None:
            self.is_obsolete = m.get('IsObsolete')
        if m.get('IsVerifiedEmail') is not None:
            self.is_verified_email = m.get('IsVerifiedEmail')
        if m.get('IsVerifiedMobile') is not None:
            self.is_verified_mobile = m.get('IsVerifiedMobile')
        if m.get('LastEmailVerificationTimeStamp') is not None:
            self.last_email_verification_time_stamp = m.get('LastEmailVerificationTimeStamp')
        if m.get('LastMobileVerificationTimeStamp') is not None:
            self.last_mobile_verification_time_stamp = m.get('LastMobileVerificationTimeStamp')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class ListContactsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        contacts: List[ListContactsResponseBodyContacts] = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.contacts = contacts
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
        if self.code is not None:
            result['Code'] = self.code
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = ListContactsResponseBodyContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListContactsResponseBody = None,
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
            temp_model = ListContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionItemGroupDetailsRequest(TeaModel):
    def __init__(
        self,
        locale: str = None,
    ):
        self.locale = locale

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        return self


class ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetailsContacts(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        contact_id: int = None,
        email: str = None,
        is_account: bool = None,
        is_obsolete: bool = None,
        is_verified_email: bool = None,
        is_verified_mobile: bool = None,
        last_email_verification_time_stamp: int = None,
        last_mobile_verification_time_stamp: int = None,
        mobile: str = None,
        name: str = None,
        position: str = None,
    ):
        self.account_uid = account_uid
        self.contact_id = contact_id
        self.email = email
        self.is_account = is_account
        self.is_obsolete = is_obsolete
        self.is_verified_email = is_verified_email
        self.is_verified_mobile = is_verified_mobile
        self.last_email_verification_time_stamp = last_email_verification_time_stamp
        self.last_mobile_verification_time_stamp = last_mobile_verification_time_stamp
        self.mobile = mobile
        self.name = name
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUID'] = self.account_uid
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.email is not None:
            result['Email'] = self.email
        if self.is_account is not None:
            result['IsAccount'] = self.is_account
        if self.is_obsolete is not None:
            result['IsObsolete'] = self.is_obsolete
        if self.is_verified_email is not None:
            result['IsVerifiedEmail'] = self.is_verified_email
        if self.is_verified_mobile is not None:
            result['IsVerifiedMobile'] = self.is_verified_mobile
        if self.last_email_verification_time_stamp is not None:
            result['LastEmailVerificationTimeStamp'] = self.last_email_verification_time_stamp
        if self.last_mobile_verification_time_stamp is not None:
            result['LastMobileVerificationTimeStamp'] = self.last_mobile_verification_time_stamp
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUID') is not None:
            self.account_uid = m.get('AccountUID')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsAccount') is not None:
            self.is_account = m.get('IsAccount')
        if m.get('IsObsolete') is not None:
            self.is_obsolete = m.get('IsObsolete')
        if m.get('IsVerifiedEmail') is not None:
            self.is_verified_email = m.get('IsVerifiedEmail')
        if m.get('IsVerifiedMobile') is not None:
            self.is_verified_mobile = m.get('IsVerifiedMobile')
        if m.get('LastEmailVerificationTimeStamp') is not None:
            self.last_email_verification_time_stamp = m.get('LastEmailVerificationTimeStamp')
        if m.get('LastMobileVerificationTimeStamp') is not None:
            self.last_mobile_verification_time_stamp = m.get('LastMobileVerificationTimeStamp')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetailsWebhooks(TeaModel):
    def __init__(
        self,
        name: str = None,
        server_url: str = None,
        webhook_id: int = None,
    ):
        self.name = name
        self.server_url = server_url
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetails(TeaModel):
    def __init__(
        self,
        channel: str = None,
        contacts: List[ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetailsContacts] = None,
        description: str = None,
        email_status: int = None,
        item_id: int = None,
        item_name: str = None,
        pmsg_status: int = None,
        region_id: str = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_status: int = None,
        webhooks: List[ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetailsWebhooks] = None,
    ):
        self.channel = channel
        self.contacts = contacts
        self.description = description
        self.email_status = email_status
        self.item_id = item_id
        self.item_name = item_name
        self.pmsg_status = pmsg_status
        self.region_id = region_id
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_status = webhook_status
        self.webhooks = webhooks

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.webhooks:
            for k in self.webhooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        result['Webhooks'] = []
        if self.webhooks is not None:
            for k in self.webhooks:
                result['Webhooks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetailsContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        self.webhooks = []
        if m.get('Webhooks') is not None:
            for k in m.get('Webhooks'):
                temp_model = ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetailsWebhooks()
                self.webhooks.append(temp_model.from_map(k))
        return self


class ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetails(TeaModel):
    def __init__(
        self,
        description: str = None,
        item_details: List[ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetails] = None,
        item_group_id: int = None,
        item_group_name: str = None,
    ):
        self.description = description
        self.item_details = item_details
        self.item_group_id = item_group_id
        self.item_group_name = item_group_name

    def validate(self):
        if self.item_details:
            for k in self.item_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['ItemDetails'] = []
        if self.item_details is not None:
            for k in self.item_details:
                result['ItemDetails'].append(k.to_map() if k else None)
        if self.item_group_id is not None:
            result['ItemGroupId'] = self.item_group_id
        if self.item_group_name is not None:
            result['ItemGroupName'] = self.item_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.item_details = []
        if m.get('ItemDetails') is not None:
            for k in m.get('ItemDetails'):
                temp_model = ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetailsItemDetails()
                self.item_details.append(temp_model.from_map(k))
        if m.get('ItemGroupId') is not None:
            self.item_group_id = m.get('ItemGroupId')
        if m.get('ItemGroupName') is not None:
            self.item_group_name = m.get('ItemGroupName')
        return self


class ListSubscriptionItemGroupDetailsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        subscription_item_group_details: List[ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetails] = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.subscription_item_group_details = subscription_item_group_details
        self.success = success

    def validate(self):
        if self.subscription_item_group_details:
            for k in self.subscription_item_group_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubscriptionItemGroupDetails'] = []
        if self.subscription_item_group_details is not None:
            for k in self.subscription_item_group_details:
                result['SubscriptionItemGroupDetails'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subscription_item_group_details = []
        if m.get('SubscriptionItemGroupDetails') is not None:
            for k in m.get('SubscriptionItemGroupDetails'):
                temp_model = ListSubscriptionItemGroupDetailsResponseBodySubscriptionItemGroupDetails()
                self.subscription_item_group_details.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSubscriptionItemGroupDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubscriptionItemGroupDetailsResponseBody = None,
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
            temp_model = ListSubscriptionItemGroupDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionItemsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        item_id: int = None,
        locale: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.filter = filter
        self.item_id = item_id
        self.locale = locale
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListSubscriptionItemsResponseBodySubscriptionItems(TeaModel):
    def __init__(
        self,
        channel: str = None,
        contact_ids: List[int] = None,
        description: str = None,
        email_status: int = None,
        item_id: int = None,
        item_name: str = None,
        pmsg_status: int = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_ids: List[int] = None,
        webhook_status: int = None,
    ):
        self.channel = channel
        self.contact_ids = contact_ids
        self.description = description
        self.email_status = email_status
        self.item_id = item_id
        self.item_name = item_name
        self.pmsg_status = pmsg_status
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_ids = webhook_ids
        self.webhook_status = webhook_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_ids is not None:
            result['WebhookIds'] = self.webhook_ids
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookIds') is not None:
            self.webhook_ids = m.get('WebhookIds')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        return self


class ListSubscriptionItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        subscription_items: List[ListSubscriptionItemsResponseBodySubscriptionItems] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.subscription_items = subscription_items
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.subscription_items:
            for k in self.subscription_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubscriptionItems'] = []
        if self.subscription_items is not None:
            for k in self.subscription_items:
                result['SubscriptionItems'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subscription_items = []
        if m.get('SubscriptionItems') is not None:
            for k in m.get('SubscriptionItems'):
                temp_model = ListSubscriptionItemsResponseBodySubscriptionItems()
                self.subscription_items.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSubscriptionItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubscriptionItemsResponseBody = None,
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
            temp_model = ListSubscriptionItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebhooksRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        locale: str = None,
        max_results: int = None,
        next_token: str = None,
        webhook_id: int = None,
    ):
        self.filter = filter
        self.locale = locale
        self.max_results = max_results
        self.next_token = next_token
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class ListWebhooksResponseBodyWebhooks(TeaModel):
    def __init__(
        self,
        server_url: str = None,
        webhook_id: int = None,
        webhook_name: str = None,
    ):
        self.server_url = server_url
        self.webhook_id = webhook_id
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class ListWebhooksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        webhooks: List[ListWebhooksResponseBodyWebhooks] = None,
    ):
        self.code = code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.webhooks = webhooks

    def validate(self):
        if self.webhooks:
            for k in self.webhooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Webhooks'] = []
        if self.webhooks is not None:
            for k in self.webhooks:
                result['Webhooks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.webhooks = []
        if m.get('Webhooks') is not None:
            for k in m.get('Webhooks'):
                temp_model = ListWebhooksResponseBodyWebhooks()
                self.webhooks.append(temp_model.from_map(k))
        return self


class ListWebhooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWebhooksResponseBody = None,
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
            temp_model = ListWebhooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationMessageRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        locale: str = None,
        type: int = None,
    ):
        self.contact_id = contact_id
        self.locale = locale
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendVerificationMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
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


class SendVerificationMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerificationMessageResponseBody = None,
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
            temp_model = SendVerificationMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContactRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        contact_id: int = None,
        contact_name: str = None,
        email: str = None,
        locale: str = None,
        mobile: str = None,
    ):
        self.client_token = client_token
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.email = email
        self.locale = locale
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class UpdateContactResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
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


class UpdateContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateContactResponseBody = None,
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
            temp_model = UpdateContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubscriptionItemRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        contact_ids: List[int] = None,
        email_status: int = None,
        item_id: int = None,
        locale: str = None,
        pmsg_status: int = None,
        region_id: str = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_ids: List[int] = None,
        webhook_status: int = None,
    ):
        self.client_token = client_token
        self.contact_ids = contact_ids
        self.email_status = email_status
        self.item_id = item_id
        self.locale = locale
        self.pmsg_status = pmsg_status
        self.region_id = region_id
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_ids = webhook_ids
        self.webhook_status = webhook_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_ids is not None:
            result['WebhookIds'] = self.webhook_ids
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookIds') is not None:
            self.webhook_ids = m.get('WebhookIds')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        return self


class UpdateSubscriptionItemShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        contact_ids_shrink: str = None,
        email_status: int = None,
        item_id: int = None,
        locale: str = None,
        pmsg_status: int = None,
        region_id: str = None,
        sms_status: int = None,
        tts_status: int = None,
        webhook_ids_shrink: str = None,
        webhook_status: int = None,
    ):
        self.client_token = client_token
        self.contact_ids_shrink = contact_ids_shrink
        self.email_status = email_status
        self.item_id = item_id
        self.locale = locale
        self.pmsg_status = pmsg_status
        self.region_id = region_id
        self.sms_status = sms_status
        self.tts_status = tts_status
        self.webhook_ids_shrink = webhook_ids_shrink
        self.webhook_status = webhook_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.contact_ids_shrink is not None:
            result['ContactIds'] = self.contact_ids_shrink
        if self.email_status is not None:
            result['EmailStatus'] = self.email_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.pmsg_status is not None:
            result['PmsgStatus'] = self.pmsg_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.tts_status is not None:
            result['TtsStatus'] = self.tts_status
        if self.webhook_ids_shrink is not None:
            result['WebhookIds'] = self.webhook_ids_shrink
        if self.webhook_status is not None:
            result['WebhookStatus'] = self.webhook_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ContactIds') is not None:
            self.contact_ids_shrink = m.get('ContactIds')
        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('PmsgStatus') is not None:
            self.pmsg_status = m.get('PmsgStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('TtsStatus') is not None:
            self.tts_status = m.get('TtsStatus')
        if m.get('WebhookIds') is not None:
            self.webhook_ids_shrink = m.get('WebhookIds')
        if m.get('WebhookStatus') is not None:
            self.webhook_status = m.get('WebhookStatus')
        return self


class UpdateSubscriptionItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
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


class UpdateSubscriptionItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSubscriptionItemResponseBody = None,
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
            temp_model = UpdateSubscriptionItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebhookRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        locale: str = None,
        server_url: str = None,
        webhook_id: int = None,
        webhook_name: str = None,
    ):
        self.client_token = client_token
        self.locale = locale
        self.server_url = server_url
        self.webhook_id = webhook_id
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class UpdateWebhookResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
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


class UpdateWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWebhookResponseBody = None,
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
            temp_model = UpdateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


