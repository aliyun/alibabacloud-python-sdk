# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataCheckTaskRequest(DaraModel):
    def __init__(
        self,
        check_template_id: str = None,
        dst_ds_id: str = None,
        dst_ds_name: str = None,
        dst_ds_type: str = None,
        dst_engine_id: str = None,
        dst_engine_name: str = None,
        dst_engine_type: str = None,
        id: int = None,
        src_ds_id: str = None,
        src_ds_name: str = None,
        src_ds_type: str = None,
        src_engine_id: str = None,
        src_engine_name: str = None,
        src_engine_type: str = None,
        task_description: str = None,
        task_name: str = None,
    ):
        # The ID of the validation template. If this field is not specified, the original value is retained.
        self.check_template_id = check_template_id
        # The ID of the destination data source.
        self.dst_ds_id = dst_ds_id
        # The name of the destination data source.
        self.dst_ds_name = dst_ds_name
        # The type of the destination data source.
        self.dst_ds_type = dst_ds_type
        # The ID of the destination validation engine.
        self.dst_engine_id = dst_engine_id
        # The name of the destination validation engine.
        self.dst_engine_name = dst_engine_name
        # The type of the destination validation engine.
        self.dst_engine_type = dst_engine_type
        # The ID of the task to modify. This field is required.
        # 
        # This parameter is required.
        self.id = id
        # The ID of the source data source.
        self.src_ds_id = src_ds_id
        # The name of the source data source.
        self.src_ds_name = src_ds_name
        # The type of the source data source.
        self.src_ds_type = src_ds_type
        # The ID of the source validation engine.
        self.src_engine_id = src_engine_id
        # The name of the source validation engine.
        self.src_engine_name = src_engine_name
        # The type of the source validation engine.
        self.src_engine_type = src_engine_type
        # The description of the task.
        self.task_description = task_description
        # The name of the task. Only Chinese characters, English letters, and digits are supported.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_template_id is not None:
            result['checkTemplateId'] = self.check_template_id

        if self.dst_ds_id is not None:
            result['dstDsId'] = self.dst_ds_id

        if self.dst_ds_name is not None:
            result['dstDsName'] = self.dst_ds_name

        if self.dst_ds_type is not None:
            result['dstDsType'] = self.dst_ds_type

        if self.dst_engine_id is not None:
            result['dstEngineId'] = self.dst_engine_id

        if self.dst_engine_name is not None:
            result['dstEngineName'] = self.dst_engine_name

        if self.dst_engine_type is not None:
            result['dstEngineType'] = self.dst_engine_type

        if self.id is not None:
            result['id'] = self.id

        if self.src_ds_id is not None:
            result['srcDsId'] = self.src_ds_id

        if self.src_ds_name is not None:
            result['srcDsName'] = self.src_ds_name

        if self.src_ds_type is not None:
            result['srcDsType'] = self.src_ds_type

        if self.src_engine_id is not None:
            result['srcEngineId'] = self.src_engine_id

        if self.src_engine_name is not None:
            result['srcEngineName'] = self.src_engine_name

        if self.src_engine_type is not None:
            result['srcEngineType'] = self.src_engine_type

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkTemplateId') is not None:
            self.check_template_id = m.get('checkTemplateId')

        if m.get('dstDsId') is not None:
            self.dst_ds_id = m.get('dstDsId')

        if m.get('dstDsName') is not None:
            self.dst_ds_name = m.get('dstDsName')

        if m.get('dstDsType') is not None:
            self.dst_ds_type = m.get('dstDsType')

        if m.get('dstEngineId') is not None:
            self.dst_engine_id = m.get('dstEngineId')

        if m.get('dstEngineName') is not None:
            self.dst_engine_name = m.get('dstEngineName')

        if m.get('dstEngineType') is not None:
            self.dst_engine_type = m.get('dstEngineType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('srcDsId') is not None:
            self.src_ds_id = m.get('srcDsId')

        if m.get('srcDsName') is not None:
            self.src_ds_name = m.get('srcDsName')

        if m.get('srcDsType') is not None:
            self.src_ds_type = m.get('srcDsType')

        if m.get('srcEngineId') is not None:
            self.src_engine_id = m.get('srcEngineId')

        if m.get('srcEngineName') is not None:
            self.src_engine_name = m.get('srcEngineName')

        if m.get('srcEngineType') is not None:
            self.src_engine_type = m.get('srcEngineType')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

