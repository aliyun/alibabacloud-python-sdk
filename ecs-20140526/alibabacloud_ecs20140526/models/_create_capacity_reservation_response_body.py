# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCapacityReservationResponseBody(DaraModel):
    def __init__(
        self,
        private_pool_options_id: str = None,
        request_id: str = None,
    ):
        # The capacity reservation ID.
        self.private_pool_options_id = private_pool_options_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options_id is not None:
            result['PrivatePoolOptionsId'] = self.private_pool_options_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptionsId') is not None:
            self.private_pool_options_id = m.get('PrivatePoolOptionsId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

