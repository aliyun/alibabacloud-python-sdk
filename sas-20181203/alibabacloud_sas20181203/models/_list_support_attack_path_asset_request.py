# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSupportAttackPathAssetRequest(DaraModel):
    def __init__(
        self,
        node_type: str = None,
        path_name: str = None,
        path_type: str = None,
        support_type: str = None,
    ):
        # Node type, with values:
        # - **start**: Start point.
        # - **end**: End point.
        self.node_type = node_type
        # Path name.
        # 
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path names.
        self.path_name = path_name
        # Path type.
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path types.
        self.path_type = path_type
        # Support type, with values:
        # - **event**: Attack path alert event.
        # - **whitelist**: Attack path whitelist.
        # - **sensitive**: Sensitive assets in the attack path.
        # 
        # This parameter is required.
        self.support_type = support_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.path_name is not None:
            result['PathName'] = self.path_name

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.support_type is not None:
            result['SupportType'] = self.support_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('SupportType') is not None:
            self.support_type = m.get('SupportType')

        return self

