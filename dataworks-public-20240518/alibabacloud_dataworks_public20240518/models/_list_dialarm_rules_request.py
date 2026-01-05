# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDIAlarmRulesRequest(DaraModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        job_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the alert rule. If you leave this parameter empty, all alert rules of the task are queried.
        self.dialarm_rule_id = dialarm_rule_id
        # The ID of the task for which alert rules are configured.
        self.job_id = job_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

