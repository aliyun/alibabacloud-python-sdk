# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListInterveneRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInterveneRulesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListInterveneRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInterveneRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        code: int = None,
        count: int = None,
        intervene_rule_list: List[main_models.ListInterveneRulesResponseBodyDataInterveneRuleList] = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.code = code
        self.count = count
        self.intervene_rule_list = intervene_rule_list
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        if self.intervene_rule_list:
            for v1 in self.intervene_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['InterveneRuleList'] = []
        if self.intervene_rule_list is not None:
            for k1 in self.intervene_rule_list:
                result['InterveneRuleList'].append(k1.to_map() if k1 else None)

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.intervene_rule_list = []
        if m.get('InterveneRuleList') is not None:
            for k1 in m.get('InterveneRuleList'):
                temp_model = main_models.ListInterveneRulesResponseBodyDataInterveneRuleList()
                self.intervene_rule_list.append(temp_model.from_map(k1))

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListInterveneRulesResponseBodyDataInterveneRuleList(DaraModel):
    def __init__(
        self,
        answer_config: List[main_models.ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig] = None,
        create_time: str = None,
        effect_time: str = None,
        intervene_type: int = None,
        namespace_list: List[str] = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.answer_config = answer_config
        self.create_time = create_time
        self.effect_time = effect_time
        self.intervene_type = intervene_type
        self.namespace_list = namespace_list
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        if self.answer_config:
            for v1 in self.answer_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k1 in self.answer_config:
                result['AnswerConfig'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time

        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type

        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k1 in m.get('AnswerConfig'):
                temp_model = main_models.ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig()
                self.answer_config.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')

        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')

        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig(DaraModel):
    def __init__(
        self,
        answer_type: int = None,
        message: str = None,
        namespace: str = None,
    ):
        self.answer_type = answer_type
        self.message = message
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

