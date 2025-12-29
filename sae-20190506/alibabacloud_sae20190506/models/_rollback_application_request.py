# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_enable_application_scaling_rule: str = None,
        batch_wait_time: int = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        update_strategy: str = None,
        version_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to automatically enable an auto scaling policy for the application. Take note of the following rules:
        # 
        # *   **true**: turns on Logon-free Sharing
        # *   **false**: turns off Logon-free Sharing
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        # The wait time between batches. Unit: seconds.
        self.batch_wait_time = batch_wait_time
        # The percentage of the minimum number of available instances. Take note of the following rules:
        # 
        # *   If you set the value to **-1**, the minimum number of available instances is not determined based on this parameter. Default value: -1.
        # *   If you set the value to a number **from 0 to 100**, the minimum number of available instances is calculated by using the following formula: Current number of instances × (Value of MinReadyInstanceRatio × 100%). The value is the nearest integer rounded up from the calculated result. For example, if the percentage is set to **50**% and five instances are available, the minimum number of available instances is 3.
        # 
        # > When both **MinReadyInstance** and **MinReadyInstanceRatio** are specified and **MinReadyInstanceRatio** is set to a number from 0 to 100, the value of **MinReadyInstanceRatio** takes precedence.** For example, if **MinReadyInstances** is set to **5, and **MinReadyInstanceRatio** is set to **50**, the minimum number of available instances is set to the nearest integer rounded up from the calculated result of the following formula: Current number of instances × **50%**.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Take note of the following rules:
        # 
        # *   If you set the value to **0**, business interruptions occur when the application is updated.
        # *   If you set the value to \\*\\*-1\\*\\*, the minimum number of available instances is automatically set to a system-recommended value. The value is the nearest integer to which the calculated result of the following formula is rounded up: Current number of instances × 25%. For example, if five instances are available, the minimum number of available instances is calculated by using the following formula: 5 × 25% = 1.25. In this case, the minimum number of available instances is 2.
        # 
        # > Make sure that at least one instance is available during application deployment and rollback to prevent business interruptions.
        self.min_ready_instances = min_ready_instances
        # The deployment policy. If the minimum number of available instances is 1, the value of the **UpdateStrategy** parameter is an empty string (""). If the minimum number of available instances is larger than 1, specify this parameter based on your requirements. Examples:
        # 
        # *   Perform canary release for one instance and release the remaining instances in two batches automatically with a one-minute interval between the deployment of each instance:
        # 
        #     `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":1},"grayUpdate":{"gray":1}}`
        # 
        # *   Perform canary release for one instance and release the remaining instances in two batches manually:
        # 
        #     `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"manual"},"grayUpdate":{"gray":1}}`
        # 
        # *   Release the instances in two batches automatically with no interval between the deployment of each instance:
        # 
        #     `{"type":"BatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":0}}`
        # 
        # The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **type**: the type of the release policy. Valid values: **GrayBatchUpdate** and **BatchUpdate**.
        # 
        # *   **batchUpdate**: the phased release policy.
        # 
        #     *   **batch**: the number of release batches.
        #     *   **releaseType**: the processing method for the batches. Valid values: **auto** and **manual**.
        #     *   **batchWaitTime**: the interval between release batches. Unit: seconds.
        # 
        # *   **grayUpdate**: the number of release batches in the phased release after a canary release. This parameter is returned only if the **type** parameter is set to **GrayBatchUpdate**.
        self.update_strategy = update_strategy
        # The ID of the application version. Call the [ListAppVersions](https://help.aliyun.com/document_detail/162054.html) operation to obtain the version ID.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

