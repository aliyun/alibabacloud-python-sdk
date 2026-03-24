# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCdnSubTaskRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        report_ids: str = None,
        start_time: str = None,
    ):
        # The domain name that you want to track. You can specify up to 500 domain names in each request. If you specify multiple domain names, separate them with commas (,). If you do not specify a domain name, operations reports are updated for all domain names in your Alibaba Cloud account.
        self.domain_name = domain_name
        # The end time of the operations report. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The IDs of operations reports that you want to update. Separate IDs with commas (,).
        self.report_ids = report_ids
        # The start time of the operations report. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.report_ids is not None:
            result['ReportIds'] = self.report_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ReportIds') is not None:
            self.report_ids = m.get('ReportIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

