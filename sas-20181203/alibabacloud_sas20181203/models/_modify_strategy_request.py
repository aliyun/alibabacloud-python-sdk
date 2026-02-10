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
        # The type of the baseline check policy. Valid values:
        # 
        # *   **custom**: a custom baseline check policy
        # *   **common**: a standard baseline check policy
        # 
        # This parameter is required.
        self.custom_type = custom_type
        # The new interval of the baseline check. Valid values:
        # 
        # *   **1**: every 2 days
        # *   **3**: every 4 days
        # *   **7**: every 8 days
        # *   **30**: every 31 days
        # 
        # This parameter is required.
        self.cycle_days = cycle_days
        # The new time range during which the baseline check starts. Valid values:
        # 
        # *   **0**: The baseline check starts within the time range from 00:00 to 06:00.
        # *   **6**: The baseline check starts within the time range from 06:00 to 12:00.
        # *   **12**: The baseline check starts within the time range from 12:00 to 18:00.
        # *   **18**: The baseline check starts within the time range from 18:00 to 24:00.
        # 
        # >  This parameter is deprecated.
        self.cycle_start_time = cycle_start_time
        # The time when the baseline check based on the baseline check policy ends. Specify the time in the hh:mm:ss format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the baseline check policy.
        self.id = id
        # The new name of the baseline check policy.
        # 
        # This parameter is required.
        self.name = name
        # The custom configurations of the baseline. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **typeName**: the name of the baseline.
        # 
        # *   **checkDetails**: the details of the baseline. The value is in the JSON format.
        # 
        #     *   **checkId**: the ID of the check item.
        # 
        #     *   **rules**: the rule configurations. The value is in the JSON format.
        # 
        #         *   **ruleId**: the ID of the rule.
        # 
        #         *   **paramList**: the list of parameters in the rule. The value is in the JSON format.
        # 
        #             *   **paramName**: the name of the parameter.
        #             *   **value**: the value of the parameter.
        self.risk_custom_params = risk_custom_params
        # The subtype of the baselines. You can call the [DescribeRiskType](~~DescribeRiskType~~) operation to query the subtypes of baselines.
        # 
        # This parameter is required.
        self.risk_sub_type_name = risk_sub_type_name
        # The source IP address of the request.
        self.source_ip = source_ip
        # The time when the baseline check based on the baseline check policy starts. Specify the time in the hh:mm:ss format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The method that is used to apply the baseline check policy. Valid values:
        # 
        # *   **groupId**: asset groups
        # *   **uuid**: assets
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

