# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class EngineVersionMetadataIndex(DaraModel):
    def __init__(
        self,
        default_engine_version: str = None,
        engine_version_metadata: List[main_models.EngineVersionMetadata] = None,
    ):
        # The default engine version that is used for a deployment.
        self.default_engine_version = default_engine_version
        # The information about all supported engine versions.
        self.engine_version_metadata = engine_version_metadata

    def validate(self):
        if self.engine_version_metadata:
            for v1 in self.engine_version_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_engine_version is not None:
            result['defaultEngineVersion'] = self.default_engine_version

        result['engineVersionMetadata'] = []
        if self.engine_version_metadata is not None:
            for k1 in self.engine_version_metadata:
                result['engineVersionMetadata'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultEngineVersion') is not None:
            self.default_engine_version = m.get('defaultEngineVersion')

        self.engine_version_metadata = []
        if m.get('engineVersionMetadata') is not None:
            for k1 in m.get('engineVersionMetadata'):
                temp_model = main_models.EngineVersionMetadata()
                self.engine_version_metadata.append(temp_model.from_map(k1))

        return self

