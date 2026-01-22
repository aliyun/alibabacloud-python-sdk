# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParameterTemplatesRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        engine_version: str = None,
        param_level: str = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.engine_version = engine_version
        self.param_level = param_level
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.param_level is not None:
            result['ParamLevel'] = self.param_level

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

