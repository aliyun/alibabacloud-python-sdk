# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendVerifyCodeRequest(DaraModel):
    def __init__(
        self,
        extra_info: str = None,
        region_id: str = None,
        verify_code_action: str = None,
    ):
        # The information required to send the verification code, in JSON format. When verifying a CEN instance, provide the CEN instance ID and the Alibaba Cloud account ID to which the CEN instance belongs.
        # - CenId: the CEN instance ID. 
        # - CenOwnerId: the Alibaba Cloud account ID to which the CEN instance belongs. 
        # 
        # > If the specified CenId belongs to the current Alibaba Cloud account, this parameter is not required. If the specified CenId belongs to a different Alibaba Cloud account, specify the Alibaba Cloud account ID of the owner.
        self.extra_info = extra_info
        # The region ID. Call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The action associated with the verification code.
        # 
        # This parameter is required.
        self.verify_code_action = verify_code_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.verify_code_action is not None:
            result['VerifyCodeAction'] = self.verify_code_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VerifyCodeAction') is not None:
            self.verify_code_action = m.get('VerifyCodeAction')

        return self

