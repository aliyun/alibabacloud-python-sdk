# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPatrolReportsRequest(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        page: int = None,
        scope_type: str = None,
        size: int = None,
        start_date: int = None,
        status: str = None,
        trigger_type: str = None,
    ):
        # The end time of the query. Unit: milliseconds (UNIX timestamp).
        self.end_date = end_date
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # Filters reports by inspection scope type. Valid values:
        # 
        # - ALL
        # - TAGS
        # - DEPLOYMENTS
        self.scope_type = scope_type
        # The number of entries per page. Default value: 20. Maximum value: 200.
        self.size = size
        # The start time of the query. Unit: milliseconds (UNIX timestamp).
        self.start_date = start_date
        # Filters reports by status. Valid values:
        # 
        # - PENDING
        # - IN_PROGRESS
        # - COMPLETED
        # - FAILED
        self.status = status
        # Filters reports by trigger type. Valid values:
        # 
        # - CRON
        # - MANUAL
        # - INNER_API
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.page is not None:
            result['page'] = self.page

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.size is not None:
            result['size'] = self.size

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.status is not None:
            result['status'] = self.status

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

