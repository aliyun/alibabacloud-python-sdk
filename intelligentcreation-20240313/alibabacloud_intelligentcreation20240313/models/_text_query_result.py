# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class TextQueryResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        texts: List[main_models.Text] = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.texts = texts
        self.total = total

    def validate(self):
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['texts'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.texts = []
        if m.get('texts') is not None:
            for k1 in m.get('texts'):
                temp_model = main_models.Text()
                self.texts.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

