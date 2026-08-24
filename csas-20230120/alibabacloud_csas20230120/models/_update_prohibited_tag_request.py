# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProhibitedTagRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tag_id: str = None,
    ):
        # The description of the prohibited software tag. The description can contain letters, digits, Chinese characters, spaces, periods (.), underscores (_), and hyphens (-), and cannot exceed 128 characters in length.
        self.description = description
        # The name of the prohibited software tag. The name must be 1 to 128 characters in length and can contain letters, digits, Chinese characters, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.name = name
        # The ID of the custom prohibited software tag. Only custom tags under the current Alibaba Cloud account can be modified. Built-in system tags cannot be modified. You can obtain the value from the following operations:
        # - [ListProhibitedTags](~~ListProhibitedTags~~): Lists prohibited software tags.
        # - [CreateProhibitedTag](~~CreateProhibitedTag~~): Creates a custom prohibited software tag.
        # 
        # This parameter is required.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

