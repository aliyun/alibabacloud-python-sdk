# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class NeuronAppClientInfo(DaraModel):
    def __init__(
        self,
        app_entry: str = None,
        app_id: int = None,
        mobi_info: main_models.MobiInfo = None,
        plugin_list: List[main_models.AppPluginInfo] = None,
        product_id: int = None,
        sidebar: str = None,
        version: str = None,
    ):
        self.app_entry = app_entry
        # This parameter is required.
        self.app_id = app_id
        self.mobi_info = mobi_info
        self.plugin_list = plugin_list
        self.product_id = product_id
        self.sidebar = sidebar
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.mobi_info:
            self.mobi_info.validate()
        if self.plugin_list:
            for v1 in self.plugin_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_entry is not None:
            result['appEntry'] = self.app_entry

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.mobi_info is not None:
            result['mobiInfo'] = self.mobi_info.to_map()

        result['pluginList'] = []
        if self.plugin_list is not None:
            for k1 in self.plugin_list:
                result['pluginList'].append(k1.to_map() if k1 else None)

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.sidebar is not None:
            result['sidebar'] = self.sidebar

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appEntry') is not None:
            self.app_entry = m.get('appEntry')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('mobiInfo') is not None:
            temp_model = main_models.MobiInfo()
            self.mobi_info = temp_model.from_map(m.get('mobiInfo'))

        self.plugin_list = []
        if m.get('pluginList') is not None:
            for k1 in m.get('pluginList'):
                temp_model = main_models.AppPluginInfo()
                self.plugin_list.append(temp_model.from_map(k1))

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('sidebar') is not None:
            self.sidebar = m.get('sidebar')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

