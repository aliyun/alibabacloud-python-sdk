# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStrategyRequest(DaraModel):
    def __init__(
        self,
        custom_type: str = None,
        cycle_days: str = None,
        cycle_start_time: str = None,
        end_time: str = None,
        id: str = None,
        name: str = None,
        risk_custom_params: str = None,
        risk_sub_type_name: str = None,
        source_ip: str = None,
        start_time: str = None,
        target_type: str = None,
    ):
        # The policy type. Valid values:
        # 
        # - **custom**: custom policy.
        # - **common**: standard policy.
        # 
        # This parameter is required.
        self.custom_type = custom_type
        # The cycle of the baseline check. Valid values:
        # 
        # - **1**: Every 1 day.
        # - **3**: Every 3 days.
        # - **7**: Every 7 days.
        # - **30**: Every 30 days.
        # 
        # This parameter is required.
        self.cycle_days = cycle_days
        # The start time of the baseline check. Valid values:
        # 
        # - **0**: The baseline check starts between 00:00 and 06:00.
        # - **6**: The baseline check starts between 06:00 and 12:00.
        # - **12**: The baseline check starts between 12:00 and 18:00.
        # - **18**: The baseline check starts between 18:00 and 24:00.
        # 
        # > This parameter is deprecated.
        # 
        # The value indicates the start hour of the daily check period, in hours.
        self.cycle_start_time = cycle_start_time
        # The end time of the policy execution. Format: hh:mm:ss.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the baseline check policy.
        self.id = id
        # The name of the baseline check policy.
        # 
        # This parameter is required.
        self.name = name
        # The custom configuration of baseline check items. The value is in JSON format and contains the following parameters:
        # 
        # - **typeName**: The baseline name.
        # - **checkDetails**: The check details. The value is in JSON format.
        # 
        #     - **checkId**: The ID of the check item.
        #     - **rules**: The policy configuration. The value is in JSON format.
        # 
        #         - **ruleId**: The ID of the policy configuration.
        #         - **paramList**: The collection of policy parameter settings. The value is in JSON format.
        # 
        #             - **paramName**: The parameter name.
        #             - **value**: The parameter settings value.
        self.risk_custom_params = risk_custom_params
        # The subtype of the check item. You can call the [DescribeRiskType](~~DescribeRiskType~~) operation to obtain the subtype.
        # 
        # This parameter is required.
        self.risk_sub_type_name = risk_sub_type_name
        # The source IP address of the request.
        self.source_ip = source_ip
        # The start time of the policy execution. Format: hh:mm:ss.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The scan method of the policy. Valid values:
        # 
        # - **groupId**: group-based scan.
        # - **uuid**: asset-based scan.
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_type is not None:
            result['CustomType'] = self.custom_type

        if self.cycle_days is not None:
            result['CycleDays'] = self.cycle_days

        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_custom_params is not None:
            result['RiskCustomParams'] = self.risk_custom_params

        if self.risk_sub_type_name is not None:
            result['RiskSubTypeName'] = self.risk_sub_type_name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')

        if m.get('CycleDays') is not None:
            self.cycle_days = m.get('CycleDays')

        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskCustomParams') is not None:
            self.risk_custom_params = m.get('RiskCustomParams')

        if m.get('RiskSubTypeName') is not None:
            self.risk_sub_type_name = m.get('RiskSubTypeName')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

