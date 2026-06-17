# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallPolarClawPluginRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        npm_package: str = None,
        plugin_id: str = None,
        restart: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The npm package name, including the version number.
        # 
        # This parameter is required.
        self.npm_package = npm_package
        # The plugin ID.
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        # Specifies whether to restart the gateway after installation. Defaults to true.
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

        if m.get('NpmPackage') is not None:
            self.npm_package = m.get('NpmPackage')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

