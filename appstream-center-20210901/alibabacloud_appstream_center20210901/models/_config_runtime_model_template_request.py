# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigRuntimeModelTemplateRequest(DaraModel):
    def __init__(
        self,
        model_template_id: str = None,
        runtime_ids: List[str] = None,
        runtime_type: str = None,
    ):
        # This parameter is required.
        self.model_template_id = model_template_id
        # This parameter is required.
        self.runtime_ids = runtime_ids
        # This parameter is required.
        self.runtime_type = runtime_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.runtime_ids is not None:
            result['RuntimeIds'] = self.runtime_ids

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('RuntimeIds') is not None:
            self.runtime_ids = m.get('RuntimeIds')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

