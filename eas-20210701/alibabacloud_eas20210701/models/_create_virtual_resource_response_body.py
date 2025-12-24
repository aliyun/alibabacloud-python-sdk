# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVirtualResourceResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        virtual_resource_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The ID of the virtual resource group.
        self.virtual_resource_id = virtual_resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.virtual_resource_id is not None:
            result['VirtualResourceId'] = self.virtual_resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VirtualResourceId') is not None:
            self.virtual_resource_id = m.get('VirtualResourceId')

        return self

