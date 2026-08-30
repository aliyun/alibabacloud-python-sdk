# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSaseUserTagRequest(DaraModel):
    def __init__(
        self,
        tag_id: str = None,
    ):
        # The user tag ID. You can obtain this value from the following operations:
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
        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

