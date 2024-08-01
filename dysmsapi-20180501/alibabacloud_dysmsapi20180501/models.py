# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class BatchSendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        from_: str = None,
        message: str = None,
        task_id: str = None,
        to: str = None,
        type: str = None,
        validity_period: int = None,
    ):
        # The mobile phone number of the sender. You can also specify a sender ID. The sender ID can contain both letters and digits. If it does, the ID must be between 1 to 11 characters in length. If the sender ID contains only digits, it must be 1 to 15 characters in length.
        self.from_ = from_
        # The content of the message.
        # 
        # This parameter is required.
        self.message = message
        # The ID of the messaging campaign. It must be 1 to 255 characters in length. The ID is the value of the TaskId field in the delivery receipt of the message.
        self.task_id = task_id
        # The mobile phone numbers to which the message is sent. You must add the dialing code to the beginning of each mobile phone number.
        # 
        # For more information, see [Dialing codes](https://www.alibabacloud.com/help/zh/short-message-service/latest/dialing-codes).
        # 
        # This parameter is required.
        self.to = to
        # The type of the message. Valid values:
        # 
        # *   **NOTIFY**: notification
        # *   **MKT**: promotional message
        self.type = type
        # The validity period of the message. Unit: seconds.
        self.validity_period = validity_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.to is not None:
            result['To'] = self.to
        if self.type is not None:
            result['Type'] = self.type
        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidityPeriod') is not None:
            self.validity_period = m.get('ValidityPeriod')
        return self


class BatchSendMessageToGlobeResponseBody(TeaModel):
    def __init__(
        self,
        failed_list: str = None,
        from_: str = None,
        message_id_list: str = None,
        request_id: str = None,
        response_code: str = None,
        response_description: str = None,
        success_count: str = None,
    ):
        # The list of mobile phone numbers that failed to receive the message.
        self.failed_list = failed_list
        # The sender ID returned.
        self.from_ = from_
        # The ID of the message.
        self.message_id_list = message_id_list
        # The ID of the request.
        self.request_id = request_id
        # The status code. If OK is returned, the request is successful. For more information, see [Error codes](https://www.alibabacloud.com/help/zh/short-message-service/latest/error-codes).
        self.response_code = response_code
        # The description of the status code.
        self.response_description = response_description
        # The number of mobile phone numbers that received the message.
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_list is not None:
            result['FailedList'] = self.failed_list
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message_id_list is not None:
            result['MessageIdList'] = self.message_id_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedList') is not None:
            self.failed_list = m.get('FailedList')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('MessageIdList') is not None:
            self.message_id_list = m.get('MessageIdList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class BatchSendMessageToGlobeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSendMessageToGlobeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchSendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConversionDataRequest(TeaModel):
    def __init__(
        self,
        conversion_rate: str = None,
        report_time: int = None,
    ):
        # Conversion rate monitoring return value.
        # 
        # >  The value of this parameter is of type double, and the value is between [0,1].
        # 
        # This parameter is required.
        self.conversion_rate = conversion_rate
        # Timestamp of the conversion rate observation should be a Unix timestamp, a millisecond-level long integer.
        # 
        # >  If this field is not specified: the current timestamp is the default.
        self.report_time = report_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversion_rate is not None:
            result['ConversionRate'] = self.conversion_rate
        if self.report_time is not None:
            result['ReportTime'] = self.report_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversionRate') is not None:
            self.conversion_rate = m.get('ConversionRate')
        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')
        return self


class ConversionDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_code: str = None,
        response_description: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Status code. Returning OK means the request was successful. For other error codes, please refer to the [Error codes](https://help.aliyun.com/document_detail/180674.html) list.
        self.response_code = response_code
        # The description of the status code.
        self.response_description = response_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        return self


class ConversionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConversionDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConversionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageRequest(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        # The ID of the message.
        # 
        # This parameter is required.
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
        country: str = None,
        region: str = None,
    ):
        # The carrier that owns the mobile phone number.
        self.carrier = carrier
        # The country to which the mobile phone number belongs.
        self.country = country
        # The region to which the mobile phone number belongs.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.country is not None:
            result['Country'] = self.country
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryMessageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_description: str = None,
        message: str = None,
        message_id: str = None,
        number_detail: QueryMessageResponseBodyNumberDetail = None,
        receive_date: str = None,
        request_id: str = None,
        response_code: str = None,
        response_description: str = None,
        send_date: str = None,
        status: str = None,
        to: str = None,
    ):
        # The status code of the message.
        self.error_code = error_code
        # The description of the status code.
        self.error_description = error_description
        # The content of the message.
        self.message = message
        # The ID of the message.
        self.message_id = message_id
        # The details about the mobile phone number.
        self.number_detail = number_detail
        # The time when the delivery receipt was received from the carrier.
        self.receive_date = receive_date
        # The ID of the request.
        self.request_id = request_id
        # The status code of the delivery request.
        self.response_code = response_code
        # The description of the delivery request status.
        self.response_description = response_description
        # The time when the message was sent to the carrier.
        self.send_date = send_date
        # The delivery status of the message.
        # 
        # *   1: The message was sent.
        # *   2: The message failed to be sent.
        # *   3: The message is being sent.
        self.status = status
        # The mobile phone number to which the message was sent.
        self.to = to

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_description is not None:
            result['ErrorDescription'] = self.error_description
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.status is not None:
            result['Status'] = self.status
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorDescription') is not None:
            self.error_description = m.get('ErrorDescription')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('NumberDetail') is not None:
            temp_model = QueryMessageResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class QueryMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageToGlobeRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        from_: str = None,
        message: str = None,
        task_id: str = None,
        to: str = None,
        validity_period: int = None,
    ):
        # The ID of the channel.
        self.channel_id = channel_id
        # The mobile phone number of the sender. You can also specify a sender ID. The sender ID can contain both letters and digits. If it does, the ID must be between 1 to 11 characters in length. If the sender ID contains only digits, it must be 1 to 15 characters in length.
        self.from_ = from_
        # The content of the message.
        # 
        # This parameter is required.
        self.message = message
        # The ID of the messaging campaign. It must be 1 to 255 characters in length. The ID is the value of the TaskId field in the delivery receipt of the message.
        self.task_id = task_id
        # The mobile phone number to which the message is sent. You must add the dialing code to the beginning of the mobile phone number. Example: 8521245567\\*\\*\\*\\*.
        # 
        # For more information, see [Dialing codes](https://www.alibabacloud.com/help/en/sms/product-overview/dialing-codes?spm=a2c63.p38356.0.0.48b940a1PFYRMz).
        # 
        # >  You cannot call the SendMessageToGlobe operation to send messages to the Chinese mainland.
        # 
        # This parameter is required.
        self.to = to
        # The validity period of the message. Unit: seconds.
        self.validity_period = validity_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.to is not None:
            result['To'] = self.to
        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('ValidityPeriod') is not None:
            self.validity_period = m.get('ValidityPeriod')
        return self


class SendMessageToGlobeResponseBodyNumberDetail(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        country: str = None,
        region: str = None,
    ):
        # The carrier that owns the mobile phone number.
        self.carrier = carrier
        # The country to which the mobile phone number belongs.
        self.country = country
        # The region to which the mobile phone number belongs.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.country is not None:
            result['Country'] = self.country
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SendMessageToGlobeResponseBody(TeaModel):
    def __init__(
        self,
        from_: str = None,
        message_id: str = None,
        number_detail: SendMessageToGlobeResponseBodyNumberDetail = None,
        request_id: str = None,
        response_code: str = None,
        response_description: str = None,
        segments: str = None,
        to: str = None,
    ):
        # The sender ID returned.
        self.from_ = from_
        # The ID of the message.
        self.message_id = message_id
        # The details about the mobile phone number of the recipient.
        self.number_detail = number_detail
        # The ID of the request.
        self.request_id = request_id
        # The status code of the delivery request.
        self.response_code = response_code
        # The description of the delivery request status.
        self.response_description = response_description
        # The number of messages that incurred fees.
        self.segments = segments
        # The mobile phone number to which the message was sent.
        self.to = to

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.segments is not None:
            result['Segments'] = self.segments
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('NumberDetail') is not None:
            temp_model = SendMessageToGlobeResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('Segments') is not None:
            self.segments = m.get('Segments')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendMessageToGlobeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageToGlobeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendMessageToGlobeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageWithTemplateRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        from_: str = None,
        sms_up_extend_code: str = None,
        template_code: str = None,
        template_param: str = None,
        to: str = None,
        validity_period: int = None,
    ):
        # The ID of the channel.
        self.channel_id = channel_id
        # The signature. To query the signature, log on to the [Short Message Service (SMS) console](https://sms-intl.console.aliyun.com/overview) and navigate to the **Signatures** tab of the **Go China** page.
        # 
        # This parameter is required.
        self.from_ = from_
        # The extension code of the MO message.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the message template. To query the code, log on to the [SMS console](https://sms-intl.console.aliyun.com/overview) and navigate to the **Templates** tab of the **Go China** page.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The value of the variable in the message template. If a variable exists in the template, the parameter is required.
        self.template_param = template_param
        # The mobile phone number to which the message is sent. You must add the country code to the beginning of the mobile phone number. Example: 861503871\\*\\*\\*\\*.
        # 
        # For more information, see [Dialing codes](https://www.alibabacloud.com/help/en/sms/product-overview/dialing-codes?spm=a2c63.p38356.0.0.367279cbwQFoeM).
        # 
        # This parameter is required.
        self.to = to
        # The validity period of the message.
        self.validity_period = validity_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        if self.to is not None:
            result['To'] = self.to
        if self.validity_period is not None:
            result['ValidityPeriod'] = self.validity_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('ValidityPeriod') is not None:
            self.validity_period = m.get('ValidityPeriod')
        return self


class SendMessageWithTemplateResponseBodyNumberDetail(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        country: str = None,
        region: str = None,
    ):
        # The carrier that owns the mobile phone number.
        self.carrier = carrier
        # The country to which the mobile phone number belongs.
        self.country = country
        # The region to which the mobile phone number belongs.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.country is not None:
            result['Country'] = self.country
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SendMessageWithTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        number_detail: SendMessageWithTemplateResponseBodyNumberDetail = None,
        request_id: str = None,
        response_code: str = None,
        response_description: str = None,
        segments: str = None,
        to: str = None,
    ):
        # The ID of the message.
        self.message_id = message_id
        # The details about the mobile phone number of the recipient.
        self.number_detail = number_detail
        # The ID of the request.
        self.request_id = request_id
        # The status code of the delivery request.
        self.response_code = response_code
        # The description of the delivery request status.
        self.response_description = response_description
        # The number of messages that incurred fees.
        self.segments = segments
        # The mobile phone number to which the message was sent. The dialing code was added to the beginning of the mobile phone number. Example: 861503871\\*\\*\\*\\*.
        self.to = to

    def validate(self):
        if self.number_detail:
            self.number_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.number_detail is not None:
            result['NumberDetail'] = self.number_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        if self.segments is not None:
            result['Segments'] = self.segments
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('NumberDetail') is not None:
            temp_model = SendMessageWithTemplateResponseBodyNumberDetail()
            self.number_detail = temp_model.from_map(m['NumberDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        if m.get('Segments') is not None:
            self.segments = m.get('Segments')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendMessageWithTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageWithTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendMessageWithTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsConversionRequest(TeaModel):
    def __init__(
        self,
        conversion_time: int = None,
        delivered: bool = None,
        message_id: str = None,
    ):
        # The time when the OTP message was delivered. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # *   If you leave the parameter empty, the current timestamp is specified by default.
        # *   If you specify the parameter, the timestamp must be greater than the message sending time and less than the current timestamp.
        self.conversion_time = conversion_time
        # Specifies whether customers replied to the OTP message. Valid values: true and false.
        # 
        # This parameter is required.
        self.delivered = delivered
        # The ID of the OTP message.
        # 
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversion_time is not None:
            result['ConversionTime'] = self.conversion_time
        if self.delivered is not None:
            result['Delivered'] = self.delivered
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversionTime') is not None:
            self.conversion_time = m.get('ConversionTime')
        if m.get('Delivered') is not None:
            self.delivered = m.get('Delivered')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SmsConversionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_code: str = None,
        response_description: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status code. If OK is returned, the request is successful. For more information, see [Error codes](https://help.aliyun.com/document_detail/180674.html).
        self.response_code = response_code
        # The description of the status code.
        self.response_description = response_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.response_description is not None:
            result['ResponseDescription'] = self.response_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResponseDescription') is not None:
            self.response_description = m.get('ResponseDescription')
        return self


class SmsConversionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmsConversionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SmsConversionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


