# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class RevokeFeedbackRequest(TeaModel):
    def __init__(
        self,
        sample_type: str = None,
        value: str = None,
    ):
        # Sample type. For phone number type samples, input PHONE; for email type samples, input EMAIL; for account type samples, input ACCOUNT.
        # 
        # This parameter is required.
        self.sample_type = sample_type
        # Sample value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sample_type is not None:
            result['SampleType'] = self.sample_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SampleType') is not None:
            self.sample_type = m.get('SampleType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class RevokeFeedbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Interface status or POP error code. Value explanations are as follows: 2xx: Success. 3xx: Redirect. 4xx: Request error. 5xx: Server error.
        self.code = code
        # Return message.
        self.message = message
        # Public parameter, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeFeedbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendFeedbackRequest(TeaModel):
    def __init__(
        self,
        reason: str = None,
        risk_label: str = None,
        sample_type: str = None,
        value: str = None,
    ):
        self.reason = reason
        # Sample labels. User-defined, separated by commas.
        self.risk_label = risk_label
        # Sample type. For phone number type samples, input PHONE; for email type samples, input EMAIL; for account type samples, input ACCOUNT.
        # 
        # This parameter is required.
        self.sample_type = sample_type
        # Sample value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.risk_label is not None:
            result['RiskLabel'] = self.risk_label
        if self.sample_type is not None:
            result['SampleType'] = self.sample_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RiskLabel') is not None:
            self.risk_label = m.get('RiskLabel')
        if m.get('SampleType') is not None:
            self.sample_type = m.get('SampleType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SendFeedbackResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Interface status or POP error code. The values are as follows: 2xx: Success. 3xx: Redirect. 4xx: Request error. 5xx: Server error.
        self.code = code
        # Return message.
        self.message = message
        # Public parameter, each request ID is unique and can be used for troubleshooting and problem localization.
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendFeedbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadSampleApiRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        data_value: str = None,
        sample_type: str = None,
        service: str = None,
    ):
        # The data type of the sample
        # 
        # - Phone number: mobile
        # - MD5 of phone number: mobileMd5
        # - IP: ip
        # - Unique device ID: umid
        # - Account ID: accountId
        # - IMEI: imei
        # - MD5 of IMEI: imeiMd5
        # - OAID: oaid
        # - MD5 of OAID: oaidMd5
        # - Android ID: androidId
        # - MD5 of Android ID: androidIdMd5
        # 
        # This parameter is required.
        self.data_type = data_type
        # Specific value of the sample, to be passed in JSON format. Do not exceed 1000 entries at a time.
        # 
        # This parameter is required.
        self.data_value = data_value
        # The type of the sample
        # 
        # - Blacklist: block
        # 
        # - Whitelist: pass
        # 
        # This parameter is required.
        self.sample_type = sample_type
        # List of effective services, separate multiple services with commas
        # 
        # - Basic/Enhanced Registration Risk Identification: account_abuse
        # - Basic/Enhanced Marketing Risk Identification: coupon_abuse
        # - Basic/Enhanced Login Risk Identification: account_takeover
        # 
        # This parameter is required.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_value is not None:
            result['DataValue'] = self.data_value
        if self.sample_type is not None:
            result['SampleType'] = self.sample_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')
        if m.get('SampleType') is not None:
            self.sample_type = m.get('SampleType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class UploadSampleApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # Request code returned
        self.code = code
        # Error message returned
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Indicator of whether the access was successful
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadSampleApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadSampleApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadSampleApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


