# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCommonSwitchConfigRequest(DaraModel):
    def __init__(
        self,
        target_default: str = None,
        type: str = None,
    ):
        # Specifies whether to turn on the switch for newly added servers. Valid values:
        # 
        # *   **add**: yes
        # *   **del**: no
        self.target_default = target_default
        # The type of the switch.
        # 
        # >  You can call the [ListClientUserDefineRules](~~ListClientUserDefineRules~~) or [ListSystemClientRules](~~ListSystemClientRules~~) operation to obtain the type from the response parameter SwitchId.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_default is not None:
            result['TargetDefault'] = self.target_default

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetDefault') is not None:
            self.target_default = m.get('TargetDefault')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

