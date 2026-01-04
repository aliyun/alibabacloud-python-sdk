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
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and instance status. If the request fails the dry run, an error message is returned. If the request passes the dry run, the system returns the ID of the request.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The payer for the shared Express Connect circuit. Valid values:
        # 
        # *   **PayByPhysicalConnectionOwner**: the owner of the shared Express Connect circuit
        # *   **PayByVirtualPhysicalConnectionOwner**: the owner of the hosted connection
        self.order_mode = order_mode
        # The region ID of the hosted connection.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.token = token
        # The ID of the associated VBR.
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

