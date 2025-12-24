# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveAIProduceRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_info_list: main_models.DescribeLiveAIProduceRulesResponseBodyRuleInfoList = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The subtitle rules.
        self.rule_info_list = rule_info_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleInfoList') is not None:
            temp_model = main_models.DescribeLiveAIProduceRulesResponseBodyRuleInfoList()
            self.rule_info_list = temp_model.from_map(m.get('RuleInfoList'))

        return self

class DescribeLiveAIProduceRulesResponseBodyRuleInfoList(DaraModel):
    def __init__(
        self,
        rule_info: List[main_models.DescribeLiveAIProduceRulesResponseBodyRuleInfoListRuleInfo] = None,
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
                temp_model = main_models.DescribeLiveAIProduceRulesResponseBodyRuleInfoListRuleInfo()
                self.rule_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveAIProduceRulesResponseBodyRuleInfoListRuleInfo(DaraModel):
    def __init__(
        self,
        app: str = None,
        description: str = None,
        domain: str = None,
        gmt_modify_time: str = None,
        is_lazy: bool = None,
        live_template: str = None,
        rules_id: str = None,
        studio_name: str = None,
        subtitle_name: str = None,
        suffix_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app = app
        # The description of the rule.
        self.description = description
        # The streaming domain.
        self.domain = domain
        # The last time when the rule was modified. The value is a timestamp.
        self.gmt_modify_time = gmt_modify_time
        # Indicates whether the rule takes effect when stream pulling starts.
        self.is_lazy = is_lazy
        # The specification of the exported subtitles.
        self.live_template = live_template
        # The ID of the subtitle rule.
        self.rules_id = rules_id
        # The name of the virtual background template.
        self.studio_name = studio_name
        # The name of the subtitle template.
        self.subtitle_name = subtitle_name
        # The suffix of the subtitle rule.
        self.suffix_name = suffix_name

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

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.is_lazy is not None:
            result['IsLazy'] = self.is_lazy

        if self.live_template is not None:
            result['LiveTemplate'] = self.live_template

        if self.rules_id is not None:
            result['RulesId'] = self.rules_id

        if self.studio_name is not None:
            result['StudioName'] = self.studio_name

        if self.subtitle_name is not None:
            result['SubtitleName'] = self.subtitle_name

        if self.suffix_name is not None:
            result['SuffixName'] = self.suffix_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('IsLazy') is not None:
            self.is_lazy = m.get('IsLazy')

        if m.get('LiveTemplate') is not None:
            self.live_template = m.get('LiveTemplate')

        if m.get('RulesId') is not None:
            self.rules_id = m.get('RulesId')

        if m.get('StudioName') is not None:
            self.studio_name = m.get('StudioName')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        if m.get('SuffixName') is not None:
            self.suffix_name = m.get('SuffixName')

        return self

