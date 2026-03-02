# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class ListLibrarysResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.LibraryListResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.LibraryListResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

