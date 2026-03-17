# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAccessGatewayBgpRouteRequest(DaraModel):
    def __init__(
        self,
        cross_account: bool = None,
        hold_time: int = None,
        keep_alive: int = None,
        local_as: int = None,
        region_id: str = None,
        resource_uid: str = None,
        router_id: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
    ):
        # Specifies whether to query only the SAG instances that belong to another Alibaba Cloud account. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.cross_account = cross_account
        # The hold time. Unit: seconds.
        # 
        # Valid values: **3** to **65535**.
        # 
        # > When the SAG device establishes a peering connection with a peer device, the hold time of both devices must be the same. If the SAG device does not receive a keepalive or update message from the peer device within the hold time, the connection between the BGP peers is closed.
        # 
        # This parameter is required.
        self.hold_time = hold_time
        # The time interval at which keep-alive packets are sent. Unit: seconds.
        # 
        # Valid values: **0** to **65535**.
        # 
        # This parameter is required.
        self.keep_alive = keep_alive
        # The autonomous system number (ASN) of the SAG device.
        # 
        # Valid values: **1** to **4294967295**.
        # 
        # This parameter is required.
        self.local_as = local_as
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account to which the SAG instance belongs.
        self.resource_uid = resource_uid
        # The ID of the BGP router.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The ID of the Smart Access Gateway (SAG) instance.
        # 
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sag_sn = sag_sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account is not None:
            result['CrossAccount'] = self.cross_account

        if self.hold_time is not None:
            result['HoldTime'] = self.hold_time

        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive

        if self.local_as is not None:
            result['LocalAs'] = self.local_as

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.sag_ins_id is not None:
            result['SagInsId'] = self.sag_ins_id

        if self.sag_sn is not None:
            result['SagSn'] = self.sag_sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccount') is not None:
            self.cross_account = m.get('CrossAccount')

        if m.get('HoldTime') is not None:
            self.hold_time = m.get('HoldTime')

        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')

        if m.get('LocalAs') is not None:
            self.local_as = m.get('LocalAs')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('SagInsId') is not None:
            self.sag_ins_id = m.get('SagInsId')

        if m.get('SagSn') is not None:
            self.sag_sn = m.get('SagSn')

        return self

