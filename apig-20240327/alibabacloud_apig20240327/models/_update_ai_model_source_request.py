# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAiModelSourceRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        expected_version: int = None,
        service_id: str = None,
    ):
        # The display name of the model source or model provider.
        self.display_name = display_name
        # The expected object version. Use the version returned by the most recent query.
        # 
        # This parameter is required.
        self.expected_version = expected_version
        # The ID of the actual AI service bound to the model source.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.expected_version is not None:
            result['expectedVersion'] = self.expected_version

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('expectedVersion') is not None:
            self.expected_version = m.get('expectedVersion')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

