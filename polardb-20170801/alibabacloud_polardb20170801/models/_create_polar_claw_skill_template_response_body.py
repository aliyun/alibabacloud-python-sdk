# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarClawSkillTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        skill_template_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The skill template ID.
        self.skill_template_id = skill_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_template_id is not None:
            result['SkillTemplateId'] = self.skill_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillTemplateId') is not None:
            self.skill_template_id = m.get('SkillTemplateId')

        return self

