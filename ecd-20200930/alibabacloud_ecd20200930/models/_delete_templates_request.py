# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteTemplatesRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        template_ids: List[str] = None,
    ):
        # >  This parameter is not publicly available.
        self.biz_type = biz_type
        # The IDs of the templates that you want to delete.
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        return self

