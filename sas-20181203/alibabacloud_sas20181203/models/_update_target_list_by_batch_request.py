# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateTargetListByBatchRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        operation_list: List[main_models.UpdateTargetListByBatchRequestOperationList] = None,
    ):
        # The ID of the release batch.
        # 
        # This parameter is required.
        self.batch_id = batch_id
        # The operations on assets.
        # 
        # This parameter is required.
        self.operation_list = operation_list

    def validate(self):
        if self.operation_list:
            for v1 in self.operation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        result['OperationList'] = []
        if self.operation_list is not None:
            for k1 in self.operation_list:
                result['OperationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        self.operation_list = []
        if m.get('OperationList') is not None:
            for k1 in m.get('OperationList'):
                temp_model = main_models.UpdateTargetListByBatchRequestOperationList()
                self.operation_list.append(temp_model.from_map(k1))

        return self

class UpdateTargetListByBatchRequestOperationList(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        operation: str = None,
        uuid: str = None,
        vpc_instance_id: str = None,
    ):
        # The ID of the server group.
        # 
        # >  You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to query the IDs of server groups.
        self.group_id = group_id
        # The operation type. Valid values:
        # 
        # *   **add**: the add operation.
        # *   **del**: the remove operation.
        self.operation = operation
        # The UUID of the server.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid = uuid
        # The ID of the VPC-connected instance.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

