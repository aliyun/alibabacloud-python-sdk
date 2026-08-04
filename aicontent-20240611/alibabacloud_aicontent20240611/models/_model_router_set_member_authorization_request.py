# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterSetMemberAuthorizationRequest(DaraModel):
    def __init__(
        self,
        allowed_model_group_config: str = None,
        allowed_models: str = None,
    ):
        # The authorization configuration (JSON string, overwrite mode): {"model_ids":[...],"group_ids":["mg_xxx"]}. The internal key names use a fixed underscore style and are not converted to the camelCase convention used by the API. If this field is specified together with allowedModels, this field takes precedence.
        self.allowed_model_group_config = allowed_model_group_config
        # The legacy authorization field (comma-separated numeric model IDs). This field is retained during the canary release of group-based authorization: tenants that have not enabled the grouping feature continue to use this field. If this field is specified together with allowedModelGroupConfig, the latter takes precedence.
        self.allowed_models = allowed_models

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_model_group_config is not None:
            result['allowedModelGroupConfig'] = self.allowed_model_group_config

        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModelGroupConfig') is not None:
            self.allowed_model_group_config = m.get('allowedModelGroupConfig')

        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        return self

