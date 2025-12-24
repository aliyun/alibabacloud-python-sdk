# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateAutoProvisioningGroupResponseBody(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_id: str = None,
        launch_results: main_models.CreateAutoProvisioningGroupResponseBodyLaunchResults = None,
        request_id: str = None,
    ):
        # The ID of the auto provisioning group.
        self.auto_provisioning_group_id = auto_provisioning_group_id
        # The instances created by the auto provisioning group. The values of the parameters in this array are returned only when AutoProvisioningGroupType is set to `instant`.
        self.launch_results = launch_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.launch_results:
            self.launch_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_group_id is not None:
            result['AutoProvisioningGroupId'] = self.auto_provisioning_group_id

        if self.launch_results is not None:
            result['LaunchResults'] = self.launch_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroupId') is not None:
            self.auto_provisioning_group_id = m.get('AutoProvisioningGroupId')

        if m.get('LaunchResults') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupResponseBodyLaunchResults()
            self.launch_results = temp_model.from_map(m.get('LaunchResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAutoProvisioningGroupResponseBodyLaunchResults(DaraModel):
    def __init__(
        self,
        launch_result: List[main_models.CreateAutoProvisioningGroupResponseBodyLaunchResultsLaunchResult] = None,
    ):
        self.launch_result = launch_result

    def validate(self):
        if self.launch_result:
            for v1 in self.launch_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LaunchResult'] = []
        if self.launch_result is not None:
            for k1 in self.launch_result:
                result['LaunchResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.launch_result = []
        if m.get('LaunchResult') is not None:
            for k1 in m.get('LaunchResult'):
                temp_model = main_models.CreateAutoProvisioningGroupResponseBodyLaunchResultsLaunchResult()
                self.launch_result.append(temp_model.from_map(k1))

        return self

class CreateAutoProvisioningGroupResponseBodyLaunchResultsLaunchResult(DaraModel):
    def __init__(
        self,
        amount: int = None,
        error_code: str = None,
        error_msg: str = None,
        instance_ids: main_models.CreateAutoProvisioningGroupResponseBodyLaunchResultsLaunchResultInstanceIds = None,
        instance_type: str = None,
        spot_strategy: str = None,
        zone_id: str = None,
    ):
        # The number of created instances.
        self.amount = amount
        # The error code returned when the instance cannot be created.
        self.error_code = error_code
        # The error message returned when the instance cannot be created.
        self.error_msg = error_msg
        # The IDs of created instances.
        self.instance_ids = instance_ids
        # The instance type of the instance.
        self.instance_type = instance_type
        # The bidding policy for the pay-as-you-go instance. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a spot instance for which you specify the maximum hourly price.
        # *   SpotAsPriceGo: The instance is a spot instance for which the market price at the time of purchase is used as the bid price.
        self.spot_strategy = spot_strategy
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('InstanceIds') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupResponseBodyLaunchResultsLaunchResultInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateAutoProvisioningGroupResponseBodyLaunchResultsLaunchResultInstanceIds(DaraModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

