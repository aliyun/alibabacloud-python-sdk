# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        template_biz_id: str = None,
        template_type: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        self.template_biz_id = template_biz_id
        # The template type.
        # 
        # Valid values:
        # 
        # *   TASK
        # *   SESSION
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.template_biz_id is not None:
            result['templateBizId'] = self.template_biz_id

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('templateBizId') is not None:
            self.template_biz_id = m.get('templateBizId')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

