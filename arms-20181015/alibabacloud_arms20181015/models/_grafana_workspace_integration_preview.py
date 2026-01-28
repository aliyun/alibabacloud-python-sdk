# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceIntegrationPreview(DaraModel):
    def __init__(
        self,
        id: str = None,
        image: str = None,
        name: str = None,
        thumbnail: str = None,
    ):
        self.id = id
        self.image = image
        self.name = name
        self.thumbnail = thumbnail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.image is not None:
            result['image'] = self.image

        if self.name is not None:
            result['name'] = self.name

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        return self

