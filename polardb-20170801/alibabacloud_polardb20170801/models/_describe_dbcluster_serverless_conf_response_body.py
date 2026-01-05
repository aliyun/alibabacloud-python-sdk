# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterServerlessConfResponseBody(DaraModel):
    def __init__(
        self,
        agile_scale_max: str = None,
        allow_shut_down: str = None,
        dbcluster_id: str = None,
        request_id: str = None,
        scale_ap_ro_num_max: str = None,
        scale_ap_ro_num_min: str = None,
        scale_max: str = None,
        scale_min: str = None,
        scale_ro_num_max: str = None,
        scale_ro_num_min: str = None,
        seconds_until_auto_pause: str = None,
        serverless_rule_cpu_enlarge_threshold: str = None,
        serverless_rule_cpu_shrink_threshold: str = None,
        serverless_rule_mode: str = None,
        switchs: str = None,
        traditional_scale_max_threshold: str = None,
    ):
        self.agile_scale_max = agile_scale_max
        # Whether to enable idle shutdown. Values:
        # 
        # - **true**: Enable
        # 
        # - **false**: Disable (default)
        self.allow_shut_down = allow_shut_down
        # Serverless cluster ID.
        self.dbcluster_id = dbcluster_id
        # Request ID.
        self.request_id = request_id
        # The maximum number of read-only column store nodes. Valid values: 0 to 15.
        self.scale_ap_ro_num_max = scale_ap_ro_num_max
        # The minimum number of read-only column store nodes. Valid values: 0 to 15.
        self.scale_ap_ro_num_min = scale_ap_ro_num_min
        # Maximum scaling limit for a single node. Range: 1 PCU~32 PCU.
        self.scale_max = scale_max
        # Minimum scaling limit for a single node. Range: 1 PCU~31 PCU.
        self.scale_min = scale_min
        # Maximum scaling limit for the number of read-only nodes. Range: 0~15.
        self.scale_ro_num_max = scale_ro_num_max
        # Minimum scaling limit for the number of read-only nodes. Range: 0~15.
        self.scale_ro_num_min = scale_ro_num_min
        # Detection duration for idle shutdown. Range: 300~86,400. Unit: seconds. The detection duration must be a multiple of 300 seconds.
        self.seconds_until_auto_pause = seconds_until_auto_pause
        # CPU upscale threshold.
        self.serverless_rule_cpu_enlarge_threshold = serverless_rule_cpu_enlarge_threshold
        # CPU downscale threshold.
        self.serverless_rule_cpu_shrink_threshold = serverless_rule_cpu_shrink_threshold
        # Elasticity sensitivity. Values:
        # 
        # - normal: Standard
        # 
        # - flexible: Sensitive
        self.serverless_rule_mode = serverless_rule_mode
        # Whether steady state is enabled. Values:
        # 
        # 1: Enabled
        # 
        # 0: Disabled
        self.switchs = switchs
        self.traditional_scale_max_threshold = traditional_scale_max_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agile_scale_max is not None:
            result['AgileScaleMax'] = self.agile_scale_max

        if self.allow_shut_down is not None:
            result['AllowShutDown'] = self.allow_shut_down

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scale_ap_ro_num_max is not None:
            result['ScaleApRoNumMax'] = self.scale_ap_ro_num_max

        if self.scale_ap_ro_num_min is not None:
            result['ScaleApRoNumMin'] = self.scale_ap_ro_num_min

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.scale_ro_num_max is not None:
            result['ScaleRoNumMax'] = self.scale_ro_num_max

        if self.scale_ro_num_min is not None:
            result['ScaleRoNumMin'] = self.scale_ro_num_min

        if self.seconds_until_auto_pause is not None:
            result['SecondsUntilAutoPause'] = self.seconds_until_auto_pause

        if self.serverless_rule_cpu_enlarge_threshold is not None:
            result['ServerlessRuleCpuEnlargeThreshold'] = self.serverless_rule_cpu_enlarge_threshold

        if self.serverless_rule_cpu_shrink_threshold is not None:
            result['ServerlessRuleCpuShrinkThreshold'] = self.serverless_rule_cpu_shrink_threshold

        if self.serverless_rule_mode is not None:
            result['ServerlessRuleMode'] = self.serverless_rule_mode

        if self.switchs is not None:
            result['Switchs'] = self.switchs

        if self.traditional_scale_max_threshold is not None:
            result['TraditionalScaleMaxThreshold'] = self.traditional_scale_max_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgileScaleMax') is not None:
            self.agile_scale_max = m.get('AgileScaleMax')

        if m.get('AllowShutDown') is not None:
            self.allow_shut_down = m.get('AllowShutDown')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScaleApRoNumMax') is not None:
            self.scale_ap_ro_num_max = m.get('ScaleApRoNumMax')

        if m.get('ScaleApRoNumMin') is not None:
            self.scale_ap_ro_num_min = m.get('ScaleApRoNumMin')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ScaleRoNumMax') is not None:
            self.scale_ro_num_max = m.get('ScaleRoNumMax')

        if m.get('ScaleRoNumMin') is not None:
            self.scale_ro_num_min = m.get('ScaleRoNumMin')

        if m.get('SecondsUntilAutoPause') is not None:
            self.seconds_until_auto_pause = m.get('SecondsUntilAutoPause')

        if m.get('ServerlessRuleCpuEnlargeThreshold') is not None:
            self.serverless_rule_cpu_enlarge_threshold = m.get('ServerlessRuleCpuEnlargeThreshold')

        if m.get('ServerlessRuleCpuShrinkThreshold') is not None:
            self.serverless_rule_cpu_shrink_threshold = m.get('ServerlessRuleCpuShrinkThreshold')

        if m.get('ServerlessRuleMode') is not None:
            self.serverless_rule_mode = m.get('ServerlessRuleMode')

        if m.get('Switchs') is not None:
            self.switchs = m.get('Switchs')

        if m.get('TraditionalScaleMaxThreshold') is not None:
            self.traditional_scale_max_threshold = m.get('TraditionalScaleMaxThreshold')

        return self

