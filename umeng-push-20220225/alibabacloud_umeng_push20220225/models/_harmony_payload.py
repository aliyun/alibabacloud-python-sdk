# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class HarmonyPayload(DaraModel):
    def __init__(
        self,
        display_type: str = None,
        extra: Dict[str, Any] = None,
        harmony_body: main_models.HarmonyBody = None,
    ):
        # This parameter is required.
        self.display_type = display_type
        self.extra = extra
        self.harmony_body = harmony_body

    def validate(self):
        if self.harmony_body:
            self.harmony_body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.extra is not None:
            result['extra'] = self.extra

        if self.harmony_body is not None:
            result['harmonyBody'] = self.harmony_body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('harmonyBody') is not None:
            temp_model = main_models.HarmonyBody()
            self.harmony_body = temp_model.from_map(m.get('harmonyBody'))

        return self

