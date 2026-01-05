# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateLineageRelationshipRequest(DaraModel):
    def __init__(
        self,
        dst_entity: main_models.LineageEntity = None,
        src_entity: main_models.LineageEntity = None,
        task: main_models.LineageTask = None,
    ):
        # The destination entity.
        self.dst_entity = dst_entity
        # The source entity.
        self.src_entity = src_entity
        # The task information.
        self.task = task

    def validate(self):
        if self.dst_entity:
            self.dst_entity.validate()
        if self.src_entity:
            self.src_entity.validate()
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_entity is not None:
            result['DstEntity'] = self.dst_entity.to_map()

        if self.src_entity is not None:
            result['SrcEntity'] = self.src_entity.to_map()

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstEntity') is not None:
            temp_model = main_models.LineageEntity()
            self.dst_entity = temp_model.from_map(m.get('DstEntity'))

        if m.get('SrcEntity') is not None:
            temp_model = main_models.LineageEntity()
            self.src_entity = temp_model.from_map(m.get('SrcEntity'))

        if m.get('Task') is not None:
            temp_model = main_models.LineageTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

