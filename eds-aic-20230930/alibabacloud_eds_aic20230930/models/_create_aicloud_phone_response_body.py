# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateAICloudPhoneResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateAICloudPhoneResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data object.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateAICloudPhoneResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAICloudPhoneResponseBodyData(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        package_ids: List[str] = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The list of package IDs. After the payment is successful, instances are created based on these IDs through a callback.
        self.package_ids = package_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')

        return self

