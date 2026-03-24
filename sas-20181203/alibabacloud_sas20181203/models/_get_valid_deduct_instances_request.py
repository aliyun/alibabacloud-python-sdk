# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetValidDeductInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        modules: str = None,
        status: int = None,
    ):
        # Resource package instance ID, can be queried through [QueryResourcePackageInstances]().
        self.instance_id = instance_id
        # Resource package name code, values:
        # 
        # - Vulnerability resource package: **sas_vul_dp_cn**
        # - CSPM resource package: **sas_cspm_dp_cn**
        # - Anti-virus resource package: **sas_viruspackage_dp_cn**
        self.modules = modules
        # Resource package status, default is valid (valid), not modifiable.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modules is not None:
            result['Modules'] = self.modules

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Modules') is not None:
            self.modules = m.get('Modules')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

