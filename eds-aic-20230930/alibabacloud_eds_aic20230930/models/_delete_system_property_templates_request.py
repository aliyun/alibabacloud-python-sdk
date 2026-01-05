# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteSystemPropertyTemplatesRequest(DaraModel):
    def __init__(
        self,
        template_ids: List[str] = None,
    ):
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        return self

