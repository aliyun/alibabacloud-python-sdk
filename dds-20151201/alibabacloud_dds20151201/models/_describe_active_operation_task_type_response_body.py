# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveOperationTaskTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        type_list: List[main_models.DescribeActiveOperationTaskTypeResponseBodyTypeList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The O\\&M tasks.
        self.type_list = type_list

    def validate(self):
        if self.type_list:
            for v1 in self.type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TypeList'] = []
        if self.type_list is not None:
            for k1 in self.type_list:
                result['TypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.type_list = []
        if m.get('TypeList') is not None:
            for k1 in m.get('TypeList'):
                temp_model = main_models.DescribeActiveOperationTaskTypeResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k1))

        return self

class DescribeActiveOperationTaskTypeResponseBodyTypeList(DaraModel):
    def __init__(
        self,
        count: int = None,
        task_type: str = None,
        task_type_info_en: str = None,
        task_type_info_zh: str = None,
    ):
        # The number of pending tasks.
        self.count = count
        # The type of the task. Valid values:
        # 
        # *   **rds_apsaradb_transfer**: data migration
        # *   **rds_apsaradb_upgrade**: minor version update
        self.task_type = task_type
        # The task type in English.
        self.task_type_info_en = task_type_info_en
        # The task type in Chinese.
        self.task_type_info_zh = task_type_info_zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_info_en is not None:
            result['TaskTypeInfoEn'] = self.task_type_info_en

        if self.task_type_info_zh is not None:
            result['TaskTypeInfoZh'] = self.task_type_info_zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeInfoEn') is not None:
            self.task_type_info_en = m.get('TaskTypeInfoEn')

        if m.get('TaskTypeInfoZh') is not None:
            self.task_type_info_zh = m.get('TaskTypeInfoZh')

        return self

