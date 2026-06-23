# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecoverPhysicalConnectionRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        instance_id: str = None,
        region_id: str = None,
        token: str = None,
    ):
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without recovering access to the Express Connect circuit. The system checks the required parameters, request format, and instance status. If the check fails, the corresponding error is returned. If the check succeeds, the request ID is returned.
        # - **false** (default): sends the request. After the request passes the check, access to the Express Connect circuit is recovered.
        self.dry_run = dry_run
        # The instance ID of the Express Connect circuit.
        # 
        # > Currently, only shared Express Connect circuits can be recovered.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client generates the value of this parameter. The value must be unique among different requests and cannot exceed 64 ASCII characters in length.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

