# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListAlertEventsResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.ListAlertEventsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned struct.
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
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.ListAlertEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAlertEventsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        events: List[main_models.ListAlertEventsResponseBodyPageBeanEvents] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The queried historical alert events.
        self.events = events
        # The number of the page returned.
        self.page = page
        # The number of entries returned per page.
        self.size = size
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.ListAlertEventsResponseBodyPageBeanEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAlertEventsResponseBodyPageBeanEvents(DaraModel):
    def __init__(
        self,
        alarms: List[main_models.ListAlertEventsResponseBodyPageBeanEventsAlarms] = None,
        alert_name: str = None,
        annotations: str = None,
        description: str = None,
        end_time: str = None,
        generator_url: str = None,
        handler_name: str = None,
        integration_name: str = None,
        integration_type: str = None,
        labels: str = None,
        notification_policies: List[main_models.ListAlertEventsResponseBodyPageBeanEventsNotificationPolicies] = None,
        receive_time: str = None,
        severity: str = None,
        start_time: str = None,
        status: str = None,
        trigger_count: int = None,
    ):
        # The associated alerts.
        self.alarms = alarms
        # The name of the alert.
        self.alert_name = alert_name
        # The annotations.
        self.annotations = annotations
        # The description of the alert event.
        self.description = description
        # The end time.
        self.end_time = end_time
        # The URL of the alert event.
        self.generator_url = generator_url
        # The user who handled the alert.
        self.handler_name = handler_name
        # The name of the alert integration.
        self.integration_name = integration_name
        # The type of the alert integration.
        self.integration_type = integration_type
        # The tags.
        self.labels = labels
        # The associated notification policies.
        self.notification_policies = notification_policies
        # The time when the alert event was received.
        self.receive_time = receive_time
        # The severity level of the alert. Valid values:
        # 
        # *   critical: P1
        # *   error: P2
        # *   warning: P3
        # *   page: P4
        # *   default: P6
        self.severity = severity
        # The start time.
        self.start_time = start_time
        # The status of the alert event. Valid values:
        # 
        # *   Active
        # *   Silenced
        # *   Resolved
        self.status = status
        # The number of times the event is triggered.
        self.trigger_count = trigger_count

    def validate(self):
        if self.alarms:
            for v1 in self.alarms:
                 if v1:
                    v1.validate()
        if self.notification_policies:
            for v1 in self.notification_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alarms'] = []
        if self.alarms is not None:
            for k1 in self.alarms:
                result['Alarms'].append(k1.to_map() if k1 else None)

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.generator_url is not None:
            result['GeneratorURL'] = self.generator_url

        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name

        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.labels is not None:
            result['Labels'] = self.labels

        result['NotificationPolicies'] = []
        if self.notification_policies is not None:
            for k1 in self.notification_policies:
                result['NotificationPolicies'].append(k1.to_map() if k1 else None)

        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger_count is not None:
            result['TriggerCount'] = self.trigger_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k1 in m.get('Alarms'):
                temp_model = main_models.ListAlertEventsResponseBodyPageBeanEventsAlarms()
                self.alarms.append(temp_model.from_map(k1))

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GeneratorURL') is not None:
            self.generator_url = m.get('GeneratorURL')

        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')

        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        self.notification_policies = []
        if m.get('NotificationPolicies') is not None:
            for k1 in m.get('NotificationPolicies'):
                temp_model = main_models.ListAlertEventsResponseBodyPageBeanEventsNotificationPolicies()
                self.notification_policies.append(temp_model.from_map(k1))

        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerCount') is not None:
            self.trigger_count = m.get('TriggerCount')

        return self

class ListAlertEventsResponseBodyPageBeanEventsNotificationPolicies(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the notification policy.
        self.id = id
        # The name of the notification policy.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListAlertEventsResponseBodyPageBeanEventsAlarms(DaraModel):
    def __init__(
        self,
        alarm_id: int = None,
        alarm_name: str = None,
        create_time: str = None,
        state: int = None,
    ):
        # The ID of the alert.
        self.alarm_id = alarm_id
        # The name of the alert.
        self.alarm_name = alarm_name
        # The time when the alert was created.
        self.create_time = create_time
        # The status of the alert. Valid values:
        # 
        # *   0: The alert is pending.
        # *   1: The alert is being handled.
        # *   2: The alert is cleared.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

