# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceInspectionRunsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        report_status: str = None,
        result: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        template_code: str = None,
    ):
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.report_status = report_status
        self.result = result
        self.sort_by = sort_by
        self.start_time = start_time
        self.status = status
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.report_status is not None:
            result['reportStatus'] = self.report_status

        if self.result is not None:
            result['result'] = self.result

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('reportStatus') is not None:
            self.report_status = m.get('reportStatus')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

