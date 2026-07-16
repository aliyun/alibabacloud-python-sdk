# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProcessDefinitionsRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The type of the process definition. Valid values:
        # 
        # - MaxCompute
        # 
        # - DataService
        # 
        # - Extension
        # 
        # - Hologres
        # 
        # - EMR (You cannot create custom definitions for this type.)
        # 
        # - DataAssetGovernance (You cannot create custom definitions for this type.)
        # 
        # - Lindorm (You cannot create custom definitions for this type.)
        # 
        # - DlfNext (You cannot create custom definitions for this type.)
        # 
        # - DlfV1 (You cannot create custom definitions for this type.)
        # 
        # - StarRocks (You cannot create custom definitions for this type.)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

