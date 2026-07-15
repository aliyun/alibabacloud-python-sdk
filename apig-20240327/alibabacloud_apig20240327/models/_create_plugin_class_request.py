# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePluginClassRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        execute_priority: int = None,
        execute_stage: str = None,
        name: str = None,
        supported_min_gateway_version: str = None,
        version: str = None,
        version_description: str = None,
        wasm_language: str = None,
        wasm_url: str = None,
    ):
        # The alias of the plugin.
        self.alias = alias
        # The description of the plugin.
        # 
        # This parameter is required.
        self.description = description
        # The execution priority of the plugin.
        self.execute_priority = execute_priority
        # The execution stage of the plugin.
        # 
        # This parameter is required.
        self.execute_stage = execute_stage
        # The name of the plugin class.
        # 
        # This parameter is required.
        self.name = name
        # The minimum gateway version that the plugin is compatible with.
        self.supported_min_gateway_version = supported_min_gateway_version
        # The version number of the plugin.
        # 
        # This parameter is required.
        self.version = version
        # The description of the current version.
        # 
        # This parameter is required.
        self.version_description = version_description
        # The programming language used to develop the WASM plugin.
        # 
        # This parameter is required.
        self.wasm_language = wasm_language
        # The download URL of the WASM plugin binary file.
        # 
        # This parameter is required.
        self.wasm_url = wasm_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority

        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage

        if self.name is not None:
            result['name'] = self.name

        if self.supported_min_gateway_version is not None:
            result['supportedMinGatewayVersion'] = self.supported_min_gateway_version

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        if self.wasm_language is not None:
            result['wasmLanguage'] = self.wasm_language

        if self.wasm_url is not None:
            result['wasmUrl'] = self.wasm_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')

        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('supportedMinGatewayVersion') is not None:
            self.supported_min_gateway_version = m.get('supportedMinGatewayVersion')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        if m.get('wasmLanguage') is not None:
            self.wasm_language = m.get('wasmLanguage')

        if m.get('wasmUrl') is not None:
            self.wasm_url = m.get('wasmUrl')

        return self

