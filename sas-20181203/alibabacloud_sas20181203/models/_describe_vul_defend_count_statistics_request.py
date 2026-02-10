# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulDefendCountStatisticsRequest(DaraModel):
    def __init__(
        self,
        vul_type: str = None,
    ):
        # The type of the vulnerabilities. Valid values:
        # 
        # *   app: application vulnerabilities
        # *   emg: urgent vulnerabilities
        self.vul_type = vul_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vul_type is not None:
            result['VulType'] = self.vul_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VulType') is not None:
            self.vul_type = m.get('VulType')

        return self

