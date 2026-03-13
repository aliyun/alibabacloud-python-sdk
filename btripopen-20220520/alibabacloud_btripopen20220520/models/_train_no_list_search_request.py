# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainNoListSearchRequest(DaraModel):
    def __init__(
        self,
        arr_location: str = None,
        dep_date: str = None,
        dep_location: str = None,
        option: main_models.TrainNoListSearchRequestOption = None,
        order_id: str = None,
    ):
        # This parameter is required.
        self.arr_location = arr_location
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.dep_location = dep_location
        # This parameter is required.
        self.option = option
        self.order_id = order_id

    def validate(self):
        if self.option:
            self.option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_location is not None:
            result['arr_location'] = self.arr_location

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.dep_location is not None:
            result['dep_location'] = self.dep_location

        if self.option is not None:
            result['option'] = self.option.to_map()

        if self.order_id is not None:
            result['order_id'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_location') is not None:
            self.arr_location = m.get('arr_location')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('dep_location') is not None:
            self.dep_location = m.get('dep_location')

        if m.get('option') is not None:
            temp_model = main_models.TrainNoListSearchRequestOption()
            self.option = temp_model.from_map(m.get('option'))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

class TrainNoListSearchRequestOption(DaraModel):
    def __init__(
        self,
        need_transfer: bool = None,
    ):
        self.need_transfer = need_transfer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_transfer is not None:
            result['need_transfer'] = self.need_transfer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('need_transfer') is not None:
            self.need_transfer = m.get('need_transfer')

        return self

