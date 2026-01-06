# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeOtsTableSnapshotsRequest(DaraModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        end_time: int = None,
        limit: int = None,
        next_token: str = None,
        ots_instances: List[main_models.DescribeOtsTableSnapshotsRequestOtsInstances] = None,
        snapshot_ids: List[str] = None,
        start_time: int = None,
    ):
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The UID of the source account used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The end time of the backup. The value must be a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The maximum number of rows that you want the current query to return.
        self.limit = limit
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The Tablestore instances that are backed up.
        self.ots_instances = ots_instances
        # The snapshot IDs.
        self.snapshot_ids = snapshot_ids
        # The start time of the backup. The value must be a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        if self.ots_instances:
            for v1 in self.ots_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['OtsInstances'] = []
        if self.ots_instances is not None:
            for k1 in self.ots_instances:
                result['OtsInstances'].append(k1.to_map() if k1 else None)

        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.ots_instances = []
        if m.get('OtsInstances') is not None:
            for k1 in m.get('OtsInstances'):
                temp_model = main_models.DescribeOtsTableSnapshotsRequestOtsInstances()
                self.ots_instances.append(temp_model.from_map(k1))

        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeOtsTableSnapshotsRequestOtsInstances(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        table_names: List[str] = None,
    ):
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        return self

