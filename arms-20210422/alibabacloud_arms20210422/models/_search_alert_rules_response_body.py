# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class SearchAlertRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.SearchAlertRulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.SearchAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchAlertRulesResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        alert_rules: List[main_models.SearchAlertRulesResponseBodyPageBeanAlertRules] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.alert_rules = alert_rules
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.alert_rules:
            for v1 in self.alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k1 in self.alert_rules:
                result['AlertRules'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k1 in m.get('AlertRules'):
                temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRules(DaraModel):
    def __init__(
        self,
        alarm_context: main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext = None,
        alert_level: str = None,
        alert_rule: main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule = None,
        alert_title: str = None,
        alert_type: int = None,
        alert_version: int = None,
        alert_way: List[str] = None,
        alert_ways: List[str] = None,
        config: str = None,
        contact_group_id_list: str = None,
        contact_group_ids: str = None,
        create_time: int = None,
        id: int = None,
        metric_param: main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam = None,
        notice: main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesNotice = None,
        region_id: str = None,
        status: str = None,
        task_id: int = None,
        task_status: str = None,
        title: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.alarm_context = alarm_context
        self.alert_level = alert_level
        self.alert_rule = alert_rule
        self.alert_title = alert_title
        self.alert_type = alert_type
        self.alert_version = alert_version
        self.alert_way = alert_way
        self.alert_ways = alert_ways
        self.config = config
        self.contact_group_id_list = contact_group_id_list
        self.contact_group_ids = contact_group_ids
        self.create_time = create_time
        self.id = id
        self.metric_param = metric_param
        self.notice = notice
        self.region_id = region_id
        self.status = status
        self.task_id = task_id
        self.task_status = task_status
        self.title = title
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.alarm_context:
            self.alarm_context.validate()
        if self.alert_rule:
            self.alert_rule.validate()
        if self.metric_param:
            self.metric_param.validate()
        if self.notice:
            self.notice.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_context is not None:
            result['AlarmContext'] = self.alarm_context.to_map()

        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()

        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_version is not None:
            result['AlertVersion'] = self.alert_version

        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way

        if self.alert_ways is not None:
            result['AlertWays'] = self.alert_ways

        if self.config is not None:
            result['Config'] = self.config

        if self.contact_group_id_list is not None:
            result['ContactGroupIdList'] = self.contact_group_id_list

        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param.to_map()

        if self.notice is not None:
            result['Notice'] = self.notice.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContext') is not None:
            temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext()
            self.alarm_context = temp_model.from_map(m.get('AlarmContext'))

        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('AlertRule') is not None:
            temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule()
            self.alert_rule = temp_model.from_map(m.get('AlertRule'))

        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertVersion') is not None:
            self.alert_version = m.get('AlertVersion')

        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')

        if m.get('AlertWays') is not None:
            self.alert_ways = m.get('AlertWays')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ContactGroupIdList') is not None:
            self.contact_group_id_list = m.get('ContactGroupIdList')

        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetricParam') is not None:
            temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam()
            self.metric_param = temp_model.from_map(m.get('MetricParam'))

        if m.get('Notice') is not None:
            temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesNotice()
            self.notice = temp_model.from_map(m.get('Notice'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRulesNotice(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        notice_end_time: int = None,
        notice_start_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.notice_end_time = notice_end_time
        self.notice_start_time = notice_start_time
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

        if self.notice_end_time is not None:
            result['NoticeEndTime'] = self.notice_end_time

        if self.notice_start_time is not None:
            result['NoticeStartTime'] = self.notice_start_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NoticeEndTime') is not None:
            self.notice_end_time = m.get('NoticeEndTime')

        if m.get('NoticeStartTime') is not None:
            self.notice_start_time = m.get('NoticeStartTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam(DaraModel):
    def __init__(
        self,
        app_group_id: str = None,
        app_id: str = None,
        dimensions: List[main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions] = None,
        pid: str = None,
        type: str = None,
    ):
        self.app_group_id = app_group_id
        self.app_id = app_id
        self.dimensions = dimensions
        self.pid = pid
        self.type = type

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule(DaraModel):
    def __init__(
        self,
        operator: str = None,
        rules: List[main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules] = None,
    ):
        self.operator = operator
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['Operator'] = self.operator

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules(DaraModel):
    def __init__(
        self,
        aggregates: str = None,
        alias: str = None,
        measure: str = None,
        nvalue: int = None,
        operator: str = None,
        value: float = None,
    ):
        self.aggregates = aggregates
        self.alias = alias
        self.measure = measure
        self.nvalue = nvalue
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.measure is not None:
            result['Measure'] = self.measure

        if self.nvalue is not None:
            result['NValue'] = self.nvalue

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Measure') is not None:
            self.measure = m.get('Measure')

        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext(DaraModel):
    def __init__(
        self,
        alarm_content_sub_title: str = None,
        alarm_content_template: str = None,
        content: str = None,
        sub_title: str = None,
    ):
        self.alarm_content_sub_title = alarm_content_sub_title
        self.alarm_content_template = alarm_content_template
        self.content = content
        self.sub_title = sub_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_content_sub_title is not None:
            result['AlarmContentSubTitle'] = self.alarm_content_sub_title

        if self.alarm_content_template is not None:
            result['AlarmContentTemplate'] = self.alarm_content_template

        if self.content is not None:
            result['Content'] = self.content

        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContentSubTitle') is not None:
            self.alarm_content_sub_title = m.get('AlarmContentSubTitle')

        if m.get('AlarmContentTemplate') is not None:
            self.alarm_content_template = m.get('AlarmContentTemplate')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')

        return self

