# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataQualityTemplateRequest(DaraModel):
    def __init__(
        self,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
    ):
        # The ID of the owner.
        self.owner = owner
        # The project ID.
        self.project_id = project_id
        # The Spec code for the detailed configuration of the rule template. For more information, see [Data quality Spec configuration](https://help.aliyun.com/document_detail/2963394.html).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

