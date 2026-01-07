# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTextLabelRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        label_template_id: str = None,
        project_id: int = None,
    ):
        self.data = data
        self.label_template_id = label_template_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.label_template_id is not None:
            result['LabelTemplateId'] = self.label_template_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('LabelTemplateId') is not None:
            self.label_template_id = m.get('LabelTemplateId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

