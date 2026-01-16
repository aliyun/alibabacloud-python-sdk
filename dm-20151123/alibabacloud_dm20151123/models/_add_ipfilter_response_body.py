# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIpfilterResponseBody(DaraModel):
    def __init__(
        self,
        ip_filter_id: str = None,
        request_id: str = None,
    ):
        # ID corresponding to the IP
        self.ip_filter_id = ip_filter_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_filter_id is not None:
            result['IpFilterId'] = self.ip_filter_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpFilterId') is not None:
            self.ip_filter_id = m.get('IpFilterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

