# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListTopicsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListTopicsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the events returned.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request. You can use the ID to troubleshoot issues.
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListTopicsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTopicsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        topics: List[main_models.ListTopicsResponseBodyDataTopics] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The events returned.
        self.topics = topics
        # The total number of the events returned.
        self.total_count = total_count

    def validate(self):
        if self.topics:
            for v1 in self.topics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Topics'] = []
        if self.topics is not None:
            for k1 in self.topics:
                result['Topics'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.topics = []
        if m.get('Topics') is not None:
            for k1 in m.get('Topics'):
                temp_model = main_models.ListTopicsResponseBodyDataTopics()
                self.topics.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTopicsResponseBodyDataTopics(DaraModel):
    def __init__(
        self,
        add_time: int = None,
        fix_time: int = None,
        happen_time: int = None,
        instance_id: int = None,
        node_id: int = None,
        node_name: str = None,
        node_owner: str = None,
        project_id: int = None,
        topic_id: int = None,
        topic_name: str = None,
        topic_status: str = None,
        topic_type: str = None,
    ):
        # The timestamp when the event was found.
        self.add_time = add_time
        # The timestamp when the event was processed.
        self.fix_time = fix_time
        # The timestamp when the event occurred. A time difference may exist between the time when the event occurred and the time when the event was found.
        self.happen_time = happen_time
        # The ID of the node instance that triggers the event.
        self.instance_id = instance_id
        # The ID of the node that triggers the event.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account that is used by the node owner.
        self.node_owner = node_owner
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The ID of the event.
        self.topic_id = topic_id
        # The name of the event.
        self.topic_name = topic_name
        # The status of the event. Valid values: IGNORE, NEW, FIXING, and RECOVER. The value IGNORE indicates that the event is ignored. The value NEW indicates that the event is a new event. The value FIXING indicates that the event is being processed. The value RECOVER indicates that the event is processed.
        self.topic_status = topic_status
        # The type of the event. Valid values: SLOW and ERROR. The value SLOW indicates that the running duration of the node in the current scheduling cycle is significantly longer than the average running duration of the node in previous scheduling cycles. The value ERROR indicates that the node fails to run.
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_time is not None:
            result['AddTime'] = self.add_time

        if self.fix_time is not None:
            result['FixTime'] = self.fix_time

        if self.happen_time is not None:
            result['HappenTime'] = self.happen_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_owner is not None:
            result['NodeOwner'] = self.node_owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.topic_status is not None:
            result['TopicStatus'] = self.topic_status

        if self.topic_type is not None:
            result['TopicType'] = self.topic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')

        if m.get('FixTime') is not None:
            self.fix_time = m.get('FixTime')

        if m.get('HappenTime') is not None:
            self.happen_time = m.get('HappenTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOwner') is not None:
            self.node_owner = m.get('NodeOwner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TopicStatus') is not None:
            self.topic_status = m.get('TopicStatus')

        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')

        return self

