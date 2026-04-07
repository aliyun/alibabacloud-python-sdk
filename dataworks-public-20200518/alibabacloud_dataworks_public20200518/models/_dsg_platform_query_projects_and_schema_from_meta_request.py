# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgPlatformQueryProjectsAndSchemaFromMetaRequest(DaraModel):
    def __init__(
        self,
        engine_name: str = None,
    ):
        # The type of the compute engine. Valid values:
        # 
        # *   ODPS.ODPS
        # *   EMR
        # *   HOLO.POSTGRES
        # 
        # This parameter is required.
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        return self

