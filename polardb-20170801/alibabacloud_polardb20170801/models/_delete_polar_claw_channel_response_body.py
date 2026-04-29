# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolarClawChannelResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        channel_id: str = None,
        code: int = None,
        message: str = None,
        ok: bool = None,
        plugin_id: str = None,
        plugin_uninstalled: bool = None,
        request_id: str = None,
        restarted: bool = None,
    ):
        self.application_id = application_id
        self.channel_id = channel_id
        self.code = code
        self.message = message
        self.ok = ok
        self.plugin_id = plugin_id
        self.plugin_uninstalled = plugin_uninstalled
        self.request_id = request_id
        self.restarted = restarted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_uninstalled is not None:
            result['PluginUninstalled'] = self.plugin_uninstalled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restarted is not None:
            result['Restarted'] = self.restarted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginUninstalled') is not None:
            self.plugin_uninstalled = m.get('PluginUninstalled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Restarted') is not None:
            self.restarted = m.get('Restarted')

        return self

