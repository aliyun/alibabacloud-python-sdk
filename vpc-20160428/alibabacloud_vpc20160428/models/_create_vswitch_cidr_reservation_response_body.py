# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVSwitchCidrReservationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        v_switch_cidr_reservation_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the reserved CIDR block.
        self.v_switch_cidr_reservation_id = v_switch_cidr_reservation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.v_switch_cidr_reservation_id is not None:
            result['VSwitchCidrReservationId'] = self.v_switch_cidr_reservation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VSwitchCidrReservationId') is not None:
            self.v_switch_cidr_reservation_id = m.get('VSwitchCidrReservationId')

        return self

