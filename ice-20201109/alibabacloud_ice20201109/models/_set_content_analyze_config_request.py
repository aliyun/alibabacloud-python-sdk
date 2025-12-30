# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetContentAnalyzeConfigRequest(DaraModel):
    def __init__(
        self,
        auto: bool = None,
        save_type: str = None,
        template_id: str = None,
    ):
        self.auto = auto
        self.save_type = save_type
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto is not None:
            result['Auto'] = self.auto

        if self.save_type is not None:
            result['SaveType'] = self.save_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')

        if m.get('SaveType') is not None:
            self.save_type = m.get('SaveType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

