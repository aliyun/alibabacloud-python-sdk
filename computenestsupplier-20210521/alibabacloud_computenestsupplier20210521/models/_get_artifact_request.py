# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetArtifactRequest(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_name: str = None,
        artifact_version: str = None,
    ):
        # The ID of the artifact.
        # 
        # Call [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) to obtain the artifact ID.
        self.artifact_id = artifact_id
        # The name of the artifact.
        # 
        # Call [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) to obtain the artifact name.
        self.artifact_name = artifact_name
        # The version of the artifact.
        # 
        # Call [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) to obtain the artifact version.
        self.artifact_version = artifact_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_name is not None:
            result['ArtifactName'] = self.artifact_name

        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactName') is not None:
            self.artifact_name = m.get('ArtifactName')

        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')

        return self

