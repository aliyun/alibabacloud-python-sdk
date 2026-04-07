# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetTopicInfluenceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetTopicInfluenceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
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
            temp_model = main_models.GetTopicInfluenceResponseBodyData()
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

class GetTopicInfluenceResponseBodyData(DaraModel):
    def __init__(
        self,
        influences: List[main_models.GetTopicInfluenceResponseBodyDataInfluences] = None,
        topic_id: int = None,
    ):
        # The affected baseline instances.
        self.influences = influences
        # The ID of the event.
        self.topic_id = topic_id

    def validate(self):
        if self.influences:
            for v1 in self.influences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Influences'] = []
        if self.influences is not None:
            for k1 in self.influences:
                result['Influences'].append(k1.to_map() if k1 else None)

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.influences = []
        if m.get('Influences') is not None:
            for k1 in m.get('Influences'):
                temp_model = main_models.GetTopicInfluenceResponseBodyDataInfluences()
                self.influences.append(temp_model.from_map(k1))

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

class GetTopicInfluenceResponseBodyDataInfluences(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        baseline_name: str = None,
        bizdate: int = None,
        buffer: int = None,
        in_group_id: int = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        status: str = None,
    ):
        # The ID of the baseline.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The data timestamp of the baseline instance.
        self.bizdate = bizdate
        # The margin of the baseline instance. Unit: seconds.
        self.buffer = buffer
        # The ID of the cycle of the baseline instance. For a baseline instance that is scheduled by day, the field value is 1. For a baseline instance that is scheduled by hour, the field value ranges from 1 to 24.
        self.in_group_id = in_group_id
        # The ID of the Alibaba Cloud account used by the baseline owner. Multiple IDs are separated by commas (,).
        self.owner = owner
        # The priority of the baseline. Valid values: 1, 2, 5, 7, and 8.
        self.priority = priority
        # The ID of the workspace to which the baseline belongs.
        self.project_id = project_id
        # The status of the baseline. Valid values: ERROR, SAFE, DANGROUS, and OVER. The value ERROR indicates that no nodes are associated with the baseline, or all nodes associated with the baseline are suspended. The value SAFE indicates that nodes are run before the alert duration begins. The value DANGROUS indicates that nodes are still running after the alert duration ends but the committed time does not arrive. The value OVER indicates that nodes are still running after the committed time.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.buffer is not None:
            result['Buffer'] = self.buffer

        if self.in_group_id is not None:
            result['InGroupId'] = self.in_group_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('Buffer') is not None:
            self.buffer = m.get('Buffer')

        if m.get('InGroupId') is not None:
            self.in_group_id = m.get('InGroupId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

