# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachVbrToVpconnResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_physical_connection: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the hosted connection.
        self.virtual_physical_connection = virtual_physical_connection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.virtual_physical_connection is not None:
            result['VirtualPhysicalConnection'] = self.virtual_physical_connection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VirtualPhysicalConnection') is not None:
            self.virtual_physical_connection = m.get('VirtualPhysicalConnection')

        return self

