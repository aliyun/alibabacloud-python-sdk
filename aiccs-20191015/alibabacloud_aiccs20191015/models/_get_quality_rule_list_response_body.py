# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetQualityRuleListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQualityRuleListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = main_models.GetQualityRuleListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityRuleListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        quality_rule_list: List[main_models.GetQualityRuleListResponseBodyDataQualityRuleList] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.quality_rule_list = quality_rule_list
        self.total = total

    def validate(self):
        if self.quality_rule_list:
            for v1 in self.quality_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['QualityRuleList'] = []
        if self.quality_rule_list is not None:
            for k1 in self.quality_rule_list:
                result['QualityRuleList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.quality_rule_list = []
        if m.get('QualityRuleList') is not None:
            for k1 in m.get('QualityRuleList'):
                temp_model = main_models.GetQualityRuleListResponseBodyDataQualityRuleList()
                self.quality_rule_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQualityRuleListResponseBodyDataQualityRuleList(DaraModel):
    def __init__(
        self,
        key_words: List[str] = None,
        match_type: int = None,
        name: str = None,
        rule_create_time: str = None,
        rule_id: int = None,
        rule_tag: int = None,
    ):
        self.key_words = key_words
        self.match_type = match_type
        self.name = name
        self.rule_create_time = rule_create_time
        self.rule_id = rule_id
        self.rule_tag = rule_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_create_time is not None:
            result['RuleCreateTime'] = self.rule_create_time

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleCreateTime') is not None:
            self.rule_create_time = m.get('RuleCreateTime')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')

        return self

