# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiStatisticsPathField(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        field_key: str = None,
        io: str = None,
        json_path: str = None,
        name: str = None,
        record_enabled: bool = None,
        rule: str = None,
        sensitive: bool = None,
        source: str = None,
    ):
        # The secondary business category of the field. Optional. Valid values: conversation (conversation content), config (configuration parameters), tools (tool calling), usage (usage statistics), metadata (metadata), choices (candidate results), identity (identity identifier), cache (cache information), media (multimedia content), logprobs (log probabilities), and custom (custom field). Set custom fields to custom.
        self.category = category
        # The field description.
        self.description = description
        # The log key (field name).
        self.field_key = field_key
        # The request or response attribution. The backend normalizes this to request or response based on source.
        self.io = io
        # The corresponding jsonPath (gjson syntax).
        self.json_path = json_path
        # The annotation for the field key name.
        self.name = name
        # Indicates whether collection is enabled to create a log record for the corresponding field in AI request logs.
        self.record_enabled = record_enabled
        # The aggregation rule for streaming response fields. Valid values: append, first, and replace. append: appends the matched values from each streaming chunk in sequence. first: retains the first matched value. replace: uses the last matched value. When source is response_streaming_body and rule is not specified, first is used by default. This field is not required for non-streaming scenarios.
        self.rule = rule
        # Specifies whether the field is sensitive.
        self.sensitive = sensitive
        # The source of the field value. Valid values: fixed_value (fixed value), request_body (request body), request_header (request header), response_header (response header), response_body (non-streaming response body), and response_streaming_body (streaming response body).
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.description is not None:
            result['description'] = self.description

        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.io is not None:
            result['io'] = self.io

        if self.json_path is not None:
            result['jsonPath'] = self.json_path

        if self.name is not None:
            result['name'] = self.name

        if self.record_enabled is not None:
            result['recordEnabled'] = self.record_enabled

        if self.rule is not None:
            result['rule'] = self.rule

        if self.sensitive is not None:
            result['sensitive'] = self.sensitive

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('io') is not None:
            self.io = m.get('io')

        if m.get('jsonPath') is not None:
            self.json_path = m.get('jsonPath')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('recordEnabled') is not None:
            self.record_enabled = m.get('recordEnabled')

        if m.get('rule') is not None:
            self.rule = m.get('rule')

        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

