# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class EngineVersionMetadata(DaraModel):
    def __init__(
        self,
        engine_version: str = None,
        features: main_models.EngineVersionSupportedFeatures = None,
        status: str = None,
    ):
        # The engine version.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The features supported by the engine version.
        self.features = features
        # The status of the engine version.
        # 
        # *   STABLE
        # *   BETA
        # *   DEPRECATED
        # *   EXPIRED
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.features:
            self.features.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version

        if self.features is not None:
            result['features'] = self.features.to_map()

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')

        if m.get('features') is not None:
            temp_model = main_models.EngineVersionSupportedFeatures()
            self.features = temp_model.from_map(m.get('features'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

