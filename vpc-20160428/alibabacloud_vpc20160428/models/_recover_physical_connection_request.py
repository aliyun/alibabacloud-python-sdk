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
        # Specifies whether to perform only a dry run on the request. Valid values:
        # 
        # - **true**: performs only a dry run and does not restore the connection of the Express Connect circuit. The system checks whether the required parameters are specified, the request format is valid, and the instance status is normal. If the request fails the dry run, an error message is returned. If the request passes the dry run, the request ID is returned.
        # - **false** (default): performs a dry run and restores the connection of the Express Connect circuit if the request passes the dry run.
        self.dry_run = dry_run
        # The instance ID of the Express Connect circuit to recover.
        # 
        # > Currently, only the connection of shared Express Connect circuits can be recovered.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
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

