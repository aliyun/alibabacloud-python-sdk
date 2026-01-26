# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertsRequest(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        dispatch_rule_id: int = None,
        end_time: str = None,
        integration_type: str = None,
        owner: str = None,
        page: int = None,
        region_id: str = None,
        severity: str = None,
        show_activities: bool = None,
        show_events: bool = None,
        size: int = None,
        start_time: str = None,
        state: int = None,
    ):
        # The name of the alert rule.
        self.alert_name = alert_name
        # The ID of the notification policy.
        self.dispatch_rule_id = dispatch_rule_id
        # The end time of the alert sending history that you want to query. Specify the time in the `YYYY-MM-DD HH:mm:ss` format.
        self.end_time = end_time
        # The integration type.
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
        # The notification object configured in the notification policy, responsible for handling alerts.
        self.owner = owner
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The ID of the region.
        self.region_id = region_id
        # The severity level of the alert. Valid values: P6, P5, P4, P3, P2, and P1. The preceding values are listed in ascending order of severity.
        self.severity = severity
        # Specifies whether to query the activities that correspond to alerts. Valid values:
        # 
        # *   `false` (default value): The activities are not queried.
        # *   `true`: The activities in the last three days are queried.
        self.show_activities = show_activities
        # Specifies whether to query the events that correspond to alerts. Valid values:
        # 
        # *   `false` (default value): The events are not queried.
        # *   `true`: The events are queried.
        self.show_events = show_events
        # The number of alerts to return on each page.
        # 
        # This parameter is required.
        self.size = size
        # The start time of the alert sending history that you want to query. Specify the time in the `YYYY-MM-DD HH:mm:ss` format.
        self.start_time = start_time
        # The status of the alert. Valid values:
        # 
        # *   0: The alert is pending.
        # *   1: The alert is being handled.
        # *   2: The alert is handled.
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

        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page is not None:
            result['Page'] = self.page

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.show_activities is not None:
            result['ShowActivities'] = self.show_activities

        if self.show_events is not None:
            result['ShowEvents'] = self.show_events

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('ShowActivities') is not None:
            self.show_activities = m.get('ShowActivities')

        if m.get('ShowEvents') is not None:
            self.show_events = m.get('ShowEvents')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

