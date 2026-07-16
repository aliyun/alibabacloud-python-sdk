# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceInstanceAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        license_data_shrink: str = None,
        reason: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The time when the service instance expires.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        # The license data.
        self.license_data_shrink = license_data_shrink
        # The reason for the request. This parameter is used to extend a trial.
        self.reason = reason
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.license_data_shrink is not None:
            result['LicenseData'] = self.license_data_shrink

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LicenseData') is not None:
            self.license_data_shrink = m.get('LicenseData')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

