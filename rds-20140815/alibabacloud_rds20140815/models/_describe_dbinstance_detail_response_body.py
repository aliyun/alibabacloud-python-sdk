# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceDetailResponseBody(DaraModel):
    def __init__(
        self,
        activation_state: str = None,
        dbinstance_id: str = None,
        license_type: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # Indicates whether the instance is in the active state.
        self.activation_state = activation_state
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The type of the license.
        self.license_type = license_type
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_state is not None:
            result['ActivationState'] = self.activation_state

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationState') is not None:
            self.activation_state = m.get('ActivationState')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

