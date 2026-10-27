# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateResponseBody(DaraModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        # The ID of the orchestration template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_id is not None:
            result['template_id'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')

        return self

