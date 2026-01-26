# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchEventsResponseBody(DaraModel):
    def __init__(
        self,
        is_trigger: int = None,
        page_bean: main_models.SearchEventsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # Specifies whether the alert event is triggered. If you do not set this parameter, all alert events are queried. Valid values:
        # 
        # *   `1`: The event is triggered.
        # *   `0`: The event is not triggered.
        self.is_trigger = is_trigger
        # The struct returned.
        self.page_bean = page_bean
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger

        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')

        if m.get('PageBean') is not None:
            temp_model = main_models.SearchEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchEventsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        event: List[main_models.SearchEventsResponseBodyPageBeanEvent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The information about the alert events.
        self.event = event
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.event:
            for v1 in self.event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Event'] = []
        if self.event is not None:
            for k1 in self.event:
                result['Event'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k1 in m.get('Event'):
                temp_model = main_models.SearchEventsResponseBodyPageBeanEvent()
                self.event.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchEventsResponseBodyPageBeanEvent(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        alert_rule: str = None,
        alert_type: int = None,
        event_level: str = None,
        event_time: int = None,
        id: int = None,
        links: List[str] = None,
        message: str = None,
    ):
        # The ID of the alert rule that is associated with the event.
        self.alert_id = alert_id
        # The name of the alert rule that is associated with the event.
        self.alert_name = alert_name
        # The condition of the alert rule.
        self.alert_rule = alert_rule
        # The type of the alert rule. This parameter is not returned. Valid values:
        # 
        # *   `1`: custom alert rules to monitor drill-down data sets
        # *   `3`: custom alert rules to monitor tiled data sets
        # *   `4`: alert rules to monitor the frontend, including the default frontend alert rules
        # *   `5`: alert rules to monitor applications, including the default application alert rules
        # *   `6`: the default frontend alert rules
        # *   `7`: the default application alert rules
        # *   `8`: Tracing Analysis alert rules
        # *   `101`: Prometheus alert rules
        self.alert_type = alert_type
        # The severity of the event.
        self.event_level = event_level
        # The timestamp when the event occurred.
        self.event_time = event_time
        # The ID of the event record.
        self.id = id
        # The list of event URLs.
        self.links = links
        # The event content. The parameter value is a JSON string. Each key indicates a dimension and each value indicates the alert content in the dimension.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.id is not None:
            result['Id'] = self.id

        if self.links is not None:
            result['Links'] = self.links

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Links') is not None:
            self.links = m.get('Links')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

