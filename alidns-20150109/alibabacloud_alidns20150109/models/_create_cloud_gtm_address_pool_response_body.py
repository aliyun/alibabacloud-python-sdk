# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmAddressPoolResponseBody(DaraModel):
    def __init__(
        self,
        address_pool_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The unique ID of the address pool.
        self.address_pool_id = address_pool_id
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # - true: The operation was successful.
        # 
        # - false: The operation failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

