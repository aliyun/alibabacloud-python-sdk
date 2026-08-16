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
        ref_scope: str = None,
    ):
        # The model group configuration JSON object. You can use this field to modify the default model. The configuration format varies depending on the agent provider (AgentProvider):
        # 
        # - **OpenClaw / AgenticComputer scenarios:**
        # Set the default model by using the `defaults.model.primary` field in the format of `provider name/model code`.
        # 
        # - **HermesAgent scenarios:**
        # Specify the provider name by using `model.provider` and the model code by using `model.default`.
        # 
        # > Note:
        # > - When you modify the default model, the system verifies whether the specified provider and model code already exist in the model group.
        self.config = config
        # The template group description.
        self.description = description
        # The model group ID.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id
        # The template group name.
        self.name = name
        # The authorization scope. This parameter is optional and can be modified only for Common model groups. Valid values: ALL_USER and USER_MIXED.
        self.ref_scope = ref_scope

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

        if self.ref_scope is not None:
            result['RefScope'] = self.ref_scope

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

        if m.get('RefScope') is not None:
            self.ref_scope = m.get('RefScope')

        return self

