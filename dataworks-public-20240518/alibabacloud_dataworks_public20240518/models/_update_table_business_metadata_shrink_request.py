# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTableBusinessMetadataShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_attributes_shrink: str = None,
        id: str = None,
        readme: str = None,
    ):
        # The custom attribute values. The key is the custom attribute identifier, and the value contains at most one element. An empty list indicates that the attribute value is deleted. Passing this parameter without Readme prevents the usage description from being cleared. An empty object indicates that custom attributes are not updated.
        self.custom_attributes_shrink = custom_attributes_shrink
        # The ID of the table. For the format, refer to the response of the ListTables operation.
        # 
        # This parameter is required.
        self.id = id
        # The usage description. Rich text format is supported.
        self.readme = readme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_attributes_shrink is not None:
            result['CustomAttributes'] = self.custom_attributes_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.readme is not None:
            result['Readme'] = self.readme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAttributes') is not None:
            self.custom_attributes_shrink = m.get('CustomAttributes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Readme') is not None:
            self.readme = m.get('Readme')

        return self

