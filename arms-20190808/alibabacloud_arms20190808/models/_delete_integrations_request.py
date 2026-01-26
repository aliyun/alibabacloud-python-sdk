# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIntegrationsRequest(DaraModel):
    def __init__(
        self,
        integration_id: int = None,
    ):
        # The ID of the alert integration.
        # 
        # This parameter is required.
        self.integration_id = integration_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')

        return self

