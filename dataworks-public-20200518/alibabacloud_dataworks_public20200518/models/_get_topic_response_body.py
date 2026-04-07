# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetTopicResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetTopicResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the event.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
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
            temp_model = main_models.GetTopicResponseBodyData()
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

class GetTopicResponseBodyData(DaraModel):
    def __init__(
        self,
        add_time: int = None,
        alert_time: int = None,
        assigner: str = None,
        baseline_buffer: int = None,
        baseline_id: int = None,
        baseline_in_group_id: int = None,
        baseline_name: str = None,
        baseline_status: str = None,
        buffer: int = None,
        deal_time: int = None,
        deal_user: str = None,
        fix_time: int = None,
        happen_time: int = None,
        instance_id: int = None,
        next_alert_time: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        project_id: int = None,
        topic_id: int = None,
        topic_name: str = None,
        topic_status: str = None,
        topic_type: str = None,
    ):
        # The timestamp when the event was found.
        self.add_time = add_time
        # The timestamp when the first alert was reported.
        self.alert_time = alert_time
        # The ID of the Alibaba Cloud account used by the alert recipient.
        self.assigner = assigner
        # The margin of the worst baseline instance. Unit: seconds.
        self.baseline_buffer = baseline_buffer
        # The ID of the baseline to which the worst baseline instance belongs.
        self.baseline_id = baseline_id
        # The ID of the cycle of the worst baseline instance.
        self.baseline_in_group_id = baseline_in_group_id
        # The name of the baseline to which the worst baseline instance belongs.
        self.baseline_name = baseline_name
        # The status of the baseline. Valid values: ERROR, SAFE, DANGROUS, and OVER. The value ERROR indicates that no nodes are associated with the baseline, or all nodes associated with the baseline are suspended. The value SAFE indicates that nodes are run before the alert duration begins. The value DANGROUS indicates that nodes are still running after the alert duration ends but the committed completion time does not arrive. The value OVER indicates that nodes are still running after the committed completion time.
        self.baseline_status = baseline_status
        # The margin of the event. Unit: seconds.
        self.buffer = buffer
        # The timestamp when the event was last processed.
        self.deal_time = deal_time
        # The ID of the Alibaba Cloud account used by the user who last processed the event.
        self.deal_user = deal_user
        # The timestamp when the event was processed.
        self.fix_time = fix_time
        # The timestamp when the event occurred. A time difference may exist between the time when the event occurred and the time when the event was found.
        self.happen_time = happen_time
        # The ID of the instance that triggered the event.
        self.instance_id = instance_id
        # The timestamp when the system reports the next alert.
        self.next_alert_time = next_alert_time
        # The ID of the node that triggered the event.
        self.node_id = node_id
        # The name of the node that triggered the event.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account used by the event owner.
        self.owner = owner
        # The ID of the workspace to which the node that triggered the event belongs.
        self.project_id = project_id
        # The event ID.
        self.topic_id = topic_id
        # The name of the event.
        self.topic_name = topic_name
        # The status of the event. Valid values: IGNORE, NEW, FIXING, and RECOVER.
        self.topic_status = topic_status
        # The type of the event. Valid values: SLOW and ERROR. The value SLOW indicates that the duration of the task is significantly longer than the average duration of the task in previous cycles. The value ERROR indicates that the task fails to run.
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

        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.assigner is not None:
            result['Assigner'] = self.assigner

        if self.baseline_buffer is not None:
            result['BaselineBuffer'] = self.baseline_buffer

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_in_group_id is not None:
            result['BaselineInGroupId'] = self.baseline_in_group_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_status is not None:
            result['BaselineStatus'] = self.baseline_status

        if self.buffer is not None:
            result['Buffer'] = self.buffer

        if self.deal_time is not None:
            result['DealTime'] = self.deal_time

        if self.deal_user is not None:
            result['DealUser'] = self.deal_user

        if self.fix_time is not None:
            result['FixTime'] = self.fix_time

        if self.happen_time is not None:
            result['HappenTime'] = self.happen_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_alert_time is not None:
            result['NextAlertTime'] = self.next_alert_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

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

        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('Assigner') is not None:
            self.assigner = m.get('Assigner')

        if m.get('BaselineBuffer') is not None:
            self.baseline_buffer = m.get('BaselineBuffer')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineInGroupId') is not None:
            self.baseline_in_group_id = m.get('BaselineInGroupId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineStatus') is not None:
            self.baseline_status = m.get('BaselineStatus')

        if m.get('Buffer') is not None:
            self.buffer = m.get('Buffer')

        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')

        if m.get('DealUser') is not None:
            self.deal_user = m.get('DealUser')

        if m.get('FixTime') is not None:
            self.fix_time = m.get('FixTime')

        if m.get('HappenTime') is not None:
            self.happen_time = m.get('HappenTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextAlertTime') is not None:
            self.next_alert_time = m.get('NextAlertTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

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

