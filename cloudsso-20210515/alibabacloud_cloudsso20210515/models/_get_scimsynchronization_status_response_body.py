# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSCIMSynchronizationStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scimsynchronization_status: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The status of SCIM synchronization. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.scimsynchronization_status = scimsynchronization_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scimsynchronization_status is not None:
            result['SCIMSynchronizationStatus'] = self.scimsynchronization_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SCIMSynchronizationStatus') is not None:
            self.scimsynchronization_status = m.get('SCIMSynchronizationStatus')

        return self

