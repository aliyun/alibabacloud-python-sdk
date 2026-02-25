# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskNumberRequest(DaraModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
        promotion_option_no: str = None,
        target: int = None,
    ):
        # Specifies whether to restart compute nodes in quick restart mode. Default value: false. Valid values:
        # 
        # *   true: Compute nodes are restarted in quick restart mode in multiple batches. The batches are executed in parallel, and the nodes in each batch are restarted at the same time.
        # *   false: Compute nodes are restarted in rolling restart mode.
        self.fast_mode = fast_mode
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        self.promotion_option_no = promotion_option_no
        # The number of disks to which you want to change to.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

