# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceConfigurationSampleRequest(DaraModel):
    def __init__(
        self,
        mock_only: str = None,
        resource_type: str = None,
    ):
        self.mock_only = mock_only
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mock_only is not None:
            result['MockOnly'] = self.mock_only

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MockOnly') is not None:
            self.mock_only = m.get('MockOnly')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

