# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCustomRoutingEndpointGroupDestinationsResponseBody(DaraModel):
    def __init__(
        self,
        destination_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the endpoint group mappings.
        self.destination_ids = destination_ids
        # The IDs of the endpoint group mappings.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_ids is not None:
            result['DestinationIds'] = self.destination_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationIds') is not None:
            self.destination_ids = m.get('DestinationIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

