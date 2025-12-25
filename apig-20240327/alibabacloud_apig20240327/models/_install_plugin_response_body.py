# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class InstallPluginResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InstallPluginResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response payload.
        self.data = data
        # The status message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.InstallPluginResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class InstallPluginResponseBodyData(DaraModel):
    def __init__(
        self,
        install_plugin_results: List[main_models.InstallPluginResponseBodyDataInstallPluginResults] = None,
    ):
        # The installation result.
        self.install_plugin_results = install_plugin_results

    def validate(self):
        if self.install_plugin_results:
            for v1 in self.install_plugin_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['installPluginResults'] = []
        if self.install_plugin_results is not None:
            for k1 in self.install_plugin_results:
                result['installPluginResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.install_plugin_results = []
        if m.get('installPluginResults') is not None:
            for k1 in m.get('installPluginResults'):
                temp_model = main_models.InstallPluginResponseBodyDataInstallPluginResults()
                self.install_plugin_results.append(temp_model.from_map(k1))

        return self

class InstallPluginResponseBodyDataInstallPluginResults(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        plugin_id: str = None,
    ):
        # The gateway ID.
        self.gateway_id = gateway_id
        # The plug-in ID.
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        return self

