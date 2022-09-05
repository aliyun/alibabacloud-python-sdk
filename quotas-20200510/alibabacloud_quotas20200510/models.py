# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateQuotaAlarmRequestQuotaDimensions(TeaModel):
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


class CreateQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[CreateQuotaAlarmRequestQuotaDimensions] = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        self.alarm_name = alarm_name
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_dimensions = quota_dimensions
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.threshold_type = threshold_type
        self.web_hook = web_hook

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = CreateQuotaAlarmRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        return self


class CreateQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        request_id: str = None,
    ):
        self.alarm_id = alarm_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaAlarmResponseBody = None,
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
            temp_model = CreateQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaApplicationRequestDimensions(TeaModel):
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


class CreateQuotaApplicationRequest(TeaModel):
    def __init__(
        self,
        audit_mode: str = None,
        desire_value: float = None,
        dimensions: List[CreateQuotaApplicationRequestDimensions] = None,
        env_language: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
    ):
        self.audit_mode = audit_mode
        self.desire_value = desire_value
        self.dimensions = dimensions
        self.env_language = env_language
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_category = quota_category
        self.reason = reason

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateQuotaApplicationRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CreateQuotaApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        desire_value: int = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.application_id = application_id
        self.apply_time = apply_time
        self.approve_value = approve_value
        self.audit_reason = audit_reason
        self.desire_value = desire_value
        self.dimension = dimension
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_arn = quota_arn
        self.quota_description = quota_description
        self.quota_name = quota_name
        self.quota_unit = quota_unit
        self.reason = reason
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateQuotaApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaApplicationResponseBody = None,
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
            temp_model = CreateQuotaApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateQuotaItemRequestDimensions(TeaModel):
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


class CreateTemplateQuotaItemRequest(TeaModel):
    def __init__(
        self,
        desire_value: float = None,
        dimensions: List[CreateTemplateQuotaItemRequestDimensions] = None,
        env_language: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        self.desire_value = desire_value
        self.dimensions = dimensions
        self.env_language = env_language
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateTemplateQuotaItemRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class CreateTemplateQuotaItemResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateQuotaItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateQuotaItemResponseBody = None,
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
            temp_model = CreateTemplateQuotaItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
    ):
        self.alarm_id = alarm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        return self


class DeleteQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQuotaAlarmResponseBody = None,
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
            temp_model = DeleteQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateQuotaItemRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTemplateQuotaItemResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateQuotaItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateQuotaItemResponseBody = None,
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
            temp_model = DeleteTemplateQuotaItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductQuotaRequestDimensions(TeaModel):
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


class GetProductQuotaRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[GetProductQuotaRequestDimensions] = None,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        self.dimensions = dimensions
        self.product_code = product_code
        self.quota_action_code = quota_action_code

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = GetProductQuotaRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class GetProductQuotaResponseBodyQuotaPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        self.period_unit = period_unit
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class GetProductQuotaResponseBodyQuotaQuotaItems(TeaModel):
    def __init__(
        self,
        quota: str = None,
        quota_unit: str = None,
        type: str = None,
        usage: str = None,
    ):
        self.quota = quota
        self.quota_unit = quota_unit
        self.type = type
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class GetProductQuotaResponseBodyQuota(TeaModel):
    def __init__(
        self,
        adjustable: bool = None,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        consumable: bool = None,
        dimensions: Dict[str, Any] = None,
        period: GetProductQuotaResponseBodyQuotaPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_items: List[GetProductQuotaResponseBodyQuotaQuotaItems] = None,
        quota_name: str = None,
        quota_type: str = None,
        quota_unit: str = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
    ):
        self.adjustable = adjustable
        self.applicable_range = applicable_range
        self.applicable_type = applicable_type
        self.consumable = consumable
        self.dimensions = dimensions
        self.period = period
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_arn = quota_arn
        self.quota_description = quota_description
        self.quota_items = quota_items
        self.quota_name = quota_name
        self.quota_type = quota_type
        self.quota_unit = quota_unit
        self.total_quota = total_quota
        self.total_usage = total_usage
        self.unadjustable_detail = unadjustable_detail

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for k in self.quota_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.consumable is not None:
            result['Consumable'] = self.consumable
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k in self.quota_items:
                result['QuotaItems'].append(k.to_map() if k else None)
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Period') is not None:
            temp_model = GetProductQuotaResponseBodyQuotaPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k in m.get('QuotaItems'):
                temp_model = GetProductQuotaResponseBodyQuotaQuotaItems()
                self.quota_items.append(temp_model.from_map(k))
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        return self


class GetProductQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quota: GetProductQuotaResponseBodyQuota = None,
        request_id: str = None,
    ):
        self.quota = quota
        self.request_id = request_id

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = GetProductQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductQuotaResponseBody = None,
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
            temp_model = GetProductQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductQuotaDimensionRequestDependentDimensions(TeaModel):
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


class GetProductQuotaDimensionRequest(TeaModel):
    def __init__(
        self,
        dependent_dimensions: List[GetProductQuotaDimensionRequestDependentDimensions] = None,
        dimension_key: str = None,
        product_code: str = None,
    ):
        self.dependent_dimensions = dependent_dimensions
        self.dimension_key = dimension_key
        self.product_code = product_code

    def validate(self):
        if self.dependent_dimensions:
            for k in self.dependent_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DependentDimensions'] = []
        if self.dependent_dimensions is not None:
            for k in self.dependent_dimensions:
                result['DependentDimensions'].append(k.to_map() if k else None)
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dependent_dimensions = []
        if m.get('DependentDimensions') is not None:
            for k in m.get('DependentDimensions'):
                temp_model = GetProductQuotaDimensionRequestDependentDimensions()
                self.dependent_dimensions.append(temp_model.from_map(k))
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProductQuotaDimensionResponseBodyQuotaDimension(TeaModel):
    def __init__(
        self,
        dependent_dimensions: List[str] = None,
        dimension_key: str = None,
        dimension_value_detail: List[GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail] = None,
        dimension_values: List[str] = None,
        name: str = None,
    ):
        self.dependent_dimensions = dependent_dimensions
        self.dimension_key = dimension_key
        self.dimension_value_detail = dimension_value_detail
        self.dimension_values = dimension_values
        self.name = name

    def validate(self):
        if self.dimension_value_detail:
            for k in self.dimension_value_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        result['DimensionValueDetail'] = []
        if self.dimension_value_detail is not None:
            for k in self.dimension_value_detail:
                result['DimensionValueDetail'].append(k.to_map() if k else None)
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        self.dimension_value_detail = []
        if m.get('DimensionValueDetail') is not None:
            for k in m.get('DimensionValueDetail'):
                temp_model = GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail()
                self.dimension_value_detail.append(temp_model.from_map(k))
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetProductQuotaDimensionResponseBody(TeaModel):
    def __init__(
        self,
        quota_dimension: GetProductQuotaDimensionResponseBodyQuotaDimension = None,
        request_id: str = None,
    ):
        self.quota_dimension = quota_dimension
        self.request_id = request_id

    def validate(self):
        if self.quota_dimension:
            self.quota_dimension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaDimension') is not None:
            temp_model = GetProductQuotaDimensionResponseBodyQuotaDimension()
            self.quota_dimension = temp_model.from_map(m['QuotaDimension'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductQuotaDimensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductQuotaDimensionResponseBody = None,
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
            temp_model = GetProductQuotaDimensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
    ):
        self.alarm_id = alarm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        return self


class GetQuotaAlarmResponseBodyQuotaAlarm(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        create_time: str = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimension: Dict[str, Any] = None,
        quota_usage: float = None,
        quota_value: float = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_name = alarm_name
        self.create_time = create_time
        self.notify_channels = notify_channels
        self.notify_target = notify_target
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_dimension = quota_dimension
        self.quota_usage = quota_usage
        self.quota_value = quota_value
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.threshold_type = threshold_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaDimension') is not None:
            self.quota_dimension = m.get('QuotaDimension')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        return self


class GetQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        quota_alarm: GetQuotaAlarmResponseBodyQuotaAlarm = None,
        request_id: str = None,
    ):
        self.quota_alarm = quota_alarm
        self.request_id = request_id

    def validate(self):
        if self.quota_alarm:
            self.quota_alarm.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_alarm is not None:
            result['QuotaAlarm'] = self.quota_alarm.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaAlarm') is not None:
            temp_model = GetQuotaAlarmResponseBodyQuotaAlarm()
            self.quota_alarm = temp_model.from_map(m['QuotaAlarm'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaAlarmResponseBody = None,
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
            temp_model = GetQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class GetQuotaApplicationResponseBodyQuotaApplication(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        desire_value: int = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        self.application_id = application_id
        self.apply_time = apply_time
        self.approve_value = approve_value
        self.audit_reason = audit_reason
        self.desire_value = desire_value
        self.dimension = dimension
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_arn = quota_arn
        self.quota_description = quota_description
        self.quota_name = quota_name
        self.quota_unit = quota_unit
        self.reason = reason
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetQuotaApplicationResponseBody(TeaModel):
    def __init__(
        self,
        quota_application: GetQuotaApplicationResponseBodyQuotaApplication = None,
        request_id: str = None,
    ):
        self.quota_application = quota_application
        self.request_id = request_id

    def validate(self):
        if self.quota_application:
            self.quota_application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_application is not None:
            result['QuotaApplication'] = self.quota_application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaApplication') is not None:
            temp_model = GetQuotaApplicationResponseBodyQuotaApplication()
            self.quota_application = temp_model.from_map(m['QuotaApplication'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQuotaApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaApplicationResponseBody = None,
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
            temp_model = GetQuotaApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaTemplateServiceStatusRequest(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
    ):
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        return self


class GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        service_status: int = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetQuotaTemplateServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_service_status: GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus = None,
    ):
        self.request_id = request_id
        self.template_service_status = template_service_status

    def validate(self):
        if self.template_service_status:
            self.template_service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_service_status is not None:
            result['TemplateServiceStatus'] = self.template_service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateServiceStatus') is not None:
            temp_model = GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus()
            self.template_service_status = temp_model.from_map(m['TemplateServiceStatus'])
        return self


class GetQuotaTemplateServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaTemplateServiceStatusResponseBody = None,
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
            temp_model = GetQuotaTemplateServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAlarmHistoriesResponseBodyAlarmHistories(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        create_time: str = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_usage: float = None,
        threshold: float = None,
        threshold_percent: float = None,
    ):
        self.alarm_name = alarm_name
        self.create_time = create_time
        self.notify_channels = notify_channels
        self.notify_target = notify_target
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_usage = quota_usage
        self.threshold = threshold
        self.threshold_percent = threshold_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        alarm_histories: List[ListAlarmHistoriesResponseBodyAlarmHistories] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.alarm_histories = alarm_histories
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = ListAlarmHistoriesResponseBodyAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlarmHistoriesResponseBody = None,
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
            temp_model = ListAlarmHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDependentQuotasRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        self.product_code = product_code
        self.quota_action_code = quota_action_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class ListDependentQuotasResponseBodyQuotasDimensions(TeaModel):
    def __init__(
        self,
        dependent_dimension: List[str] = None,
        dimension_key: str = None,
        dimension_values: List[str] = None,
    ):
        self.dependent_dimension = dependent_dimension
        self.dimension_key = dimension_key
        self.dimension_values = dimension_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependent_dimension is not None:
            result['DependentDimension'] = self.dependent_dimension
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimension') is not None:
            self.dependent_dimension = m.get('DependentDimension')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        return self


class ListDependentQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        dimensions: List[ListDependentQuotasResponseBodyQuotasDimensions] = None,
        product_code: str = None,
        quota_action_code: str = None,
        scale: float = None,
    ):
        self.dimensions = dimensions
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.scale = scale

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.scale is not None:
            result['Scale'] = self.scale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListDependentQuotasResponseBodyQuotasDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        return self


class ListDependentQuotasResponseBody(TeaModel):
    def __init__(
        self,
        quotas: List[ListDependentQuotasResponseBodyQuotas] = None,
        request_id: str = None,
    ):
        self.quotas = quotas
        self.request_id = request_id

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListDependentQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDependentQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDependentQuotasResponseBody = None,
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
            temp_model = ListDependentQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductDimensionGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code

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
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductDimensionGroupsResponseBodyDimensionGroups(TeaModel):
    def __init__(
        self,
        dimension_keys: List[str] = None,
        group_code: str = None,
        group_name: str = None,
        product_code: str = None,
    ):
        self.dimension_keys = dimension_keys
        self.group_code = group_code
        self.group_name = group_name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_keys is not None:
            result['DimensionKeys'] = self.dimension_keys
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKeys') is not None:
            self.dimension_keys = m.get('DimensionKeys')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductDimensionGroupsResponseBody(TeaModel):
    def __init__(
        self,
        dimension_groups: List[ListProductDimensionGroupsResponseBodyDimensionGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dimension_groups = dimension_groups
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dimension_groups:
            for k in self.dimension_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DimensionGroups'] = []
        if self.dimension_groups is not None:
            for k in self.dimension_groups:
                result['DimensionGroups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimension_groups = []
        if m.get('DimensionGroups') is not None:
            for k in m.get('DimensionGroups'):
                temp_model = ListProductDimensionGroupsResponseBodyDimensionGroups()
                self.dimension_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductDimensionGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductDimensionGroupsResponseBody = None,
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
            temp_model = ListProductDimensionGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductQuotaDimensionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_category: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_category = quota_category

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
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductQuotaDimensionsResponseBodyQuotaDimensions(TeaModel):
    def __init__(
        self,
        dependent_dimensions: List[str] = None,
        dimension_key: str = None,
        dimension_value_detail: List[ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail] = None,
        dimension_values: List[str] = None,
        name: str = None,
        requisite: bool = None,
    ):
        self.dependent_dimensions = dependent_dimensions
        self.dimension_key = dimension_key
        self.dimension_value_detail = dimension_value_detail
        self.dimension_values = dimension_values
        self.name = name
        self.requisite = requisite

    def validate(self):
        if self.dimension_value_detail:
            for k in self.dimension_value_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        result['DimensionValueDetail'] = []
        if self.dimension_value_detail is not None:
            for k in self.dimension_value_detail:
                result['DimensionValueDetail'].append(k.to_map() if k else None)
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        if self.name is not None:
            result['Name'] = self.name
        if self.requisite is not None:
            result['Requisite'] = self.requisite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        self.dimension_value_detail = []
        if m.get('DimensionValueDetail') is not None:
            for k in m.get('DimensionValueDetail'):
                temp_model = ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail()
                self.dimension_value_detail.append(temp_model.from_map(k))
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Requisite') is not None:
            self.requisite = m.get('Requisite')
        return self


class ListProductQuotaDimensionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_dimensions: List[ListProductQuotaDimensionsResponseBodyQuotaDimensions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.quota_dimensions = quota_dimensions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
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
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = ListProductQuotaDimensionsResponseBodyQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductQuotaDimensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductQuotaDimensionsResponseBody = None,
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
            temp_model = ListProductQuotaDimensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductQuotasRequestDimensions(TeaModel):
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


class ListProductQuotasRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[ListProductQuotasRequestDimensions] = None,
        group_code: str = None,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        sort_field: str = None,
        sort_order: str = None,
    ):
        self.dimensions = dimensions
        self.group_code = group_code
        self.key_word = key_word
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_category = quota_category
        self.sort_field = sort_field
        self.sort_order = sort_order

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListProductQuotasRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProductQuotasResponseBodyQuotasPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        self.period_unit = period_unit
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class ListProductQuotasResponseBodyQuotasQuotaItems(TeaModel):
    def __init__(
        self,
        quota: str = None,
        quota_unit: str = None,
        type: str = None,
        usage: str = None,
    ):
        self.quota = quota
        self.quota_unit = quota_unit
        self.type = type
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListProductQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        adjustable: bool = None,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        consumable: bool = None,
        dimensions: Dict[str, Any] = None,
        period: ListProductQuotasResponseBodyQuotasPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_items: List[ListProductQuotasResponseBodyQuotasQuotaItems] = None,
        quota_name: str = None,
        quota_type: str = None,
        quota_unit: str = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
    ):
        self.adjustable = adjustable
        self.applicable_range = applicable_range
        self.applicable_type = applicable_type
        self.consumable = consumable
        self.dimensions = dimensions
        self.period = period
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_arn = quota_arn
        self.quota_description = quota_description
        self.quota_items = quota_items
        self.quota_name = quota_name
        self.quota_type = quota_type
        self.quota_unit = quota_unit
        self.total_quota = total_quota
        self.total_usage = total_usage
        self.unadjustable_detail = unadjustable_detail

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for k in self.quota_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.consumable is not None:
            result['Consumable'] = self.consumable
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k in self.quota_items:
                result['QuotaItems'].append(k.to_map() if k else None)
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Period') is not None:
            temp_model = ListProductQuotasResponseBodyQuotasPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k in m.get('QuotaItems'):
                temp_model = ListProductQuotasResponseBodyQuotasQuotaItems()
                self.quota_items.append(temp_model.from_map(k))
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        return self


class ListProductQuotasResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quotas: List[ListProductQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.quotas = quotas
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quotas:
            for k in self.quotas:
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
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListProductQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductQuotasResponseBody = None,
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
            temp_model = ListProductQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListProductsResponseBodyProductInfo(TeaModel):
    def __init__(
        self,
        common_quota_support: str = None,
        dynamic: bool = None,
        flow_control_support: str = None,
        product_code: str = None,
        product_name: str = None,
        product_name_en: str = None,
        second_category_id: int = None,
        second_category_name: str = None,
        second_category_name_en: str = None,
    ):
        self.common_quota_support = common_quota_support
        self.dynamic = dynamic
        self.flow_control_support = flow_control_support
        self.product_code = product_code
        self.product_name = product_name
        self.product_name_en = product_name_en
        self.second_category_id = second_category_id
        self.second_category_name = second_category_name
        self.second_category_name_en = second_category_name_en

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_quota_support is not None:
            result['CommonQuotaSupport'] = self.common_quota_support
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.flow_control_support is not None:
            result['FlowControlSupport'] = self.flow_control_support
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_name_en is not None:
            result['ProductNameEn'] = self.product_name_en
        if self.second_category_id is not None:
            result['SecondCategoryId'] = self.second_category_id
        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name
        if self.second_category_name_en is not None:
            result['SecondCategoryNameEn'] = self.second_category_name_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonQuotaSupport') is not None:
            self.common_quota_support = m.get('CommonQuotaSupport')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('FlowControlSupport') is not None:
            self.flow_control_support = m.get('FlowControlSupport')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductNameEn') is not None:
            self.product_name_en = m.get('ProductNameEn')
        if m.get('SecondCategoryId') is not None:
            self.second_category_id = m.get('SecondCategoryId')
        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')
        if m.get('SecondCategoryNameEn') is not None:
            self.second_category_name_en = m.get('SecondCategoryNameEn')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_info: List[ListProductsResponseBodyProductInfo] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.product_info = product_info
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.product_info:
            for k in self.product_info:
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
        result['ProductInfo'] = []
        if self.product_info is not None:
            for k in self.product_info:
                result['ProductInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.product_info = []
        if m.get('ProductInfo') is not None:
            for k in m.get('ProductInfo'):
                temp_model = ListProductsResponseBodyProductInfo()
                self.product_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
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
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaAlarmsRequestQuotaDimensions(TeaModel):
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


class ListQuotaAlarmsRequest(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[ListQuotaAlarmsRequestQuotaDimensions] = None,
    ):
        self.alarm_name = alarm_name
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_dimensions = quota_dimensions

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = ListQuotaAlarmsRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        return self


class ListQuotaAlarmsResponseBodyQuotaAlarms(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        create_time: str = None,
        exceed_threshold: bool = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: Dict[str, Any] = None,
        quota_usage: float = None,
        quota_value: float = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_name = alarm_name
        self.create_time = create_time
        self.exceed_threshold = exceed_threshold
        self.notify_channels = notify_channels
        self.notify_target = notify_target
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_dimensions = quota_dimensions
        self.quota_usage = quota_usage
        self.quota_value = quota_value
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.threshold_type = threshold_type
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exceed_threshold is not None:
            result['ExceedThreshold'] = self.exceed_threshold
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_dimensions is not None:
            result['QuotaDimensions'] = self.quota_dimensions
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExceedThreshold') is not None:
            self.exceed_threshold = m.get('ExceedThreshold')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaDimensions') is not None:
            self.quota_dimensions = m.get('QuotaDimensions')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        return self


class ListQuotaAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_alarms: List[ListQuotaAlarmsResponseBodyQuotaAlarms] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.quota_alarms = quota_alarms
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quota_alarms:
            for k in self.quota_alarms:
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
        result['QuotaAlarms'] = []
        if self.quota_alarms is not None:
            for k in self.quota_alarms:
                result['QuotaAlarms'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_alarms = []
        if m.get('QuotaAlarms') is not None:
            for k in m.get('QuotaAlarms'):
                temp_model = ListQuotaAlarmsResponseBodyQuotaAlarms()
                self.quota_alarms.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaAlarmsResponseBody = None,
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
            temp_model = ListQuotaAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaApplicationTemplatesRequestDimensions(TeaModel):
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


class ListQuotaApplicationTemplatesRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[ListQuotaApplicationTemplatesRequestDimensions] = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        self.dimensions = dimensions
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_action_code = quota_action_code

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListQuotaApplicationTemplatesRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates(TeaModel):
    def __init__(
        self,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        desire_value: float = None,
        dimensions: Dict[str, Any] = None,
        env_language: str = None,
        id: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_description: str = None,
        quota_name: str = None,
    ):
        self.applicable_range = applicable_range
        self.applicable_type = applicable_type
        self.desire_value = desire_value
        self.dimensions = dimensions
        self.env_language = env_language
        self.id = id
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_description = quota_description
        self.quota_name = quota_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.id is not None:
            result['Id'] = self.id
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        return self


class ListQuotaApplicationTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_application_templates: List[ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.quota_application_templates = quota_application_templates
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quota_application_templates:
            for k in self.quota_application_templates:
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
        result['QuotaApplicationTemplates'] = []
        if self.quota_application_templates is not None:
            for k in self.quota_application_templates:
                result['QuotaApplicationTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_application_templates = []
        if m.get('QuotaApplicationTemplates') is not None:
            for k in m.get('QuotaApplicationTemplates'):
                temp_model = ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates()
                self.quota_application_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaApplicationTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaApplicationTemplatesResponseBody = None,
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
            temp_model = ListQuotaApplicationTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaApplicationsRequestDimensions(TeaModel):
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


class ListQuotaApplicationsRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[ListQuotaApplicationsRequestDimensions] = None,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        status: str = None,
    ):
        self.dimensions = dimensions
        self.key_word = key_word
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_category = quota_category
        self.status = status

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListQuotaApplicationsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        self.period_unit = period_unit
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class ListQuotaApplicationsResponseBodyQuotaApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        comment: str = None,
        desire_value: float = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        period: ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        self.application_id = application_id
        self.apply_time = apply_time
        self.approve_value = approve_value
        self.audit_reason = audit_reason
        self.comment = comment
        self.desire_value = desire_value
        self.dimension = dimension
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.notice_type = notice_type
        self.period = period
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_arn = quota_arn
        self.quota_description = quota_description
        self.quota_name = quota_name
        self.quota_unit = quota_unit
        self.reason = reason
        self.status = status

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('Period') is not None:
            temp_model = ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_applications: List[ListQuotaApplicationsResponseBodyQuotaApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.quota_applications = quota_applications
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quota_applications:
            for k in self.quota_applications:
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
        result['QuotaApplications'] = []
        if self.quota_applications is not None:
            for k in self.quota_applications:
                result['QuotaApplications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_applications = []
        if m.get('QuotaApplications') is not None:
            for k in m.get('QuotaApplications'):
                temp_model = ListQuotaApplicationsResponseBodyQuotaApplications()
                self.quota_applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaApplicationsResponseBody = None,
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
            temp_model = ListQuotaApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyQuotaTemplateServiceStatusRequest(TeaModel):
    def __init__(
        self,
        service_status: int = None,
    ):
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ModifyQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        service_status: int = None,
    ):
        self.resource_directory_id = resource_directory_id
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ModifyQuotaTemplateServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_service_status: ModifyQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus = None,
    ):
        self.request_id = request_id
        self.template_service_status = template_service_status

    def validate(self):
        if self.template_service_status:
            self.template_service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_service_status is not None:
            result['TemplateServiceStatus'] = self.template_service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateServiceStatus') is not None:
            temp_model = ModifyQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus()
            self.template_service_status = temp_model.from_map(m['TemplateServiceStatus'])
        return self


class ModifyQuotaTemplateServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyQuotaTemplateServiceStatusResponseBody = None,
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
            temp_model = ModifyQuotaTemplateServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateQuotaItemRequestDimensions(TeaModel):
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


class ModifyTemplateQuotaItemRequest(TeaModel):
    def __init__(
        self,
        desire_value: float = None,
        dimensions: List[ModifyTemplateQuotaItemRequestDimensions] = None,
        env_language: str = None,
        id: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        self.desire_value = desire_value
        self.dimensions = dimensions
        self.env_language = env_language
        self.id = id
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.id is not None:
            result['Id'] = self.id
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ModifyTemplateQuotaItemRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class ModifyTemplateQuotaItemResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTemplateQuotaItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTemplateQuotaItemResponseBody = None,
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
            temp_model = ModifyTemplateQuotaItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_name = alarm_name
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.threshold_type = threshold_type
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        return self


class UpdateQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaAlarmResponseBody = None,
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
            temp_model = UpdateQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


