# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListChangeSetsResponseBody(DaraModel):
    def __init__(
        self,
        change_sets: List[main_models.ListChangeSetsResponseBodyChangeSets] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The change sets.
        self.change_sets = change_sets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of change sets returned.
        self.total_count = total_count

    def validate(self):
        if self.change_sets:
            for v1 in self.change_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChangeSets'] = []
        if self.change_sets is not None:
            for k1 in self.change_sets:
                result['ChangeSets'].append(k1.to_map() if k1 else None)

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
        self.change_sets = []
        if m.get('ChangeSets') is not None:
            for k1 in m.get('ChangeSets'):
                temp_model = main_models.ListChangeSetsResponseBodyChangeSets()
                self.change_sets.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListChangeSetsResponseBodyChangeSets(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: str = None,
        change_set_type: str = None,
        create_time: str = None,
        description: str = None,
        execution_status: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.ListChangeSetsResponseBodyChangeSetsTags] = None,
    ):
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The name of the change set.
        self.change_set_name = change_set_name
        # The type of the change set.
        self.change_set_type = change_set_type
        # The time when the change set was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the change set.
        self.description = description
        # The execution status of the change set.
        self.execution_status = execution_status
        # The region ID of the change set.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The ID of the stack with which the change set is associated.
        self.stack_id = stack_id
        # The name of the stack with which the change set is associated.
        self.stack_name = stack_name
        # The status of the change set.
        self.status = status
        # The reason why the change set is in its current state.
        self.status_reason = status_reason
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name

        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')

        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListChangeSetsResponseBodyChangeSetsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListChangeSetsResponseBodyChangeSetsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

