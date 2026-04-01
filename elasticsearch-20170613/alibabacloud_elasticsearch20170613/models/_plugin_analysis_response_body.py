# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class PluginAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.PluginAnalysisResponseBodyResult] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.PluginAnalysisResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class PluginAnalysisResponseBodyResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        elasticsearch_version: str = None,
        name: str = None,
        security_policy: str = None,
        version: str = None,
    ):
        self.description = description
        self.elasticsearch_version = elasticsearch_version
        self.name = name
        self.security_policy = security_policy
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.elasticsearch_version is not None:
            result['elasticsearchVersion'] = self.elasticsearch_version

        if self.name is not None:
            result['name'] = self.name

        if self.security_policy is not None:
            result['securityPolicy'] = self.security_policy

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elasticsearchVersion') is not None:
            self.elasticsearch_version = m.get('elasticsearchVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('securityPolicy') is not None:
            self.security_policy = m.get('securityPolicy')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

