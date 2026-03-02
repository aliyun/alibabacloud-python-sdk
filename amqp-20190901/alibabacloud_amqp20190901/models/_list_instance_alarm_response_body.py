# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class ListInstanceAlarmResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListInstanceAlarmResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.ListInstanceAlarmResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstanceAlarmResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: main_models.ListInstanceAlarmResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VoList') is not None:
            temp_model = main_models.ListInstanceAlarmResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m.get('VoList'))

        return self

class ListInstanceAlarmResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        commodity_instance_alarm_vo: List[main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVO] = None,
    ):
        self.commodity_instance_alarm_vo = commodity_instance_alarm_vo

    def validate(self):
        if self.commodity_instance_alarm_vo:
            for v1 in self.commodity_instance_alarm_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommodityInstanceAlarmVO'] = []
        if self.commodity_instance_alarm_vo is not None:
            for k1 in self.commodity_instance_alarm_vo:
                result['CommodityInstanceAlarmVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity_instance_alarm_vo = []
        if m.get('CommodityInstanceAlarmVO') is not None:
            for k1 in m.get('CommodityInstanceAlarmVO'):
                temp_model = main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVO()
                self.commodity_instance_alarm_vo.append(temp_model.from_map(k1))

        return self

class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVO(DaraModel):
    def __init__(
        self,
        alarm_vo: main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVO = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.alarm_vo = alarm_vo
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        if self.alarm_vo:
            self.alarm_vo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_vo is not None:
            result['AlarmVO'] = self.alarm_vo.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmVO') is not None:
            temp_model = main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVO()
            self.alarm_vo = temp_model.from_map(m.get('AlarmVO'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVO(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        alarm_details: main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetails = None,
        has_config_alarm: bool = None,
    ):
        self.alarm_count = alarm_count
        self.alarm_details = alarm_details
        self.has_config_alarm = has_config_alarm

    def validate(self):
        if self.alarm_details:
            self.alarm_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.alarm_details is not None:
            result['AlarmDetails'] = self.alarm_details.to_map()

        if self.has_config_alarm is not None:
            result['HasConfigAlarm'] = self.has_config_alarm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('AlarmDetails') is not None:
            temp_model = main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetails()
            self.alarm_details = temp_model.from_map(m.get('AlarmDetails'))

        if m.get('HasConfigAlarm') is not None:
            self.has_config_alarm = m.get('HasConfigAlarm')

        return self

class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetails(DaraModel):
    def __init__(
        self,
        alarm_detail: List[main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetailsAlarmDetail] = None,
    ):
        self.alarm_detail = alarm_detail

    def validate(self):
        if self.alarm_detail:
            for v1 in self.alarm_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmDetail'] = []
        if self.alarm_detail is not None:
            for k1 in self.alarm_detail:
                result['AlarmDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_detail = []
        if m.get('AlarmDetail') is not None:
            for k1 in m.get('AlarmDetail'):
                temp_model = main_models.ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetailsAlarmDetail()
                self.alarm_detail.append(temp_model.from_map(k1))

        return self

class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetailsAlarmDetail(DaraModel):
    def __init__(
        self,
        alert_state: str = None,
        comparison_operator: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        effective_interval: str = None,
        enable_state: bool = None,
        group_id: str = None,
        group_name: str = None,
        mail_subject: str = None,
        metric_name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
        webhook: str = None,
    ):
        self.alert_state = alert_state
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.effective_interval = effective_interval
        self.enable_state = enable_state
        self.group_id = group_id
        self.group_name = group_name
        self.mail_subject = mail_subject
        self.metric_name = metric_name
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.resources = resources
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.statistics = statistics
        self.threshold = threshold
        self.times = times
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state

        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.enable_state is not None:
            result['EnableState'] = self.enable_state

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.mail_subject is not None:
            result['MailSubject'] = self.mail_subject

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval

        if self.period is not None:
            result['Period'] = self.period

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')

        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('MailSubject') is not None:
            self.mail_subject = m.get('MailSubject')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

