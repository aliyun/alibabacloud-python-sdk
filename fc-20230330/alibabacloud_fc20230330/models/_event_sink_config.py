# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class EventSinkConfig(DaraModel):
    def __init__(
        self,
        delivery_option: main_models.DeliveryOption = None,
    ):
        self.delivery_option = delivery_option

    def validate(self):
        if self.delivery_option:
            self.delivery_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_option is not None:
            result['deliveryOption'] = self.delivery_option.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deliveryOption') is not None:
            temp_model = main_models.DeliveryOption()
            self.delivery_option = temp_model.from_map(m.get('deliveryOption'))

        return self

