# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class VerifyCenResponseBody(DaraModel):
    def __init__(
        self,
        cidr_blocks: List[str] = None,
        request_id: str = None,
        route_entries: List[main_models.VerifyCenResponseBodyRouteEntries] = None,
        status: str = None,
    ):
        # The recommended IPv4 CIDR blocks. Three CIDR blocks are randomly recommended. This parameter is returned when the `Status` value is `Conflict`.
        self.cidr_blocks = cidr_blocks
        # The ID of the request.
        self.request_id = request_id
        # The routes provided by the CEN instance.
        self.route_entries = route_entries
        # The check result of CIDR block conflict.
        # 
        # Valid values:
        # 
        # *   InvalidCen.CenUidInvalid: The Alibaba Cloud account is invalid or the Alibaba Cloud account does not have the permission to access Elastic Desktop Service.
        # *   VerifyCode.InvalidTokenCode: The verification code is invalid.
        # *   VerifyCode.ReachTokenRetryTime: The maximum number of times for entering a verification code reaches the limit.
        # *   Conflict: A CIDR block conflict exists. If the verification result of at least one route is Conflict, Conflict is returned for this parameter.
        # *   Access: The verification is passed. If the verification result for all routes is Access, Access is returned for this parameter.
        # *   InvalidCen.ParameterCenInstanceId: The Alibaba Cloud account does not own the CEN instance.
        self.status = status

    def validate(self):
        if self.route_entries:
            for v1 in self.route_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_blocks is not None:
            result['CidrBlocks'] = self.cidr_blocks

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteEntries'] = []
        if self.route_entries is not None:
            for k1 in self.route_entries:
                result['RouteEntries'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlocks') is not None:
            self.cidr_blocks = m.get('CidrBlocks')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_entries = []
        if m.get('RouteEntries') is not None:
            for k1 in m.get('RouteEntries'):
                temp_model = main_models.VerifyCenResponseBodyRouteEntries()
                self.route_entries.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class VerifyCenResponseBodyRouteEntries(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        next_hop_instance_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the instance corresponding to the route.
        self.next_hop_instance_id = next_hop_instance_id
        # The region ID of the route.
        self.region_id = region_id
        # The verification result of the route.
        # 
        # Valid values:
        # 
        # *   Conflict: A CIDR block conflict exists.
        # *   Access: The verification is passed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

