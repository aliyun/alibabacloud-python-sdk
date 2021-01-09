# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class BatchSendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: str = None,
        from_: str = None,
        message: str = None,
        type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to = to
        self.from_ = from_
        self.message = message
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to is not None:
            result['To'] = self.to
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class BatchSendMessageToGlobeResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        request_id: str = None,
        failed_list: str = None,
        response_description: str = None,
        from_: str = None,
        success_count: str = None,
    ):
        self.response_code = response_code
        self.request_id = request_id
        self.failed_list = failed_list
        self.response_description = response_description
        self.from_ = from_
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.failed_list is not None:
            result['FailedList'] = self.failed_list
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.from_ is not None:
            result['From'] = self.from_
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FailedList') is not None:
            self.failed_list = m.get('FailedList')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class BatchSendMessageToGlobeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSendMessageToGlobeResponseBody = None,
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
            temp_model = BatchSendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        message_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class QueryMessageResponseBodyNumberDetail(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        region: str = None,
        country: str = None,
    ):
        self.carrier = carrier
        self.region = region
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        return self


class QueryMessageResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_description: str = None,
        response_code: str = None,
        receive_date: str = None,
        number_detail: QueryMessageResponseBodyNumberDetail = None,
        message: str = None,
        response_description: str = None,
        error_code: str = None,
        send_date: str = None,
        to: str = None,
    ):
        self.status = status
        self.error_description = error_description
        self.response_code = response_code
        self.receive_date = receive_date
        self.number_detail = number_detail
        self.message = message
        self.response_description = response_description
        self.error_code = error_code
        self.send_date = send_date
        self.to = to

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_description is not None:
            result['ErrorDescription'] = self.error_description
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorDescription') is not None:
            self.error_description = m.get('ErrorDescription')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('NumberDetail') is not None:
            temp_model = QueryMessageResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class QueryMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMessageResponseBody = None,
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
            temp_model = QueryMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: str = None,
        from_: str = None,
        message: str = None,
        type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to = to
        self.from_ = from_
        self.message = message
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to is not None:
            result['To'] = self.to
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SendMessageToGlobeResponseBodyNumberDetail(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        region: str = None,
        country: str = None,
    ):
        self.carrier = carrier
        self.region = region
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        return self


class SendMessageToGlobeResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        number_detail: SendMessageToGlobeResponseBodyNumberDetail = None,
        segments: str = None,
        response_description: str = None,
        from_: str = None,
        to: str = None,
        message_id: str = None,
    ):
        self.response_code = response_code
        self.number_detail = number_detail
        self.segments = segments
        self.response_description = response_description
        self.from_ = from_
        self.to = to
        self.message_id = message_id

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.segments is not None:
            result['Segments'] = self.segments
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('NumberDetail') is not None:
            temp_model = SendMessageToGlobeResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('Segments') is not None:
            self.segments = m.get('Segments')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendMessageToGlobeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageToGlobeResponseBody = None,
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
            temp_model = SendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageWithTemplateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        to: str = None,
        from_: str = None,
        template_code: str = None,
        template_param: str = None,
        sms_up_extend_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.to = to
        self.from_ = from_
        self.template_code = template_code
        self.template_param = template_param
        self.sms_up_extend_code = sms_up_extend_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to is not None:
            result['To'] = self.to
        if self.from_ is not None:
            result['From'] = self.from_
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        return self


class SendMessageWithTemplateResponseBodyNumberDetail(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        region: str = None,
        country: str = None,
    ):
        self.carrier = carrier
        self.region = region
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        return self


class SendMessageWithTemplateResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        number_detail: SendMessageWithTemplateResponseBodyNumberDetail = None,
        response_description: str = None,
        segments: str = None,
        to: str = None,
        message_id: str = None,
    ):
        self.response_code = response_code
        self.number_detail = number_detail
        self.response_description = response_description
        self.segments = segments
        self.to = to
        self.message_id = message_id

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.segments is not None:
            result['Segments'] = self.segments
        if self.to is not None:
            result['To'] = self.to
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('NumberDetail') is not None:
            temp_model = SendMessageWithTemplateResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('Segments') is not None:
            self.segments = m.get('Segments')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendMessageWithTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageWithTemplateResponseBody = None,
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
            temp_model = SendMessageWithTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsConversionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        message_id: str = None,
        conversion_date: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.message_id = message_id
        self.conversion_date = conversion_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.conversion_date is not None:
            result['ConversionDate'] = self.conversion_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('ConversionDate') is not None:
            self.conversion_date = m.get('ConversionDate')
        return self


class SmsConversionResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        response_description: str = None,
    ):
        self.response_code = response_code
        self.response_description = response_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        return self


class SmsConversionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SmsConversionResponseBody = None,
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
            temp_model = SmsConversionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


