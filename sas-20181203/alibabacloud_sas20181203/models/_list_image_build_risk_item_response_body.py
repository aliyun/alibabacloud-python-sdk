# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListImageBuildRiskItemResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListImageBuildRiskItemResponseBodyData] = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListImageBuildRiskItemResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImageBuildRiskItemResponseBodyData(DaraModel):
    def __init__(
        self,
        item_key: str = None,
        item_name: str = None,
    ):
        # The type key of the risky build command.
        self.item_key = item_key
        # The type name of the risky build command.
        self.item_name = item_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_key is not None:
            result['ItemKey'] = self.item_key

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemKey') is not None:
            self.item_key = m.get('ItemKey')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        return self

