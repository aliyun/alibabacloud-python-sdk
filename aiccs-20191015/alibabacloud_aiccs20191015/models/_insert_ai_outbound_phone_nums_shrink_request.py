# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertAiOutboundPhoneNumsShrinkRequest(DaraModel):
    def __init__(
        self,
        batch_version: int = None,
        details_shrink: str = None,
        instance_id: str = None,
        task_id: int = None,
    ):
        self.batch_version = batch_version
        # This parameter is required.
        self.details_shrink = details_shrink
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_version is not None:
            result['BatchVersion'] = self.batch_version

        if self.details_shrink is not None:
            result['Details'] = self.details_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchVersion') is not None:
            self.batch_version = m.get('BatchVersion')

        if m.get('Details') is not None:
            self.details_shrink = m.get('Details')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

