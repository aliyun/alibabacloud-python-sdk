# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListProductQuotasResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quotas: List[main_models.ListProductQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the current query.
        self.max_results = max_results
        # Indicates whether a token for the next query is available.
        # 
        # - If NextToken is empty, it indicates that no subsequent query is available.
        # - If NextToken is returned, the value is the token used to start the next query.
        self.next_token = next_token
        # The quota details.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id
        # The total number of records returned for the current request.
        self.total_count = total_count

    def validate(self):
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListProductQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProductQuotasResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        adjustable: bool = None,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        apply_reason_tips: str = None,
        consumable: bool = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        global_quota: bool = None,
        period: main_models.ListProductQuotasResponseBodyQuotasPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_items: List[main_models.ListProductQuotasResponseBodyQuotasQuotaItems] = None,
        quota_name: str = None,
        quota_type: str = None,
        quota_unit: str = None,
        supported_range: List[float] = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
        usage_metric: main_models.ListProductQuotasResponseBodyQuotasUsageMetric = None,
    ):
        # Indicates whether the quota is adjustable.
        self.adjustable = adjustable
        # The range of quota values that can be applied for the current quota item, which serves as a reference for quota applications.
        self.applicable_range = applicable_range
        # The quota adjustment type.
        self.applicable_type = applicable_type
        # The sample reasons for applying for a quota adjustment.
        self.apply_reason_tips = apply_reason_tips
        # Indicates whether the used quota is displayed.
        self.consumable = consumable
        # The quota dimensions. Format: `{"regionId":"region"}`.
        self.dimensions = dimensions
        # The UTC time when the quota takes effect.
        self.effective_time = effective_time
        # The UTC time when the quota expires.
        self.expire_time = expire_time
        # Indicates whether the quota is a global quota.
        self.global_quota = global_quota
        # The quota calculation period.
        self.period = period
        # The abbreviation of the cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The ARN of the quota.
        self.quota_arn = quota_arn
        # The quota type.
        self.quota_category = quota_category
        # The quota description.
        self.quota_description = quota_description
        # The quota details.
        self.quota_items = quota_items
        # The quota name.
        self.quota_name = quota_name
        # The quota type.
        self.quota_type = quota_type
        # The quota unit.
        self.quota_unit = quota_unit
        # The range of quota values supported by the current quota item, which serves as a reference when you configure a quota template.
        self.supported_range = supported_range
        # The quota value.
        self.total_quota = total_quota
        # The quota usage.
        self.total_usage = total_usage
        # The reason why the quota is not adjustable.
        self.unadjustable_detail = unadjustable_detail
        # The monitoring information of the quota usage in CloudMonitor.
        # 
        # > An empty value indicates that no monitoring data is available for this quota in CloudMonitor.
        self.usage_metric = usage_metric

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for v1 in self.quota_items:
                 if v1:
                    v1.validate()
        if self.usage_metric:
            self.usage_metric.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable

        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range

        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type

        if self.apply_reason_tips is not None:
            result['ApplyReasonTips'] = self.apply_reason_tips

        if self.consumable is not None:
            result['Consumable'] = self.consumable

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.global_quota is not None:
            result['GlobalQuota'] = self.global_quota

        if self.period is not None:
            result['Period'] = self.period.to_map()

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description

        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k1 in self.quota_items:
                result['QuotaItems'].append(k1.to_map() if k1 else None)

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit

        if self.supported_range is not None:
            result['SupportedRange'] = self.supported_range

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage

        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail

        if self.usage_metric is not None:
            result['UsageMetric'] = self.usage_metric.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')

        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')

        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')

        if m.get('ApplyReasonTips') is not None:
            self.apply_reason_tips = m.get('ApplyReasonTips')

        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GlobalQuota') is not None:
            self.global_quota = m.get('GlobalQuota')

        if m.get('Period') is not None:
            temp_model = main_models.ListProductQuotasResponseBodyQuotasPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')

        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k1 in m.get('QuotaItems'):
                temp_model = main_models.ListProductQuotasResponseBodyQuotasQuotaItems()
                self.quota_items.append(temp_model.from_map(k1))

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')

        if m.get('SupportedRange') is not None:
            self.supported_range = m.get('SupportedRange')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')

        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')

        if m.get('UsageMetric') is not None:
            temp_model = main_models.ListProductQuotasResponseBodyQuotasUsageMetric()
            self.usage_metric = temp_model.from_map(m.get('UsageMetric'))

        return self

class ListProductQuotasResponseBodyQuotasUsageMetric(DaraModel):
    def __init__(
        self,
        metric_dimensions: Dict[str, str] = None,
        metric_name: str = None,
        metric_namespace: str = None,
    ):
        # The CloudMonitor monitoring dimensions.
        # 
        # Format: a collection of `key:value` pairs. Example:
        # `{"productCode":"***","metricKey":"***","regionId":"***","label":"***"}`.
        self.metric_dimensions = metric_dimensions
        # The name of the CloudMonitor monitoring metric.
        self.metric_name = metric_name
        # The namespace of the CloudMonitor monitoring data.
        self.metric_namespace = metric_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_dimensions is not None:
            result['MetricDimensions'] = self.metric_dimensions

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_namespace is not None:
            result['MetricNamespace'] = self.metric_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricDimensions') is not None:
            self.metric_dimensions = m.get('MetricDimensions')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricNamespace') is not None:
            self.metric_namespace = m.get('MetricNamespace')

        return self

class ListProductQuotasResponseBodyQuotasQuotaItems(DaraModel):
    def __init__(
        self,
        quota: str = None,
        quota_unit: str = None,
        type: str = None,
        usage: str = None,
    ):
        # The quota value.
        self.quota = quota
        # The quota unit.
        self.quota_unit = quota_unit
        # The quota category.
        self.type = type
        # The quota usage.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListProductQuotasResponseBodyQuotasPeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the quota calculation period.
        self.period_unit = period_unit
        # The value of the quota calculation period.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

