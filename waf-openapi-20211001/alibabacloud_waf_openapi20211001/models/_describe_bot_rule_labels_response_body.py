# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeBotRuleLabelsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rule_labels: List[main_models.DescribeBotRuleLabelsResponseBodyRuleLabels] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned per page. Valid values: 1 to 200. Default value: 20.
        self.max_results = max_results
        # The token to retrieve the next page of results. This parameter is returned if a next page exists.
        # 
        # > If a value is returned for this parameter, it indicates that more results are available. Use the returned **NextToken** value in the next request to retrieve the next page of results. Repeat this process until no value is returned for this parameter. This indicates that all results have been retrieved.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of bot management rule labels.
        self.rule_labels = rule_labels
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rule_labels:
            for v1 in self.rule_labels:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleLabels'] = []
        if self.rule_labels is not None:
            for k1 in self.rule_labels:
                result['RuleLabels'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_labels = []
        if m.get('RuleLabels') is not None:
            for k1 in m.get('RuleLabels'):
                temp_model = main_models.DescribeBotRuleLabelsResponseBodyRuleLabels()
                self.rule_labels.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBotRuleLabelsResponseBodyRuleLabels(DaraModel):
    def __init__(
        self,
        bot_behavior: str = None,
        label_key: str = None,
        label_type: str = None,
        sub_scene: str = None,
    ):
        # The bot behavior that corresponds to the rule label. Valid values:
        # 
        # - **malicious**: malicious bot.
        # 
        # - **suspicious**: suspected bot.
        # 
        # - **normal**: normal bot.
        self.bot_behavior = bot_behavior
        # The key of the bot management rule label.
        self.label_key = label_key
        # The type of the bot rule label.
        self.label_type = label_type
        # The bot management scenarios to which the rule belongs. Multiple scenarios are separated by commas (,). Valid values:
        # 
        # - **web**: web protection.
        # 
        # - **app**: app protection.
        self.sub_scene = sub_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_behavior is not None:
            result['BotBehavior'] = self.bot_behavior

        if self.label_key is not None:
            result['LabelKey'] = self.label_key

        if self.label_type is not None:
            result['LabelType'] = self.label_type

        if self.sub_scene is not None:
            result['SubScene'] = self.sub_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotBehavior') is not None:
            self.bot_behavior = m.get('BotBehavior')

        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')

        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')

        if m.get('SubScene') is not None:
            self.sub_scene = m.get('SubScene')

        return self

