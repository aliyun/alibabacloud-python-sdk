# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertOutputGroupOutput(DaraModel):
    def __init__(
        self,
        features: str = None,
        name: str = None,
        output_file_name: str = None,
        override_params: str = None,
        priority: int = None,
        template_id: str = None,
    ):
        self.features = features
        self.name = name
        self.output_file_name = output_file_name
        self.override_params = override_params
        self.priority = priority
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.features is not None:
            result['Features'] = self.features

        if self.name is not None:
            result['Name'] = self.name

        if self.output_file_name is not None:
            result['OutputFileName'] = self.output_file_name

        if self.override_params is not None:
            result['OverrideParams'] = self.override_params

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputFileName') is not None:
            self.output_file_name = m.get('OutputFileName')

        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

