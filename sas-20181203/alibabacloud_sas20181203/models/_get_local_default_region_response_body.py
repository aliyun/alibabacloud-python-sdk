# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLocalDefaultRegionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The access type of the multi-cloud site. Valid values:
        # 
        # *   **0**: The current site is not the default site of the multi-cloud site. You can specify a site as the default site of the multi-cloud site.
        # *   **1**: The current site is the default site of the multi-cloud site.
        # *   **2**: Another site is set as the default site of the multi-cloud site.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

