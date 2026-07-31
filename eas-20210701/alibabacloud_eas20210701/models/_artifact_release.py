# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ArtifactRelease(DaraModel):
    def __init__(
        self,
        artifact_ref: str = None,
        created_at: str = None,
        description: str = None,
        image: str = None,
        type: str = None,
        version: str = None,
    ):
        self.artifact_ref = artifact_ref
        self.created_at = created_at
        self.description = description
        self.image = image
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_ref is not None:
            result['ArtifactRef'] = self.artifact_ref

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.image is not None:
            result['Image'] = self.image

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactRef') is not None:
            self.artifact_ref = m.get('ArtifactRef')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

