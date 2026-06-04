# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetaEntityShrinkRequest(DaraModel):
    def __init__(
        self,
        attributes_shrink: str = None,
        comment: str = None,
        custom_attributes_shrink: str = None,
        id: str = None,
    ):
        self.attributes_shrink = attributes_shrink
        self.comment = comment
        self.custom_attributes_shrink = custom_attributes_shrink
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.custom_attributes_shrink is not None:
            result['CustomAttributes'] = self.custom_attributes_shrink

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CustomAttributes') is not None:
            self.custom_attributes_shrink = m.get('CustomAttributes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

