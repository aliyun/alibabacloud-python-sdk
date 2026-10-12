# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataFieldPathsValue(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        json_path: str = None,
        source: str = None,
        category: str = None,
    ):
        # The identifier key of the template field, such as input_token.
        self.field_key = field_key
        # The JSONPath expression of the template field in the request or response message, such as usage.prompt_tokens.
        self.json_path = json_path
        # The value source of the field, which indicates the part of the message from which the field is read, such as response_body.
        self.source = source
        # The statistical category to which the field belongs.
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.json_path is not None:
            result['jsonPath'] = self.json_path

        if self.source is not None:
            result['source'] = self.source

        if self.category is not None:
            result['category'] = self.category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('jsonPath') is not None:
            self.json_path = m.get('jsonPath')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('category') is not None:
            self.category = m.get('category')

        return self

