# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateHttpApiVersionRequest(DaraModel):
    def __init__(
        self,
        version_config: main_models.HttpApiVersionConfig = None,
    ):
        self.version_config = version_config

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('versionConfig') is not None:
            temp_model = main_models.HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m.get('versionConfig'))

        return self

