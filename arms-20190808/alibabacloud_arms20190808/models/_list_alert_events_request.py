# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertEventsRequest(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        end_time: str = None,
        matching_conditions: str = None,
        page: int = None,
        show_notification_policies: bool = None,
        size: int = None,
        start_time: str = None,
        status: str = None,
    ):
        # The name of the alert.
        self.alert_name = alert_name
        # The end time of the alert events that you want to query. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        self.end_time = end_time
        # The list of matching conditions.
        self.matching_conditions = matching_conditions
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # Specifies whether to show the associated notification policy.
        self.show_notification_policies = show_notification_policies
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.size = size
        # The start time of the alert events that you want to query. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        self.start_time = start_time
        # The status of the alert events. Valid values:
        # 
        # *   Active
        # *   Silenced
        # *   Resolved
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.matching_conditions is not None:
            result['MatchingConditions'] = self.matching_conditions

        if self.page is not None:
            result['Page'] = self.page

        if self.show_notification_policies is not None:
            result['ShowNotificationPolicies'] = self.show_notification_policies

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MatchingConditions') is not None:
            self.matching_conditions = m.get('MatchingConditions')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('ShowNotificationPolicies') is not None:
            self.show_notification_policies = m.get('ShowNotificationPolicies')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

