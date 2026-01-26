# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchAlertRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.SearchAlertRulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned struct.
        self.page_bean = page_bean
        # The ID of the request.
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
        # The details of the alert rules.
        self.alert_rules = alert_rules
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
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
        alert_ways: List[str] = None,
        config: str = None,
        contact_group_id_list: str = None,
        contact_group_ids: str = None,
        create_time: int = None,
        host_by_alert_manager: bool = None,
        id: int = None,
        metric_param: main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam = None,
        notice: main_models.SearchAlertRulesResponseBodyPageBeanAlertRulesNotice = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        task_id: int = None,
        task_status: str = None,
        title: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The format of the alert notification.
        self.alarm_context = alarm_context
        # The severity of the alerts. Only the value `WARN` is supported.
        self.alert_level = alert_level
        # The conditions of the alert rule. Multiple conditions are separated by the AND or OR logical operators.
        self.alert_rule = alert_rule
        # The name of the alert rule.
        self.alert_title = alert_title
        # The type of the alert rule. Valid values:
        # 
        # *   `1`: custom alert rules that are used to monitor drill-down data sets
        # *   `3`: custom alert rules that are used to monitor tiled data sets
        # *   `4`: alert rules that are used to monitor the browser, including the default frontend alert rules
        # *   `5`: alert rules that are used to monitor applications, including the default application alert rules
        # *   `6`: the default browser alert rules
        # *   `7`: the default application alert rules
        # *   `8`: Tracing Analysis alert rules
        # *   `101`: Prometheus alert rules
        self.alert_type = alert_type
        # The version of the alert rule. Default value: `1`.
        self.alert_version = alert_version
        # Sending method of alarm notification.
        self.alert_ways = alert_ways
        # The configuration items of the alert rule. The value is a JSON string.
        # 
        # The configuration item **continuous** indicates whether alert notifications are continuously sent. Valid values:
        # 
        # *   `true`: Alert notifications are sent every minute.
        # *   `false`: The alert silence feature is enabled.
        # 
        # The configuration item **dataRevision** indicates the data revision policy that is used if no data is obtained or the data is null. Default value: 2. Valid values:
        # 
        # *   `0`: overwrites the data by using the value 0
        # *   `1`: overwrites the data by using the value 1
        # *   `2`: overwrites the data by using the value null. This value indicates that no alert is triggered if no data exists
        self.config = config
        # The ID of the contact group. Multiple IDs are separated by commas (,).
        self.contact_group_id_list = contact_group_id_list
        # The IDs of the alert contact groups. The value is a JSON array.
        self.contact_group_ids = contact_group_ids
        # The timestamp that shows when the alert rule was created.
        self.create_time = create_time
        # Indicates whether the alert is sent through the alert center. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.host_by_alert_manager = host_by_alert_manager
        # The ID of the alert rule.
        self.id = id
        # The information about the application that is associated with the alert rule.
        self.metric_param = metric_param
        # The time ranges when the alert rule takes effect and when alert notifications are sent.
        self.notice = notice
        # The ID of the region to which the alert rule belongs.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the alert rule. `RUNNING`: The alert rule is enabled. `STOPPED`: The alert rule is disabled.
        self.status = status
        # The ID of the Application Real-Time Monitoring Service (ARMS) task that is associated with the alert rule.
        self.task_id = task_id
        # The status of the task. This parameter is hidden from users.
        self.task_status = task_status
        # The name of the alert.
        self.title = title
        # The timestamp that shows when the alert rule was updated.
        self.update_time = update_time
        # The ID of the user to which the alert rule belongs.
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

        if self.host_by_alert_manager is not None:
            result['HostByAlertManager'] = self.host_by_alert_manager

        if self.id is not None:
            result['Id'] = self.id

        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param.to_map()

        if self.notice is not None:
            result['Notice'] = self.notice.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('HostByAlertManager') is not None:
            self.host_by_alert_manager = m.get('HostByAlertManager')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

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
        # The end of the time range when the alert rule takes effect within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed.
        self.end_time = end_time
        # The end of the time range when alert notifications are sent based on the alert rule within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed.
        self.notice_end_time = notice_end_time
        # The beginning of the time range when alert notifications are sent based on the alert rule within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed.
        self.notice_start_time = notice_start_time
        # The beginning of the time range when the alert rule takes effect within 24 hours per day. This value is a UNIX timestamp. The year, month, and day that are indicated by the timestamp are not displayed in this value. Only the hour, minute, and second are displayed.
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
        # The ID of the application group that is associated with the alert rule. This parameter is applicable to Enterprise Distributed Application Service (EDAS) applications.
        self.app_group_id = app_group_id
        # The auto-increment ID of the ARMS application. You can ignore this ID.
        self.app_id = app_id
        # The dimensions in the condition.
        self.dimensions = dimensions
        # The PID of the application that is associated with the alert rule.
        self.pid = pid
        # The type of the metric. Valid values:
        # 
        # *   `txn`: the number of API calls during application monitoring
        # *   `txn_type`: the types of API calls during application monitoring
        # *   `db`: database metrics
        # *   `jvm`: Java virtual machine (JVM) metrics
        # *   `host`: host metrics
        # *   `exception`: API call errors
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
        # The key of the dimension. Valid values:
        # 
        # *   `rpc`: the name of the API
        # *   `rpcType`: the type of the API call, such as HTTP or DUBBO
        # *   `endpoint`: the name of the database
        # *   `rootIp`: the IP address of the host
        self.key = key
        # The type of the dimension. Valid values:
        # 
        # *   `STATIC`: checks only the value of this dimension. In this case, you must set the **dimensions.value** parameter.
        # *   `ALL`: checks the values of all dimensions. The metrics of all API calls are checked. If an API call triggers an alert, the name of the API is displayed in the alert notification. In this case, you do not need to set the **dimensions.value** parameter.
        # *   `DISABLE`: aggregates the values of all dimensions. In this case, you do not need to set the **dimensions.value** parameter.
        self.type = type
        # The value of the dimension.
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
        # The logical operator between conditions. Valid values: `&`: AND. `|`: OR.
        self.operator = operator
        # The condition of the alert rule.
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
        # The aggregation logic of the metric data of the alert rule. Valid values:
        # 
        # *   `AVG`: calculates the average value for each minute
        # *   `SUM`: calculates the total value for each minute
        # *   `MAX`: calculates the maximum value for each minute
        # *   `MIN`: calculates the minimum value for each minute
        self.aggregates = aggregates
        # The displayed description of the alert metric.
        self.alias = alias
        # The metric based on which alerts are triggered. For more information, see the "[Alert metrics](https://help.aliyun.com/document_detail/175825.html#h2-url-4)" section in this topic.
        self.measure = measure
        # The time range when data is requested. Unit: minutes. For example, a value of 5 indicates that the alert rule applies to the data in the last 5 minutes.
        self.nvalue = nvalue
        # The operation logic of the condition. Valid values:
        # 
        # *   CURRENT_GTE: greater than or equal to
        # *   CURRENT_LTE: less than or equal to
        # *   PREVIOUS_UP: the increase percentage compared with the last period
        # *   PREVIOUS_DOWN: the decrease percentage compared with the last period
        # *   HOH_UP: the increase percentage compared with the last hour
        # *   HOH_DOWN: the decrease percentage compared with the last hour
        # *   DOD_UP: the increase percentage compared with the last day
        # *   DOD_DOWN: the decrease percentage compared with the last day
        self.operator = operator
        # The threshold of the condition.
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
        # The sub-title of the alert notification content.
        self.alarm_content_sub_title = alarm_content_sub_title
        # The template of the alert notification.
        self.alarm_content_template = alarm_content_template
        # The content of the alert notification.
        self.content = content
        # The sub-title of the alert notification.
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

