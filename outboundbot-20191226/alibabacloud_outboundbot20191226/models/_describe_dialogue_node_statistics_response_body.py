# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeDialogueNodeStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        group_id: str = None,
        hang_up_dialogue_nodes: List[main_models.DescribeDialogueNodeStatisticsResponseBodyHangUpDialogueNodes] = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        no_answer_dialogue_nodes: List[main_models.DescribeDialogueNodeStatisticsResponseBodyNoAnswerDialogueNodes] = None,
        request_id: str = None,
        success: bool = None,
        total_completed: int = None,
    ):
        self.code = code
        self.group_id = group_id
        self.hang_up_dialogue_nodes = hang_up_dialogue_nodes
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.no_answer_dialogue_nodes = no_answer_dialogue_nodes
        self.request_id = request_id
        self.success = success
        self.total_completed = total_completed

    def validate(self):
        if self.hang_up_dialogue_nodes:
            for v1 in self.hang_up_dialogue_nodes:
                 if v1:
                    v1.validate()
        if self.no_answer_dialogue_nodes:
            for v1 in self.no_answer_dialogue_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['HangUpDialogueNodes'] = []
        if self.hang_up_dialogue_nodes is not None:
            for k1 in self.hang_up_dialogue_nodes:
                result['HangUpDialogueNodes'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        result['NoAnswerDialogueNodes'] = []
        if self.no_answer_dialogue_nodes is not None:
            for k1 in self.no_answer_dialogue_nodes:
                result['NoAnswerDialogueNodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_completed is not None:
            result['TotalCompleted'] = self.total_completed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.hang_up_dialogue_nodes = []
        if m.get('HangUpDialogueNodes') is not None:
            for k1 in m.get('HangUpDialogueNodes'):
                temp_model = main_models.DescribeDialogueNodeStatisticsResponseBodyHangUpDialogueNodes()
                self.hang_up_dialogue_nodes.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.no_answer_dialogue_nodes = []
        if m.get('NoAnswerDialogueNodes') is not None:
            for k1 in m.get('NoAnswerDialogueNodes'):
                temp_model = main_models.DescribeDialogueNodeStatisticsResponseBodyNoAnswerDialogueNodes()
                self.no_answer_dialogue_nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCompleted') is not None:
            self.total_completed = m.get('TotalCompleted')

        return self

class DescribeDialogueNodeStatisticsResponseBodyNoAnswerDialogueNodes(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        hang_up_num: int = None,
        hit_num: int = None,
        id: str = None,
        instance_id: str = None,
        no_answer_num: int = None,
        node_id: str = None,
        node_name: str = None,
    ):
        self.group_id = group_id
        self.hang_up_num = hang_up_num
        self.hit_num = hit_num
        # id
        self.id = id
        self.instance_id = instance_id
        self.no_answer_num = no_answer_num
        self.node_id = node_id
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hang_up_num is not None:
            result['HangUpNum'] = self.hang_up_num

        if self.hit_num is not None:
            result['HitNum'] = self.hit_num

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.no_answer_num is not None:
            result['NoAnswerNum'] = self.no_answer_num

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HangUpNum') is not None:
            self.hang_up_num = m.get('HangUpNum')

        if m.get('HitNum') is not None:
            self.hit_num = m.get('HitNum')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NoAnswerNum') is not None:
            self.no_answer_num = m.get('NoAnswerNum')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

class DescribeDialogueNodeStatisticsResponseBodyHangUpDialogueNodes(DaraModel):
    def __init__(
        self,
        hang_up_num: int = None,
        node_id: str = None,
        node_name: str = None,
        rate_display: str = None,
    ):
        self.hang_up_num = hang_up_num
        self.node_id = node_id
        self.node_name = node_name
        self.rate_display = rate_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hang_up_num is not None:
            result['HangUpNum'] = self.hang_up_num

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.rate_display is not None:
            result['RateDisplay'] = self.rate_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HangUpNum') is not None:
            self.hang_up_num = m.get('HangUpNum')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('RateDisplay') is not None:
            self.rate_display = m.get('RateDisplay')

        return self

