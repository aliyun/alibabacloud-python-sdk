# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNormalizationSchemaRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        normalization_schema_id: str = None,
        normalization_schema_type: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_schema_id = normalization_schema_id
        self.normalization_schema_type = normalization_schema_type
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

