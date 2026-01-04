# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemovePublicIpsFromEpnInstanceRequest(DaraModel):
    def __init__(
        self,
        epninstance_id: str = None,
        instance_infos: str = None,
    ):
        # The ID of the EPN instance.
        # 
        # This parameter is required.
        self.epninstance_id = epninstance_id
        # The information about the public IP addresses that you want to delete.
        # 
        # This parameter is required.
        self.instance_infos = instance_infos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')

        return self

