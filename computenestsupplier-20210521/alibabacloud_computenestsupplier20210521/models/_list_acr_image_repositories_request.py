# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAcrImageRepositoriesRequest(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        max_results: int = None,
        next_token: str = None,
        repo_name: str = None,
    ):
        # The type of the artifact. Default value: AcrImage. Valid values:
        # 
        # *   HelmChart: Helm chart image.
        # *   AcrImage: container image.
        self.artifact_type = artifact_type
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The name of the image repository.
        self.repo_name = repo_name

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

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        return self

