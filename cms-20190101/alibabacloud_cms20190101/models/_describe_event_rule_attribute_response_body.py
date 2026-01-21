# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeEventRuleAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.DescribeEventRuleAttributeResponseBodyResult = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details of the event-triggered alert rule.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEventRuleAttributeResponseBodyResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_pattern: main_models.DescribeEventRuleAttributeResponseBodyResultEventPattern = None,
        event_type: str = None,
        group_id: str = None,
        name: str = None,
        state: str = None,
    ):
        # The description of the event-triggered alert rule.
        self.description = description
        # The event pattern. This parameter describes the trigger conditions of an event.
        self.event_pattern = event_pattern
        # The event type. Valid values:
        # 
        # *   SYSTEM: system event
        # *   CUSTOM: custom event
        self.event_type = event_type
        # The ID of the application group.
        self.group_id = group_id
        # The name of the event-triggered alert rule.
        self.name = name
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

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventPattern') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPattern()
            self.event_pattern = temp_model.from_map(m.get('EventPattern'))

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeEventRuleAttributeResponseBodyResultEventPattern(DaraModel):
    def __init__(
        self,
        event_type_list: main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternEventTypeList = None,
        keyword_filter_obj: main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternKeywordFilterObj = None,
        level_list: main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternLevelList = None,
        name_list: main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternNameList = None,
        product: str = None,
        sqlfilter: str = None,
        status_list: main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternStatusList = None,
    ):
        # The types of the event-triggered alert rules.
        self.event_type_list = event_type_list
        # The keyword for filtering.
        self.keyword_filter_obj = keyword_filter_obj
        self.level_list = level_list
        self.name_list = name_list
        # The name of the cloud service.
        self.product = product
        # Indicates that logs are filtered based on the specified SQL statement. If the specified conditions are met, an alert is triggered.
        self.sqlfilter = sqlfilter
        self.status_list = status_list

    def validate(self):
        if self.event_type_list:
            self.event_type_list.validate()
        if self.keyword_filter_obj:
            self.keyword_filter_obj.validate()
        if self.level_list:
            self.level_list.validate()
        if self.name_list:
            self.name_list.validate()
        if self.status_list:
            self.status_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list.to_map()

        if self.keyword_filter_obj is not None:
            result['KeywordFilterObj'] = self.keyword_filter_obj.to_map()

        if self.level_list is not None:
            result['LevelList'] = self.level_list.to_map()

        if self.name_list is not None:
            result['NameList'] = self.name_list.to_map()

        if self.product is not None:
            result['Product'] = self.product

        if self.sqlfilter is not None:
            result['SQLFilter'] = self.sqlfilter

        if self.status_list is not None:
            result['StatusList'] = self.status_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTypeList') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternEventTypeList()
            self.event_type_list = temp_model.from_map(m.get('EventTypeList'))

        if m.get('KeywordFilterObj') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternKeywordFilterObj()
            self.keyword_filter_obj = temp_model.from_map(m.get('KeywordFilterObj'))

        if m.get('LevelList') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternLevelList()
            self.level_list = temp_model.from_map(m.get('LevelList'))

        if m.get('NameList') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternNameList()
            self.name_list = temp_model.from_map(m.get('NameList'))

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('SQLFilter') is not None:
            self.sqlfilter = m.get('SQLFilter')

        if m.get('StatusList') is not None:
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternStatusList()
            self.status_list = temp_model.from_map(m.get('StatusList'))

        return self

class DescribeEventRuleAttributeResponseBodyResultEventPatternStatusList(DaraModel):
    def __init__(
        self,
        status_list: List[str] = None,
    ):
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

class DescribeEventRuleAttributeResponseBodyResultEventPatternNameList(DaraModel):
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

class DescribeEventRuleAttributeResponseBodyResultEventPatternLevelList(DaraModel):
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

class DescribeEventRuleAttributeResponseBodyResultEventPatternKeywordFilterObj(DaraModel):
    def __init__(
        self,
        keywords: main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternKeywordFilterObjKeywords = None,
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
            temp_model = main_models.DescribeEventRuleAttributeResponseBodyResultEventPatternKeywordFilterObjKeywords()
            self.keywords = temp_model.from_map(m.get('Keywords'))

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

class DescribeEventRuleAttributeResponseBodyResultEventPatternKeywordFilterObjKeywords(DaraModel):
    def __init__(
        self,
        keyword: List[str] = None,
    ):
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        return self

class DescribeEventRuleAttributeResponseBodyResultEventPatternEventTypeList(DaraModel):
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

