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
        # The information that is required to send the verification code, in JSON format. When you verify the CEN instance of another Alibaba Cloud account, you must provide the ID of the CEN instance and the ID of the Alibaba Cloud account to which the instance belongs.
        # 
        # *   CenId: the ID of the CEN instance.
        # *   CenOwnerId: the ID of the Alibaba Cloud account to which the CEN instance belongs.
        # 
        # >  If you own the CEN instance, skip this parameter. If you do not own the CEN instance, specify the ID of the Alibaba Cloud account that owns the CEN instance.
        self.extra_info = extra_info
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The action that you want to perform by using the verification code.
        # 
        # Valid value:
        # 
        # *   eds_cenID_securityverification: Use the verification code to verify the CEN instance.
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

