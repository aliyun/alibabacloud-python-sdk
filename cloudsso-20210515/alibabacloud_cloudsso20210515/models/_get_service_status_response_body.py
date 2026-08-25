# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetServiceStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_status: main_models.GetServiceStatusResponseBodyServiceStatus = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The status information of CloudSSO.
        self.service_status = service_status

    def validate(self):
        if self.service_status:
            self.service_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceStatus') is not None:
            temp_model = main_models.GetServiceStatusResponseBodyServiceStatus()
            self.service_status = temp_model.from_map(m.get('ServiceStatus'))

        return self

class GetServiceStatusResponseBodyServiceStatus(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        prerequisite_check_result: str = None,
        regions_in_use: List[str] = None,
        status: str = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # Indicates whether the prerequisites for enabling CloudSSO are met. Valid values:
        # 
        # - Success: The prerequisites are met.
        # 
        # - Failed: The prerequisites are not met.
        # 
        # > The value of this parameter is returned only if the value of `Status` is `Disabled`.
        self.prerequisite_check_result = prerequisite_check_result
        # The IDs of regions where directories are deployed.
        self.regions_in_use = regions_in_use
        # The status of CloudSSO. Valid values:
        # 
        # - Enabled
        # 
        # - Disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.prerequisite_check_result is not None:
            result['PrerequisiteCheckResult'] = self.prerequisite_check_result

        if self.regions_in_use is not None:
            result['RegionsInUse'] = self.regions_in_use

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('PrerequisiteCheckResult') is not None:
            self.prerequisite_check_result = m.get('PrerequisiteCheckResult')

        if m.get('RegionsInUse') is not None:
            self.regions_in_use = m.get('RegionsInUse')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

