# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class UpdateEvaluatorRequest(DaraModel):
    def __init__(
        self,
        annotations: List[str] = None,
        config: Dict[str, Any] = None,
        description: str = None,
        display_name: str = None,
        properties: Dict[str, Any] = None,
        version: str = None,
        version_description: str = None,
        client_token: str = None,
    ):
        # The list of annotation marks.
        self.annotations = annotations
        # The new version configuration. This parameter is typically required when `version` is specified.
        self.config = config
        # The evaluator description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The evaluator properties.
        self.properties = properties
        # The new version number. If specified, a new version is created.
        self.version = version
        # The version description.
        self.version_description = version_description
        # The idempotency token. CloudSpec declares this query parameter, but the backend does not currently perform idempotency comparison.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

