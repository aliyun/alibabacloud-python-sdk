# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ListArtifactsResponseBody(DaraModel):
    def __init__(
        self,
        artifacts: List[main_models.ListArtifactsResponseBodyArtifacts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.artifacts = artifacts
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['artifacts'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifacts = []
        if m.get('artifacts') is not None:
            for k1 in m.get('artifacts'):
                temp_model = main_models.ListArtifactsResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListArtifactsResponseBodyArtifacts(DaraModel):
    def __init__(
        self,
        is_directory: bool = None,
        last_modified: str = None,
        path: str = None,
        size: int = None,
    ):
        self.is_directory = is_directory
        self.last_modified = last_modified
        self.path = path
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_directory is not None:
            result['isDirectory'] = self.is_directory

        if self.last_modified is not None:
            result['lastModified'] = self.last_modified

        if self.path is not None:
            result['path'] = self.path

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isDirectory') is not None:
            self.is_directory = m.get('isDirectory')

        if m.get('lastModified') is not None:
            self.last_modified = m.get('lastModified')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

