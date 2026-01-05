# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SendSystemPropertyTemplateRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        template_id: str = None,
        template_ids: List[str] = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.template_id = template_id
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        return self

