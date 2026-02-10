# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrivateRegistryListRequest(DaraModel):
    def __init__(
        self,
        registry_type: str = None,
    ):
        # The type of the image repository. Valid values:
        # 
        # *   **acr**: Container Registry
        # *   **harbor**: Harbor
        # *   **quay**: Quay
        # *   **CI/CD**: Jenkins
        self.registry_type = registry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        return self

