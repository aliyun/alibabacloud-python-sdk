# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class QueryMessageRequest(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        message_id: str = None,
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
        self.message_id = message_id

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.message_id is not None:
            result['MessageId'] = self.message_id
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
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
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
            temp_model = QueryMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        to: str = None,
        from_: str = None,
        message: str = None,
        type: str = None,
        task_id: str = None,
    ):
        self.to = to
        self.from_ = from_
        self.message = message
        self.type = type
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to is not None:
            result['To'] = self.to
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.type is not None:
            result['Type'] = self.type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BatchSendMessageToGlobeResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        request_id: str = None,
        failed_list: str = None,
        response_description: str = None,
        from_: str = None,
        message_id_list: str = None,
        success_count: str = None,
    ):
        self.response_code = response_code
        self.request_id = request_id
        self.failed_list = failed_list
        self.response_description = response_description
        self.from_ = from_
        self.message_id_list = message_id_list
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.message_id_list is not None:
            result['MessageIdList'] = self.message_id_list
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
        if m.get('MessageIdList') is not None:
            self.message_id_list = m.get('MessageIdList')
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
            temp_model = BatchSendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsConversionRequest(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        delivered: bool = None,
        conversion_time: int = None,
    ):
        self.message_id = message_id
        self.delivered = delivered
        self.conversion_time = conversion_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.delivered is not None:
            result['Delivered'] = self.delivered
        if self.conversion_time is not None:
            result['ConversionTime'] = self.conversion_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Delivered') is not None:
            self.delivered = m.get('Delivered')
        if m.get('ConversionTime') is not None:
            self.conversion_time = m.get('ConversionTime')
        return self


class SmsConversionResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        response_description: str = None,
        request_id: str = None,
    ):
        self.response_code = response_code
        self.response_description = response_description
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = SmsConversionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        to: str = None,
        from_: str = None,
        message: str = None,
        task_id: str = None,
    ):
        self.to = to
        self.from_ = from_
        self.message = message
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to is not None:
            result['To'] = self.to
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        segments: str = None,
        response_description: str = None,
        from_: str = None,
        to: str = None,
        message_id: str = None,
    ):
        self.response_code = response_code
        self.number_detail = number_detail
        self.request_id = request_id
        self.segments = segments
        self.response_description = response_description
        self.from_ = from_
        self.to = to
        self.message_id = message_id

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = SendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConversionDataRequest(TeaModel):
    def __init__(
        self,
        report_time: int = None,
        conversion_rate: str = None,
    ):
        self.report_time = report_time
        self.conversion_rate = conversion_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_time is not None:
            result['ReportTime'] = self.report_time
        if self.conversion_rate is not None:
            result['ConversionRate'] = self.conversion_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')
        if m.get('ConversionRate') is not None:
            self.conversion_rate = m.get('ConversionRate')
        return self


class ConversionDataResponseBody(TeaModel):
    def __init__(
        self,
        response_code: str = None,
        response_description: str = None,
        request_id: str = None,
    ):
        self.response_code = response_code
        self.response_description = response_description
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConversionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConversionDataResponseBody = None,
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
            temp_model = ConversionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageWithTemplateRequest(TeaModel):
    def __init__(
        self,
        to: str = None,
        from_: str = None,
        template_code: str = None,
        template_param: str = None,
        sms_up_extend_code: str = None,
    ):
        self.to = to
        self.from_ = from_
        self.template_code = template_code
        self.template_param = template_param
        self.sms_up_extend_code = sms_up_extend_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SendMessageWithTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


