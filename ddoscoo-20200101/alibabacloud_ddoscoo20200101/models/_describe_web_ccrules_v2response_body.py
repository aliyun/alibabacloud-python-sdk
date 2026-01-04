# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebCCRulesV2ResponseBody(DaraModel):
    def __init__(
        self,
        domain: str = None,
        request_id: str = None,
        total_count: str = None,
        web_ccrules: List[main_models.DescribeWebCCRulesV2ResponseBodyWebCCRules] = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The request ID.
        self.request_id = request_id
        # The total number of returned custom frequency control rules.
        self.total_count = total_count
        # The custom frequency control rules.
        self.web_ccrules = web_ccrules

    def validate(self):
        if self.web_ccrules:
            for v1 in self.web_ccrules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WebCCRules'] = []
        if self.web_ccrules is not None:
            for k1 in self.web_ccrules:
                result['WebCCRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.web_ccrules = []
        if m.get('WebCCRules') is not None:
            for k1 in m.get('WebCCRules'):
                temp_model = main_models.DescribeWebCCRulesV2ResponseBodyWebCCRules()
                self.web_ccrules.append(temp_model.from_map(k1))

        return self

class DescribeWebCCRulesV2ResponseBodyWebCCRules(DaraModel):
    def __init__(
        self,
        expires: int = None,
        name: str = None,
        owner: str = None,
        rule_detail: main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetail = None,
    ):
        # The validity period of the rule. Unit: seconds. If the Action parameter is set to block, the system blocks the requests that match the rule within the validity period of the rule. The value 0 indicates that the rule is permanently valid.
        self.expires = expires
        # The name of the rule.
        self.name = name
        # The method used to create the rule. Valid values:
        # 
        # *   **manual** (default): manually created.
        # *   **clover**: automatically created.
        self.owner = owner
        # The details of the rule.
        self.rule_detail = rule_detail

    def validate(self):
        if self.rule_detail:
            self.rule_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires is not None:
            result['Expires'] = self.expires

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.rule_detail is not None:
            result['RuleDetail'] = self.rule_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RuleDetail') is not None:
            temp_model = main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetail()
            self.rule_detail = temp_model.from_map(m.get('RuleDetail'))

        return self

class DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetail(DaraModel):
    def __init__(
        self,
        action: str = None,
        condition: List[main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailCondition] = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        rate_limit: main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailRateLimit = None,
        statistics: main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailStatistics = None,
        status_code: main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailStatusCode = None,
        ttl: int = None,
        uri: str = None,
    ):
        # The action triggered if the rule is matched. Valid values:
        # 
        # *   **accept**: The requests that match the rule are allowed.
        # *   **block**: The requests that match the rule are blocked.
        # *   **challenge**: Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA) verification for the requests that match the rule is implemented.
        # *   **watch**: The requests that match the rule are recorded in logs and allowed.
        self.action = action
        # The match conditions.
        self.condition = condition
        # The parameter is deprecated.
        self.count = count
        # The parameter is deprecated.
        self.interval = interval
        # The parameter is deprecated.
        self.mode = mode
        # The name of the rule.
        self.name = name
        # The frequency statistics.
        self.rate_limit = rate_limit
        # The statistics after deduplication. By default, the system collects statistics before deduplication.
        self.statistics = statistics
        # The status codes.
        self.status_code = status_code
        # The parameter is deprecated.
        self.ttl = ttl
        # The parameter is deprecated.
        self.uri = uri

    def validate(self):
        if self.condition:
            for v1 in self.condition:
                 if v1:
                    v1.validate()
        if self.rate_limit:
            self.rate_limit.validate()
        if self.statistics:
            self.statistics.validate()
        if self.status_code:
            self.status_code.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Condition'] = []
        if self.condition is not None:
            for k1 in self.condition:
                result['Condition'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit.to_map()

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code.to_map()

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.condition = []
        if m.get('Condition') is not None:
            for k1 in m.get('Condition'):
                temp_model = main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailCondition()
                self.condition.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RateLimit') is not None:
            temp_model = main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailRateLimit()
            self.rate_limit = temp_model.from_map(m.get('RateLimit'))

        if m.get('Statistics') is not None:
            temp_model = main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('StatusCode') is not None:
            temp_model = main_models.DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailStatusCode()
            self.status_code = temp_model.from_map(m.get('StatusCode'))

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailStatusCode(DaraModel):
    def __init__(
        self,
        code: int = None,
        count_threshold: int = None,
        enabled: bool = None,
        ratio_threshold: int = None,
        use_ratio: bool = None,
    ):
        # The status code. Valid values: **100** to **599**.
        # 
        # *   **200**: The request was successful.
        # *   Other codes: The request failed.
        self.code = code
        # If a ratio is not used, the handling action is triggered only when the number of requests of the corresponding status code reaches the value of **CountThreshold**. Valid values: **2** to **50000**.
        self.count_threshold = count_threshold
        # Indicates whether the status code is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # If a ratio is used, the handling action is triggered only when the number of requests of the corresponding status code reaches the value of **RatioThreshold**. Valid values: **1** to **100**.
        self.ratio_threshold = ratio_threshold
        # Indicates whether to use a ratio.
        # 
        # *   **true**
        # *   **false**
        self.use_ratio = use_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count_threshold is not None:
            result['CountThreshold'] = self.count_threshold

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.use_ratio is not None:
            result['UseRatio'] = self.use_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CountThreshold') is not None:
            self.count_threshold = m.get('CountThreshold')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('UseRatio') is not None:
            self.use_ratio = m.get('UseRatio')

        return self

class DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailStatistics(DaraModel):
    def __init__(
        self,
        field: str = None,
        header_name: str = None,
        mode: str = None,
    ):
        # The statistical method. Valid values:
        # 
        # *   **ip**
        # *   **header**
        # *   **uri**
        self.field = field
        # The name of the header. This parameter is required only when the Field parameter is set to header.
        self.header_name = header_name
        # Indicates whether the system collects statistics after deduplication. Valid values:
        # 
        # *   **count**: The system collects statistics before deduplication.
        # *   **distinct**: The system collects statistics after deduplication.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.header_name is not None:
            result['HeaderName'] = self.header_name

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailRateLimit(DaraModel):
    def __init__(
        self,
        interval: int = None,
        sub_key: str = None,
        target: str = None,
        threshold: int = None,
        ttl: int = None,
    ):
        # The statistical period. Unit: seconds.
        self.interval = interval
        # The name of the field. This parameter is required only when the Target parameter is set to header.
        self.sub_key = sub_key
        # The statistical method. Valid values:
        # 
        # *   **ip**
        # *   **header**
        self.target = target
        # The trigger threshold.
        self.threshold = threshold
        # The blocking duration. Unit: seconds.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.sub_key is not None:
            result['SubKey'] = self.sub_key

        if self.target is not None:
            result['Target'] = self.target

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('SubKey') is not None:
            self.sub_key = m.get('SubKey')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class DescribeWebCCRulesV2ResponseBodyWebCCRulesRuleDetailCondition(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_list: str = None,
        field: str = None,
        header_name: str = None,
        match_method: str = None,
    ):
        # The match content.
        self.content = content
        # The match content when the match method is Equals to One of Multiple Values.
        self.content_list = content_list
        # The match field.
        self.field = field
        # The custom HTTP request header.
        # 
        # >  This parameter takes effect only when **Field** is set to **header**.
        self.header_name = header_name
        # The match method.
        self.match_method = match_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_list is not None:
            result['ContentList'] = self.content_list

        if self.field is not None:
            result['Field'] = self.field

        if self.header_name is not None:
            result['HeaderName'] = self.header_name

        if self.match_method is not None:
            result['MatchMethod'] = self.match_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentList') is not None:
            self.content_list = m.get('ContentList')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')

        if m.get('MatchMethod') is not None:
            self.match_method = m.get('MatchMethod')

        return self

