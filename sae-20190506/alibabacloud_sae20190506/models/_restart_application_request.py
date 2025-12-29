# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_enable_application_scaling_rule: bool = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to automatically enable an auto scaling policy for the application. Valid values:
        # 
        # *   **true**: enabled.
        # *   **false**: disabled
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        # The percentage of the minimum number of available instances. Take note of the following rules:
        # 
        # *   If you set the value to **-1**, the minimum number of available instances is not determined based on this parameter. Default value: -1.
        # *   If you set the value to a number **from 0 to 100**, the minimum number of available instances is calculated by using the following formula: Current number of instances × (Value of MinReadyInstanceRatio × 100%). The value is the nearest integer rounded up from the calculated result. For example, if the percentage is set to **50**% and five instances are available, the minimum number of available instances is 3.
        # 
        # > When **MinReadyInstance** and **MinReadyInstanceRatio** are specified and **MinReadyInstanceRatio** is set to a number from 0 to 100, the value of \\*\\*MinReadyInstanceRatio** takes precedence.**** For example, if **MinReadyInstances** is set to **5\\*\\*, and **MinReadyInstanceRatio** is set to **50**, the minimum number of available instances is set to the nearest integer rounded up from the calculated result of the following formula: Current number of instances × **50%**.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Special values:
        # 
        # *   If you set the value to **0**, business interruptions occur when the application is updated.
        # *   If you set the value to \\*\\*-1\\*\\*, the minimum number of available instances is automatically set to a system-recommended value. The value is the nearest integer to which the calculated result of the following formula is rounded up: Current number of instances × 25%. For example, if five instances are available, the minimum number of available instances is calculated by using the following formula: 5 × 25% = 1.25. In this case, the minimum number of available instances is 2.
        # 
        # > Make sure that at least one instance is available during application deployment and rollback to prevent business interruptions.
        self.min_ready_instances = min_ready_instances

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

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        return self

