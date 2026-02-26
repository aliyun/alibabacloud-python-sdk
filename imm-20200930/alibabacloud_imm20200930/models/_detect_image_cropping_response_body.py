# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectImageCroppingResponseBody(DaraModel):
    def __init__(
        self,
        croppings: List[main_models.CroppingSuggestion] = None,
        request_id: str = None,
    ):
        # The image cropping suggestions.
        self.croppings = croppings
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.croppings:
            for v1 in self.croppings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Croppings'] = []
        if self.croppings is not None:
            for k1 in self.croppings:
                result['Croppings'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.croppings = []
        if m.get('Croppings') is not None:
            for k1 in m.get('Croppings'):
                temp_model = main_models.CroppingSuggestion()
                self.croppings.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

