# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class AndroidShortPayload(DaraModel):
    def __init__(
        self,
        body: main_models.AndroidShortPayloadBody = None,
        extra: Dict[str, Any] = None,
    ):
        self.body = body
        self.extra = extra

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.extra is not None:
            result['extra'] = self.extra

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.AndroidShortPayloadBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        return self



class AndroidShortPayloadBody(DaraModel):
    def __init__(
        self,
        custom: str = None,
    ):
        self.custom = custom

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom is not None:
            result['custom'] = self.custom

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom') is not None:
            self.custom = m.get('custom')

        return self

