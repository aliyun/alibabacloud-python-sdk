# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaUtilizationReportResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        generated_at: str = None,
        message: str = None,
        next_token: str = None,
        quotas: List[main_models.ListQuotaUtilizationReportResponseBodyQuotas] = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.generated_at = generated_at
        self.message = message
        self.next_token = next_token
        self.quotas = quotas
        self.request_id = request_id
        self.status = status
        self.success = success
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.generated_at is not None:
            result['GeneratedAt'] = self.generated_at

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GeneratedAt') is not None:
            self.generated_at = m.get('GeneratedAt')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListQuotaUtilizationReportResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotaUtilizationReportResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        adjustable: bool = None,
        consumable: bool = None,
        dimensions: Dict[str, str] = None,
        flow_control_algo: main_models.ListQuotaUtilizationReportResponseBodyQuotasFlowControlAlgo = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_name: str = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
        usage_metric: main_models.ListQuotaUtilizationReportResponseBodyQuotasUsageMetric = None,
        utilization: float = None,
        utilization_status: str = None,
    ):
        self.adjustable = adjustable
        self.consumable = consumable
        self.dimensions = dimensions
        self.flow_control_algo = flow_control_algo
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_arn = quota_arn
        self.quota_category = quota_category
        self.quota_description = quota_description
        self.quota_name = quota_name
        self.total_quota = total_quota
        self.total_usage = total_usage
        self.unadjustable_detail = unadjustable_detail
        self.usage_metric = usage_metric
        self.utilization = utilization
        self.utilization_status = utilization_status

    def validate(self):
        if self.flow_control_algo:
            self.flow_control_algo.validate()
        if self.usage_metric:
            self.usage_metric.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable

        if self.consumable is not None:
            result['Consumable'] = self.consumable

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.flow_control_algo is not None:
            result['FlowControlAlgo'] = self.flow_control_algo.to_map()

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

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage

        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail

        if self.usage_metric is not None:
            result['UsageMetric'] = self.usage_metric.to_map()

        if self.utilization is not None:
            result['Utilization'] = self.utilization

        if self.utilization_status is not None:
            result['UtilizationStatus'] = self.utilization_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')

        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('FlowControlAlgo') is not None:
            temp_model = main_models.ListQuotaUtilizationReportResponseBodyQuotasFlowControlAlgo()
            self.flow_control_algo = temp_model.from_map(m.get('FlowControlAlgo'))

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

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')

        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')

        if m.get('UsageMetric') is not None:
            temp_model = main_models.ListQuotaUtilizationReportResponseBodyQuotasUsageMetric()
            self.usage_metric = temp_model.from_map(m.get('UsageMetric'))

        if m.get('Utilization') is not None:
            self.utilization = m.get('Utilization')

        if m.get('UtilizationStatus') is not None:
            self.utilization_status = m.get('UtilizationStatus')

        return self

class ListQuotaUtilizationReportResponseBodyQuotasUsageMetric(DaraModel):
    def __init__(
        self,
        metric_dimensions: Dict[str, str] = None,
        metric_name: str = None,
        metric_namespace: str = None,
    ):
        self.metric_dimensions = metric_dimensions
        self.metric_name = metric_name
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

class ListQuotaUtilizationReportResponseBodyQuotasFlowControlAlgo(DaraModel):
    def __init__(
        self,
        algo_type: str = None,
        period: main_models.ListQuotaUtilizationReportResponseBodyQuotasFlowControlAlgoPeriod = None,
        refill_interval: int = None,
        tokens_per_refill: int = None,
        total_quota: float = None,
    ):
        self.algo_type = algo_type
        self.period = period
        self.refill_interval = refill_interval
        self.tokens_per_refill = tokens_per_refill
        self.total_quota = total_quota

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algo_type is not None:
            result['AlgoType'] = self.algo_type

        if self.period is not None:
            result['Period'] = self.period.to_map()

        if self.refill_interval is not None:
            result['RefillInterval'] = self.refill_interval

        if self.tokens_per_refill is not None:
            result['TokensPerRefill'] = self.tokens_per_refill

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgoType') is not None:
            self.algo_type = m.get('AlgoType')

        if m.get('Period') is not None:
            temp_model = main_models.ListQuotaUtilizationReportResponseBodyQuotasFlowControlAlgoPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        if m.get('RefillInterval') is not None:
            self.refill_interval = m.get('RefillInterval')

        if m.get('TokensPerRefill') is not None:
            self.tokens_per_refill = m.get('TokensPerRefill')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        return self

class ListQuotaUtilizationReportResponseBodyQuotasFlowControlAlgoPeriod(DaraModel):
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

