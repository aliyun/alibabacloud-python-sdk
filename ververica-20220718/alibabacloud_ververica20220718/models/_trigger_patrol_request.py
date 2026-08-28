# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class TriggerPatrolRequest(DaraModel):
    def __init__(
        self,
        scope_config: main_models.TriggerPatrolRequestScopeConfig = None,
        scope_type: str = None,
    ):
        # The inspection scope configuration.
        self.scope_config = scope_config
        # The inspection scope type.
        # 
        # This parameter is required.
        self.scope_type = scope_type

    def validate(self):
        if self.scope_config:
            self.scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope_config is not None:
            result['scopeConfig'] = self.scope_config.to_map()

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scopeConfig') is not None:
            temp_model = main_models.TriggerPatrolRequestScopeConfig()
            self.scope_config = temp_model.from_map(m.get('scopeConfig'))

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        return self

class TriggerPatrolRequestScopeConfig(DaraModel):
    def __init__(
        self,
        deployment_ids: List[str] = None,
        tags: Dict[str, List[str]] = None,
    ):
        # The list of deployment IDs. This parameter is valid only when scopeType is set to DEPLOYMENTS.
        self.deployment_ids = deployment_ids
        # The tag mapping. This parameter is valid only when scopeType is set to TAGS. The key is the tag name, and the value is a list of tag values.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_ids is not None:
            result['deploymentIds'] = self.deployment_ids

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentIds') is not None:
            self.deployment_ids = m.get('deploymentIds')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

