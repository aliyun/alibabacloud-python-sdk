# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceNews(DaraModel):
    def __init__(
        self,
        date: int = None,
        description: str = None,
        image: str = None,
        link: str = None,
        title: str = None,
    ):
        self.date = date
        self.description = description
        self.image = image
        self.link = link
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.description is not None:
            result['description'] = self.description

        if self.image is not None:
            result['image'] = self.image

        if self.link is not None:
            result['link'] = self.link

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

