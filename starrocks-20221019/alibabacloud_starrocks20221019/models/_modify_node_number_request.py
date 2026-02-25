# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodeNumberRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        parallelism: int = None,
        promotion_option_no: str = None,
        target: int = None,
        termination_grace_period_seconds: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.parallelism = parallelism
        self.promotion_option_no = promotion_option_no
        # The number of nodes to which you want to change to.
        # 
        # This parameter is required.
        self.target = target
        self.termination_grace_period_seconds = termination_grace_period_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.target is not None:
            result['Target'] = self.target

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        return self

