# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class IllustrationResult(DaraModel):
    def __init__(
        self,
        illustration: main_models.Illustration = None,
        request_id: str = None,
    ):
        self.illustration = illustration
        self.request_id = request_id

    def validate(self):
        if self.illustration:
            self.illustration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.illustration is not None:
            result['illustration'] = self.illustration.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('illustration') is not None:
            temp_model = main_models.Illustration()
            self.illustration = temp_model.from_map(m.get('illustration'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

