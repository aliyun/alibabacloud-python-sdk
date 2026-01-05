# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
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
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
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
        allow_cancel: int = None,
        allow_change: int = None,
        change_level: str = None,
        change_level_en: str = None,
        change_level_zh: str = None,
        created_time: str = None,
        current_avz: str = None,
        dbcluster_id: str = None,
        dbnode_ids: List[str] = None,
        dbtype: str = None,
        dbversion: str = None,
        deadline: str = None,
        impact: str = None,
        impact_en: str = None,
        impact_zh: str = None,
        ins_comment: str = None,
        modified_time: str = None,
        prepare_interval: str = None,
        region: str = None,
        result_info: str = None,
        start_time: str = None,
        status: int = None,
        switch_time: str = None,
        task_id: int = None,
        task_params: str = None,
        task_type: str = None,
        task_type_en: str = None,
        task_type_zh: str = None,
    ):
        self.allow_cancel = allow_cancel
        self.allow_change = allow_change
        self.change_level = change_level
        self.change_level_en = change_level_en
        self.change_level_zh = change_level_zh
        self.created_time = created_time
        self.current_avz = current_avz
        self.dbcluster_id = dbcluster_id
        self.dbnode_ids = dbnode_ids
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.deadline = deadline
        self.impact = impact
        self.impact_en = impact_en
        self.impact_zh = impact_zh
        self.ins_comment = ins_comment
        self.modified_time = modified_time
        self.prepare_interval = prepare_interval
        self.region = region
        self.result_info = result_info
        self.start_time = start_time
        self.status = status
        self.switch_time = switch_time
        self.task_id = task_id
        self.task_params = task_params
        self.task_type = task_type
        self.task_type_en = task_type_en
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.impact is not None:
            result['Impact'] = self.impact

        if self.impact_en is not None:
            result['ImpactEn'] = self.impact_en

        if self.impact_zh is not None:
            result['ImpactZh'] = self.impact_zh

        if self.ins_comment is not None:
            result['InsComment'] = self.ins_comment

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

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

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

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('Impact') is not None:
            self.impact = m.get('Impact')

        if m.get('ImpactEn') is not None:
            self.impact_en = m.get('ImpactEn')

        if m.get('ImpactZh') is not None:
            self.impact_zh = m.get('ImpactZh')

        if m.get('InsComment') is not None:
            self.ins_comment = m.get('InsComment')

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

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeEn') is not None:
            self.task_type_en = m.get('TaskTypeEn')

        if m.get('TaskTypeZh') is not None:
            self.task_type_zh = m.get('TaskTypeZh')

        return self

