# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetExpressionFieldsShrinkRequest(DaraModel):
    def __init__(
        self,
        expressions_shrink: str = None,
        instance_id: str = None,
        kind: str = None,
        phase: str = None,
        plan_name_en: str = None,
        site_id: int = None,
    ):
        # List of expressions.
        self.expressions_shrink = expressions_shrink
        self.instance_id = instance_id
        self.kind = kind
        # WAF Phase
        self.phase = phase
        self.plan_name_en = plan_name_en
        # Site ID
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expressions_shrink is not None:
            result['Expressions'] = self.expressions_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.plan_name_en is not None:
            result['PlanNameEn'] = self.plan_name_en

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expressions') is not None:
            self.expressions_shrink = m.get('Expressions')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('PlanNameEn') is not None:
            self.plan_name_en = m.get('PlanNameEn')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

