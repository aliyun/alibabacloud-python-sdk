# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ApplyScenarioRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        config: Dict[str, Any] = None,
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
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.config = config
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        self.scenario = scenario
        self.sign = sign
        self.sn_dump = sn_dump
        self.sn_force = sn_force
        self.sn_stat = sn_stat
        self.sn_transfer = sn_transfer
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

        if self.config is not None:
            result['Config'] = self.config

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
            self.config = m.get('Config')

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

