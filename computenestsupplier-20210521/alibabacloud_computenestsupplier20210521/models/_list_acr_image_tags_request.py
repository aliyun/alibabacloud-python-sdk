# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAcrImageTagsRequest(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        max_results: int = None,
        next_token: str = None,
        repo_id: str = None,
    ):
        # The artifact type. The default value is AcrImage. Possible values:
        # 
        # - HelmChart: A Helm Chart image.
        # 
        # - AcrImage: A container image.
        self.artifact_type = artifact_type
        # The number of entries to return on each page. The maximum value is 100. The default value is 20.
        self.max_results = max_results
        # The token for the next page of results.
        self.next_token = next_token
        # The ID of the image repository.
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

