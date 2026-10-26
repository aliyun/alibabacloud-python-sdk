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
        start_timestamp_ms: int = None,
    ):
        # **The instance ID.**
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # **The enumeration value for the table synchronization mode**:
        # - `Merge`: Merge.
        self.mode = mode
        # The partition of the table to be published.
        self.partition = partition
        # The partition of the table to be published.
        self.partitions = partitions
        # **Specifies whether to skip the threshold check when synchronizing the table.**
        self.skip_threshold_check = skip_threshold_check
        # The start time of incremental data playback (UNIX milliseconds).
        self.start_timestamp_ms = start_timestamp_ms

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

        if self.start_timestamp_ms is not None:
            result['StartTimestampMs'] = self.start_timestamp_ms

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

        if m.get('StartTimestampMs') is not None:
            self.start_timestamp_ms = m.get('StartTimestampMs')

        return self

