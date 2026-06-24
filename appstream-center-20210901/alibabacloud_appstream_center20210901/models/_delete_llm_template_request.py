# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLlmTemplateRequest(DaraModel):
    def __init__(
        self,
        llm_template_id: str = None,
    ):
        # The ID of the model template.
        # 
        # This parameter is required.
        self.llm_template_id = llm_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_template_id is not None:
            result['LlmTemplateId'] = self.llm_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LlmTemplateId') is not None:
            self.llm_template_id = m.get('LlmTemplateId')

        return self

