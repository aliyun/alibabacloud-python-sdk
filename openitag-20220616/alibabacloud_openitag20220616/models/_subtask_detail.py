# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class SubtaskDetail(DaraModel):
    def __init__(
        self,
        can_discard: bool = None,
        can_reassign: bool = None,
        can_release: bool = None,
        current_work_node: str = None,
        ext_configs: str = None,
        items: List[main_models.SubtaskDetailItems] = None,
        status: str = None,
        subtask_id: str = None,
        task_id: str = None,
        weight: int = None,
        work_node_state: str = None,
        workforce: List[main_models.Workforce] = None,
    ):
        # is discardable
        self.can_discard = can_discard
        # Can assign
        self.can_reassign = can_reassign
        # is releasable
        self.can_release = can_release
        # current File Type
        self.current_work_node = current_work_node
        # extra parameters
        self.ext_configs = ext_configs
        # List of items in the sub-job
        self.items = items
        # status
        self.status = status
        # Subtask ID
        self.subtask_id = subtask_id
        # parent job ID of the sub-job
        self.task_id = task_id
        # Job weight
        self.weight = weight
        # Current edge zone status
        self.work_node_state = work_node_state
        # list of annotators assigned to the sub-job
        self.workforce = workforce

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.workforce:
            for v1 in self.workforce:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_discard is not None:
            result['CanDiscard'] = self.can_discard

        if self.can_reassign is not None:
            result['CanReassign'] = self.can_reassign

        if self.can_release is not None:
            result['CanRelease'] = self.can_release

        if self.current_work_node is not None:
            result['CurrentWorkNode'] = self.current_work_node

        if self.ext_configs is not None:
            result['ExtConfigs'] = self.ext_configs

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.work_node_state is not None:
            result['WorkNodeState'] = self.work_node_state

        result['Workforce'] = []
        if self.workforce is not None:
            for k1 in self.workforce:
                result['Workforce'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDiscard') is not None:
            self.can_discard = m.get('CanDiscard')

        if m.get('CanReassign') is not None:
            self.can_reassign = m.get('CanReassign')

        if m.get('CanRelease') is not None:
            self.can_release = m.get('CanRelease')

        if m.get('CurrentWorkNode') is not None:
            self.current_work_node = m.get('CurrentWorkNode')

        if m.get('ExtConfigs') is not None:
            self.ext_configs = m.get('ExtConfigs')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.SubtaskDetailItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('WorkNodeState') is not None:
            self.work_node_state = m.get('WorkNodeState')

        self.workforce = []
        if m.get('Workforce') is not None:
            for k1 in m.get('Workforce'):
                temp_model = main_models.Workforce()
                self.workforce.append(temp_model.from_map(k1))

        return self

class SubtaskDetailItems(DaraModel):
    def __init__(
        self,
        abandon_flag: bool = None,
        abandon_remark: str = None,
        data_id: str = None,
        feedback_flag: bool = None,
        feedback_remark: str = None,
        fixed_flag: bool = None,
        mine: int = None,
        reject_flag: bool = None,
        state: str = None,
        weight: int = None,
    ):
        # Abandon mark
        self.abandon_flag = abandon_flag
        # discard reason
        self.abandon_remark = abandon_remark
        # Date ID
        self.data_id = data_id
        # feedback mark
        self.feedback_flag = feedback_flag
        # Validate feedback
        self.feedback_remark = feedback_remark
        # Failed mark
        self.fixed_flag = fixed_flag
        # Is assigned to me
        self.mine = mine
        # skip mark
        self.reject_flag = reject_flag
        # status
        self.state = state
        # Weight
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag

        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag

        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark

        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag

        if self.mine is not None:
            result['Mine'] = self.mine

        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag

        if self.state is not None:
            result['State'] = self.state

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')

        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')

        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')

        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')

        if m.get('Mine') is not None:
            self.mine = m.get('Mine')

        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

