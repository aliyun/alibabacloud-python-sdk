# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopySnapshotShrinkRequest(DaraModel):
    def __init__(
        self,
        destination_region_ids_shrink: str = None,
        destination_snapshot_description: str = None,
        destination_snapshot_name: str = None,
        instance_billing_cycle: str = None,
        snapshot_id: str = None,
    ):
        # The IDs of destination nodes.
        # 
        # This parameter is required.
        self.destination_region_ids_shrink = destination_region_ids_shrink
        # The description of the snapshot. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.destination_snapshot_description = destination_snapshot_description
        # The name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.destination_snapshot_name = destination_snapshot_name
        self.instance_billing_cycle = instance_billing_cycle
        # The ID of the source snapshot.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_ids_shrink is not None:
            result['DestinationRegionIds'] = self.destination_region_ids_shrink

        if self.destination_snapshot_description is not None:
            result['DestinationSnapshotDescription'] = self.destination_snapshot_description

        if self.destination_snapshot_name is not None:
            result['DestinationSnapshotName'] = self.destination_snapshot_name

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids_shrink = m.get('DestinationRegionIds')

        if m.get('DestinationSnapshotDescription') is not None:
            self.destination_snapshot_description = m.get('DestinationSnapshotDescription')

        if m.get('DestinationSnapshotName') is not None:
            self.destination_snapshot_name = m.get('DestinationSnapshotName')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

