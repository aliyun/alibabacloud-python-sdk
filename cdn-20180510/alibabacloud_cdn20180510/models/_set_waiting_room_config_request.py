# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetWaitingRoomConfigRequest(DaraModel):
    def __init__(
        self,
        allow_pct: int = None,
        domain_name: str = None,
        gap_time: int = None,
        max_time_wait: int = None,
        wait_uri: str = None,
        wait_url: str = None,
    ):
        # The percentage of requests that are allowed to be redirected to the origin server. Valid values: **0** to **100**.
        # 
        # This parameter is required.
        self.allow_pct = allow_pct
        # The accelerated domain name. You can specify only one domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The length of waiting time to skip after an exit from the queue. Unit: seconds.
        # 
        # This parameter is required.
        self.gap_time = gap_time
        # The maximum length of waiting time in the queue. Unit: seconds.
        # 
        # This parameter is required.
        self.max_time_wait = max_time_wait
        # The regular expression that is used to match URI strings for which the virtual waiting room feature is enabled.
        # 
        # This parameter is required.
        self.wait_uri = wait_uri
        # The URL of the waiting page.
        # 
        # This parameter is required.
        self.wait_url = wait_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_pct is not None:
            result['AllowPct'] = self.allow_pct

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gap_time is not None:
            result['GapTime'] = self.gap_time

        if self.max_time_wait is not None:
            result['MaxTimeWait'] = self.max_time_wait

        if self.wait_uri is not None:
            result['WaitUri'] = self.wait_uri

        if self.wait_url is not None:
            result['WaitUrl'] = self.wait_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPct') is not None:
            self.allow_pct = m.get('AllowPct')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GapTime') is not None:
            self.gap_time = m.get('GapTime')

        if m.get('MaxTimeWait') is not None:
            self.max_time_wait = m.get('MaxTimeWait')

        if m.get('WaitUri') is not None:
            self.wait_uri = m.get('WaitUri')

        if m.get('WaitUrl') is not None:
            self.wait_url = m.get('WaitUrl')

        return self

