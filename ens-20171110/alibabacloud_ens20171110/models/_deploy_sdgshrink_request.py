# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeploySDGShrinkRequest(DaraModel):
    def __init__(
        self,
        deployment_type: str = None,
        instance_ids_shrink: str = None,
        sdgid: str = None,
    ):
        # The SDG deployment type. Valid values:
        # 
        # - common: (default) read/write deployment. Data updates are written to the cloud disk.
        # - overlay: read/write splitting deployment. The SDG content is read-only, and data updates are written to the local storage of the instance.
        self.deployment_type = deployment_type
        # The list of device resource IDs to which the SDG is deployed. Batch deployment is supported, with a maximum of 100 instances per request.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The SDG ID. A cloud disk is created based on this SDG ID and mounted to the specified instance.
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

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentType') is not None:
            self.deployment_type = m.get('DeploymentType')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

