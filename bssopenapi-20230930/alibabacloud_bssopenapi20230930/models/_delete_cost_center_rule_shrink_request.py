# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCostCenterRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression_shrink: str = None,
        nbid: str = None,
    ):
        # The cost center ID.
        self.cost_center_id = cost_center_id
        # The rule expression.
        # **This field does not need to be specified for delete operations.**
        self.filter_expression_shrink = filter_expression_shrink
        # The primary marketplace ID. If left empty, the marketplace ID of the current user is used by default.
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.filter_expression_shrink is not None:
            result['FilterExpression'] = self.filter_expression_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('FilterExpression') is not None:
            self.filter_expression_shrink = m.get('FilterExpression')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

