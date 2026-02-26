# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetBindingResponseBody(DaraModel):
    def __init__(
        self,
        binding: main_models.Binding = None,
        request_id: str = None,
    ):
        # The details of the binding.
        self.binding = binding
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = main_models.Binding()
            self.binding = temp_model.from_map(m.get('Binding'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

