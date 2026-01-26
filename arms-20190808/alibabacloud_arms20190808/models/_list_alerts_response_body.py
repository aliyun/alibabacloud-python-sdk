# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListAlertsResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page_bean: main_models.ListAlertsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned error message.
        self.message = message
        # The struct returned.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageBean') is not None:
            temp_model = main_models.ListAlertsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAlertsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        list_alerts: List[main_models.ListAlertsResponseBodyPageBeanListAlerts] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The queried alert notification history records.
        self.list_alerts = list_alerts
        # The page number of the returned page.
        self.page = page
        # The number of alerts returned per page.
        self.size = size
        # The total number of queried alerts.
        self.total = total

    def validate(self):
        if self.list_alerts:
            for v1 in self.list_alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListAlerts'] = []
        if self.list_alerts is not None:
            for k1 in self.list_alerts:
                result['ListAlerts'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_alerts = []
        if m.get('ListAlerts') is not None:
            for k1 in m.get('ListAlerts'):
                temp_model = main_models.ListAlertsResponseBodyPageBeanListAlerts()
                self.list_alerts.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAlertsResponseBodyPageBeanListAlerts(DaraModel):
    def __init__(
        self,
        acknowledge_time: int = None,
        activities: List[main_models.ListAlertsResponseBodyPageBeanListAlertsActivities] = None,
        alert_events: List[main_models.ListAlertsResponseBodyPageBeanListAlertsAlertEvents] = None,
        alert_id: int = None,
        alert_name: str = None,
        create_time: str = None,
        describe: str = None,
        dispatch_rule_id: float = None,
        dispatch_rule_name: str = None,
        handler: str = None,
        notify_robots: str = None,
        owner: str = None,
        recover_time: int = None,
        severity: str = None,
        solution: str = None,
        state: int = None,
    ):
        # Time to claim the alarm.
        self.acknowledge_time = acknowledge_time
        # The list of activities.
        self.activities = activities
        # The list of events.
        self.alert_events = alert_events
        # The alert ID.
        self.alert_id = alert_id
        # The name of the alert rule.
        self.alert_name = alert_name
        # The time when the alert was created.
        self.create_time = create_time
        # The description of a event execution status.
        self.describe = describe
        # The ID of the notification policy.
        self.dispatch_rule_id = dispatch_rule_id
        # The name of the notification policy.
        self.dispatch_rule_name = dispatch_rule_name
        # Alarm handler.
        self.handler = handler
        # The contact card of an instant messaging app.
        self.notify_robots = notify_robots
        # The notification object configured in the notification policy, responsible for handling alerts.
        self.owner = owner
        # Alarm recovery time.
        self.recover_time = recover_time
        # The severity level of the alert. Valid values: P6, P5, P4, P3, P2, and P1. The preceding values are listed in ascending order of severity.
        self.severity = severity
        # The Alert solution.
        self.solution = solution
        # The status of the alert. Valid values:
        # 
        # *   0: The alert is pending.
        # *   1: The alert is being handled.
        # *   2: The alert is handled.
        self.state = state

    def validate(self):
        if self.activities:
            for v1 in self.activities:
                 if v1:
                    v1.validate()
        if self.alert_events:
            for v1 in self.alert_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acknowledge_time is not None:
            result['AcknowledgeTime'] = self.acknowledge_time

        result['Activities'] = []
        if self.activities is not None:
            for k1 in self.activities:
                result['Activities'].append(k1.to_map() if k1 else None)

        result['AlertEvents'] = []
        if self.alert_events is not None:
            for k1 in self.alert_events:
                result['AlertEvents'].append(k1.to_map() if k1 else None)

        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id

        if self.dispatch_rule_name is not None:
            result['DispatchRuleName'] = self.dispatch_rule_name

        if self.handler is not None:
            result['Handler'] = self.handler

        if self.notify_robots is not None:
            result['NotifyRobots'] = self.notify_robots

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcknowledgeTime') is not None:
            self.acknowledge_time = m.get('AcknowledgeTime')

        self.activities = []
        if m.get('Activities') is not None:
            for k1 in m.get('Activities'):
                temp_model = main_models.ListAlertsResponseBodyPageBeanListAlertsActivities()
                self.activities.append(temp_model.from_map(k1))

        self.alert_events = []
        if m.get('AlertEvents') is not None:
            for k1 in m.get('AlertEvents'):
                temp_model = main_models.ListAlertsResponseBodyPageBeanListAlertsAlertEvents()
                self.alert_events.append(temp_model.from_map(k1))

        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')

        if m.get('DispatchRuleName') is not None:
            self.dispatch_rule_name = m.get('DispatchRuleName')

        if m.get('Handler') is not None:
            self.handler = m.get('Handler')

        if m.get('NotifyRobots') is not None:
            self.notify_robots = m.get('NotifyRobots')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ListAlertsResponseBodyPageBeanListAlertsAlertEvents(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        annotations: str = None,
        description: str = None,
        end_time: str = None,
        generator_url: str = None,
        integration_name: str = None,
        integration_type: str = None,
        labels: str = None,
        receive_time: str = None,
        severity: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # The name of the event.
        self.alert_name = alert_name
        # The annotations.
        self.annotations = annotations
        # The description of the event.
        self.description = description
        # The time when the event ended.
        self.end_time = end_time
        # The URL of the event.
        self.generator_url = generator_url
        # The name of the integration that corresponds to the alert event.
        self.integration_name = integration_name
        # The type of the integration that corresponds to the alert event. Valid values:
        # 
        # *   ARMS
        # *   CLOUD_MONITOR
        # *   MSE
        # *   ARMS_CLOUD_DIALTEST
        # *   PROMETHEUS
        # *   LOG_SERVICE
        # *   CUSTOM
        # *   ARMS_PROMETHEUS
        # *   ARMS_APP_MON
        # *   ARMS_FRONT_MON
        # *   ARMS_CUSTOM
        # *   XTRACE
        # *   GRAFANA
        # *   ZABBIX
        # *   SKYWALKING
        # *   EVENT_BRIDGE
        # *   NAGIOS
        # *   OPENFALCON
        # *   ARMS_INSIGHTS
        self.integration_type = integration_type
        # The tags.
        self.labels = labels
        # The time when the event was created.
        self.receive_time = receive_time
        # The severity level of the event. Valid values:
        # 
        # *   critical
        # *   error
        # *   warning
        # *   info
        self.severity = severity
        # The time when the event started.
        self.start_time = start_time
        # The status of the event. Valid values:
        # 
        # *   Active: The event is not cleared.
        # *   Silenced: The event is silenced.
        # *   Resolved: The event is cleared.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ListAlertsResponseBodyPageBeanListAlertsActivities(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        handler_name: str = None,
        time: str = None,
        type: int = None,
    ):
        # The content of the alert notification.
        self.content = content
        # The description of the activity.
        self.description = description
        # The name of the handler.
        self.handler_name = handler_name
        # The operation time of the activity.
        self.time = time
        # The type of the activity. Valid values:
        # 
        # *   1: The alert is claimed.
        # *   2: The alert is disclaimed.
        # *   3: A comment is added for the alert.
        # *   4: The alert is disabled.
        # *   5: An alert notification is sent.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

