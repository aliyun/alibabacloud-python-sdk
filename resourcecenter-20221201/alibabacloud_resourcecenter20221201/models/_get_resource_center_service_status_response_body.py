# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceCenterServiceStatusResponseBody(DaraModel):
    def __init__(
        self,
        initial_status: str = None,
        request_id: str = None,
        service_status: str = None,
    ):
        # The initialization status. Valid values:
        # 
        # - Pending
        # 
        # - Finished
        self.initial_status = initial_status
        # The request ID.
        self.request_id = request_id
        # The service status. Valid values:
        # 
        # - Enabled
        # 
        # - Disabled
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.initial_status is not None:
            result['InitialStatus'] = self.initial_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialStatus') is not None:
            self.initial_status = m.get('InitialStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        return self

