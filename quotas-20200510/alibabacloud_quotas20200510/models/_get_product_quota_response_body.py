# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetProductQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: main_models.GetProductQuotaResponseBodyQuota = None,
        request_id: str = None,
    ):
        # The quota details.
        self.quota = quota
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = main_models.GetProductQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProductQuotaResponseBodyQuota(DaraModel):
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
        period: main_models.GetProductQuotaResponseBodyQuotaPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_items: List[main_models.GetProductQuotaResponseBodyQuotaQuotaItems] = None,
        quota_name: str = None,
        quota_type: str = None,
        quota_unit: str = None,
        supported_range: List[float] = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
        usage_metric: main_models.GetProductQuotaResponseBodyQuotaUsageMetric = None,
    ):
        # Indicates whether the quota is adjustable. Valid values:
        # 
        # - true: Adjustable.
        # 
        # - false: Not adjustable.
        self.adjustable = adjustable
        # The applicable range for quota adjustment.
        self.applicable_range = applicable_range
        # The type of quota adjustment. Valid values:
        # 
        # - continuous: Continuous.
        # 
        # - discontinuous: Discontinuous.
        self.applicable_type = applicable_type
        # The sample reasons for applying for a quota adjustment.
        self.apply_reason_tips = apply_reason_tips
        # Indicates whether the used quota is displayed. Valid values:
        # 
        # - true: The used quota is displayed.
        # 
        # - false: The used quota is not displayed.
        self.consumable = consumable
        # The quota dimensions. Format: `{"regionId":"region"}`.
        self.dimensions = dimensions
        # The UTC time when the quota takes effect.
        self.effective_time = effective_time
        # The UTC time when the quota expires.
        self.expire_time = expire_time
        # Indicates whether the quota is a global quota. Valid values:
        # - true: The quota item is shared across all regions.
        # - false: The quota item is independent for each region.
        self.global_quota = global_quota
        # The quota period.
        self.period = period
        # The abbreviated name of the cloud service.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The ARN of the quota.
        self.quota_arn = quota_arn
        # The quota category. Valid values:
        # - CommonQuota: General quota.
        # 
        # - FlowControl: API rate limit.
        # 
        # - WhiteListLabel: Privilege.
        self.quota_category = quota_category
        # The quota description.
        self.quota_description = quota_description
        # The quota details.
        self.quota_items = quota_items
        # The quota name.
        self.quota_name = quota_name
        # The quota type. Valid values:
        # 
        # - privilege: Privilege.
        # 
        # - normal: Normal.
        self.quota_type = quota_type
        # The quota unit.
        # 
        # > The unit varies for each quota. For example, the unit of the q_cbdch3 quota (maximum number of clusters) for Container Service for Kubernetes is Cluster, and the unit of the q_security-groups quota (maximum number of security groups) for Elastic Compute Service servers is count.
        self.quota_unit = quota_unit
        # The supported range of quota values for the current quota item, which can be used as a reference when configuring a quota template.
        self.supported_range = supported_range
        # The quota value.
        self.total_quota = total_quota
        # The quota usage.
        self.total_usage = total_usage
        # The reason why the quota cannot be adjusted. Valid values:
        # 
        # - nonactivated: The service is not activated.
        # 
        # - applicationProcess: The quota application is being processed.
        # 
        # - limitReached: The quota limit is reached.
        # 
        # - supportTicketRequired: A ticket must be submitted for the application.
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
            temp_model = main_models.GetProductQuotaResponseBodyQuotaPeriod()
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
                temp_model = main_models.GetProductQuotaResponseBodyQuotaQuotaItems()
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
            temp_model = main_models.GetProductQuotaResponseBodyQuotaUsageMetric()
            self.usage_metric = temp_model.from_map(m.get('UsageMetric'))

        return self

class GetProductQuotaResponseBodyQuotaUsageMetric(DaraModel):
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
        # The CloudMonitor metric name.
        self.metric_name = metric_name
        # The CloudMonitor metric namespace.
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

class GetProductQuotaResponseBodyQuotaQuotaItems(DaraModel):
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
        # 
        # > The unit varies for each quota. For example, the unit of the q_cbdch3 quota (maximum number of clusters) for Container Service for Kubernetes is Cluster, and the unit of the q_security-groups quota (maximum number of security groups) for Elastic Compute Service servers is count.
        self.quota_unit = quota_unit
        # The quota item type. Valid values:
        # 
        # - BaseQuota: Base quota.
        # 
        # - ReservedQuota: Reserved quota.
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

class GetProductQuotaResponseBodyQuotaPeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the quota period. Valid values:
        # 
        # - second: Seconds.
        # 
        # - minute: Minutes.
        # 
        # - hour: Hours.
        # 
        # - day: Days.
        # 
        # - week: Weeks.
        self.period_unit = period_unit
        # The value of the quota period.
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

