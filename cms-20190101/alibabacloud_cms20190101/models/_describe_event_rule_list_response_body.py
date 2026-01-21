# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeEventRuleListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        event_rules: main_models.DescribeEventRuleListResponseBodyEventRules = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The event-triggered alert rule.
        self.event_rules = event_rules
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.event_rules:
            self.event_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.event_rules is not None:
            result['EventRules'] = self.event_rules.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EventRules') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRules()
            self.event_rules = temp_model.from_map(m.get('EventRules'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeEventRuleListResponseBodyEventRules(DaraModel):
    def __init__(
        self,
        event_rule: List[main_models.DescribeEventRuleListResponseBodyEventRulesEventRule] = None,
    ):
        self.event_rule = event_rule

    def validate(self):
        if self.event_rule:
            for v1 in self.event_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventRule'] = []
        if self.event_rule is not None:
            for k1 in self.event_rule:
                result['EventRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_rule = []
        if m.get('EventRule') is not None:
            for k1 in m.get('EventRule'):
                temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRule()
                self.event_rule.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_pattern: main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPattern = None,
        event_type: str = None,
        group_id: str = None,
        name: str = None,
        silence_time: int = None,
        state: str = None,
    ):
        # The description of the event-triggered alert rule.
        self.description = description
        # The mode of the event-triggered alert rule.
        self.event_pattern = event_pattern
        # The type of the event-triggered alert rule. Valid values:
        # 
        # *   SYSTEM: system event-triggered alert rule
        # *   CUSTOM: custom event-triggered alert rule
        self.event_type = event_type
        # The ID of the application group.
        self.group_id = group_id
        # The name of the event-triggered alert rule.
        self.name = name
        # The mute period during which new alert notifications are not sent even if the trigger conditions are met.
        self.silence_time = silence_time
        # The status of the event-triggered alert rule. Valid values:
        # 
        # *   ENABLED
        # *   DISABLED
        self.state = state

    def validate(self):
        if self.event_pattern:
            self.event_pattern.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.event_pattern is not None:
            result['EventPattern'] = self.event_pattern.to_map()

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.name is not None:
            result['Name'] = self.name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventPattern') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPattern()
            self.event_pattern = temp_model.from_map(m.get('EventPattern'))

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPattern(DaraModel):
    def __init__(
        self,
        event_pattern: List[main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPattern] = None,
    ):
        self.event_pattern = event_pattern

    def validate(self):
        if self.event_pattern:
            for v1 in self.event_pattern:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventPattern'] = []
        if self.event_pattern is not None:
            for k1 in self.event_pattern:
                result['EventPattern'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_pattern = []
        if m.get('EventPattern') is not None:
            for k1 in m.get('EventPattern'):
                temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPattern()
                self.event_pattern.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPattern(DaraModel):
    def __init__(
        self,
        custom_filters: str = None,
        event_type_list: main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternEventTypeList = None,
        keyword_filter: main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternKeywordFilter = None,
        level_list: main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternLevelList = None,
        name_list: main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternNameList = None,
        product: str = None,
        sqlfilter: str = None,
    ):
        # The custom filter conditions.
        self.custom_filters = custom_filters
        # The types of the event-triggered alert rules.
        self.event_type_list = event_type_list
        # The keyword for filtering.
        self.keyword_filter = keyword_filter
        # The levels of the event-triggered alerts.
        self.level_list = level_list
        # The event names.
        self.name_list = name_list
        # The abbreviation of the Alibaba Cloud service name.
        self.product = product
        # Indicates that logs are filtered based on the specified SQL statement. If the specified conditions are met, an alert is triggered.
        self.sqlfilter = sqlfilter

    def validate(self):
        if self.event_type_list:
            self.event_type_list.validate()
        if self.keyword_filter:
            self.keyword_filter.validate()
        if self.level_list:
            self.level_list.validate()
        if self.name_list:
            self.name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters

        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list.to_map()

        if self.keyword_filter is not None:
            result['KeywordFilter'] = self.keyword_filter.to_map()

        if self.level_list is not None:
            result['LevelList'] = self.level_list.to_map()

        if self.name_list is not None:
            result['NameList'] = self.name_list.to_map()

        if self.product is not None:
            result['Product'] = self.product

        if self.sqlfilter is not None:
            result['SQLFilter'] = self.sqlfilter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('EventTypeList') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternEventTypeList()
            self.event_type_list = temp_model.from_map(m.get('EventTypeList'))

        if m.get('KeywordFilter') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternKeywordFilter()
            self.keyword_filter = temp_model.from_map(m.get('KeywordFilter'))

        if m.get('LevelList') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternLevelList()
            self.level_list = temp_model.from_map(m.get('LevelList'))

        if m.get('NameList') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternNameList()
            self.name_list = temp_model.from_map(m.get('NameList'))

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('SQLFilter') is not None:
            self.sqlfilter = m.get('SQLFilter')

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternNameList(DaraModel):
    def __init__(
        self,
        name_list: List[str] = None,
    ):
        self.name_list = name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_list is not None:
            result['NameList'] = self.name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternLevelList(DaraModel):
    def __init__(
        self,
        level_list: List[str] = None,
    ):
        self.level_list = level_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level_list is not None:
            result['LevelList'] = self.level_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LevelList') is not None:
            self.level_list = m.get('LevelList')

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternKeywordFilter(DaraModel):
    def __init__(
        self,
        keywords: main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternKeywordFilterKeywords = None,
        relation: str = None,
    ):
        # The keywords that are used to match events.
        self.keywords = keywords
        # The relationship between multiple keywords in a condition. Valid values:
        # 
        # *   OR: The relationship between keywords is OR.
        # *   NOT: The keyword is excluded. The value NOT indicates that all events that do not contain the keywords are matched.
        self.relation = relation

    def validate(self):
        if self.keywords:
            self.keywords.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['Keywords'] = self.keywords.to_map()

        if self.relation is not None:
            result['Relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            temp_model = main_models.DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternKeywordFilterKeywords()
            self.keywords = temp_model.from_map(m.get('Keywords'))

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternKeywordFilterKeywords(DaraModel):
    def __init__(
        self,
        keywords: List[str] = None,
    ):
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['Keywords'] = self.keywords

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        return self

class DescribeEventRuleListResponseBodyEventRulesEventRuleEventPatternEventPatternEventTypeList(DaraModel):
    def __init__(
        self,
        event_type_list: List[str] = None,
    ):
        self.event_type_list = event_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')

        return self

