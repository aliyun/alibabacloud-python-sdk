# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertOutputGroupDetail(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        finish_time: str = None,
        message: str = None,
        name: str = None,
        outputs: List[main_models.MediaConvertOutputDetail] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.code = code
        self.create_time = create_time
        self.finish_time = finish_time
        self.message = message
        self.name = name
        self.outputs = outputs
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.MediaConvertOutputDetail()
                self.outputs.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

