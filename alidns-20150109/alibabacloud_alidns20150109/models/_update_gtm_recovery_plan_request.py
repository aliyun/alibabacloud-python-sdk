# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGtmRecoveryPlanRequest(DaraModel):
    def __init__(
        self,
        fault_addr_pool: str = None,
        lang: str = None,
        name: str = None,
        recovery_plan_id: int = None,
        remark: str = None,
    ):
        # The list of faulty address pools.
        self.fault_addr_pool = fault_addr_pool
        # The language in which you want the values of some response parameters to be returned. These response parameters support multiple languages.
        self.lang = lang
        # The name of the disaster recovery plan.
        self.name = name
        # The ID of the disaster recovery plan.
        # 
        # This parameter is required.
        self.recovery_plan_id = recovery_plan_id
        # The remarks about the disaster recovery plan.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_addr_pool is not None:
            result['FaultAddrPool'] = self.fault_addr_pool

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultAddrPool') is not None:
            self.fault_addr_pool = m.get('FaultAddrPool')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

