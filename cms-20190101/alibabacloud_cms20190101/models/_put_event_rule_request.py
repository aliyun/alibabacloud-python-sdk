# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutEventRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_pattern: List[main_models.PutEventRuleRequestEventPattern] = None,
        event_type: str = None,
        group_id: str = None,
        region_id: str = None,
        rule_name: str = None,
        silence_time: int = None,
        state: str = None,
    ):
        # The description of the event-triggered alert rule.
        self.description = description
        # This parameter is required.
        self.event_pattern = event_pattern
        # The type of the event-triggered alert rule. Valid values:
        # 
        # *   SYSTEM: system event-triggered alert rule
        # *   CUSTOM: custom event-triggered alert rule
        self.event_type = event_type
        # The ID of the application group to which the event-triggered alert rule belongs.
        self.group_id = group_id
        self.region_id = region_id
        # The name of the event-triggered alert rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds.
        self.silence_time = silence_time
        # The status of the event-triggered alert rule. Valid values:
        # 
        # *   ENABLED: enabled
        # *   DISABLED: disabled
        self.state = state

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
        if self.description is not None:
            result['Description'] = self.description

        result['EventPattern'] = []
        if self.event_pattern is not None:
            for k1 in self.event_pattern:
                result['EventPattern'].append(k1.to_map() if k1 else None)

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.event_pattern = []
        if m.get('EventPattern') is not None:
            for k1 in m.get('EventPattern'):
                temp_model = main_models.PutEventRuleRequestEventPattern()
                self.event_pattern.append(temp_model.from_map(k1))

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class PutEventRuleRequestEventPattern(DaraModel):
    def __init__(
        self,
        custom_filters: str = None,
        event_type_list: List[str] = None,
        level_list: List[str] = None,
        name_list: List[str] = None,
        product: str = None,
        sqlfilter: str = None,
        status_list: List[str] = None,
    ):
        # The keyword that is used to filter events. If the content of an event contains the specified keyword, an alert is automatically triggered.
        self.custom_filters = custom_filters
        self.event_type_list = event_type_list
        self.level_list = level_list
        self.name_list = name_list
        # The type of the cloud service. Valid values of N: 1 to 50.
        # 
        # >  You can call the DescribeSystemEventMetaList operation to query the cloud services that support event-triggered alerts. For more information, see [DescribeSystemEventMetaList](https://help.aliyun.com/document_detail/114972.html).
        # 
        # This parameter is required.
        self.product = product
        # The SQL condition that is used to filter events. If the content of an event meets the specified SQL condition, an alert is automatically triggered.
        # 
        # >  The syntax of SQL event filtering is consistent with the query syntax of Log Service.
        self.sqlfilter = sqlfilter
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters

        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list

        if self.level_list is not None:
            result['LevelList'] = self.level_list

        if self.name_list is not None:
            result['NameList'] = self.name_list

        if self.product is not None:
            result['Product'] = self.product

        if self.sqlfilter is not None:
            result['SQLFilter'] = self.sqlfilter

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')

        if m.get('LevelList') is not None:
            self.level_list = m.get('LevelList')

        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('SQLFilter') is not None:
            self.sqlfilter = m.get('SQLFilter')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

