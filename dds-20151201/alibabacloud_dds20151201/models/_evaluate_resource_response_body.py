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
        # Indicates whether the resources are sufficient in the region. Valid values:
        # 
        # *   **1**: The resources are sufficient.
        # *   **0**: The resources are insufficient.
        self.dbinstance_available = dbinstance_available
        # The database engine of the instance. Only MongoDB is returned.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The ID of the request.
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

