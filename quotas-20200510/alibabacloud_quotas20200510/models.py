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
        product_code: str = None,
        quota_action_code: str = None,
        alarm_name: str = None,
        threshold: float = None,
        threshold_percent: float = None,
        web_hook: str = None,
        quota_dimensions: List[CreateQuotaAlarmRequestQuotaDimensions] = None,
    ):
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.alarm_name = alarm_name
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.web_hook = web_hook
        self.quota_dimensions = quota_dimensions

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = CreateQuotaAlarmRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
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
        body: CreateQuotaAlarmResponseBody = None,
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
        product_code: str = None,
        quota_action_code: str = None,
        desire_value: float = None,
        reason: str = None,
        notice_type: int = None,
        dimensions: List[CreateQuotaApplicationRequestDimensions] = None,
    ):
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.desire_value = desire_value
        self.reason = reason
        self.notice_type = notice_type
        self.dimensions = dimensions

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateQuotaApplicationRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        return self


class CreateQuotaApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        application_id: str = None,
    ):
        self.request_id = request_id
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class CreateQuotaApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateQuotaApplicationResponseBody = None,
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
            temp_model = CreateQuotaApplicationResponseBody()
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
        body: DeleteQuotaAlarmResponseBody = None,
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
            temp_model = DeleteQuotaAlarmResponseBody()
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
        product_code: str = None,
        quota_action_code: str = None,
        dimensions: List[GetProductQuotaRequestDimensions] = None,
    ):
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.dimensions = dimensions

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = GetProductQuotaRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        return self


class GetProductQuotaResponseBodyQuotaPeriod(TeaModel):
    def __init__(
        self,
        period_value: int = None,
        period_unit: str = None,
    ):
        self.period_value = period_value
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class GetProductQuotaResponseBodyQuotaQuotaItems(TeaModel):
    def __init__(
        self,
        type: str = None,
        quota: str = None,
        quota_unit: str = None,
        usage: str = None,
    ):
        self.type = type
        self.quota = quota
        self.quota_unit = quota_unit
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class GetProductQuotaResponseBodyQuota(TeaModel):
    def __init__(
        self,
        quota_unit: str = None,
        quota_action_code: str = None,
        total_usage: float = None,
        applicable_range: List[float] = None,
        quota_type: str = None,
        quota_description: str = None,
        period: GetProductQuotaResponseBodyQuotaPeriod = None,
        quota_arn: str = None,
        applicable_type: str = None,
        quota_items: List[GetProductQuotaResponseBodyQuotaQuotaItems] = None,
        dimensions: Dict[str, Any] = None,
        adjustable: bool = None,
        quota_name: str = None,
        unadjustable_detail: str = None,
        consumable: bool = None,
        total_quota: float = None,
        product_code: str = None,
    ):
        self.quota_unit = quota_unit
        self.quota_action_code = quota_action_code
        self.total_usage = total_usage
        self.applicable_range = applicable_range
        self.quota_type = quota_type
        self.quota_description = quota_description
        self.period = period
        self.quota_arn = quota_arn
        self.applicable_type = applicable_type
        self.quota_items = quota_items
        self.dimensions = dimensions
        self.adjustable = adjustable
        self.quota_name = quota_name
        self.unadjustable_detail = unadjustable_detail
        self.consumable = consumable
        self.total_quota = total_quota
        self.product_code = product_code

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for k in self.quota_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k in self.quota_items:
                result['QuotaItems'].append(k.to_map() if k else None)
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        if self.consumable is not None:
            result['Consumable'] = self.consumable
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('Period') is not None:
            temp_model = GetProductQuotaResponseBodyQuotaPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k in m.get('QuotaItems'):
                temp_model = GetProductQuotaResponseBodyQuotaQuotaItems()
                self.quota_items.append(temp_model.from_map(k))
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class GetProductQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        quota: GetProductQuotaResponseBodyQuota = None,
    ):
        self.request_id = request_id
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Quota') is not None:
            temp_model = GetProductQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m['Quota'])
        return self


class GetProductQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductQuotaResponseBody = None,
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
        product_code: str = None,
        dimension_key: str = None,
        dependent_dimensions: List[GetProductQuotaDimensionRequestDependentDimensions] = None,
    ):
        self.product_code = product_code
        self.dimension_key = dimension_key
        self.dependent_dimensions = dependent_dimensions

    def validate(self):
        if self.dependent_dimensions:
            for k in self.dependent_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        result['DependentDimensions'] = []
        if self.dependent_dimensions is not None:
            for k in self.dependent_dimensions:
                result['DependentDimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        self.dependent_dimensions = []
        if m.get('DependentDimensions') is not None:
            for k in m.get('DependentDimensions'):
                temp_model = GetProductQuotaDimensionRequestDependentDimensions()
                self.dependent_dimensions.append(temp_model.from_map(k))
        return self


class GetProductQuotaDimensionResponseBodyQuotaDimension(TeaModel):
    def __init__(
        self,
        dimension_key: str = None,
        dependent_dimensions: List[str] = None,
        dimension_values: List[str] = None,
        name: str = None,
    ):
        self.dimension_key = dimension_key
        self.dependent_dimensions = dependent_dimensions
        self.dimension_values = dimension_values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetProductQuotaDimensionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        quota_dimension: GetProductQuotaDimensionResponseBodyQuotaDimension = None,
    ):
        self.request_id = request_id
        self.quota_dimension = quota_dimension

    def validate(self):
        if self.quota_dimension:
            self.quota_dimension.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QuotaDimension') is not None:
            temp_model = GetProductQuotaDimensionResponseBodyQuotaDimension()
            self.quota_dimension = temp_model.from_map(m['QuotaDimension'])
        return self


class GetProductQuotaDimensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProductQuotaDimensionResponseBody = None,
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
        threshold_percent: float = None,
        quota_dimension: Dict[str, Any] = None,
        create_time: str = None,
        quota_action_code: str = None,
        alarm_name: str = None,
        notify_target: str = None,
        notify_channels: List[str] = None,
        quota_usage: float = None,
        quota_value: float = None,
        alarm_id: str = None,
        threshold: float = None,
        product_code: str = None,
    ):
        self.threshold_percent = threshold_percent
        self.quota_dimension = quota_dimension
        self.create_time = create_time
        self.quota_action_code = quota_action_code
        self.alarm_name = alarm_name
        self.notify_target = notify_target
        self.notify_channels = notify_channels
        self.quota_usage = quota_usage
        self.quota_value = quota_value
        self.alarm_id = alarm_id
        self.threshold = threshold
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('QuotaDimension') is not None:
            self.quota_dimension = m.get('QuotaDimension')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class GetQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        quota_alarm: GetQuotaAlarmResponseBodyQuotaAlarm = None,
    ):
        self.request_id = request_id
        self.quota_alarm = quota_alarm

    def validate(self):
        if self.quota_alarm:
            self.quota_alarm.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota_alarm is not None:
            result['QuotaAlarm'] = self.quota_alarm.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QuotaAlarm') is not None:
            temp_model = GetQuotaAlarmResponseBodyQuotaAlarm()
            self.quota_alarm = temp_model.from_map(m['QuotaAlarm'])
        return self


class GetQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQuotaAlarmResponseBody = None,
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
        status: str = None,
        desire_value: int = None,
        quota_action_code: str = None,
        quota_name: str = None,
        application_id: str = None,
        reason: str = None,
        audit_reason: str = None,
        quota_description: str = None,
        product_code: str = None,
        quota_arn: str = None,
        apply_time: str = None,
    ):
        self.status = status
        self.desire_value = desire_value
        self.quota_action_code = quota_action_code
        self.quota_name = quota_name
        self.application_id = application_id
        self.reason = reason
        self.audit_reason = audit_reason
        self.quota_description = quota_description
        self.product_code = product_code
        self.quota_arn = quota_arn
        self.apply_time = apply_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        return self


class GetQuotaApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        quota_application: GetQuotaApplicationResponseBodyQuotaApplication = None,
    ):
        self.request_id = request_id
        self.quota_application = quota_application

    def validate(self):
        if self.quota_application:
            self.quota_application.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota_application is not None:
            result['QuotaApplication'] = self.quota_application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QuotaApplication') is not None:
            temp_model = GetQuotaApplicationResponseBodyQuotaApplication()
            self.quota_application = temp_model.from_map(m['QuotaApplication'])
        return self


class GetQuotaApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQuotaApplicationResponseBody = None,
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
            temp_model = GetQuotaApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        keyword: str = None,
        start_time: int = None,
        end_time: int = None,
        product_code: str = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.keyword = keyword
        self.start_time = start_time
        self.end_time = end_time
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListAlarmHistoriesResponseBodyAlarmHistories(TeaModel):
    def __init__(
        self,
        quota_usage: float = None,
        threshold_percent: float = None,
        create_time: str = None,
        quota_action_code: str = None,
        alarm_name: str = None,
        notify_target: str = None,
        notify_channels: List[str] = None,
        threshold: float = None,
        product_code: str = None,
    ):
        self.quota_usage = quota_usage
        self.threshold_percent = threshold_percent
        self.create_time = create_time
        self.quota_action_code = quota_action_code
        self.alarm_name = alarm_name
        self.notify_target = notify_target
        self.notify_channels = notify_channels
        self.threshold = threshold
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        alarm_histories: List[ListAlarmHistoriesResponseBodyAlarmHistories] = None,
    ):
        self.total_count = total_count
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.alarm_histories = alarm_histories

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = ListAlarmHistoriesResponseBodyAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmHistoriesResponseBody = None,
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
        dimension_key: str = None,
        dependent_dimension: List[str] = None,
        dimension_values: List[str] = None,
    ):
        self.dimension_key = dimension_key
        self.dependent_dimension = dependent_dimension
        self.dimension_values = dimension_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dependent_dimension is not None:
            result['DependentDimension'] = self.dependent_dimension
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DependentDimension') is not None:
            self.dependent_dimension = m.get('DependentDimension')
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        return self


class ListDependentQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        quota_action_code: str = None,
        dimensions: List[ListDependentQuotasResponseBodyQuotasDimensions] = None,
        product_code: str = None,
        scale: float = None,
    ):
        self.quota_action_code = quota_action_code
        self.dimensions = dimensions
        self.product_code = product_code
        self.scale = scale

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scale is not None:
            result['Scale'] = self.scale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListDependentQuotasResponseBodyQuotasDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        return self


class ListDependentQuotasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        quotas: List[ListDependentQuotasResponseBodyQuotas] = None,
    ):
        self.request_id = request_id
        self.quotas = quotas

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListDependentQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        return self


class ListDependentQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDependentQuotasResponseBody = None,
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
            temp_model = ListDependentQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductQuotaDimensionsRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        product_code: str = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductQuotaDimensionsResponseBodyQuotaDimensions(TeaModel):
    def __init__(
        self,
        requisite: bool = None,
        dimension_key: str = None,
        dependent_dimensions: List[str] = None,
        dimension_values: List[str] = None,
        name: str = None,
    ):
        self.requisite = requisite
        self.dimension_key = dimension_key
        self.dependent_dimensions = dependent_dimensions
        self.dimension_values = dimension_values
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.requisite is not None:
            result['Requisite'] = self.requisite
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Requisite') is not None:
            self.requisite = m.get('Requisite')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListProductQuotaDimensionsResponseBody(TeaModel):
    def __init__(
        self,
        quota_dimensions: List[ListProductQuotaDimensionsResponseBodyQuotaDimensions] = None,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.quota_dimensions = quota_dimensions
        self.total_count = total_count
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = ListProductQuotaDimensionsResponseBodyQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListProductQuotaDimensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductQuotaDimensionsResponseBody = None,
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
        next_token: str = None,
        max_results: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        key_word: str = None,
        sort_field: str = None,
        sort_order: str = None,
        dimensions: List[ListProductQuotasRequestDimensions] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.key_word = key_word
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.dimensions = dimensions

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListProductQuotasRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        return self


class ListProductQuotasResponseBodyQuotasPeriod(TeaModel):
    def __init__(
        self,
        period_value: int = None,
        period_unit: str = None,
    ):
        self.period_value = period_value
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class ListProductQuotasResponseBodyQuotasQuotaItems(TeaModel):
    def __init__(
        self,
        type: str = None,
        quota: str = None,
        quota_unit: str = None,
        usage: str = None,
    ):
        self.type = type
        self.quota = quota
        self.quota_unit = quota_unit
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListProductQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        quota_unit: str = None,
        quota_action_code: str = None,
        total_usage: float = None,
        applicable_range: List[float] = None,
        quota_type: str = None,
        quota_description: str = None,
        period: ListProductQuotasResponseBodyQuotasPeriod = None,
        quota_arn: str = None,
        applicable_type: str = None,
        quota_items: List[ListProductQuotasResponseBodyQuotasQuotaItems] = None,
        dimensions: Dict[str, Any] = None,
        adjustable: bool = None,
        quota_name: str = None,
        unadjustable_detail: str = None,
        consumable: bool = None,
        total_quota: float = None,
        product_code: str = None,
    ):
        self.quota_unit = quota_unit
        self.quota_action_code = quota_action_code
        self.total_usage = total_usage
        self.applicable_range = applicable_range
        self.quota_type = quota_type
        self.quota_description = quota_description
        self.period = period
        self.quota_arn = quota_arn
        self.applicable_type = applicable_type
        self.quota_items = quota_items
        self.dimensions = dimensions
        self.adjustable = adjustable
        self.quota_name = quota_name
        self.unadjustable_detail = unadjustable_detail
        self.consumable = consumable
        self.total_quota = total_quota
        self.product_code = product_code

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for k in self.quota_items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k in self.quota_items:
                result['QuotaItems'].append(k.to_map() if k else None)
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        if self.consumable is not None:
            result['Consumable'] = self.consumable
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('Period') is not None:
            temp_model = ListProductQuotasResponseBodyQuotasPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k in m.get('QuotaItems'):
                temp_model = ListProductQuotasResponseBodyQuotasQuotaItems()
                self.quota_items.append(temp_model.from_map(k))
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductQuotasResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        quotas: List[ListProductQuotasResponseBodyQuotas] = None,
        max_results: int = None,
    ):
        self.total_count = total_count
        self.next_token = next_token
        self.request_id = request_id
        self.quotas = quotas
        self.max_results = max_results

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListProductQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListProductQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductQuotasResponseBody = None,
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
            temp_model = ListProductQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListProductsResponseBodyProductInfo(TeaModel):
    def __init__(
        self,
        product_name: str = None,
        second_category_id: int = None,
        product_name_en: str = None,
        dynamic: bool = None,
        second_category_name_en: str = None,
        second_category_name: str = None,
        product_code: str = None,
    ):
        self.product_name = product_name
        self.second_category_id = second_category_id
        self.product_name_en = product_name_en
        self.dynamic = dynamic
        self.second_category_name_en = second_category_name_en
        self.second_category_name = second_category_name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.second_category_id is not None:
            result['SecondCategoryId'] = self.second_category_id
        if self.product_name_en is not None:
            result['ProductNameEn'] = self.product_name_en
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.second_category_name_en is not None:
            result['SecondCategoryNameEn'] = self.second_category_name_en
        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SecondCategoryId') is not None:
            self.second_category_id = m.get('SecondCategoryId')
        if m.get('ProductNameEn') is not None:
            self.product_name_en = m.get('ProductNameEn')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('SecondCategoryNameEn') is not None:
            self.second_category_name_en = m.get('SecondCategoryNameEn')
        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        product_info: List[ListProductsResponseBodyProductInfo] = None,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.product_info = product_info
        self.total_count = total_count
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.product_info:
            for k in self.product_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ProductInfo'] = []
        if self.product_info is not None:
            for k in self.product_info:
                result['ProductInfo'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_info = []
        if m.get('ProductInfo') is not None:
            for k in m.get('ProductInfo'):
                temp_model = ListProductsResponseBodyProductInfo()
                self.product_info.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProductsResponseBody = None,
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
        next_token: str = None,
        max_results: int = None,
        product_code: str = None,
        alarm_name: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[ListQuotaAlarmsRequestQuotaDimensions] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.product_code = product_code
        self.alarm_name = alarm_name
        self.quota_action_code = quota_action_code
        self.quota_dimensions = quota_dimensions

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
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
        threshold_percent: float = None,
        quota_dimensions: Dict[str, Any] = None,
        create_time: str = None,
        quota_action_code: str = None,
        alarm_name: str = None,
        notify_target: str = None,
        notify_channels: List[str] = None,
        quota_usage: float = None,
        quota_value: float = None,
        alarm_id: str = None,
        threshold: float = None,
        product_code: str = None,
        web_hook: str = None,
        exceed_threshold: bool = None,
    ):
        self.threshold_percent = threshold_percent
        self.quota_dimensions = quota_dimensions
        self.create_time = create_time
        self.quota_action_code = quota_action_code
        self.alarm_name = alarm_name
        self.notify_target = notify_target
        self.notify_channels = notify_channels
        self.quota_usage = quota_usage
        self.quota_value = quota_value
        self.alarm_id = alarm_id
        self.threshold = threshold
        self.product_code = product_code
        self.web_hook = web_hook
        self.exceed_threshold = exceed_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.quota_dimensions is not None:
            result['QuotaDimensions'] = self.quota_dimensions
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        if self.exceed_threshold is not None:
            result['ExceedThreshold'] = self.exceed_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('QuotaDimensions') is not None:
            self.quota_dimensions = m.get('QuotaDimensions')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        if m.get('ExceedThreshold') is not None:
            self.exceed_threshold = m.get('ExceedThreshold')
        return self


class ListQuotaAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        quota_alarms: List[ListQuotaAlarmsResponseBodyQuotaAlarms] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.total_count = total_count
        self.quota_alarms = quota_alarms
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.quota_alarms:
            for k in self.quota_alarms:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['QuotaAlarms'] = []
        if self.quota_alarms is not None:
            for k in self.quota_alarms:
                result['QuotaAlarms'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.quota_alarms = []
        if m.get('QuotaAlarms') is not None:
            for k in m.get('QuotaAlarms'):
                temp_model = ListQuotaAlarmsResponseBodyQuotaAlarms()
                self.quota_alarms.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListQuotaAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQuotaAlarmsResponseBody = None,
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
            temp_model = ListQuotaAlarmsResponseBody()
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
        next_token: str = None,
        max_results: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        status: str = None,
        key_word: str = None,
        dimensions: List[ListQuotaApplicationsRequestDimensions] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.status = status
        self.key_word = key_word
        self.dimensions = dimensions

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.status is not None:
            result['Status'] = self.status
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListQuotaApplicationsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        return self


class ListQuotaApplicationsResponseBodyQuotaApplications(TeaModel):
    def __init__(
        self,
        status: str = None,
        comment: str = None,
        expire_time: str = None,
        quota_unit: str = None,
        desire_value: float = None,
        notice_type: int = None,
        quota_action_code: str = None,
        dimension: Dict[str, Any] = None,
        quota_description: str = None,
        quota_arn: str = None,
        effective_time: str = None,
        approve_value: float = None,
        quota_name: str = None,
        application_id: str = None,
        audit_reason: str = None,
        reason: str = None,
        apply_time: str = None,
        product_code: str = None,
    ):
        self.status = status
        self.comment = comment
        self.expire_time = expire_time
        self.quota_unit = quota_unit
        self.desire_value = desire_value
        self.notice_type = notice_type
        self.quota_action_code = quota_action_code
        self.dimension = dimension
        self.quota_description = quota_description
        self.quota_arn = quota_arn
        self.effective_time = effective_time
        self.approve_value = approve_value
        self.quota_name = quota_name
        self.application_id = application_id
        self.audit_reason = audit_reason
        self.reason = reason
        self.apply_time = apply_time
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListQuotaApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        quota_applications: List[ListQuotaApplicationsResponseBodyQuotaApplications] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.total_count = total_count
        self.quota_applications = quota_applications
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.quota_applications:
            for k in self.quota_applications:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['QuotaApplications'] = []
        if self.quota_applications is not None:
            for k in self.quota_applications:
                result['QuotaApplications'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.quota_applications = []
        if m.get('QuotaApplications') is not None:
            for k in m.get('QuotaApplications'):
                temp_model = ListQuotaApplicationsResponseBodyQuotaApplications()
                self.quota_applications.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListQuotaApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQuotaApplicationsResponseBody = None,
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
            temp_model = ListQuotaApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        threshold: float = None,
        threshold_percent: float = None,
        web_hook: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_name = alarm_name
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
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
        body: UpdateQuotaAlarmResponseBody = None,
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
            temp_model = UpdateQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


