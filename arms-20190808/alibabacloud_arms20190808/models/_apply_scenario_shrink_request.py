# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyScenarioShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        config_shrink: str = None,
        name: str = None,
        region_id: str = None,
        scenario: str = None,
        sign: str = None,
        sn_dump: bool = None,
        sn_force: bool = None,
        sn_stat: bool = None,
        sn_transfer: bool = None,
        update_option: bool = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The configuration of the business monitoring job. The value is a JSON string. For more information about this parameter, see the following additional information about the **Config** parameter.
        # 
        # This parameter is required.
        self.config_shrink = config_shrink
        # The name of the business monitoring job.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The scenario where you want to use the business monitoring job. Valid values:
        # 
        # *   `USER-DEFINED`: user-defined. This is the default value.
        # *   `EDAS-ROLLOUT`: application release in Enterprise Distributed Application Service (EDAS)
        # *   `OAM-ROLLOUT`: application release based on Open Application Model (OAM)
        # *   `MSC-CANARY`: canary release based on Microservice Engine (MSE)
        self.scenario = scenario
        # The code of the business monitoring job. This parameter is not required when you create a business monitoring job. However, this parameter is required when you update a business monitoring job.
        self.sign = sign
        # Specifies whether to record business parameters to the trace marked with the coloring sign.
        # 
        # *   `true`
        # *   `false`: This is the default value.
        self.sn_dump = sn_dump
        # Specifies whether traffic in the trace marked with the coloring sign is all collected.
        # 
        # *   `true`
        # *   `false`: This is the default value.
        self.sn_force = sn_force
        # Specifies whether to count traffic based on the coloring sign.
        # 
        # *   `true`
        # *   `false`: This is the default value.
        self.sn_stat = sn_stat
        # Specifies whether the coloring sign is transparently passed down to downstream application nodes in the trace.
        # 
        # *   `true`
        # *   `false`: This is the default value.
        self.sn_transfer = sn_transfer
        # Specifies whether the operation is an update operation.
        # 
        # *   `true`: update
        # *   `false`: insert
        # 
        # This parameter is required.
        self.update_option = update_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.sign is not None:
            result['Sign'] = self.sign

        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump

        if self.sn_force is not None:
            result['SnForce'] = self.sn_force

        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat

        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer

        if self.update_option is not None:
            result['UpdateOption'] = self.update_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('Sign') is not None:
            self.sign = m.get('Sign')

        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')

        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')

        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')

        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')

        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')

        return self

