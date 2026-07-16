# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKmsInstanceBindVpcRequest(DaraModel):
    def __init__(
        self,
        bind_vpcs: str = None,
        kms_instance_id: str = None,
    ):
        # The VPC configuration. Each VPC configuration contains the following parameters:
        # 
        # - VpcId: The ID of the VPC.
        # 
        # - VSwitchId: The vSwitch in the VPC.
        # 
        # - RegionID: The region where the VPC resides.
        # 
        # - VpcOwnerId: The Alibaba Cloud account that owns the VPC.
        # 
        # The value is a JSON string in the following format: `[{"VpcId":"${VpcId}","VSwitchId":"${VSwitchId}","RegionId":"${RegionId}","VpcOwnerId":${VpcOwnerId}},...]`.
        # 
        # This parameter is required.
        self.bind_vpcs = bind_vpcs
        # The ID of the KMS instance.
        # 
        # This parameter is required.
        self.kms_instance_id = kms_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs

        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindVpcs') is not None:
            self.bind_vpcs = m.get('BindVpcs')

        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        return self

