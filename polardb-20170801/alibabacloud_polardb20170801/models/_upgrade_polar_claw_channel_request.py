# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpgradePolarClawChannelRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        channel_config: Dict[str, Any] = None,
        channel_id: str = None,
        npm_package: str = None,
        plugin_id: str = None,
        restart: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The channel configuration object.
        self.channel_config = channel_config
        # The channel ID.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The npm package name of the channel plugin, including the version number.
        self.npm_package = npm_package
        # The ID of the channel plugin.
        self.plugin_id = plugin_id
        # Specifies whether to restart the gateway after the upgrade. The default value is `true`.
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.channel_config is not None:
            result['ChannelConfig'] = self.channel_config

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.npm_package is not None:
            result['NpmPackage'] = self.npm_package

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ChannelConfig') is not None:
            self.channel_config = m.get('ChannelConfig')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('NpmPackage') is not None:
            self.npm_package = m.get('NpmPackage')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

