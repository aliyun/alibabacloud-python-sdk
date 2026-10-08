# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListScheduleTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list_schedule_templates_response: main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponse = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.list_schedule_templates_response = list_schedule_templates_response
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.list_schedule_templates_response:
            self.list_schedule_templates_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.list_schedule_templates_response is not None:
            result['ListScheduleTemplatesResponse'] = self.list_schedule_templates_response.to_map()

        if self.message is not None:
            result['Message'] = self.message

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

        if m.get('ListScheduleTemplatesResponse') is not None:
            temp_model = main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponse()
            self.list_schedule_templates_response = temp_model.from_map(m.get('ListScheduleTemplatesResponse'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListScheduleTemplatesResponseBodyListScheduleTemplatesResponse(DaraModel):
    def __init__(
        self,
        count: int = None,
        result_data: List[main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultData] = None,
    ):
        self.count = count
        self.result_data = result_data

    def validate(self):
        if self.result_data:
            for v1 in self.result_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['ResultData'] = []
        if self.result_data is not None:
            for k1 in self.result_data:
                result['ResultData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.result_data = []
        if m.get('ResultData') is not None:
            for k1 in m.get('ResultData'):
                temp_model = main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultData()
                self.result_data.append(temp_model.from_map(k1))

        return self

class ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultData(DaraModel):
    def __init__(
        self,
        condition_schedule_param_list: List[main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataConditionScheduleParamList] = None,
        cron_expression: str = None,
        custom_cron_expression: bool = None,
        custom_interval_config: main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataCustomIntervalConfig = None,
        custom_interval_config_type: str = None,
        custom_interval_configs: List[main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataCustomIntervalConfigs] = None,
        gmt_create: int = None,
        gmt_modify: int = None,
        has_reference: bool = None,
        modifier_id: str = None,
        modifier_name: str = None,
        schedule_interval_type: str = None,
        schedule_template_desc: str = None,
        schedule_template_id: int = None,
        schedule_template_name: str = None,
        schedule_template_type: str = None,
        schedule_type: int = None,
        tenant_id: int = None,
        user_id: str = None,
        user_name: str = None,
        valid_end_date: str = None,
        valid_start_date: str = None,
    ):
        self.condition_schedule_param_list = condition_schedule_param_list
        self.cron_expression = cron_expression
        self.custom_cron_expression = custom_cron_expression
        self.custom_interval_config = custom_interval_config
        self.custom_interval_config_type = custom_interval_config_type
        self.custom_interval_configs = custom_interval_configs
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.has_reference = has_reference
        self.modifier_id = modifier_id
        self.modifier_name = modifier_name
        self.schedule_interval_type = schedule_interval_type
        self.schedule_template_desc = schedule_template_desc
        self.schedule_template_id = schedule_template_id
        self.schedule_template_name = schedule_template_name
        self.schedule_template_type = schedule_template_type
        self.schedule_type = schedule_type
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.user_name = user_name
        self.valid_end_date = valid_end_date
        self.valid_start_date = valid_start_date

    def validate(self):
        if self.condition_schedule_param_list:
            for v1 in self.condition_schedule_param_list:
                 if v1:
                    v1.validate()
        if self.custom_interval_config:
            self.custom_interval_config.validate()
        if self.custom_interval_configs:
            for v1 in self.custom_interval_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionScheduleParamList'] = []
        if self.condition_schedule_param_list is not None:
            for k1 in self.condition_schedule_param_list:
                result['ConditionScheduleParamList'].append(k1.to_map() if k1 else None)

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.custom_cron_expression is not None:
            result['CustomCronExpression'] = self.custom_cron_expression

        if self.custom_interval_config is not None:
            result['CustomIntervalConfig'] = self.custom_interval_config.to_map()

        if self.custom_interval_config_type is not None:
            result['CustomIntervalConfigType'] = self.custom_interval_config_type

        result['CustomIntervalConfigs'] = []
        if self.custom_interval_configs is not None:
            for k1 in self.custom_interval_configs:
                result['CustomIntervalConfigs'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        if self.has_reference is not None:
            result['HasReference'] = self.has_reference

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name

        if self.schedule_interval_type is not None:
            result['ScheduleIntervalType'] = self.schedule_interval_type

        if self.schedule_template_desc is not None:
            result['ScheduleTemplateDesc'] = self.schedule_template_desc

        if self.schedule_template_id is not None:
            result['ScheduleTemplateId'] = self.schedule_template_id

        if self.schedule_template_name is not None:
            result['ScheduleTemplateName'] = self.schedule_template_name

        if self.schedule_template_type is not None:
            result['ScheduleTemplateType'] = self.schedule_template_type

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date

        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_schedule_param_list = []
        if m.get('ConditionScheduleParamList') is not None:
            for k1 in m.get('ConditionScheduleParamList'):
                temp_model = main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataConditionScheduleParamList()
                self.condition_schedule_param_list.append(temp_model.from_map(k1))

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('CustomCronExpression') is not None:
            self.custom_cron_expression = m.get('CustomCronExpression')

        if m.get('CustomIntervalConfig') is not None:
            temp_model = main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataCustomIntervalConfig()
            self.custom_interval_config = temp_model.from_map(m.get('CustomIntervalConfig'))

        if m.get('CustomIntervalConfigType') is not None:
            self.custom_interval_config_type = m.get('CustomIntervalConfigType')

        self.custom_interval_configs = []
        if m.get('CustomIntervalConfigs') is not None:
            for k1 in m.get('CustomIntervalConfigs'):
                temp_model = main_models.ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataCustomIntervalConfigs()
                self.custom_interval_configs.append(temp_model.from_map(k1))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        if m.get('HasReference') is not None:
            self.has_reference = m.get('HasReference')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')

        if m.get('ScheduleIntervalType') is not None:
            self.schedule_interval_type = m.get('ScheduleIntervalType')

        if m.get('ScheduleTemplateDesc') is not None:
            self.schedule_template_desc = m.get('ScheduleTemplateDesc')

        if m.get('ScheduleTemplateId') is not None:
            self.schedule_template_id = m.get('ScheduleTemplateId')

        if m.get('ScheduleTemplateName') is not None:
            self.schedule_template_name = m.get('ScheduleTemplateName')

        if m.get('ScheduleTemplateType') is not None:
            self.schedule_template_type = m.get('ScheduleTemplateType')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')

        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')

        return self

class ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataCustomIntervalConfigs(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        interval_unit: str = None,
        schedule_period: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.interval = interval
        self.interval_unit = interval_unit
        self.schedule_period = schedule_period
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataCustomIntervalConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        interval_unit: str = None,
        schedule_period: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.interval = interval
        self.interval_unit = interval_unit
        self.schedule_period = schedule_period
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit

        if self.schedule_period is not None:
            result['SchedulePeriod'] = self.schedule_period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')

        if m.get('SchedulePeriod') is not None:
            self.schedule_period = m.get('SchedulePeriod')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListScheduleTemplatesResponseBodyListScheduleTemplatesResponseResultDataConditionScheduleParamList(DaraModel):
    def __init__(
        self,
        condition_name: str = None,
        cron_expression: str = None,
        enable: bool = None,
        follow_schedule_param: bool = None,
        node_status: int = None,
        schedule_condition_json: str = None,
        schedule_time: str = None,
    ):
        self.condition_name = condition_name
        self.cron_expression = cron_expression
        self.enable = enable
        self.follow_schedule_param = follow_schedule_param
        self.node_status = node_status
        self.schedule_condition_json = schedule_condition_json
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_name is not None:
            result['ConditionName'] = self.condition_name

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.follow_schedule_param is not None:
            result['FollowScheduleParam'] = self.follow_schedule_param

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.schedule_condition_json is not None:
            result['ScheduleConditionJson'] = self.schedule_condition_json

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionName') is not None:
            self.condition_name = m.get('ConditionName')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FollowScheduleParam') is not None:
            self.follow_schedule_param = m.get('FollowScheduleParam')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('ScheduleConditionJson') is not None:
            self.schedule_condition_json = m.get('ScheduleConditionJson')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        return self

