# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RenewElasticityAssurancesResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        private_pool_options_id_set: main_models.RenewElasticityAssurancesResponseBodyPrivatePoolOptionsIdSet = None,
        request_id: str = None,
    ):
        # The ID of the renewal order.
        self.order_id = order_id
        # The IDs of the elasticity assurances.
        self.private_pool_options_id_set = private_pool_options_id_set
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.private_pool_options_id_set:
            self.private_pool_options_id_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.private_pool_options_id_set is not None:
            result['PrivatePoolOptionsIdSet'] = self.private_pool_options_id_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PrivatePoolOptionsIdSet') is not None:
            temp_model = main_models.RenewElasticityAssurancesResponseBodyPrivatePoolOptionsIdSet()
            self.private_pool_options_id_set = temp_model.from_map(m.get('PrivatePoolOptionsIdSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RenewElasticityAssurancesResponseBodyPrivatePoolOptionsIdSet(DaraModel):
    def __init__(
        self,
        private_pool_options_id: List[str] = None,
    ):
        self.private_pool_options_id = private_pool_options_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options_id is not None:
            result['PrivatePoolOptionsId'] = self.private_pool_options_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptionsId') is not None:
            self.private_pool_options_id = m.get('PrivatePoolOptionsId')

        return self

