# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        name: str = None,
        site_ids: List[int] = None,
    ):
        # The page content, which must be provided in BASE64 encoding. For example, the value PGh0bWw+aGVsbG8gcGFnZTwvaHRtbD4= decodes to \\<html>hello page\\</html>.
        self.content = content
        # The `Content-Type` HTTP header. Examples:
        # 
        # - text/html
        # 
        # - application/json
        # 
        # This parameter is required.
        self.content_type = content_type
        # The description of the page.
        self.description = description
        # The name of the custom error page.
        # 
        # This parameter is required.
        self.name = name
        self.site_ids = site_ids

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

        if self.name is not None:
            result['Name'] = self.name

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        return self

