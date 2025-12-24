# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamWatermarkRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_info_list: main_models.DescribeLiveStreamWatermarkRulesResponseBodyRuleInfoList = None,
        total: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The watermark rules.
        self.rule_info_list = rule_info_list
        # The total number of entries that meet the specified conditions.
        self.total = total

    def validate(self):
        if self.rule_info_list:
            self.rule_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_info_list is not None:
            result['RuleInfoList'] = self.rule_info_list.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleInfoList') is not None:
            temp_model = main_models.DescribeLiveStreamWatermarkRulesResponseBodyRuleInfoList()
            self.rule_info_list = temp_model.from_map(m.get('RuleInfoList'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLiveStreamWatermarkRulesResponseBodyRuleInfoList(DaraModel):
    def __init__(
        self,
        rule_info: List[main_models.DescribeLiveStreamWatermarkRulesResponseBodyRuleInfoListRuleInfo] = None,
    ):
        self.rule_info = rule_info

    def validate(self):
        if self.rule_info:
            for v1 in self.rule_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleInfo'] = []
        if self.rule_info is not None:
            for k1 in self.rule_info:
                result['RuleInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_info = []
        if m.get('RuleInfo') is not None:
            for k1 in m.get('RuleInfo'):
                temp_model = main_models.DescribeLiveStreamWatermarkRulesResponseBodyRuleInfoListRuleInfo()
                self.rule_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamWatermarkRulesResponseBodyRuleInfoListRuleInfo(DaraModel):
    def __init__(
        self,
        app: str = None,
        description: str = None,
        domain: str = None,
        name: str = None,
        rule_id: str = None,
        stream: str = None,
        template_id: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The description of the custom rule.
        self.description = description
        # The streaming domain.
        self.domain = domain
        # The name of the custom rule.
        self.name = name
        # The ID of the watermark rule.
        # 
        # >  You can obtain the rule ID by checking the value of the RuleId parameter that is returned by the [AddLiveStreamWatermarkRule](https://help.aliyun.com/document_detail/2848100.html) operation.
        self.rule_id = rule_id
        # The name of the live stream. The following matching rules apply:
        # 
        # *   A stream name can be exactly matched. Example: liveStreamA.
        # *   Fuzzy match is also supported. The use of an asterisk (`*`) allows all approximate matches to be found.
        # *   You can place the asterisk before or after an approximate string.
        # 
        # > 
        # 
        # *   Fuzzy match: Only one asterisk (`*`) before or after an approximate string is allowed. The approximate string must be enclosed in `()`. Separate multiple strings with vertical bars (`|`).
        # 
        # *   For example, `*(t1|t2)` matches all streams whose name has the `t1` or `t2` suffix, and `(abc|123)*` matches all streams whose name has the `abc` or `123` prefix.
        self.stream = stream
        # The ID of the watermark template.
        # 
        # >  You can obtain the template ID by checking the value of the TemplateId parameter that is returned by the [AddLiveStreamWatermark](https://help.aliyun.com/document_detail/2848096.html) operation.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

