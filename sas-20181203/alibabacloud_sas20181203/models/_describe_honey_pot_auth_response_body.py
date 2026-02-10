# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHoneyPotAuthResponseBody(DaraModel):
    def __init__(
        self,
        honey_pot_auth_count: int = None,
        honey_pot_count: int = None,
        request_id: str = None,
    ):
        # The total quota.
        self.honey_pot_auth_count = honey_pot_auth_count
        # The quota that is consumed.
        self.honey_pot_count = honey_pot_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honey_pot_auth_count is not None:
            result['HoneyPotAuthCount'] = self.honey_pot_auth_count

        if self.honey_pot_count is not None:
            result['HoneyPotCount'] = self.honey_pot_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneyPotAuthCount') is not None:
            self.honey_pot_auth_count = m.get('HoneyPotAuthCount')

        if m.get('HoneyPotCount') is not None:
            self.honey_pot_count = m.get('HoneyPotCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

