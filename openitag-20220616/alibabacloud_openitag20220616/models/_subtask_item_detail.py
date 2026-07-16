# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class SubtaskItemDetail(DaraModel):
    def __init__(
        self,
        annotations: List[main_models.SubtaskItemDetailAnnotations] = None,
        data_source: Dict[str, Any] = None,
        item_id: int = None,
    ):
        # List of annotation results
        self.annotations = annotations
        # data source
        self.data_source = data_source
        # Item ID
        self.item_id = item_id

    def validate(self):
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['Annotations'].append(k1.to_map() if k1 else None)

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.SubtaskItemDetailAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        return self

class SubtaskItemDetailAnnotations(DaraModel):
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
        # Abandonment remark
        self.abandon_remark = abandon_remark
        # Date ID
        self.data_id = data_id
        # Feedback mark
        self.feedback_flag = feedback_flag
        # Validation feedback
        self.feedback_remark = feedback_remark
        # Failure mark
        self.fixed_flag = fixed_flag
        # Is assigned to me
        self.mine = mine
        # Skip mark
        self.reject_flag = reject_flag
        # Status
        self.state = state
        # weight
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

