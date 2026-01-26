# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class PublishRecallManagementTableRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mode: str = None,
        partition: Dict[str, str] = None,
        partitions: Dict[str, str] = None,
        skip_threshold_check: bool = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.mode = mode
        self.partition = partition
        self.partitions = partitions
        self.skip_threshold_check = skip_threshold_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.partition is not None:
            result['Partition'] = self.partition

        if self.partitions is not None:
            result['Partitions'] = self.partitions

        if self.skip_threshold_check is not None:
            result['SkipThresholdCheck'] = self.skip_threshold_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')

        if m.get('SkipThresholdCheck') is not None:
            self.skip_threshold_check = m.get('SkipThresholdCheck')

        return self

