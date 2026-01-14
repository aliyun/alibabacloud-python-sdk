# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserTagMetaRequest(DaraModel):
    def __init__(
        self,
        tag_description: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        # The tag description.
        # 
        # - Format check: Maximum length is 255 characters.
        self.tag_description = tag_description
        # The specified TagID.
        # 
        # - Format check: Maximum length is 64 characters.
        # 
        # This parameter is required.
        self.tag_id = tag_id
        # The tag name.
        # - Format check: Maximum length is 50 characters.
        # - Only Chinese, English, numbers, and /\\|[]() symbols are allowed.
        # 
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

