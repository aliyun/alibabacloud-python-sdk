# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateComputeJobCuRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cu_limit: float = None,
        cu_reserved: float = None,
        instance_id: str = None,
        job_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.cu_limit = cu_limit
        self.cu_reserved = cu_reserved
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_name = job_name
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cu_limit is not None:
            result['CuLimit'] = self.cu_limit

        if self.cu_reserved is not None:
            result['CuReserved'] = self.cu_reserved

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CuLimit') is not None:
            self.cu_limit = m.get('CuLimit')

        if m.get('CuReserved') is not None:
            self.cu_reserved = m.get('CuReserved')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

