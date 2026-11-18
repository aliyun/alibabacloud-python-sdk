# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiStatisticsConfig(DaraModel):
    def __init__(
        self,
        log_request_content: bool = None,
        log_response_content: bool = None,
        path_field_configs: List[main_models.AiStatisticsConfigPathFieldConfigs] = None,
    ):
        # **[Deprecated]** Specifies whether to record the request content (controls whether question-related attributes are generated). This field is deprecated in new versions.
        self.log_request_content = log_request_content
        # **[Deprecated]** Specifies whether to record the response content (controls whether answer-related attributes are generated). This field is deprecated in new versions.
        self.log_response_content = log_response_content
        # The list of AI request log field collection configurations, configured by API path.
        self.path_field_configs = path_field_configs

    def validate(self):
        if self.path_field_configs:
            for v1 in self.path_field_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_request_content is not None:
            result['logRequestContent'] = self.log_request_content

        if self.log_response_content is not None:
            result['logResponseContent'] = self.log_response_content

        result['pathFieldConfigs'] = []
        if self.path_field_configs is not None:
            for k1 in self.path_field_configs:
                result['pathFieldConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestContent') is not None:
            self.log_request_content = m.get('logRequestContent')

        if m.get('logResponseContent') is not None:
            self.log_response_content = m.get('logResponseContent')

        self.path_field_configs = []
        if m.get('pathFieldConfigs') is not None:
            for k1 in m.get('pathFieldConfigs'):
                temp_model = main_models.AiStatisticsConfigPathFieldConfigs()
                self.path_field_configs.append(temp_model.from_map(k1))

        return self

class AiStatisticsConfigPathFieldConfigs(DaraModel):
    def __init__(
        self,
        field_paths: Dict[str, main_models.AiStatisticsPathField] = None,
        path: str = None,
    ):
        # The AI request log field configuration groups corresponding to the API path, passed as a map. The valid keys for the map are fixed to basic and custom, and the values are arrays of log field configurations for the corresponding groups. basic indicates basic log fields, and custom indicates custom log fields. For the current API path, fieldPaths represents the complete desired state of the field configuration. Incremental appending or diff merging is not supported.
        # 
        # If pathFieldConfigs is not passed, is passed as null, or is passed as an empty array, the existing log field configurations are not updated. If a non-empty array is passed, a desired state replacement is performed based on the complete set of paths in the request, and historical path configurations not included in the request are deleted.
        # 
        # For example, to add a custom field named test to the /v1/chat/completions API path based on the existing configuration, the caller must use the read-merge-full write-back approach:
        # 1. Read all current path configurations.
        # 2. Retain the current complete basic and custom arrays for the target API path /v1/chat/completions.
        # 3. Append test to the current custom array.
        # 4. Retain the configurations for other API paths as they are.
        # 5. Submit the merged and complete pathFieldConfigs.
        self.field_paths = field_paths
        # The API path.
        self.path = path

    def validate(self):
        if self.field_paths:
            for v1 in self.field_paths.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['fieldPaths'] = {}
        if self.field_paths is not None:
            for k1, v1 in self.field_paths.items():
                result['fieldPaths'][k1] = v1.to_map() if v1 else None

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_paths = {}
        if m.get('fieldPaths') is not None:
            for k1, v1 in m.get('fieldPaths').items():
                temp_model = main_models.AiStatisticsPathField()
                self.field_paths[k1] = temp_model.from_map(v1)

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

