# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeReplicationSlotsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        slots: List[main_models.DescribeReplicationSlotsResponseBodySlots] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of replication slots.
        self.slots = slots

    def validate(self):
        if self.slots:
            for v1 in self.slots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Slots'] = []
        if self.slots is not None:
            for k1 in self.slots:
                result['Slots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.slots = []
        if m.get('Slots') is not None:
            for k1 in m.get('Slots'):
                temp_model = main_models.DescribeReplicationSlotsResponseBodySlots()
                self.slots.append(temp_model.from_map(k1))

        return self

class DescribeReplicationSlotsResponseBodySlots(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        database: str = None,
        plugin: str = None,
        slot_name: str = None,
        slot_status: str = None,
        slot_type: str = None,
        sub_group_name: str = None,
        sub_replay_lag: str = None,
        temporary: str = None,
        wal_delay: str = None,
    ):
        # The ID of the PolarDB cluster to which the replication slot belongs.
        self.dbcluster_id = dbcluster_id
        # The name of the database associated with the replication slot.
        self.database = database
        # The name of the output plugin used by the logical replication slot.
        self.plugin = plugin
        # The name of the replication slot.
        self.slot_name = slot_name
        # The status of the replication slot.
        self.slot_status = slot_status
        # The type of the replication slot.
        self.slot_type = slot_type
        # The name of the child node of the distributed instance.
        self.sub_group_name = sub_group_name
        # The replay lag of the subscription.
        self.sub_replay_lag = sub_replay_lag
        # Indicates whether the replication slot is temporary. The value is a string: true or false.
        self.temporary = temporary
        # The WAL latency.
        self.wal_delay = wal_delay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.database is not None:
            result['Database'] = self.database

        if self.plugin is not None:
            result['Plugin'] = self.plugin

        if self.slot_name is not None:
            result['SlotName'] = self.slot_name

        if self.slot_status is not None:
            result['SlotStatus'] = self.slot_status

        if self.slot_type is not None:
            result['SlotType'] = self.slot_type

        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name

        if self.sub_replay_lag is not None:
            result['SubReplayLag'] = self.sub_replay_lag

        if self.temporary is not None:
            result['Temporary'] = self.temporary

        if self.wal_delay is not None:
            result['WalDelay'] = self.wal_delay

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Plugin') is not None:
            self.plugin = m.get('Plugin')

        if m.get('SlotName') is not None:
            self.slot_name = m.get('SlotName')

        if m.get('SlotStatus') is not None:
            self.slot_status = m.get('SlotStatus')

        if m.get('SlotType') is not None:
            self.slot_type = m.get('SlotType')

        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')

        if m.get('SubReplayLag') is not None:
            self.sub_replay_lag = m.get('SubReplayLag')

        if m.get('Temporary') is not None:
            self.temporary = m.get('Temporary')

        if m.get('WalDelay') is not None:
            self.wal_delay = m.get('WalDelay')

        return self

