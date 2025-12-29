# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class UpdateAttributesInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        http_trigger_config: main_models.HTTPTriggerConfig = None,
        version_id: str = None,
    ):
        self.description = description
        self.http_trigger_config = http_trigger_config
        self.version_id = version_id

    def validate(self):
        if self.http_trigger_config:
            self.http_trigger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.http_trigger_config is not None:
            result['httpTriggerConfig'] = self.http_trigger_config.to_map()

        if self.version_id is not None:
            result['versionID'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('httpTriggerConfig') is not None:
            temp_model = main_models.HTTPTriggerConfig()
            self.http_trigger_config = temp_model.from_map(m.get('httpTriggerConfig'))

        if m.get('versionID') is not None:
            self.version_id = m.get('versionID')

        return self

