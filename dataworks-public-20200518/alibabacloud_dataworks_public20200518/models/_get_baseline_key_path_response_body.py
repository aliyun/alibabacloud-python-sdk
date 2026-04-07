# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetBaselineKeyPathResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetBaselineKeyPathResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the key path.
        self.data = data
        # Error code
        self.error_code = error_code
        # Error message
        self.error_message = error_message
        # The timestamp when the event was found.
        self.http_status_code = http_status_code
        # The unique ID of the call. After an error occurs, you can troubleshoot the problem based on the ID.
        self.request_id = request_id
        # Whether the call is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetBaselineKeyPathResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class GetBaselineKeyPathResponseBodyData(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        in_group_id: int = None,
        instance_id: int = None,
        node_id: int = None,
        node_name: str = None,
        owner: str = None,
        prg_type: int = None,
        project_id: int = None,
        runs: List[main_models.GetBaselineKeyPathResponseBodyDataRuns] = None,
        topics: List[main_models.GetBaselineKeyPathResponseBodyDataTopics] = None,
    ):
        # The data timestamp of the instance.
        self.bizdate = bizdate
        # The ID of the scheduling cycle of the instance. Valid values: 1 to 288.
        self.in_group_id = in_group_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account used by the node owner.
        self.owner = owner
        # The type of the node. Valid values: 23, 10, 6, and 99. The value 23 indicates that the node is a Data Integration node. The value 10 indicates that the node is a MaxCompute SQL node. The value 6 indicates that the node is a Shell node. The value 99 indicates that the node is a zero load node.
        self.prg_type = prg_type
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The running records of the instance.
        self.runs = runs
        # The information about the events that are associated with the instance.
        self.topics = topics

    def validate(self):
        if self.runs:
            for v1 in self.runs:
                 if v1:
                    v1.validate()
        if self.topics:
            for v1 in self.topics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.in_group_id is not None:
            result['InGroupId'] = self.in_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.prg_type is not None:
            result['PrgType'] = self.prg_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Runs'] = []
        if self.runs is not None:
            for k1 in self.runs:
                result['Runs'].append(k1.to_map() if k1 else None)

        result['Topics'] = []
        if self.topics is not None:
            for k1 in self.topics:
                result['Topics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('InGroupId') is not None:
            self.in_group_id = m.get('InGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PrgType') is not None:
            self.prg_type = m.get('PrgType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.runs = []
        if m.get('Runs') is not None:
            for k1 in m.get('Runs'):
                temp_model = main_models.GetBaselineKeyPathResponseBodyDataRuns()
                self.runs.append(temp_model.from_map(k1))

        self.topics = []
        if m.get('Topics') is not None:
            for k1 in m.get('Topics'):
                temp_model = main_models.GetBaselineKeyPathResponseBodyDataTopics()
                self.topics.append(temp_model.from_map(k1))

        return self

class GetBaselineKeyPathResponseBodyDataTopics(DaraModel):
    def __init__(
        self,
        add_time: int = None,
        instance_id: int = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # The timestamp when the event was found.
        self.add_time = add_time
        # The instance ID.
        self.instance_id = instance_id
        # The event ID.
        self.topic_id = topic_id
        # The name of the event.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_time is not None:
            result['AddTime'] = self.add_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class GetBaselineKeyPathResponseBodyDataRuns(DaraModel):
    def __init__(
        self,
        abs_time: int = None,
        begin_cast: int = None,
        begin_running_time: int = None,
        begin_wait_res_time: int = None,
        begin_wait_time_time: int = None,
        end_cast: int = None,
        finish_time: int = None,
        status: str = None,
    ):
        # The timestamp obtained by adding the predicted time when the instance started to run to the historical average running duration of the instance.
        self.abs_time = abs_time
        # The timestamp of the predicted time when the instance started to run.
        self.begin_cast = begin_cast
        # The timestamp of the actual time when the instance started to run.
        self.begin_running_time = begin_running_time
        # The timestamp when the instance started to wait for resources.
        self.begin_wait_res_time = begin_wait_res_time
        # The timestamp when the instance started to wait for the scheduling time.
        self.begin_wait_time_time = begin_wait_time_time
        # The timestamp of the predicted time when the instance finished running.
        self.end_cast = end_cast
        # The timestamp of the actual time when the instance finished running.
        self.finish_time = finish_time
        # The status of the instance. Valid values: NOT_RUN, WAIT_TIME, WAIT_RESOURCE, RUNNING, CHECKING, CHECKING_CONDITION, FAILURE, and SUCCESS. The value NOT_RUN indicates that the instance is not run. The value WAIT_TIME indicates that the instance is waiting to be run. The value WAIT_RESOURCE indicates that the instance is waiting for resources. The value RUNNING indicates that the instance is running. The value CHECKING indicates that data quality is being checked for the instance. The value CHECKING_CONDITION indicates that branch conditions are being checked for the instance. The value FAILURE indicates that the instance fails to run. The value SUCCESS indicates that the instance is run.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abs_time is not None:
            result['AbsTime'] = self.abs_time

        if self.begin_cast is not None:
            result['BeginCast'] = self.begin_cast

        if self.begin_running_time is not None:
            result['BeginRunningTime'] = self.begin_running_time

        if self.begin_wait_res_time is not None:
            result['BeginWaitResTime'] = self.begin_wait_res_time

        if self.begin_wait_time_time is not None:
            result['BeginWaitTimeTime'] = self.begin_wait_time_time

        if self.end_cast is not None:
            result['EndCast'] = self.end_cast

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbsTime') is not None:
            self.abs_time = m.get('AbsTime')

        if m.get('BeginCast') is not None:
            self.begin_cast = m.get('BeginCast')

        if m.get('BeginRunningTime') is not None:
            self.begin_running_time = m.get('BeginRunningTime')

        if m.get('BeginWaitResTime') is not None:
            self.begin_wait_res_time = m.get('BeginWaitResTime')

        if m.get('BeginWaitTimeTime') is not None:
            self.begin_wait_time_time = m.get('BeginWaitTimeTime')

        if m.get('EndCast') is not None:
            self.end_cast = m.get('EndCast')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

