# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseArtifactRequest(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        client_token: str = None,
    ):
        # The artifact ID.
        # 
        # Call [ListArtifacts](https://help.aliyun.com/document_detail/469993.html) to obtain the artifact ID.
        # 
        # This parameter is required.
        self.artifact_id = artifact_id
        # A client-generated token that ensures the idempotence of the request. The token must be unique for each request. The value of **ClientToken** can contain only ASCII characters and must be no more than 64 characters in length.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

