# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodeNumberRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
        parallelism: int = None,
        promotion_option_no: str = None,
        target: int = None,
        termination_grace_period_seconds: int = None,
    ):
        # Specifies whether to automatically purchase (pay for) all products specified in the Products parameter. Valid values:
        # - true: Automatic payment.
        # - false: No automatic payment.
        self.auto_pay = auto_pay
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The compute group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The decommission concurrency for BE scale-in scenarios in compute-storage coupled mode. Default value: 1.
        self.parallelism = parallelism
        # The coupon ID.
        self.promotion_option_no = promotion_option_no
        # The target number of nodes.
        # 
        # This parameter is required.
        self.target = target
        # The wait time for running tasks to complete before dropping nodes during CN scale-in scenarios in compute-storage decoupled mode.
        self.termination_grace_period_seconds = termination_grace_period_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

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
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

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

