# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdatePluginAttachmentRequest(DaraModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        enable: bool = None,
        plugin_config: str = None,
    ):
        # The IDs of the resources to which the plug-in is attached.
        self.attach_resource_ids = attach_resource_ids
        # Specifies whether to enable the plug-in.
        self.enable = enable
        # The Base64-encoded configurations of the plug-in.
        self.plugin_config = plugin_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids

        if self.enable is not None:
            result['enable'] = self.enable

        if self.plugin_config is not None:
            result['pluginConfig'] = self.plugin_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('pluginConfig') is not None:
            self.plugin_config = m.get('pluginConfig')

        return self

