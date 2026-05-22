# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePageShrinkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        site_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.content_type = content_type
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
        self.site_ids_shrink = site_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.site_ids_shrink is not None:
            result['SiteIds'] = self.site_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids_shrink = m.get('SiteIds')

        return self

