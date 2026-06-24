# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteModelTemplateRequest(DaraModel):
    def __init__(
        self,
        model_template_id: str = None,
    ):
        # The model group ID.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        return self

