# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarClawChannelResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        channel_id: str = None,
        code: int = None,
        message: str = None,
        npm_package: str = None,
        ok: bool = None,
        plugin_id: str = None,
        plugin_installed: bool = None,
        request_id: str = None,
        restarted: bool = None,
    ):
        # **The application ID.**
        self.application_id = application_id
        # The ID of the channel that was created.
        self.channel_id = channel_id
        # The response status code.
        self.code = code
        # The response message.
        self.message = message
        # The name of the installed npm package.
        self.npm_package = npm_package
        # Indicates whether the operation was successful.
        self.ok = ok
        # **The plugin ID.**
        self.plugin_id = plugin_id
        # Indicates whether a new plugin was installed.
        self.plugin_installed = plugin_installed
        # **The request ID.**
        self.request_id = request_id
        # Indicates whether the gateway was restarted.
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

        if self.npm_package is not None:
            result['NpmPackage'] = self.npm_package

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_installed is not None:
            result['PluginInstalled'] = self.plugin_installed

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

        if m.get('NpmPackage') is not None:
            self.npm_package = m.get('NpmPackage')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginInstalled') is not None:
            self.plugin_installed = m.get('PluginInstalled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Restarted') is not None:
            self.restarted = m.get('Restarted')

        return self

