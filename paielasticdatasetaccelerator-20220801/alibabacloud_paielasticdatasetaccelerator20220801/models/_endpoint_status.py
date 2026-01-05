# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class EndpointStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        detail: main_models.EndpointStatusDetail = None,
        message: str = None,
        phase: str = None,
    ):
        self.code = code
        self.detail = detail
        self.message = message
        self.phase = phase

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.phase is not None:
            result['Phase'] = self.phase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Detail') is not None:
            temp_model = main_models.EndpointStatusDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        return self

