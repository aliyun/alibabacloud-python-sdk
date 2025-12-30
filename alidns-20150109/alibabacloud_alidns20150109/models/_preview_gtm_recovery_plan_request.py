# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreviewGtmRecoveryPlanRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        recovery_plan_id: int = None,
    ):
        # The language used by the user.
        self.lang = lang
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on per page. Maximum value: **20**. Default value: **5**.
        self.page_size = page_size
        # The ID of the disaster recovery plan that you want to preview.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')

        return self

