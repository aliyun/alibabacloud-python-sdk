# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelDTO(DaraModel):
    def __init__(
        self,
        api_key_preview: str = None,
        base_url: str = None,
        delete_tag: int = None,
        description: str = None,
        extensions: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_billing_rule: bool = None,
        id: int = None,
        in_out: str = None,
        is_custom: bool = None,
        max_input_length: str = None,
        max_output_length: str = None,
        model_code: str = None,
        model_type: str = None,
        name: str = None,
        symbol: str = None,
        tag_names: str = None,
        tags: str = None,
        version: int = None,
    ):
        self.api_key_preview = api_key_preview
        # Base URL
        self.base_url = base_url
        self.delete_tag = delete_tag
        self.description = description
        self.extensions = extensions
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.has_billing_rule = has_billing_rule
        # ID
        self.id = id
        self.in_out = in_out
        self.is_custom = is_custom
        self.max_input_length = max_input_length
        self.max_output_length = max_output_length
        self.model_code = model_code
        self.model_type = model_type
        self.name = name
        self.symbol = symbol
        self.tag_names = tag_names
        self.tags = tags
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_preview is not None:
            result['apiKeyPreview'] = self.api_key_preview

        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.description is not None:
            result['description'] = self.description

        if self.extensions is not None:
            result['extensions'] = self.extensions

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.has_billing_rule is not None:
            result['hasBillingRule'] = self.has_billing_rule

        if self.id is not None:
            result['id'] = self.id

        if self.in_out is not None:
            result['inOut'] = self.in_out

        if self.is_custom is not None:
            result['isCustom'] = self.is_custom

        if self.max_input_length is not None:
            result['maxInputLength'] = self.max_input_length

        if self.max_output_length is not None:
            result['maxOutputLength'] = self.max_output_length

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.name is not None:
            result['name'] = self.name

        if self.symbol is not None:
            result['symbol'] = self.symbol

        if self.tag_names is not None:
            result['tagNames'] = self.tag_names

        if self.tags is not None:
            result['tags'] = self.tags

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyPreview') is not None:
            self.api_key_preview = m.get('apiKeyPreview')

        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extensions') is not None:
            self.extensions = m.get('extensions')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hasBillingRule') is not None:
            self.has_billing_rule = m.get('hasBillingRule')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inOut') is not None:
            self.in_out = m.get('inOut')

        if m.get('isCustom') is not None:
            self.is_custom = m.get('isCustom')

        if m.get('maxInputLength') is not None:
            self.max_input_length = m.get('maxInputLength')

        if m.get('maxOutputLength') is not None:
            self.max_output_length = m.get('maxOutputLength')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')

        if m.get('tagNames') is not None:
            self.tag_names = m.get('tagNames')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

