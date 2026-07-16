# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateResourceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_available: str = None,
        engine: str = None,
        engine_version: str = None,
        request_id: str = None,
    ):
        # Indicates whether resources are available in the current region. Valid values:
        # 
        # - **1**: Resources are sufficient.
        # 
        # - **0**: Resources are insufficient.
        self.dbinstance_available = dbinstance_available
        # The database engine. The value is fixed to MongoDB.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_available is not None:
            result['DBInstanceAvailable'] = self.dbinstance_available

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceAvailable') is not None:
            self.dbinstance_available = m.get('DBInstanceAvailable')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

