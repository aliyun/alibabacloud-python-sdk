# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebPathRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        target: str = None,
        type: str = None,
    ):
        # The configuration of the web directory. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **webPathType**: the type of the web directory
        # *   **webPath**: the web directory
        self.config = config
        # The protected asset to which the web directory belongs. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **target**: the protected asset.
        # *   **targetType**: the type of the asset. Set the value to uuid.
        # *   **flag**: the type of the operation.
        self.target = target
        # The type of the configuration item. Set the value to **web_path**.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

