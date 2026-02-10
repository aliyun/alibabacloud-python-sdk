# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListClusterPluginInfoRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        lang: str = None,
        plugin_name: str = None,
    ):
        # The IDs of the clusters.
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the plug-in.
        self.plugin_name = plugin_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        return self

