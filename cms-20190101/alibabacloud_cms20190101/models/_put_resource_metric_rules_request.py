# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutResourceMetricRulesRequest(DaraModel):
    def __init__(
        self,
        rules: List[main_models.PutResourceMetricRulesRequestRules] = None,
    ):
        # The list of threshold alert rules.
        # 
        # Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.PutResourceMetricRulesRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class PutResourceMetricRulesRequestRules(DaraModel):
    def __init__(
        self,
        escalations: main_models.PutResourceMetricRulesRequestRulesEscalations = None,
        contact_groups: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        interval: str = None,
        labels: List[main_models.PutResourceMetricRulesRequestRulesLabels] = None,
        metric_name: str = None,
        namespace: str = None,
        no_data_policy: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        send_ok: bool = None,
        silence_time: int = None,
        webhook: str = None,
    ):
        self.escalations = escalations
        # 报警联系组。报警通知会发送给该报警联系组中的报警联系人。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警联系组是一组报警联系人，可以包含一个或多个报警联系人。关于如何创建报警联系人和报警联系组，请参见[PutContact](https://help.aliyun.com/document_detail/114923.html)和[PutContactGroup](https://help.aliyun.com/document_detail/114929.html)。
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # 报警规则的生效时间范围。
        # 
        # N的取值范围：1~50。
        self.effective_interval = effective_interval
        # 报警邮件主题。
        # 
        # N的取值范围：1~50。
        self.email_subject = email_subject
        # 报警规则的触发周期。
        # 
        # 单位：秒。
        # 
        # N的取值范围：1~50。
        # 
        # >关于如何查询监控项的统计周期，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        self.interval = interval
        # 当监控项达到报警条件并进行报警时，标签同时写入监控项，在报警通知中进行展示。
        self.labels = labels
        # 监控项名称。
        # 
        # N的取值范围：1~50。
        # 
        # 关于如何查询监控项名称，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        self.metric_name = metric_name
        # 云产品的数据命名空间。
        # 
        # N的取值范围：1~50。
        # 
        # 关于如何查询云产品的数据命名空间，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # This parameter is required.
        self.namespace = namespace
        # 无监控数据时报警的处理方式。取值：
        # 
        # - KEEP_LAST_STATE（默认值）：不做任何处理。
        # - INSUFFICIENT_DATA：报警内容为无数据。
        # - OK：正常。
        # 
        # N的取值范围：1~50。
        self.no_data_policy = no_data_policy
        # 报警规则的失效时间范围。
        # 
        # N的取值范围：1~50。
        self.no_effective_interval = no_effective_interval
        # 监控项的统计周期。
        # 
        # 单位：秒。默认为监控项的原始上报周期。
        # 
        # N的取值范围：1~50。
        # 
        # >关于如何查询监控项的统计周期，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        self.period = period
        # 资源信息，例如：`[{"instanceId":"i-uf6j91r34rnwawoo****"}]`、`[{"userId":"100931896542****"}]`。
        # 
        # N的取值范围：1~50。
        # 
        # 关于资源信息支持的维度Dimensions，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # This parameter is required.
        self.resources = resources
        # 报警规则ID。
        # 
        # N的取值范围：1~50。
        # 
        # 您可以输入新的报警规则ID，也可以使用云监控已存在的报警规则ID。关于如何查询报警规则ID，请参见[DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html)。
        # 
        # > 输入新的报警规则ID，表示创建一条阈值报警规则。
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # 报警规则名称。
        # 
        # N的取值范围：1~50。
        # 
        # 您可以输入新的报警规则名称，也可以使用云监控已存在的报警规则名称。关于如何查询报警规则名称，请参见[DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html)。
        # 
        # > 输入新的报警规则名称，表示创建一条阈值报警规则。
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # 是否发送恢复通知
        self.send_ok = send_ok
        # 通道沉默周期。
        # 
        # 单位：秒，默认值：86400。
        # 
        # N的取值范围：1~50。
        # 
        # > 通道沉默周期是指报警发生后未恢复正常，间隔多久重新发送一次报警通知。
        self.silence_time = silence_time
        # 报警发生回调时指定的URL地址，向URL发送POST请求。
        # 
        # N的取值范围：1~50。
        self.webhook = webhook

    def validate(self):
        if self.escalations:
            self.escalations.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.escalations is not None:
            result['Escalations'] = self.escalations.to_map()

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.email_subject is not None:
            result['EmailSubject'] = self.email_subject

        if self.interval is not None:
            result['Interval'] = self.interval

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.no_data_policy is not None:
            result['NoDataPolicy'] = self.no_data_policy

        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval

        if self.period is not None:
            result['Period'] = self.period

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.send_ok is not None:
            result['SendOK'] = self.send_ok

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Escalations') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalations()
            self.escalations = temp_model.from_map(m.get('Escalations'))

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.PutResourceMetricRulesRequestRulesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoDataPolicy') is not None:
            self.no_data_policy = m.get('NoDataPolicy')

        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SendOK') is not None:
            self.send_ok = m.get('SendOK')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class PutResourceMetricRulesRequestRulesLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键。
        self.key = key
        # 标签值。
        # 
        # > 标签值支持模板参数，将模板参数替换为实际标签值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class PutResourceMetricRulesRequestRulesEscalations(DaraModel):
    def __init__(
        self,
        critical: main_models.PutResourceMetricRulesRequestRulesEscalationsCritical = None,
        info: main_models.PutResourceMetricRulesRequestRulesEscalationsInfo = None,
        warn: main_models.PutResourceMetricRulesRequestRulesEscalationsWarn = None,
    ):
        self.critical = critical
        self.info = info
        self.warn = warn

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.info:
            self.info.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()

        if self.info is not None:
            result['Info'] = self.info.to_map()

        if self.warn is not None:
            result['Warn'] = self.warn.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalationsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Info') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalationsInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Warn') is not None:
            temp_model = main_models.PutResourceMetricRulesRequestRulesEscalationsWarn()
            self.warn = temp_model.from_map(m.get('Warn'))

        return self

class PutResourceMetricRulesRequestRulesEscalationsWarn(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # Warn级别阈值比较符。取值：
        # 
        # - GreaterThanOrEqualToThreshold：大于等于。
        # - GreaterThanThreshold：大于。
        # - LessThanOrEqualToThreshold：小于等于。
        # - LessThanThreshold：小于。
        # - NotEqualToThreshold：不等于。
        # - EqualToThreshold：等于。
        # - GreaterThanYesterday：同比昨天时间上涨。
        # - LessThanYesterday：同比昨天时间下降。
        # - GreaterThanLastWeek：同比上周同一时间上涨。
        # - LessThanLastWeek：同比上周同一时间下降。
        # - GreaterThanLastPeriod：环比上周期上涨。
        # - LessThanLastPeriod：环比上周期下降。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # Warn级别报警统计方法。
        # 
        # N的取值范围：1~50。
        # 
        # 该参数的取值由指定云产品的`MetricName`对应的`Statistics`列决定，例如：Maximum、Minimum和Average。关于如何获取该参数的取值，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.statistics = statistics
        # Warn级别报警阈值。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.threshold = threshold
        # Warn级别报警重试次数。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.n is not None:
            result['N'] = self.n

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class PutResourceMetricRulesRequestRulesEscalationsInfo(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # Info级别阈值比较符。取值：
        # 
        # - GreaterThanOrEqualToThreshold：大于等于。
        # - GreaterThanThreshold：大于。
        # - LessThanOrEqualToThreshold：小于等于。
        # - LessThanThreshold：小于。
        # - NotEqualToThreshold：不等于。
        # - EqualToThreshold：等于。
        # - GreaterThanYesterday：同比昨天时间上涨。
        # - LessThanYesterday：同比昨天时间下降。
        # - GreaterThanLastWeek：同比上周同一时间上涨。
        # - LessThanLastWeek：同比上周同一时间下降。
        # - GreaterThanLastPeriod：环比上周期上涨。
        # - LessThanLastPeriod：环比上周期下降。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # Info级别报警统计方法。
        # 
        # N的取值范围：1~50。
        # 
        # 该参数的取值由指定云产品的`MetricName`对应的`Statistics`列决定，例如：Maximum、Minimum和Average。关于如何获取该参数的取值，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.statistics = statistics
        # Info级别报警阈值。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.threshold = threshold
        # Info级别报警重试次数。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.n is not None:
            result['N'] = self.n

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class PutResourceMetricRulesRequestRulesEscalationsCritical(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        n: int = None,
        pre_condition: str = None,
        statistics: str = None,
        threshold: str = None,
        times: int = None,
    ):
        # Critical级别阈值比较符。取值：
        # 
        # - GreaterThanOrEqualToThreshold：大于等于。
        # - GreaterThanThreshold：大于。
        # - LessThanOrEqualToThreshold：小于等于。
        # - LessThanThreshold：小于。
        # - NotEqualToThreshold：不等于。
        # - EqualToThreshold：等于。
        # - GreaterThanYesterday：同比昨天时间上涨。
        # - LessThanYesterday：同比昨天时间下降。
        # - GreaterThanLastWeek：同比上周同一时间上涨。
        # - LessThanLastWeek：同比上周同一时间下降。
        # - GreaterThanLastPeriod：环比上周期上涨。
        # - LessThanLastPeriod：环比上周期下降。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.comparison_operator = comparison_operator
        self.n = n
        self.pre_condition = pre_condition
        # Critical级别报警统计方法。
        # 
        # N的取值范围：1~50。
        # 
        # 该参数的取值由指定云产品的`MetricName`对应的`Statistics`列决定，例如：Maximum、Minimum和Average。关于如何获取该参数的取值，请参见[云产品监控项](https://help.aliyun.com/document_detail/163515.html)。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.statistics = statistics
        # Critical级别报警阈值。
        # 
        # N的取值范围：1~50。
        # 
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.threshold = threshold
        # Critical级别报警重试次数。
        # 
        # N的取值范围：1~50。
        # 
        # > 报警级别Critical（严重）、Warn（警告）或Info（信息）至少设置一个，且该报警级别中的参数Statistics、ComparisonOperator、Threshold和Times必须同时设置。
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.n is not None:
            result['N'] = self.n

        if self.pre_condition is not None:
            result['PreCondition'] = self.pre_condition

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PreCondition') is not None:
            self.pre_condition = m.get('PreCondition')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

