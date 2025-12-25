# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDashboardShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        api_id: str = None,
        filter_shrink: str = None,
        name: str = None,
        plugin_class_id: str = None,
        plugin_id: str = None,
        route_id: str = None,
        source: str = None,
        upstream_cluster: str = None,
    ):
        # The language. Valid values: zh (Chinese) and en (English).
        self.accept_language = accept_language
        # API ID
        self.api_id = api_id
        # The filter configurations.
        self.filter_shrink = filter_shrink
        # The dashboard name.
        # 
        # *   LOG: access logs
        # *   PLUGIN: plug-in logs
        self.name = name
        # The plug-in ID.
        self.plugin_class_id = plugin_class_id
        self.plugin_id = plugin_id
        self.route_id = route_id
        # The dashboard source. Valid values:
        # 
        # *   SLS: Simple Log Service
        self.source = source
        self.upstream_cluster = upstream_cluster

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language

        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink

        if self.name is not None:
            result['name'] = self.name

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.route_id is not None:
            result['routeId'] = self.route_id

        if self.source is not None:
            result['source'] = self.source

        if self.upstream_cluster is not None:
            result['upstreamCluster'] = self.upstream_cluster

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')

        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('upstreamCluster') is not None:
            self.upstream_cluster = m.get('upstreamCluster')

        return self

