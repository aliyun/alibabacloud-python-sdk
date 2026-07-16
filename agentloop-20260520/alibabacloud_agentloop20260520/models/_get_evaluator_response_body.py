# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetEvaluatorResponseBody(DaraModel):
    def __init__(
        self,
        evaluator: main_models.GetEvaluatorResponseBodyEvaluator = None,
        request_id: str = None,
    ):
        # The evaluator details.
        self.evaluator = evaluator
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.evaluator:
            self.evaluator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluator is not None:
            result['evaluator'] = self.evaluator.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('evaluator') is not None:
            temp_model = main_models.GetEvaluatorResponseBodyEvaluator()
            self.evaluator = temp_model.from_map(m.get('evaluator'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetEvaluatorResponseBodyEvaluator(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        annotations: List[str] = None,
        config: Dict[str, Any] = None,
        created_at: int = None,
        current_version: str = None,
        description: str = None,
        display_name: str = None,
        latest_version: str = None,
        metric_name: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        type: str = None,
        updated_at: int = None,
        versions: List[main_models.GetEvaluatorResponseBodyEvaluatorVersions] = None,
    ):
        # The AgentSpace name.
        self.agent_space = agent_space
        # The list of annotations.
        self.annotations = annotations
        # The configuration of the current version.
        self.config = config
        # The time when the evaluator was created. The value is a UNIX timestamp in seconds.
        self.created_at = created_at
        # The version number returned in the current response.
        self.current_version = current_version
        # The evaluator description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The latest version number.
        self.latest_version = latest_version
        # The evaluation metric name.
        self.metric_name = metric_name
        # The evaluator name.
        self.name = name
        # The evaluator properties.
        self.properties = properties
        # The evaluator type.
        self.type = type
        # The time when the evaluator was last updated. The value is a UNIX timestamp in seconds.
        self.updated_at = updated_at
        # The list of versions.
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.config is not None:
            result['config'] = self.config

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.current_version is not None:
            result['currentVersion'] = self.current_version

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.name is not None:
            result['name'] = self.name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.GetEvaluatorResponseBodyEvaluatorVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class GetEvaluatorResponseBodyEvaluatorVersions(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        version: str = None,
        version_description: str = None,
    ):
        # The time when the version was created. The value is a UNIX timestamp in seconds.
        self.created_at = created_at
        # The version number.
        self.version = version
        # The version description.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        return self

