# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        region_id: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The application type, such as polarclaw. This parameter is required. If it is not provided, the service returns an InvalidApplicationType.Malformed (400) error. The value of this parameter must not include the polardb_ prefix, which differs from the format of the ApplicationType field returned by DescribeApplications. For example, if DescribeApplications returns polardb_polarclaw, set this parameter to polarclaw.
        self.application_type = application_type
        # The region ID of the application.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

