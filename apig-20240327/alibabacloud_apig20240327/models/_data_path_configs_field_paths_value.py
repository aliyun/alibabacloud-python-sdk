# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataPathConfigsFieldPathsValue(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        json_path: str = None,
        rule: str = None,
        name: str = None,
        description: str = None,
        source: str = None,
        category: str = None,
        io: str = None,
        sensitive: bool = None,
        record_enabled: bool = None,
        toggle_allowed: bool = None,
        json_path_rewrite_allowed: bool = None,
        from_template: bool = None,
    ):
        # The identity key of the field, which is unique within the same request path, such as input_token.
        self.field_key = field_key
        # The JSONPath expression of the field in the request or response message, such as usage.prompt_tokens.
        self.json_path = json_path
        # The value extraction rule for the field.
        self.rule = rule
        # The display name of the field.
        self.name = name
        # The description of the field.
        self.description = description
        # The source of the field value, indicating which part of the message the field is read from, such as response_body.
        self.source = source
        # The statistical category to which the field belongs.
        self.category = category
        # The message direction to which the field belongs, indicating whether it is extracted from the request or the response.
        self.io = io
        # Indicates whether the field contains sensitive information.
        self.sensitive = sensitive
        # Indicates whether collection is enabled for the field.
        self.record_enabled = record_enabled
        # Indicates whether the collection status of the field can be toggled.
        self.toggle_allowed = toggle_allowed
        # Indicates whether the JSONPath of the field can be rewritten.
        self.json_path_rewrite_allowed = json_path_rewrite_allowed
        # Indicates whether the field configuration is derived from a field template.
        self.from_template = from_template

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

        if self.rule is not None:
            result['rule'] = self.rule

        if self.name is not None:
            result['name'] = self.name

        if self.description is not None:
            result['description'] = self.description

        if self.source is not None:
            result['source'] = self.source

        if self.category is not None:
            result['category'] = self.category

        if self.io is not None:
            result['io'] = self.io

        if self.sensitive is not None:
            result['sensitive'] = self.sensitive

        if self.record_enabled is not None:
            result['recordEnabled'] = self.record_enabled

        if self.toggle_allowed is not None:
            result['toggleAllowed'] = self.toggle_allowed

        if self.json_path_rewrite_allowed is not None:
            result['jsonPathRewriteAllowed'] = self.json_path_rewrite_allowed

        if self.from_template is not None:
            result['fromTemplate'] = self.from_template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('jsonPath') is not None:
            self.json_path = m.get('jsonPath')

        if m.get('rule') is not None:
            self.rule = m.get('rule')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('io') is not None:
            self.io = m.get('io')

        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')

        if m.get('recordEnabled') is not None:
            self.record_enabled = m.get('recordEnabled')

        if m.get('toggleAllowed') is not None:
            self.toggle_allowed = m.get('toggleAllowed')

        if m.get('jsonPathRewriteAllowed') is not None:
            self.json_path_rewrite_allowed = m.get('jsonPathRewriteAllowed')

        if m.get('fromTemplate') is not None:
            self.from_template = m.get('fromTemplate')

        return self

