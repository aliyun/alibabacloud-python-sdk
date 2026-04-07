# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertMessagesRequest(DaraModel):
    def __init__(
        self,
        alert_methods: str = None,
        alert_rule_types: str = None,
        alert_user: str = None,
        baseline_id: int = None,
        begin_time: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        remind_id: int = None,
    ):
        # The notification method. Valid values:
        # 
        # *   MAIL
        # *   SMS Alert notifications can be sent by text message only in the Singapore, Malaysia (Kuala Lumpur), and Germany (Frankfurt) regions.
        # 
        # You can specify multiple notification methods. Separate them with commas (,).
        self.alert_methods = alert_methods
        # The type of the alert rule. Valid values: GLOBAL, USER_DEFINE, and OTHER. The value GLOBAL indicates that the alert rule is a global alert rule. The value USER_DEFINE indicates that the alert rule is customized by a user. The value OTHER indicates that the alert rule is a rule of another type. You can specify multiple types. Separate them with commas (,).
        self.alert_rule_types = alert_rule_types
        # The ID of the Alibaba Cloud account used by the alert recipient.
        self.alert_user = alert_user
        # The baseline ID. This parameter takes effect if the AlertRuleTypes parameter is set to GLOBAL. You can configure either this parameter or the RemindId parameter.
        self.baseline_id = baseline_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd\\"T\\"HH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd\\"T\\"HH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The page number. Default value: 1. Minimum value: 1. Maximum value: 30.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The custom alert rule ID. This parameter takes effect if the AlertRuleTypes parameter is set to USER_DEFINE. You can configure either this parameter or the BaselineId parameter.
        self.remind_id = remind_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_methods is not None:
            result['AlertMethods'] = self.alert_methods

        if self.alert_rule_types is not None:
            result['AlertRuleTypes'] = self.alert_rule_types

        if self.alert_user is not None:
            result['AlertUser'] = self.alert_user

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertMethods') is not None:
            self.alert_methods = m.get('AlertMethods')

        if m.get('AlertRuleTypes') is not None:
            self.alert_rule_types = m.get('AlertRuleTypes')

        if m.get('AlertUser') is not None:
            self.alert_user = m.get('AlertUser')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        return self

