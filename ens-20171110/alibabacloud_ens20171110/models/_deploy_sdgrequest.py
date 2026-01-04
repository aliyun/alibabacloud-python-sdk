# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeploySDGRequest(DaraModel):
    def __init__(
        self,
        deployment_type: str = None,
        instance_ids: List[str] = None,
        sdgid: str = None,
    ):
        # The SDG deployment type. Valid values:
        # 
        # *   common (default): read/write deployment. Data updates are written to disks.
        # *   overlay: read/write splitting deployment. Content in SDGs is read-only. Data updates are written to the local storage of the instance.
        self.deployment_type = deployment_type
        # The IDs of instances on which you want to deploy SDGs. You can deploy SDGs on a maximum of 100 instances at a time.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The SDG ID. This parameter is used to create a disk, which is attached to an instance.
        # 
        # This parameter is required.
        self.sdgid = sdgid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_type is not None:
            result['DeploymentType'] = self.deployment_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentType') is not None:
            self.deployment_type = m.get('DeploymentType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

