# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ResolveModelAmbiguity(DaraModel):
    def __init__(
        self,
        options: List[Dict[str, Any]] = None,
        question: str = None,
        type: str = None,
    ):
        # The list of candidate options. **The shape is determined by `type`**. Both shapes include an `id` (such as `o1` or `o2`) for the caller to pass back the selection. When `type=semantic`, each item contains exactly four fields: `id` / `label` / `description` / `context`, where `context` has the same structure as the top-level `context` in the response (**note that the candidate item itself is not a context but a wrapper around it**). When `type=data_source`, each item contains exactly two fields: `id` / `dataSource`, with the physical coordinates embedded in `dataSource` (including `region` / `project` / `logstore`), **not flattened at the top level of the candidate item**. Each item is an **open object**. The server may add or remove fields as the semantic layer evolves. Callers should read fields as needed and tolerate unknown fields.
        # 
        # This parameter is required.
        self.options = options
        # A clarification question for the caller. You can display it directly to the user or a downstream agent to make a selection from `options`.
        # 
        # This parameter is required.
        self.question = question
        # The ambiguity type. Valid values: `semantic` (the question semantically points to multiple candidate contexts) or `data_source` (the semantics are unique but map to multiple physical data source coordinates). Note that the value `data_source` of this field is not the same as the top-level `dataSource` field in the response.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.options is not None:
            result['options'] = self.options

        if self.question is not None:
            result['question'] = self.question

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

