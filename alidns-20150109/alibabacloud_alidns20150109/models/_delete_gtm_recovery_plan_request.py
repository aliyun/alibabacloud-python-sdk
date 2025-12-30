# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGtmRecoveryPlanRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        recovery_plan_id: int = None,
    ):
        # The language used by the user.
        self.lang = lang
        # The ID of the disaster recovery plan that you want to delete.
        # 
        # This parameter is required.
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')

        return self

