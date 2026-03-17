# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ViewSmartAccessGatewayPortRouteProtocolRequest(DaraModel):
    def __init__(
        self,
        cross_account: bool = None,
        region_id: str = None,
        resource_uid: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
    ):
        self.cross_account = cross_account
        # This parameter is required.
        self.region_id = region_id
        self.resource_uid = resource_uid
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid

        if self.sag_ins_id is not None:
            result['SagInsId'] = self.sag_ins_id

        if self.sag_sn is not None:
            result['SagSn'] = self.sag_sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccount') is not None:
            self.cross_account = m.get('CrossAccount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')

        if m.get('SagInsId') is not None:
            self.sag_ins_id = m.get('SagInsId')

        if m.get('SagSn') is not None:
            self.sag_sn = m.get('SagSn')

        return self

