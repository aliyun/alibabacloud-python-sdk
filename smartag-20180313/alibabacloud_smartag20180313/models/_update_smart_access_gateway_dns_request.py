# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAccessGatewayDnsRequest(DaraModel):
    def __init__(
        self,
        cross_account: bool = None,
        master_dns: str = None,
        region_id: str = None,
        resource_uid: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
        slave_dns: str = None,
    ):
        # Specifies whether to query only the SAG instances that belong to another Alibaba Cloud account. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.cross_account = cross_account
        # The IP address of the primary DNS server.
        self.master_dns = master_dns
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account to which the SAG instance belongs.
        self.resource_uid = resource_uid
        # The ID of the Smart Access Gateway (SAG) instance.
        # 
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sag_sn = sag_sn
        # The IP address of the secondary DNS server.
        self.slave_dns = slave_dns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account is not None:
            result['CrossAccount'] = self.cross_account

        if self.master_dns is not None:
            result['MasterDns'] = self.master_dns

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid

        if self.sag_ins_id is not None:
            result['SagInsId'] = self.sag_ins_id

        if self.sag_sn is not None:
            result['SagSn'] = self.sag_sn

        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccount') is not None:
            self.cross_account = m.get('CrossAccount')

        if m.get('MasterDns') is not None:
            self.master_dns = m.get('MasterDns')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')

        if m.get('SagInsId') is not None:
            self.sag_ins_id = m.get('SagInsId')

        if m.get('SagSn') is not None:
            self.sag_sn = m.get('SagSn')

        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')

        return self

