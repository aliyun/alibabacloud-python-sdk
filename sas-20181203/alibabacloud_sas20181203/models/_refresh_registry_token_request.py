# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshRegistryTokenRequest(DaraModel):
    def __init__(
        self,
        registry_id: int = None,
    ):
        # The ID of the image repository.
        # 
        # >  You can call the [PageImageRegistry](~~PageImageRegistry~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.registry_id = registry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registry_id is not None:
            result['RegistryId'] = self.registry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistryId') is not None:
            self.registry_id = m.get('RegistryId')

        return self

