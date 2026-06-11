# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiNetworkSearchConfig(DaraModel):
    def __init__(
        self,
        default_enable: bool = None,
        default_lang: str = None,
        need_reference: bool = None,
        plugin_status: main_models.AiPluginStatus = None,
        reference_format: str = None,
        reference_location: str = None,
        search_engine_config: main_models.AiNetworkConfigSearchEngine = None,
        search_from: List[main_models.AiNetworkConfigSearchEngine] = None,
        search_rewrite: main_models.AiNetworkSearchConfigSearchRewrite = None,
    ):
        # Whether the network search feature is enabled by default.
        self.default_enable = default_enable
        # The default language for the search query.
        self.default_lang = default_lang
        # Whether to include references in the search results.
        self.need_reference = need_reference
        # The status of the AI plugin.
        self.plugin_status = plugin_status
        # The format of the references.
        self.reference_format = reference_format
        # The location of the references in the response.
        self.reference_location = reference_location
        # The search engine configuration.
        self.search_engine_config = search_engine_config
        # A list of search engine configurations for the network search.
        self.search_from = search_from
        # Configuration for search query rewriting.
        self.search_rewrite = search_rewrite

    def validate(self):
        if self.plugin_status:
            self.plugin_status.validate()
        if self.search_engine_config:
            self.search_engine_config.validate()
        if self.search_from:
            for v1 in self.search_from:
                 if v1:
                    v1.validate()
        if self.search_rewrite:
            self.search_rewrite.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_enable is not None:
            result['defaultEnable'] = self.default_enable

        if self.default_lang is not None:
            result['defaultLang'] = self.default_lang

        if self.need_reference is not None:
            result['needReference'] = self.need_reference

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.reference_format is not None:
            result['referenceFormat'] = self.reference_format

        if self.reference_location is not None:
            result['referenceLocation'] = self.reference_location

        if self.search_engine_config is not None:
            result['searchEngineConfig'] = self.search_engine_config.to_map()

        result['searchFrom'] = []
        if self.search_from is not None:
            for k1 in self.search_from:
                result['searchFrom'].append(k1.to_map() if k1 else None)

        if self.search_rewrite is not None:
            result['searchRewrite'] = self.search_rewrite.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultEnable') is not None:
            self.default_enable = m.get('defaultEnable')

        if m.get('defaultLang') is not None:
            self.default_lang = m.get('defaultLang')

        if m.get('needReference') is not None:
            self.need_reference = m.get('needReference')

        if m.get('pluginStatus') is not None:
            temp_model = main_models.AiPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('referenceFormat') is not None:
            self.reference_format = m.get('referenceFormat')

        if m.get('referenceLocation') is not None:
            self.reference_location = m.get('referenceLocation')

        if m.get('searchEngineConfig') is not None:
            temp_model = main_models.AiNetworkConfigSearchEngine()
            self.search_engine_config = temp_model.from_map(m.get('searchEngineConfig'))

        self.search_from = []
        if m.get('searchFrom') is not None:
            for k1 in m.get('searchFrom'):
                temp_model = main_models.AiNetworkConfigSearchEngine()
                self.search_from.append(temp_model.from_map(k1))

        if m.get('searchRewrite') is not None:
            temp_model = main_models.AiNetworkSearchConfigSearchRewrite()
            self.search_rewrite = temp_model.from_map(m.get('searchRewrite'))

        return self

class AiNetworkSearchConfigSearchRewrite(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        max_count: int = None,
        model_name: str = None,
        service_id: str = None,
        timeout_millisecond: int = None,
    ):
        # Whether to enable the search query rewrite feature.
        self.enable = enable
        # The maximum number of rewritten queries to generate.
        self.max_count = max_count
        # The name of the model to use for query rewriting.
        self.model_name = model_name
        # The ID of the query rewriting service.
        self.service_id = service_id
        # Timeout for the query rewriting operation, in milliseconds.
        self.timeout_millisecond = timeout_millisecond

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.max_count is not None:
            result['maxCount'] = self.max_count

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('maxCount') is not None:
            self.max_count = m.get('maxCount')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        return self

