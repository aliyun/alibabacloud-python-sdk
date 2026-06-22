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
        # The configuration target. This parameter is in JSON format and contains the following fields:
        # 
        # - **vulType**: The vulnerability type. Valid values:
        #      - **cve**: Linux software vulnerability.
        #     - **sys**: Windows system vulnerability.
        #     - **cms**: Web-CMS vulnerability.
        #     - **emg**: Emergency vulnerability.
        self.config = config
        # The operation target. This parameter is in JSON format and contains the following fields:
        # 
        # - **target**: The UUID of the target machine.
        # - **targetType**: The target type. Fixed value: uuid.
        # - **flag**: The flag. Valid values:
        #     - **add**: Selected.
        #     - **del**: Deselected.
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

