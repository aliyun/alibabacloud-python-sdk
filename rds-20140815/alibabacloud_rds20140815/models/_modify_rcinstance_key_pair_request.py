# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCInstanceKeyPairRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        key_pair_name: str = None,
        reboot: bool = None,
        region_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # Specifies whether to restart the instance.
        # 
        # *   **true**
        # *   **false**
        self.reboot = reboot
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.reboot is not None:
            result['Reboot'] = self.reboot

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Reboot') is not None:
            self.reboot = m.get('Reboot')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

