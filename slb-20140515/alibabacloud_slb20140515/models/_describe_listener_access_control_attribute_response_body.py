# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeListenerAccessControlAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_control_status: str = None,
        request_id: str = None,
        source_items: str = None,
    ):
        # Indicates whether the whitelist is enabled. Valid values:
        # 
        # *   **open_white_list**: the whitelist is enabled.
        # *   **close**: the whitelist is disabled.
        self.access_control_status = access_control_status
        # The request ID.
        self.request_id = request_id
        # The queried ACLs.
        self.source_items = source_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_control_status is not None:
            result['AccessControlStatus'] = self.access_control_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_items is not None:
            result['SourceItems'] = self.source_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlStatus') is not None:
            self.access_control_status = m.get('AccessControlStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceItems') is not None:
            self.source_items = m.get('SourceItems')

        return self

