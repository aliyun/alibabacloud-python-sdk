# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataQualityRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        project_id: int = None,
    ):
        # The code for the template.
        # 
        # This parameter is required.
        self.code = code
        # The DataWorks workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

