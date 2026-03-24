# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyBroadcastSceneFromTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        ratio: str = None,
        template_id: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.ratio = ratio
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

