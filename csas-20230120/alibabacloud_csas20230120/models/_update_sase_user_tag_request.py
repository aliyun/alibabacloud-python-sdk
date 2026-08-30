# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSaseUserTagRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tag_id: str = None,
    ):
        # The description of the user tag.
        self.description = description
        # The name of the user tag.
        self.name = name
        # The ID of the user tag. You can obtain the tag ID from the following operations:
        # - [ListSaseUserTags](~~ListSaseUserTags~~): Lists user tags.
        # - [CreateSaseUserTag](~~CreateSaseUserTag~~): Creates a user tag.
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

