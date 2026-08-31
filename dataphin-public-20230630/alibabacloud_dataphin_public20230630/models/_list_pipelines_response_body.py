# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListPipelinesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPipelinesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The paged query result.
        self.data = data
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListPipelinesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListPipelinesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListPipelinesResponseBodyDataList] = None,
        next_cursor: int = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of node information on the current page.
        self.list = list
        # The cursor for the next page (an opaque cursor that the caller does not need to interpret). A null value indicates that there are no more pages. Otherwise, pass this value as the nextCursor parameter in the next request to retrieve the next page.
        self.next_cursor = next_cursor
        # The current page number, starting from 1.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records that match the conditions. For the first page request, the actual total count is returned. For subsequent page requests (when nextCursor is passed in), if totalCount is included in the request, the same value is returned. Otherwise, this field is not returned. The total value is a snapshot taken at the time of the first page query and is not updated in real time as data changes during pagination.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.next_cursor is not None:
            result['NextCursor'] = self.next_cursor

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListPipelinesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('NextCursor') is not None:
            self.next_cursor = m.get('NextCursor')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListPipelinesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        develop_owners: List[str] = None,
        directory: str = None,
        file_id: int = None,
        node_id: str = None,
        node_name: str = None,
        ops_owners: List[str] = None,
        pipeline_id: int = None,
        schedule_type: int = None,
        tags: List[str] = None,
        task_status: str = None,
        task_type: int = None,
    ):
        # The list of user IDs of development owners.
        self.develop_owners = develop_owners
        # The directory where the node is located.
        self.directory = directory
        # The file ID.
        self.file_id = file_id
        # The schedule node ID.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The list of user IDs of O&M owners.
        self.ops_owners = ops_owners
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The schedule type. Valid values:
        # 
        # - 1: periodic scheduling.
        # - 3: manual scheduling.
        # - 5: real-time scheduling.
        self.schedule_type = schedule_type
        # The list of node tag names.
        self.tags = tags
        # The node status. Valid values:
        # 
        # - DRAFT: draft.
        # - SUBMITTING: being submitted.
        # - SUBMITTED: submitted.
        # - PUBLISHED: published.
        self.task_status = task_status
        # The node type. Valid values:
        # 
        # - 0: offline integration.
        # - 1: real-time integration.
        # - 13: data aggregation.
        # - 14: offline unstructured workflow.
        # - 15: real-time unstructured workflow.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.develop_owners is not None:
            result['DevelopOwners'] = self.develop_owners

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.ops_owners is not None:
            result['OpsOwners'] = self.ops_owners

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevelopOwners') is not None:
            self.develop_owners = m.get('DevelopOwners')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OpsOwners') is not None:
            self.ops_owners = m.get('OpsOwners')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

