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
        # Specifies whether the elastic scaling policy for the application is automatically enabled. Valid values:
        # - **true**: enables the policy.
        # - **false**: disables the policy.
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        # The percentage of the minimum number of ready instances. Valid values:
        # 
        #  - **-1**: the initial value, which indicates that the percentage is not used.
        #  - **0 to 100**: the percentage, which is rounded up. For example, if you set this parameter to **50** and you have 5 instances, the minimum number of ready instances is 3.
        # 
        # > If both **MinReadyInstances** and **MinReadyInstanceRatio** are specified and the value of **MinReadyInstanceRatio** is not **-1**, the **MinReadyInstanceRatio** parameter takes precedence. For example, if **MinReadyInstances** is set to **5** and **MinReadyInstanceRatio** is set to **50**, the system uses **50** to calculate the minimum number of ready instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of ready instances. Valid values:
        # 
        # - If you set this parameter to **0**, services are interrupted during the application upgrade.
        # - If you set this parameter to **-1**, the system uses the recommended value, which is 25% of the current number of instances. For example, if you have 5 instances, 5 × 25% = 1.25. The value is rounded up to 2.
        # 
        # > For each rolling deployment, set the minimum number of ready instances to 1 or greater to ensure service continuity.
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

