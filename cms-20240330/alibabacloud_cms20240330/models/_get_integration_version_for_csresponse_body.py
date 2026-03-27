# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIntegrationVersionForCSResponseBody(DaraModel):
    def __init__(
        self,
        integration_version: str = None,
        request_id: str = None,
    ):
        self.integration_version = integration_version
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integration_version is not None:
            result['integrationVersion'] = self.integration_version

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('integrationVersion') is not None:
            self.integration_version = m.get('integrationVersion')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

