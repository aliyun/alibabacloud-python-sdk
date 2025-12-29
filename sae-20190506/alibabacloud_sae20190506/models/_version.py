# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Version(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        image: str = None,
        last_modified_time: str = None,
        request_id: str = None,
        version_id: str = None,
        weight: float = None,
    ):
        self.created_time = created_time
        self.description = description
        self.image = image
        self.last_modified_time = last_modified_time
        self.request_id = request_id
        self.version_id = version_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.image is not None:
            result['image'] = self.image

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.version_id is not None:
            result['versionId'] = self.version_id

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

