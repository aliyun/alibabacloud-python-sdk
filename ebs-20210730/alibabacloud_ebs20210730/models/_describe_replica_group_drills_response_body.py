# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeReplicaGroupDrillsResponseBody(DaraModel):
    def __init__(
        self,
        drills: List[main_models.DescribeReplicaGroupDrillsResponseBodyDrills] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of disaster recovery drills that were performed on the replication pair-consistent group.
        self.drills = drills
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.drills:
            for v1 in self.drills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Drills'] = []
        if self.drills is not None:
            for k1 in self.drills:
                result['Drills'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.drills = []
        if m.get('Drills') is not None:
            for k1 in m.get('Drills'):
                temp_model = main_models.DescribeReplicaGroupDrillsResponseBodyDrills()
                self.drills.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeReplicaGroupDrillsResponseBodyDrills(DaraModel):
    def __init__(
        self,
        drill_id: str = None,
        group_id: str = None,
        pairs_info: List[main_models.DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo] = None,
        recover_point: int = None,
        start_at: int = None,
        status: str = None,
        status_message: str = None,
    ):
        # The ID of the drill.
        self.drill_id = drill_id
        # The ID of the replication pair-consistent group.
        self.group_id = group_id
        # The information of replication pairs.
        self.pairs_info = pairs_info
        # The recovery point of the drill. The value of this parameter is a timestamp. Unit: seconds.
        self.recover_point = recover_point
        # The beginning time of the drill. The value of this parameter is a timestamp. Unit: seconds.
        self.start_at = start_at
        # The status of the drill. Valid values:
        # 
        # *   execute_failed
        # *   executed
        # *   executing
        # *   clear_failed
        # *   clearing
        self.status = status
        # The error message that appears if the drill fails to be executed.
        self.status_message = status_message

    def validate(self):
        if self.pairs_info:
            for v1 in self.pairs_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['PairsInfo'] = []
        if self.pairs_info is not None:
            for k1 in self.pairs_info:
                result['PairsInfo'].append(k1.to_map() if k1 else None)

        if self.recover_point is not None:
            result['RecoverPoint'] = self.recover_point

        if self.start_at is not None:
            result['StartAt'] = self.start_at

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.pairs_info = []
        if m.get('PairsInfo') is not None:
            for k1 in m.get('PairsInfo'):
                temp_model = main_models.DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo()
                self.pairs_info.append(temp_model.from_map(k1))

        if m.get('RecoverPoint') is not None:
            self.recover_point = m.get('RecoverPoint')

        if m.get('StartAt') is not None:
            self.start_at = m.get('StartAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        return self

class DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo(DaraModel):
    def __init__(
        self,
        drill_disk_id: str = None,
        drill_disk_status: str = None,
        pair_id: str = None,
    ):
        # The ID of the drill disk.
        self.drill_disk_id = drill_disk_id
        # The status of the drill disk. Valid values:
        # 
        # *   created
        # *   deleted
        # *   creating
        # *   deleting
        # 
        # >  This parameter can also display error code details if your drill disk fails to be created or deleted.
        self.drill_disk_status = drill_disk_status
        # The ID of the replication pair.
        self.pair_id = pair_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drill_disk_id is not None:
            result['DrillDiskId'] = self.drill_disk_id

        if self.drill_disk_status is not None:
            result['DrillDiskStatus'] = self.drill_disk_status

        if self.pair_id is not None:
            result['PairId'] = self.pair_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrillDiskId') is not None:
            self.drill_disk_id = m.get('DrillDiskId')

        if m.get('DrillDiskStatus') is not None:
            self.drill_disk_status = m.get('DrillDiskStatus')

        if m.get('PairId') is not None:
            self.pair_id = m.get('PairId')

        return self

