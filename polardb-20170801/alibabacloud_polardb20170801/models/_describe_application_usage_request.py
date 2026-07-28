# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationUsageRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        days: int = None,
    ):
        # The Hermes application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The number of recent days to query. Valid values: 1 to 365. Default value: 30.
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.days is not None:
            result['Days'] = self.days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        return self

