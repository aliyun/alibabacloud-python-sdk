# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateModelTemplateRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        model_template_id: str = None,
        name: str = None,
    ):
        # The model group configuration JSON object.
        self.config = config
        # The template group description.
        self.description = description
        # The model group ID.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id
        # The template group name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

