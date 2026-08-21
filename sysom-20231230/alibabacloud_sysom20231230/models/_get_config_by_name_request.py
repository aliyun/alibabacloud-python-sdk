# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConfigByNameRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        config_name: str = None,
        config_type: str = None,
        entity_id: str = None,
        use_global_uid: bool = None,
        version_id: int = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The configuration name.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The type of the configuration parameter.
        # 
        # This parameter is required.
        self.config_type = config_type
        # The entity ID. Default value: "default".
        self.entity_id = entity_id
        # Specifies whether to use the global UID.
        self.use_global_uid = use_global_uid
        # The version ID.
        self.version_id = version_id
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.use_global_uid is not None:
            result['useGlobalUid'] = self.use_global_uid

        if self.version_id is not None:
            result['versionId'] = self.version_id

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('useGlobalUid') is not None:
            self.use_global_uid = m.get('useGlobalUid')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

