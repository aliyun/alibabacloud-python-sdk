# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachVbrToVpconnRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        region_id: str = None,
        token: str = None,
        vbr_id: str = None,
        vpconn_id: str = None,
    ):
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without associating the VBR instance with shared Express Connect circuits. The system checks whether the required parameters are specified, the request format is valid, and the instance status is correct. If the check fails, the corresponding error is returned. If the check passes, the request ID is returned.
        # - **false** (default): sends a normal request. After the check passes, the VBR instance is directly associated with shared Express Connect circuits.
        self.dry_run = dry_run
        # The region ID of the shared Express Connect circuits.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client token must be unique among different requests. The maximum length is 64 ASCII characters.
        self.token = token
        # The VBR instance ID.
        # >The ID of the VBR instance to be migrated. The VBR must currently be directly attached to an Express Connect circuit owned by the caller, and must be the same VBR specified in CreateVpconnFromVbr.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id
        # The ID of the shared Express Connect circuits (VirtualPhysicalConnection) instance.
        # >The shared Express Connect circuits instance ID returned by CreateVpconnFromVbr. The instance must have been confirmed and accepted by the tenant (Confirmed) and be in the Enabled state.
        # 
        # This parameter is required.
        self.vpconn_id = vpconn_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.token is not None:
            result['Token'] = self.token

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vpconn_id is not None:
            result['VpconnId'] = self.vpconn_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VpconnId') is not None:
            self.vpconn_id = m.get('VpconnId')

        return self

