# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePluginResponseBody(DaraModel):
    def __init__(
        self,
        plugin_id: str = None,
        request_id: str = None,
        tag_status: bool = None,
    ):
        # The ID of the plug-in.
        self.plugin_id = plugin_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the plug-in is successfully marked.
        self.tag_status = tag_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_status is not None:
            result['TagStatus'] = self.tag_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagStatus') is not None:
            self.tag_status = m.get('TagStatus')

        return self

