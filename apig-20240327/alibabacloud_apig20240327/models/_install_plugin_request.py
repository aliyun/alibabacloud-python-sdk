# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallPluginRequest(DaraModel):
    def __init__(
        self,
        gateway_ids: List[str] = None,
        plugin_class_id: str = None,
    ):
        # The list of gateway IDs.
        self.gateway_ids = gateway_ids
        # The plug-in type ID.
        self.plugin_class_id = plugin_class_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_ids is not None:
            result['gatewayIds'] = self.gateway_ids

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayIds') is not None:
            self.gateway_ids = m.get('gatewayIds')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        return self

