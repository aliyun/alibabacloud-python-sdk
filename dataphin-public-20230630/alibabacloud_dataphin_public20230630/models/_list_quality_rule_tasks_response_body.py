# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityRuleTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListQualityRuleTasksResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListQualityRuleTasksResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListQualityRuleTasksResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        quality_rule_task_list: List[main_models.ListQualityRuleTasksResponseBodyPageResultQualityRuleTaskList] = None,
        total_count: int = None,
    ):
        self.quality_rule_task_list = quality_rule_task_list
        self.total_count = total_count

    def validate(self):
        if self.quality_rule_task_list:
            for v1 in self.quality_rule_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QualityRuleTaskList'] = []
        if self.quality_rule_task_list is not None:
            for k1 in self.quality_rule_task_list:
                result['QualityRuleTaskList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_rule_task_list = []
        if m.get('QualityRuleTaskList') is not None:
            for k1 in m.get('QualityRuleTaskList'):
                temp_model = main_models.ListQualityRuleTasksResponseBodyPageResultQualityRuleTaskList()
                self.quality_rule_task_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQualityRuleTasksResponseBodyPageResultQualityRuleTaskList(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        biz_date_format: str = None,
        create_time: str = None,
        creator: str = None,
        end_time: str = None,
        id: int = None,
        modifier: str = None,
        modify_time: str = None,
        rule_id: int = None,
        start_time: str = None,
        status: str = None,
        template_id: int = None,
        validate_object_name: str = None,
        validate_object_type: str = None,
        validate_partition: str = None,
        validate_success: bool = None,
        watch_id: int = None,
        watch_task_id: int = None,
    ):
        self.biz_date = biz_date
        self.biz_date_format = biz_date_format
        self.create_time = create_time
        self.creator = creator
        self.end_time = end_time
        self.id = id
        self.modifier = modifier
        self.modify_time = modify_time
        self.rule_id = rule_id
        self.start_time = start_time
        self.status = status
        self.template_id = template_id
        self.validate_object_name = validate_object_name
        self.validate_object_type = validate_object_type
        self.validate_partition = validate_partition
        self.validate_success = validate_success
        self.watch_id = watch_id
        self.watch_task_id = watch_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.biz_date_format is not None:
            result['BizDateFormat'] = self.biz_date_format

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.validate_object_name is not None:
            result['ValidateObjectName'] = self.validate_object_name

        if self.validate_object_type is not None:
            result['ValidateObjectType'] = self.validate_object_type

        if self.validate_partition is not None:
            result['ValidatePartition'] = self.validate_partition

        if self.validate_success is not None:
            result['ValidateSuccess'] = self.validate_success

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        if self.watch_task_id is not None:
            result['WatchTaskId'] = self.watch_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('BizDateFormat') is not None:
            self.biz_date_format = m.get('BizDateFormat')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('ValidateObjectName') is not None:
            self.validate_object_name = m.get('ValidateObjectName')

        if m.get('ValidateObjectType') is not None:
            self.validate_object_type = m.get('ValidateObjectType')

        if m.get('ValidatePartition') is not None:
            self.validate_partition = m.get('ValidatePartition')

        if m.get('ValidateSuccess') is not None:
            self.validate_success = m.get('ValidateSuccess')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        if m.get('WatchTaskId') is not None:
            self.watch_task_id = m.get('WatchTaskId')

        return self

