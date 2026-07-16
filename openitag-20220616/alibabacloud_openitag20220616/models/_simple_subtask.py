# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class SimpleSubtask(DaraModel):
    def __init__(
        self,
        items: List[main_models.SimpleSubtaskItems] = None,
        status: str = None,
        subtask_id: int = None,
    ):
        # List of items for subtasks.
        self.items = items
        # Status.
        self.status = status
        # Subtask ID.
        self.subtask_id = subtask_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.SimpleSubtaskItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')

        return self

class SimpleSubtaskItems(DaraModel):
    def __init__(
        self,
        abandon_flag: bool = None,
        abandon_remark: str = None,
        data_id: str = None,
        feedback_flag: bool = None,
        feedback_remark: str = None,
        fixed_flag: bool = None,
        item_id: int = None,
        mine: int = None,
        reject_flag: bool = None,
        state: str = None,
        weight: int = None,
    ):
        # Abandon flag.
        self.abandon_flag = abandon_flag
        # Abandonment remark.
        self.abandon_remark = abandon_remark
        # Date ID.
        self.data_id = data_id
        # Feedback flag.
        self.feedback_flag = feedback_flag
        # Validation feedback.
        self.feedback_remark = feedback_remark
        # Failed mark.
        self.fixed_flag = fixed_flag
        # Data item ID.
        self.item_id = item_id
        # Assigned to me:
        # - 0: Not assigned to me.
        # - 1: Assigned to me.
        self.mine = mine
        # Skip flag.
        self.reject_flag = reject_flag
        # Status:
        # 
        # - INIT: Initial status.
        # - TOPUBLISH: Pending publish.
        # - CREATED: Created.
        # - HANDLING: In progress.
        # - VOTING: Voting in progress.
        # - FINISHED: Completed.
        # - FAIL: Failed.
        # - EXPIRE: Timeout.
        # - DISCARDED: Passively abandoned.
        # - DISABLE: Actively abandoned.
        # - LOCKED: Edit Lock.
        # - OFFLINE: Unpublished.
        # - MERGING: Merging results.
        self.state = state
        # Weight.
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

        if self.item_id is not None:
            result['ItemId'] = self.item_id

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

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Mine') is not None:
            self.mine = m.get('Mine')

        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

