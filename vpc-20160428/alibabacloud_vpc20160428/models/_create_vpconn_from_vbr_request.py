# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpconnFromVbrRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        order_mode: str = None,
        region_id: str = None,
        token: str = None,
        vbr_id: str = None,
    ):
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: sends a check request without transforming the shared Express Connect circuits mode. The system checks the required parameters, request format, and instance status. If the check fails, the corresponding error is returned. If the check succeeds, the request ID is returned.
        # - **false** (default): sends a Normal request and transforms the shared Express Connect circuits mode after the check succeeds.
        self.dry_run = dry_run
        # The payer of the shared Express Connect circuits. Valid values:
        # 
        # - **PayByPhysicalConnectionOwner**: The owner of the Express Connect circuit associated with the shared Express Connect circuits pays the fee.
        # - **PayByVirtualPhysicalConnectionOwner**: The owner of the shared Express Connect circuits pays the fee.
        self.order_mode = order_mode
        # The region ID of the shared Express Connect circuits.
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client token must be unique among different requests. The maximum length is 64 ASCII characters.
        self.token = token
        # The instance ID of the cross-account VBR.
        # 
        # This parameter is required.
        self.vbr_id = vbr_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.token is not None:
            result['Token'] = self.token

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        return self

