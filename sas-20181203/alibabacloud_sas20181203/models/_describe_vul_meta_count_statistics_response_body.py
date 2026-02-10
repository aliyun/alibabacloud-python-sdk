# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulMetaCountStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        app_count: int = None,
        cve_count: int = None,
        rasp_defend_count: int = None,
        request_id: str = None,
        sys_count: int = None,
    ):
        # The number of application vulnerabilities.
        self.app_count = app_count
        # The number of Linux software vulnerabilities.
        self.cve_count = cve_count
        # The number of vulnerabilities that can be defended by the application protection feature.
        self.rasp_defend_count = rasp_defend_count
        # The request ID.
        self.request_id = request_id
        # The number of Windows system vulnerabilities.
        self.sys_count = sys_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_count is not None:
            result['AppCount'] = self.app_count

        if self.cve_count is not None:
            result['CveCount'] = self.cve_count

        if self.rasp_defend_count is not None:
            result['RaspDefendCount'] = self.rasp_defend_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sys_count is not None:
            result['SysCount'] = self.sys_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        if m.get('CveCount') is not None:
            self.cve_count = m.get('CveCount')

        if m.get('RaspDefendCount') is not None:
            self.rasp_defend_count = m.get('RaspDefendCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SysCount') is not None:
            self.sys_count = m.get('SysCount')

        return self

