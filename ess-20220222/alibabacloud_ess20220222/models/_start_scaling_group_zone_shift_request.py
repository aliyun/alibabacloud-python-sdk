# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartScalingGroupZoneShiftRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        expiry_time: str = None,
        impaired_zone_ids: List[str] = None,
        region_id: str = None,
        scaling_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see Ensure idempotence.
        self.client_token = client_token
        # The expiration time of the zone transfer. After the time expires, the system automatically ends the transfer and restores the related zones. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time must be in UTC. The value must be later than the current time and cannot be more than 3 days after the current time.
        # 
        # This parameter is required.
        self.expiry_time = expiry_time
        # The IDs of the impaired zones. Valid values of N: 1 to 5.
        # 
        # This parameter is required.
        self.impaired_zone_ids = impaired_zone_ids
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time

        if self.impaired_zone_ids is not None:
            result['ImpairedZoneIds'] = self.impaired_zone_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')

        if m.get('ImpairedZoneIds') is not None:
            self.impaired_zone_ids = m.get('ImpairedZoneIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

