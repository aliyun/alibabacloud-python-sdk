# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPatrolReportDetailRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        report_id: str = None,
        timezone: str = None,
    ):
        # The report date in ISO format such as 2026-08-13, or a special value such as today or yesterday. Specify either this parameter or reportId. This parameter is used to retrieve the latest report for the specified date.
        self.date = date
        # The report ID. Specify either this parameter or date. The reportId parameter takes priority over the date parameter.
        self.report_id = report_id
        # The time zone. Used together with the date parameter. Default value: UTC.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

