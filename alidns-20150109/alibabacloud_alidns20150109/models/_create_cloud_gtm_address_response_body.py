# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmAddressResponseBody(DaraModel):
    def __init__(
        self,
        address_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The address ID. This ID uniquely identifies the address.
        self.address_id = address_id
        # Unique request identification code.
        self.request_id = request_id
        # Indicates whether the address creation operation is successful:
        # - true: Operation was successful
        # - false: Operation was failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

