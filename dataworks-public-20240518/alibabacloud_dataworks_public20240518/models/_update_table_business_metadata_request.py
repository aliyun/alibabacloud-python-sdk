# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class UpdateTableBusinessMetadataRequest(DaraModel):
    def __init__(
        self,
        custom_attributes: Dict[str, List[str]] = None,
        id: str = None,
        readme: str = None,
    ):
        # The values of custom attributes. The key specifies the identifier of a custom attribute, and the value is an array that can contain at most one item. To delete the value for an attribute, pass an empty array. To update only custom attributes, omit the `Readme` parameter to prevent its existing value from being cleared. To leave the custom attributes unchanged, pass an empty object `{}`.
        self.custom_attributes = custom_attributes
        # The table ID. For the required format, see the response of the `ListTables` operation.
        # 
        # This parameter is required.
        self.id = id
        # The Readme of the table, which supports rich text format.
        self.readme = readme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.id is not None:
            result['Id'] = self.id

        if self.readme is not None:
            result['Readme'] = self.readme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Readme') is not None:
            self.readme = m.get('Readme')

        return self

