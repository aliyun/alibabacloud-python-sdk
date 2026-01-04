# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVbrHaResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        name: str = None,
        peer_vbr_id: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        vbr_ha_id: str = None,
        vbr_id: str = None,
    ):
        # The time when the VBR was created.
        self.creation_time = creation_time
        # The description of the VBR failover group.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # The name of the VBR failover group.
        self.name = name
        # The ID of the other VBR in the VBR failover group.
        self.peer_vbr_id = peer_vbr_id
        # The ID of the region in which the VBR is deployed.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The status of the VBR failover group.
        # 
        # *   **Creating**
        # *   **Active**
        self.status = status
        # The ID of the VBR failover group.
        self.vbr_ha_id = vbr_ha_id
        # The VBR ID.
        self.vbr_id = vbr_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.peer_vbr_id is not None:
            result['PeerVbrId'] = self.peer_vbr_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vbr_ha_id is not None:
            result['VbrHaId'] = self.vbr_ha_id

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PeerVbrId') is not None:
            self.peer_vbr_id = m.get('PeerVbrId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VbrHaId') is not None:
            self.vbr_ha_id = m.get('VbrHaId')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        return self

