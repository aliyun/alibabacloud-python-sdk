# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualityWatchTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        watch_task_info: main_models.GetQualityWatchTaskResponseBodyWatchTaskInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.watch_task_info = watch_task_info

    def validate(self):
        if self.watch_task_info:
            self.watch_task_info.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.watch_task_info is not None:
            result['WatchTaskInfo'] = self.watch_task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('WatchTaskInfo') is not None:
            temp_model = main_models.GetQualityWatchTaskResponseBodyWatchTaskInfo()
            self.watch_task_info = temp_model.from_map(m.get('WatchTaskInfo'))

        return self

class GetQualityWatchTaskResponseBodyWatchTaskInfo(DaraModel):
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
        quality_owner: str = None,
        quality_owner_name: str = None,
        rule_count_info: main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfo = None,
        rule_id_list: List[int] = None,
        start_time: str = None,
        status: str = None,
        watch_id: int = None,
    ):
        self.biz_date = biz_date
        self.biz_date_format = biz_date_format
        self.create_time = create_time
        self.creator = creator
        self.end_time = end_time
        self.id = id
        self.modifier = modifier
        self.modify_time = modify_time
        self.quality_owner = quality_owner
        self.quality_owner_name = quality_owner_name
        self.rule_count_info = rule_count_info
        self.rule_id_list = rule_id_list
        self.start_time = start_time
        self.status = status
        self.watch_id = watch_id

    def validate(self):
        if self.rule_count_info:
            self.rule_count_info.validate()

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

        if self.quality_owner is not None:
            result['QualityOwner'] = self.quality_owner

        if self.quality_owner_name is not None:
            result['QualityOwnerName'] = self.quality_owner_name

        if self.rule_count_info is not None:
            result['RuleCountInfo'] = self.rule_count_info.to_map()

        if self.rule_id_list is not None:
            result['RuleIdList'] = self.rule_id_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

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

        if m.get('QualityOwner') is not None:
            self.quality_owner = m.get('QualityOwner')

        if m.get('QualityOwnerName') is not None:
            self.quality_owner_name = m.get('QualityOwnerName')

        if m.get('RuleCountInfo') is not None:
            temp_model = main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfo()
            self.rule_count_info = temp_model.from_map(m.get('RuleCountInfo'))

        if m.get('RuleIdList') is not None:
            self.rule_id_list = m.get('RuleIdList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

class GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfo(DaraModel):
    def __init__(
        self,
        strong_rule_count: main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoStrongRuleCount = None,
        validate_rule_count: main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoValidateRuleCount = None,
        weak_rule_count: main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoWeakRuleCount = None,
    ):
        self.strong_rule_count = strong_rule_count
        self.validate_rule_count = validate_rule_count
        self.weak_rule_count = weak_rule_count

    def validate(self):
        if self.strong_rule_count:
            self.strong_rule_count.validate()
        if self.validate_rule_count:
            self.validate_rule_count.validate()
        if self.weak_rule_count:
            self.weak_rule_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strong_rule_count is not None:
            result['StrongRuleCount'] = self.strong_rule_count.to_map()

        if self.validate_rule_count is not None:
            result['ValidateRuleCount'] = self.validate_rule_count.to_map()

        if self.weak_rule_count is not None:
            result['WeakRuleCount'] = self.weak_rule_count.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrongRuleCount') is not None:
            temp_model = main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoStrongRuleCount()
            self.strong_rule_count = temp_model.from_map(m.get('StrongRuleCount'))

        if m.get('ValidateRuleCount') is not None:
            temp_model = main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoValidateRuleCount()
            self.validate_rule_count = temp_model.from_map(m.get('ValidateRuleCount'))

        if m.get('WeakRuleCount') is not None:
            temp_model = main_models.GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoWeakRuleCount()
            self.weak_rule_count = temp_model.from_map(m.get('WeakRuleCount'))

        return self

class GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoWeakRuleCount(DaraModel):
    def __init__(
        self,
        error_rule_count: int = None,
        finished_rule_count: int = None,
        success_rule_count: int = None,
        total_rule_count: int = None,
    ):
        self.error_rule_count = error_rule_count
        self.finished_rule_count = finished_rule_count
        self.success_rule_count = success_rule_count
        self.total_rule_count = total_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_rule_count is not None:
            result['ErrorRuleCount'] = self.error_rule_count

        if self.finished_rule_count is not None:
            result['FinishedRuleCount'] = self.finished_rule_count

        if self.success_rule_count is not None:
            result['SuccessRuleCount'] = self.success_rule_count

        if self.total_rule_count is not None:
            result['TotalRuleCount'] = self.total_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorRuleCount') is not None:
            self.error_rule_count = m.get('ErrorRuleCount')

        if m.get('FinishedRuleCount') is not None:
            self.finished_rule_count = m.get('FinishedRuleCount')

        if m.get('SuccessRuleCount') is not None:
            self.success_rule_count = m.get('SuccessRuleCount')

        if m.get('TotalRuleCount') is not None:
            self.total_rule_count = m.get('TotalRuleCount')

        return self

class GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoValidateRuleCount(DaraModel):
    def __init__(
        self,
        error_rule_count: int = None,
        finished_rule_count: int = None,
        success_rule_count: int = None,
        total_rule_count: int = None,
    ):
        self.error_rule_count = error_rule_count
        self.finished_rule_count = finished_rule_count
        self.success_rule_count = success_rule_count
        self.total_rule_count = total_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_rule_count is not None:
            result['ErrorRuleCount'] = self.error_rule_count

        if self.finished_rule_count is not None:
            result['FinishedRuleCount'] = self.finished_rule_count

        if self.success_rule_count is not None:
            result['SuccessRuleCount'] = self.success_rule_count

        if self.total_rule_count is not None:
            result['TotalRuleCount'] = self.total_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorRuleCount') is not None:
            self.error_rule_count = m.get('ErrorRuleCount')

        if m.get('FinishedRuleCount') is not None:
            self.finished_rule_count = m.get('FinishedRuleCount')

        if m.get('SuccessRuleCount') is not None:
            self.success_rule_count = m.get('SuccessRuleCount')

        if m.get('TotalRuleCount') is not None:
            self.total_rule_count = m.get('TotalRuleCount')

        return self

class GetQualityWatchTaskResponseBodyWatchTaskInfoRuleCountInfoStrongRuleCount(DaraModel):
    def __init__(
        self,
        error_rule_count: int = None,
        finished_rule_count: int = None,
        success_rule_count: int = None,
        total_rule_count: int = None,
    ):
        self.error_rule_count = error_rule_count
        self.finished_rule_count = finished_rule_count
        self.success_rule_count = success_rule_count
        self.total_rule_count = total_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_rule_count is not None:
            result['ErrorRuleCount'] = self.error_rule_count

        if self.finished_rule_count is not None:
            result['FinishedRuleCount'] = self.finished_rule_count

        if self.success_rule_count is not None:
            result['SuccessRuleCount'] = self.success_rule_count

        if self.total_rule_count is not None:
            result['TotalRuleCount'] = self.total_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorRuleCount') is not None:
            self.error_rule_count = m.get('ErrorRuleCount')

        if m.get('FinishedRuleCount') is not None:
            self.finished_rule_count = m.get('FinishedRuleCount')

        if m.get('SuccessRuleCount') is not None:
            self.success_rule_count = m.get('SuccessRuleCount')

        if m.get('TotalRuleCount') is not None:
            self.total_rule_count = m.get('TotalRuleCount')

        return self

