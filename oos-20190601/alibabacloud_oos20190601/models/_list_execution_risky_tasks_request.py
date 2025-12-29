# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExecutionRiskyTasksRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # The name of the template.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

