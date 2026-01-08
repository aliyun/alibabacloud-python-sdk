# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolicyAdvancedConfigResponseBody(DaraModel):
    def __init__(
        self,
        internet_switch: str = None,
        request_id: str = None,
    ):
        # Indicates whether the strict mode is enabled for the access control policy. Valid values:
        # 
        # *   **on**: The strict mode is enabled.
        # *   **off**: The strict mode is disabled.
        self.internet_switch = internet_switch
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

