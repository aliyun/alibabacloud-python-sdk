# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserTagMetaRequest(DaraModel):
    def __init__(
        self,
        tag_description: str = None,
        tag_name: str = None,
    ):
        # The tag description. Format requirements: The maximum length is 255 characters.
        self.tag_description = tag_description
        # The tag name. Format requirements:
        # - The maximum length is 50 characters.
        # - Only Chinese characters, English letters, digits, and the /\\|[]() symbols are allowed.
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

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

