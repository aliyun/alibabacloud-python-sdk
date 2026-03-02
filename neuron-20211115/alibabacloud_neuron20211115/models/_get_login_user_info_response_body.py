# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class GetLoginUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        result: main_models.BucUser = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = main_models.BucUser()
            self.result = temp_model.from_map(m.get('result'))

        return self

