# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyCenRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        cidr_block: str = None,
        region_id: str = None,
        verify_code: str = None,
    ):
        # The CEN instance ID.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The Alibaba Cloud account ID to which the CEN instance belongs.
        # 
        # - If the specified CenId belongs to your Alibaba Cloud account, you do not need to configure this parameter.
        # 
        # - If the specified CenId belongs to another Alibaba Cloud account, specify the ID of that Alibaba Cloud account.
        self.cen_owner_id = cen_owner_id
        # The IPv4 CIDR block of the office network.
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The verification code. If the specified CenId belongs to another Alibaba Cloud account, you must first call [SendVerifyCode](https://help.aliyun.com/document_detail/436847.html) to obtain the verification code.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        return self

