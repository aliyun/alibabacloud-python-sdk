# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHttpDDoSAttackProtectionResponseBody(DaraModel):
    def __init__(
        self,
        global_mode: str = None,
        request_id: str = None,
        site_id: int = None,
    ):
        # The level of HTTP DDoS attack protection. Valid values:
        # 
        # *   **very weak**: very loose.
        # *   **weak**: loose.
        # *   **default**: normal.
        # *   **hard**: strict.
        self.global_mode = global_mode
        # The request ID.
        self.request_id = request_id
        # The website ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_mode is not None:
            result['GlobalMode'] = self.global_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalMode') is not None:
            self.global_mode = m.get('GlobalMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

