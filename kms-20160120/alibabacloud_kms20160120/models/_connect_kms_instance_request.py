# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConnectKmsInstanceRequest(DaraModel):
    def __init__(
        self,
        kmprovider: str = None,
        kms_instance_id: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
        zone_ids: str = None,
    ):
        # The provider of the KMS instance. Set the value to Aliyun.
        # 
        # This parameter is required.
        self.kmprovider = kmprovider
        # The ID of the KMS instance that you want to enable.
        # 
        # This parameter is required.
        self.kms_instance_id = kms_instance_id
        # The vSwitch in the two zones. The vSwitch must have at least one available IP address.
        # 
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC) that is associated with the KMS instance.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The two zones for the KMS instance. Dual-zone deployment improves service availability and disaster recovery capabilities.
        # 
        # This parameter is required.
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kmprovider is not None:
            result['KMProvider'] = self.kmprovider

        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KMProvider') is not None:
            self.kmprovider = m.get('KMProvider')

        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

