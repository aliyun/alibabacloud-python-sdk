# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveOperationTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeActiveOperationTasksResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The O\\&M tasks.
        self.items = items
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_record_count = total_record_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeActiveOperationTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeActiveOperationTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        allow_cancel: str = None,
        allow_change: str = None,
        change_level: str = None,
        change_level_en: str = None,
        change_level_zh: str = None,
        created_time: str = None,
        current_avz: str = None,
        db_type: str = None,
        db_version: str = None,
        deadline: str = None,
        id: int = None,
        impact_en: str = None,
        impact_zh: str = None,
        ins_comment: str = None,
        ins_name: str = None,
        modified_time: str = None,
        prepare_interval: str = None,
        region: str = None,
        result_info: str = None,
        start_time: str = None,
        status: int = None,
        sub_ins_names: List[str] = None,
        switch_time: str = None,
        task_params: str = None,
        task_type: str = None,
        task_type_en: str = None,
        task_type_zh: str = None,
    ):
        # N/A
        self.allow_cancel = allow_cancel
        # Indicates whether the modification operation is allowed.
        # 
        # *   **0**: The modification operation is not allowed.
        # *   **1**: The modification operation is allowed.
        self.allow_change = allow_change
        # The change level of the O\\&M task.
        self.change_level = change_level
        # N/A
        self.change_level_en = change_level_en
        # The task type in English.
        self.change_level_zh = change_level_zh
        # The time when the task was created.
        self.created_time = created_time
        # N/A
        self.current_avz = current_avz
        # The type of the database engine.
        self.db_type = db_type
        # The version of the database engine.
        self.db_version = db_version
        # The end time of the O\\&M task.
        self.deadline = deadline
        # The task ID.
        self.id = id
        # N/A
        self.impact_en = impact_en
        # N/A
        self.impact_zh = impact_zh
        # The description of the instance.
        self.ins_comment = ins_comment
        # The ID of the node.
        self.ins_name = ins_name
        # The time when the task is modified. The time follows the ISO 8601 standard in the *yyyy-mm-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The required preparation period between the task start time and the switchover time. The time is displayed in the *HH:mm:ss* format.
        self.prepare_interval = prepare_interval
        # The region of the instance.
        self.region = region
        # The result information. The value of this parameter can be ignored.
        self.result_info = result_info
        # The start time of the task. The time follows the ISO 8601 standard in the *yyyy-mm-dd* T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # N/A
        self.status = status
        # The subinstances.
        self.sub_ins_names = sub_ins_names
        # The switchover point in time in which disconnection may occur. The time follows the ISO 8601 standard in the *yyyy-mm-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.switch_time = switch_time
        self.task_params = task_params
        # The task type.
        self.task_type = task_type
        # N/A
        self.task_type_en = task_type_en
        # The task type in Chinese.
        self.task_type_zh = task_type_zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel

        if self.allow_change is not None:
            result['AllowChange'] = self.allow_change

        if self.change_level is not None:
            result['ChangeLevel'] = self.change_level

        if self.change_level_en is not None:
            result['ChangeLevelEn'] = self.change_level_en

        if self.change_level_zh is not None:
            result['ChangeLevelZh'] = self.change_level_zh

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.current_avz is not None:
            result['CurrentAVZ'] = self.current_avz

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.id is not None:
            result['Id'] = self.id

        if self.impact_en is not None:
            result['ImpactEn'] = self.impact_en

        if self.impact_zh is not None:
            result['ImpactZh'] = self.impact_zh

        if self.ins_comment is not None:
            result['InsComment'] = self.ins_comment

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval

        if self.region is not None:
            result['Region'] = self.region

        if self.result_info is not None:
            result['ResultInfo'] = self.result_info

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_ins_names is not None:
            result['SubInsNames'] = self.sub_ins_names

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.task_params is not None:
            result['TaskParams'] = self.task_params

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_en is not None:
            result['TaskTypeEn'] = self.task_type_en

        if self.task_type_zh is not None:
            result['TaskTypeZh'] = self.task_type_zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')

        if m.get('AllowChange') is not None:
            self.allow_change = m.get('AllowChange')

        if m.get('ChangeLevel') is not None:
            self.change_level = m.get('ChangeLevel')

        if m.get('ChangeLevelEn') is not None:
            self.change_level_en = m.get('ChangeLevelEn')

        if m.get('ChangeLevelZh') is not None:
            self.change_level_zh = m.get('ChangeLevelZh')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CurrentAVZ') is not None:
            self.current_avz = m.get('CurrentAVZ')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImpactEn') is not None:
            self.impact_en = m.get('ImpactEn')

        if m.get('ImpactZh') is not None:
            self.impact_zh = m.get('ImpactZh')

        if m.get('InsComment') is not None:
            self.ins_comment = m.get('InsComment')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubInsNames') is not None:
            self.sub_ins_names = m.get('SubInsNames')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeEn') is not None:
            self.task_type_en = m.get('TaskTypeEn')

        if m.get('TaskTypeZh') is not None:
            self.task_type_zh = m.get('TaskTypeZh')

        return self

