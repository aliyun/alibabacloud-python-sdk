# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class UpdateMetaEntityRequest(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        comment: str = None,
        custom_attributes: Dict[str, List[str]] = None,
        id: str = None,
    ):
        self.attributes = attributes
        self.comment = comment
        self.custom_attributes = custom_attributes
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

