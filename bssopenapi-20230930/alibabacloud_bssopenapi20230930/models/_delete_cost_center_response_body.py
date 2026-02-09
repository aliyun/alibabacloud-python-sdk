# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class DeleteCostCenterResponseBody(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        is_success: bool = None,
        metadata: Any = None,
        owner_account_id: int = None,
        request_id: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.is_success = is_success
        self.metadata = metadata
        self.owner_account_id = owner_account_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

