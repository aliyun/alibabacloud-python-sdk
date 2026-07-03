# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PluginClassInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        config_example: str = None,
        description: str = None,
        execute_priority: int = None,
        execute_stage: str = None,
        image_name: str = None,
        inner_plugin: bool = None,
        mode: str = None,
        name: str = None,
        plugin_class_id: str = None,
        source: str = None,
        supported_min_gateway_version: str = None,
        type: str = None,
        version: str = None,
        version_description: str = None,
        wasm_language: str = None,
        wasm_url: str = None,
    ):
        # The plugin class alias.
        self.alias = alias
        # The configuration example (JSON string).
        self.config_example = config_example
        # The plugin class description.
        self.description = description
        # The execution priority.
        self.execute_priority = execute_priority
        # The execution stage.
        self.execute_stage = execute_stage
        # The Wasm image name.
        self.image_name = image_name
        # Indicates whether the plugin is a built-in plugin.
        self.inner_plugin = inner_plugin
        # The plugin running mode.
        self.mode = mode
        # The plugin class name.
        self.name = name
        # The plugin class ID.
        self.plugin_class_id = plugin_class_id
        # The plugin source.
        self.source = source
        # The minimum supported gateway DPI engine version.
        self.supported_min_gateway_version = supported_min_gateway_version
        # The plugin type category.
        self.type = type
        # The plugin version number.
        self.version = version
        # The version description.
        self.version_description = version_description
        # The Wasm programming language.
        self.wasm_language = wasm_language
        # The Wasm file download URL.
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

        if self.config_example is not None:
            result['configExample'] = self.config_example

        if self.description is not None:
            result['description'] = self.description

        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority

        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage

        if self.image_name is not None:
            result['imageName'] = self.image_name

        if self.inner_plugin is not None:
            result['innerPlugin'] = self.inner_plugin

        if self.mode is not None:
            result['mode'] = self.mode

        if self.name is not None:
            result['name'] = self.name

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        if self.source is not None:
            result['source'] = self.source

        if self.supported_min_gateway_version is not None:
            result['supportedMinGatewayVersion'] = self.supported_min_gateway_version

        if self.type is not None:
            result['type'] = self.type

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

        if m.get('configExample') is not None:
            self.config_example = m.get('configExample')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')

        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')

        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')

        if m.get('innerPlugin') is not None:
            self.inner_plugin = m.get('innerPlugin')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('supportedMinGatewayVersion') is not None:
            self.supported_min_gateway_version = m.get('supportedMinGatewayVersion')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        if m.get('wasmLanguage') is not None:
            self.wasm_language = m.get('wasmLanguage')

        if m.get('wasmUrl') is not None:
            self.wasm_url = m.get('wasmUrl')

        return self

