# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        cu: int = None,
        gpu: int = None,
        gpu_spec: List[str] = None,
        gpu_subscription: main_models.UpdateWorkspaceRequestGpuSubscription = None,
        ip_white_list: List[str] = None,
        resource_group_id: str = None,
        subscription: main_models.UpdateWorkspaceRequestSubscription = None,
        workspace_id: str = None,
        workspace_name: str = None,
        region_id: str = None,
    ):
        # The upper limit of workspace resources.
        self.cu = cu
        # The number of GPU cards.
        self.gpu = gpu
        # The GPU instance type.
        self.gpu_spec = gpu_spec
        self.gpu_subscription = gpu_subscription
        self.ip_white_list = ip_white_list
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The information for converting from pay-as-you-go to subscription.
        self.subscription = subscription
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.gpu_subscription:
            self.gpu_subscription.validate()
        if self.subscription:
            self.subscription.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.gpu is not None:
            result['gpu'] = self.gpu

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.gpu_subscription is not None:
            result['gpuSubscription'] = self.gpu_subscription.to_map()

        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.subscription is not None:
            result['subscription'] = self.subscription.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('gpuSubscription') is not None:
            temp_model = main_models.UpdateWorkspaceRequestGpuSubscription()
            self.gpu_subscription = temp_model.from_map(m.get('gpuSubscription'))

        if m.get('ipWhiteList') is not None:
            self.ip_white_list = m.get('ipWhiteList')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('subscription') is not None:
            temp_model = main_models.UpdateWorkspaceRequestSubscription()
            self.subscription = temp_model.from_map(m.get('subscription'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class UpdateWorkspaceRequestSubscription(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_renew_period: str = None,
        auto_renew_period_unit: str = None,
        client_token: str = None,
        duration: str = None,
        payment_duration_unit: str = None,
        queue: List[str] = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter is required for the pre-paid billing type.
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter is required for the pre-paid billing type.
        self.auto_renew_period = auto_renew_period
        # The auto-renewal period unit. This parameter is required for the pre-paid billing type.
        self.auto_renew_period_unit = auto_renew_period_unit
        # The idempotency token.
        self.client_token = client_token
        # The number of subscription periods. This parameter is required for the pre-paid billing type.
        self.duration = duration
        # The subscription period unit.
        self.payment_duration_unit = payment_duration_unit
        # The list of running queues to be converted.
        self.queue = queue

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period

        if self.auto_renew_period_unit is not None:
            result['autoRenewPeriodUnit'] = self.auto_renew_period_unit

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.duration is not None:
            result['duration'] = self.duration

        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit

        if self.queue is not None:
            result['queue'] = self.queue

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')

        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')

        if m.get('queue') is not None:
            self.queue = m.get('queue')

        return self

class UpdateWorkspaceRequestGpuSubscription(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        gpu_machine_num: int = None,
        instance_id: str = None,
        instance_type_id: str = None,
        operation: str = None,
        payment_duration_unit: str = None,
    ):
        self.auto_renew = auto_renew
        self.duration = duration
        self.gpu_machine_num = gpu_machine_num
        self.instance_id = instance_id
        self.instance_type_id = instance_type_id
        self.operation = operation
        self.payment_duration_unit = payment_duration_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.duration is not None:
            result['duration'] = self.duration

        if self.gpu_machine_num is not None:
            result['gpuMachineNum'] = self.gpu_machine_num

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type_id is not None:
            result['instanceTypeId'] = self.instance_type_id

        if self.operation is not None:
            result['operation'] = self.operation

        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('gpuMachineNum') is not None:
            self.gpu_machine_num = m.get('gpuMachineNum')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceTypeId') is not None:
            self.instance_type_id = m.get('instanceTypeId')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')

        return self

