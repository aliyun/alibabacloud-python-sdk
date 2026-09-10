# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataCheckTaskRequest(DaraModel):
    def __init__(
        self,
        check_template_id: str = None,
        check_type: int = None,
        dst_ds_id: str = None,
        dst_ds_name: str = None,
        dst_ds_type: str = None,
        src_ds_id: str = None,
        src_ds_name: str = None,
        src_ds_type: str = None,
        task_mode: int = None,
        task_name: str = None,
    ):
        # The validation template ID. If not specified, the built-in default template is used.
        self.check_template_id = check_template_id
        # The validation type. Valid values:
        # 
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        # 
        # This parameter is required.
        self.check_type = check_type
        # The ID of the destination data source.
        # 
        # This parameter is required.
        self.dst_ds_id = dst_ds_id
        # The name of the destination data source.
        self.dst_ds_name = dst_ds_name
        # The type of the destination data source.
        # 
        # This parameter is required.
        self.dst_ds_type = dst_ds_type
        # The ID of the source data source.
        # 
        # This parameter is required.
        self.src_ds_id = src_ds_id
        # The name of the source data source.
        self.src_ds_name = src_ds_name
        # The type of the source data source.
        # 
        # This parameter is required.
        self.src_ds_type = src_ds_type
        # The table detail creation mode. Valid values:
        # 
        # - 0: table-by-table fine-grained creation.
        # - 1: batch creation with the same schema.
        # 
        # This parameter is required.
        self.task_mode = task_mode
        # The task name. Only Chinese characters, English characters, and digits are supported.
        # 
        # This parameter is required.
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

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.dst_ds_id is not None:
            result['dstDsId'] = self.dst_ds_id

        if self.dst_ds_name is not None:
            result['dstDsName'] = self.dst_ds_name

        if self.dst_ds_type is not None:
            result['dstDsType'] = self.dst_ds_type

        if self.src_ds_id is not None:
            result['srcDsId'] = self.src_ds_id

        if self.src_ds_name is not None:
            result['srcDsName'] = self.src_ds_name

        if self.src_ds_type is not None:
            result['srcDsType'] = self.src_ds_type

        if self.task_mode is not None:
            result['taskMode'] = self.task_mode

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkTemplateId') is not None:
            self.check_template_id = m.get('checkTemplateId')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('dstDsId') is not None:
            self.dst_ds_id = m.get('dstDsId')

        if m.get('dstDsName') is not None:
            self.dst_ds_name = m.get('dstDsName')

        if m.get('dstDsType') is not None:
            self.dst_ds_type = m.get('dstDsType')

        if m.get('srcDsId') is not None:
            self.src_ds_id = m.get('srcDsId')

        if m.get('srcDsName') is not None:
            self.src_ds_name = m.get('srcDsName')

        if m.get('srcDsType') is not None:
            self.src_ds_type = m.get('srcDsType')

        if m.get('taskMode') is not None:
            self.task_mode = m.get('taskMode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

