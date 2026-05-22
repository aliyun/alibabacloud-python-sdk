# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteArtifactRequest(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_version: str = None,
        client_token: str = None,
    ):
        # The ID of the artifact.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # The version of the artifact.
        self.artifact_version = artifact_version
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id

        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

