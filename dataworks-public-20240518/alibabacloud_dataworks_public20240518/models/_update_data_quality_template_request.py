# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataQualityTemplateRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
    ):
        # The ID of the custom rule template.
        self.id = id
        # The account ID of the owner.
        self.owner = owner
        # The project ID.
        self.project_id = project_id
        # Detailed configuration Spec code of the rule template. For more information, see [Data quality Spec configuration description](~2963394~).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

