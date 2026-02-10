# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVulTargetRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        target: str = None,
    ):
        # The configurations. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **vulType**: the type of the vulnerabilities to scan. Valid values:
        # 
        #     *   **cve**: Linux software vulnerabilities
        #     *   **sys**: Windows system vulnerabilities
        #     *   **cms**: Web-CMS vulnerabilities
        #     *   **emg**: urgent vulnerabilities
        self.config = config
        # The operation. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **target**: the UUID of the server.
        # 
        # *   **targetType**: the application scope of the operation. Set the value to uuid.
        # 
        # *   **flag**: the type of the operation. Valid values:
        # 
        #     *   **add**: select
        #     *   **del**: deselect
        self.target = target

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

