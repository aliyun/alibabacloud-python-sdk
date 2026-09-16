# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateArtifactUploadTokenRequest(DaraModel):
    def __init__(
        self,
        artifact_path: str = None,
    ):
        # The artifact upload directory, relative to the digital human artifact root directory. The value can only be empty or a directory under upload/. If not specified, upload/{YYYY-MM-DD}/ is used by default.
        self.artifact_path = artifact_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_path is not None:
            result['artifactPath'] = self.artifact_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactPath') is not None:
            self.artifact_path = m.get('artifactPath')

        return self

