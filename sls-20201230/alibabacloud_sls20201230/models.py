# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AlertTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ConditionConfiguration(TeaModel):
    def __init__(
        self,
        condition: str = None,
        count_condition: str = None,
    ):
        self.condition = condition
        self.count_condition = count_condition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.count_condition is not None:
            result['countCondition'] = self.count_condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('countCondition') is not None:
            self.count_condition = m.get('countCondition')
        return self


class GroupConfiguration(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
        type: str = None,
    ):
        self.fields = fields
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class JoinConfiguration(TeaModel):
    def __init__(
        self,
        condition: str = None,
        type: str = None,
    ):
        self.condition = condition
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PolicyConfiguration(TeaModel):
    def __init__(
        self,
        action_policy_id: str = None,
        alert_policy_id: str = None,
        repeat_interval: str = None,
    ):
        self.action_policy_id = action_policy_id
        self.alert_policy_id = alert_policy_id
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_policy_id is not None:
            result['actionPolicyId'] = self.action_policy_id
        if self.alert_policy_id is not None:
            result['alertPolicyId'] = self.alert_policy_id
        if self.repeat_interval is not None:
            result['repeatInterval'] = self.repeat_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionPolicyId') is not None:
            self.action_policy_id = m.get('actionPolicyId')
        if m.get('alertPolicyId') is not None:
            self.alert_policy_id = m.get('alertPolicyId')
        if m.get('repeatInterval') is not None:
            self.repeat_interval = m.get('repeatInterval')
        return self


class AlertQuery(TeaModel):
    def __init__(
        self,
        chart_title: str = None,
        dashboard_id: str = None,
        end: str = None,
        power_sql_mode: str = None,
        project: str = None,
        query: str = None,
        region: str = None,
        role_arn: str = None,
        start: str = None,
        store: str = None,
        store_type: str = None,
        time_span_type: str = None,
        ui: str = None,
    ):
        self.chart_title = chart_title
        self.dashboard_id = dashboard_id
        # This parameter is required.
        self.end = end
        self.power_sql_mode = power_sql_mode
        # This parameter is required.
        self.project = project
        # This parameter is required.
        self.query = query
        # This parameter is required.
        self.region = region
        self.role_arn = role_arn
        # This parameter is required.
        self.start = start
        # This parameter is required.
        self.store = store
        # This parameter is required.
        self.store_type = store_type
        # This parameter is required.
        self.time_span_type = time_span_type
        self.ui = ui

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart_title is not None:
            result['chartTitle'] = self.chart_title
        if self.dashboard_id is not None:
            result['dashboardId'] = self.dashboard_id
        if self.end is not None:
            result['end'] = self.end
        if self.power_sql_mode is not None:
            result['powerSqlMode'] = self.power_sql_mode
        if self.project is not None:
            result['project'] = self.project
        if self.query is not None:
            result['query'] = self.query
        if self.region is not None:
            result['region'] = self.region
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.start is not None:
            result['start'] = self.start
        if self.store is not None:
            result['store'] = self.store
        if self.store_type is not None:
            result['storeType'] = self.store_type
        if self.time_span_type is not None:
            result['timeSpanType'] = self.time_span_type
        if self.ui is not None:
            result['ui'] = self.ui
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chartTitle') is not None:
            self.chart_title = m.get('chartTitle')
        if m.get('dashboardId') is not None:
            self.dashboard_id = m.get('dashboardId')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('powerSqlMode') is not None:
            self.power_sql_mode = m.get('powerSqlMode')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('store') is not None:
            self.store = m.get('store')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        if m.get('timeSpanType') is not None:
            self.time_span_type = m.get('timeSpanType')
        if m.get('ui') is not None:
            self.ui = m.get('ui')
        return self


class SeverityConfiguration(TeaModel):
    def __init__(
        self,
        eval_condition: ConditionConfiguration = None,
        severity: int = None,
    ):
        self.eval_condition = eval_condition
        self.severity = severity

    def validate(self):
        if self.eval_condition:
            self.eval_condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eval_condition is not None:
            result['evalCondition'] = self.eval_condition.to_map()
        if self.severity is not None:
            result['severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('evalCondition') is not None:
            temp_model = ConditionConfiguration()
            self.eval_condition = temp_model.from_map(m['evalCondition'])
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        return self


class SinkAlerthubConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class SinkCmsConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class SinkEventStoreConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        endpoint: str = None,
        event_store: str = None,
        project: str = None,
        role_arn: str = None,
    ):
        self.enabled = enabled
        self.endpoint = endpoint
        self.event_store = event_store
        self.project = project
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.event_store is not None:
            result['eventStore'] = self.event_store
        if self.project is not None:
            result['project'] = self.project
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('eventStore') is not None:
            self.event_store = m.get('eventStore')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        return self


class TemplateConfiguration(TeaModel):
    def __init__(
        self,
        aonotations: Dict[str, Any] = None,
        id: str = None,
        lang: str = None,
        tokens: Dict[str, Any] = None,
        type: str = None,
        version: str = None,
    ):
        self.aonotations = aonotations
        # This parameter is required.
        self.id = id
        self.lang = lang
        self.tokens = tokens
        # This parameter is required.
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aonotations is not None:
            result['aonotations'] = self.aonotations
        if self.id is not None:
            result['id'] = self.id
        if self.lang is not None:
            result['lang'] = self.lang
        if self.tokens is not None:
            result['tokens'] = self.tokens
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aonotations') is not None:
            self.aonotations = m.get('aonotations')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('tokens') is not None:
            self.tokens = m.get('tokens')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class AlertConfiguration(TeaModel):
    def __init__(
        self,
        annotations: List[AlertTag] = None,
        auto_annotation: bool = None,
        condition_configuration: ConditionConfiguration = None,
        dashboard: str = None,
        group_configuration: GroupConfiguration = None,
        join_configurations: List[JoinConfiguration] = None,
        labels: List[AlertTag] = None,
        mute_until: int = None,
        no_data_fire: bool = None,
        no_data_severity: int = None,
        policy_configuration: PolicyConfiguration = None,
        query_list: List[AlertQuery] = None,
        send_resolved: bool = None,
        severity_configurations: List[SeverityConfiguration] = None,
        sink_alerthub: SinkAlerthubConfiguration = None,
        sink_cms: SinkCmsConfiguration = None,
        sink_event_store: SinkEventStoreConfiguration = None,
        tags: List[str] = None,
        template_configuration: TemplateConfiguration = None,
        threshold: int = None,
        type: str = None,
        version: str = None,
    ):
        self.annotations = annotations
        # This parameter is required.
        self.auto_annotation = auto_annotation
        self.condition_configuration = condition_configuration
        self.dashboard = dashboard
        # This parameter is required.
        self.group_configuration = group_configuration
        self.join_configurations = join_configurations
        self.labels = labels
        self.mute_until = mute_until
        # This parameter is required.
        self.no_data_fire = no_data_fire
        self.no_data_severity = no_data_severity
        self.policy_configuration = policy_configuration
        # This parameter is required.
        self.query_list = query_list
        # This parameter is required.
        self.send_resolved = send_resolved
        # This parameter is required.
        self.severity_configurations = severity_configurations
        self.sink_alerthub = sink_alerthub
        self.sink_cms = sink_cms
        self.sink_event_store = sink_event_store
        self.tags = tags
        self.template_configuration = template_configuration
        # This parameter is required.
        self.threshold = threshold
        self.type = type
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.condition_configuration:
            self.condition_configuration.validate()
        if self.group_configuration:
            self.group_configuration.validate()
        if self.join_configurations:
            for k in self.join_configurations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.policy_configuration:
            self.policy_configuration.validate()
        if self.query_list:
            for k in self.query_list:
                if k:
                    k.validate()
        if self.severity_configurations:
            for k in self.severity_configurations:
                if k:
                    k.validate()
        if self.sink_alerthub:
            self.sink_alerthub.validate()
        if self.sink_cms:
            self.sink_cms.validate()
        if self.sink_event_store:
            self.sink_event_store.validate()
        if self.template_configuration:
            self.template_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['annotations'].append(k.to_map() if k else None)
        if self.auto_annotation is not None:
            result['autoAnnotation'] = self.auto_annotation
        if self.condition_configuration is not None:
            result['conditionConfiguration'] = self.condition_configuration.to_map()
        if self.dashboard is not None:
            result['dashboard'] = self.dashboard
        if self.group_configuration is not None:
            result['groupConfiguration'] = self.group_configuration.to_map()
        result['joinConfigurations'] = []
        if self.join_configurations is not None:
            for k in self.join_configurations:
                result['joinConfigurations'].append(k.to_map() if k else None)
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.mute_until is not None:
            result['muteUntil'] = self.mute_until
        if self.no_data_fire is not None:
            result['noDataFire'] = self.no_data_fire
        if self.no_data_severity is not None:
            result['noDataSeverity'] = self.no_data_severity
        if self.policy_configuration is not None:
            result['policyConfiguration'] = self.policy_configuration.to_map()
        result['queryList'] = []
        if self.query_list is not None:
            for k in self.query_list:
                result['queryList'].append(k.to_map() if k else None)
        if self.send_resolved is not None:
            result['sendResolved'] = self.send_resolved
        result['severityConfigurations'] = []
        if self.severity_configurations is not None:
            for k in self.severity_configurations:
                result['severityConfigurations'].append(k.to_map() if k else None)
        if self.sink_alerthub is not None:
            result['sinkAlerthub'] = self.sink_alerthub.to_map()
        if self.sink_cms is not None:
            result['sinkCms'] = self.sink_cms.to_map()
        if self.sink_event_store is not None:
            result['sinkEventStore'] = self.sink_event_store.to_map()
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template_configuration is not None:
            result['templateConfiguration'] = self.template_configuration.to_map()
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('annotations') is not None:
            for k in m.get('annotations'):
                temp_model = AlertTag()
                self.annotations.append(temp_model.from_map(k))
        if m.get('autoAnnotation') is not None:
            self.auto_annotation = m.get('autoAnnotation')
        if m.get('conditionConfiguration') is not None:
            temp_model = ConditionConfiguration()
            self.condition_configuration = temp_model.from_map(m['conditionConfiguration'])
        if m.get('dashboard') is not None:
            self.dashboard = m.get('dashboard')
        if m.get('groupConfiguration') is not None:
            temp_model = GroupConfiguration()
            self.group_configuration = temp_model.from_map(m['groupConfiguration'])
        self.join_configurations = []
        if m.get('joinConfigurations') is not None:
            for k in m.get('joinConfigurations'):
                temp_model = JoinConfiguration()
                self.join_configurations.append(temp_model.from_map(k))
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = AlertTag()
                self.labels.append(temp_model.from_map(k))
        if m.get('muteUntil') is not None:
            self.mute_until = m.get('muteUntil')
        if m.get('noDataFire') is not None:
            self.no_data_fire = m.get('noDataFire')
        if m.get('noDataSeverity') is not None:
            self.no_data_severity = m.get('noDataSeverity')
        if m.get('policyConfiguration') is not None:
            temp_model = PolicyConfiguration()
            self.policy_configuration = temp_model.from_map(m['policyConfiguration'])
        self.query_list = []
        if m.get('queryList') is not None:
            for k in m.get('queryList'):
                temp_model = AlertQuery()
                self.query_list.append(temp_model.from_map(k))
        if m.get('sendResolved') is not None:
            self.send_resolved = m.get('sendResolved')
        self.severity_configurations = []
        if m.get('severityConfigurations') is not None:
            for k in m.get('severityConfigurations'):
                temp_model = SeverityConfiguration()
                self.severity_configurations.append(temp_model.from_map(k))
        if m.get('sinkAlerthub') is not None:
            temp_model = SinkAlerthubConfiguration()
            self.sink_alerthub = temp_model.from_map(m['sinkAlerthub'])
        if m.get('sinkCms') is not None:
            temp_model = SinkCmsConfiguration()
            self.sink_cms = temp_model.from_map(m['sinkCms'])
        if m.get('sinkEventStore') is not None:
            temp_model = SinkEventStoreConfiguration()
            self.sink_event_store = temp_model.from_map(m['sinkEventStore'])
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('templateConfiguration') is not None:
            temp_model = TemplateConfiguration()
            self.template_configuration = temp_model.from_map(m['templateConfiguration'])
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Schedule(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        delay: int = None,
        interval: str = None,
        run_immediately: bool = None,
        time_zone: str = None,
        type: str = None,
    ):
        self.cron_expression = cron_expression
        self.delay = delay
        self.interval = interval
        self.run_immediately = run_immediately
        self.time_zone = time_zone
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.delay is not None:
            result['delay'] = self.delay
        if self.interval is not None:
            result['interval'] = self.interval
        if self.run_immediately is not None:
            result['runImmediately'] = self.run_immediately
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('delay') is not None:
            self.delay = m.get('delay')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('runImmediately') is not None:
            self.run_immediately = m.get('runImmediately')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Alert(TeaModel):
    def __init__(
        self,
        configuration: AlertConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        schedule: Schedule = None,
        status: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schedule = schedule
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = AlertConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ConsumeProcessorConfiguration(TeaModel):
    def __init__(
        self,
        spl: str = None,
    ):
        # This parameter is required.
        self.spl = spl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spl is not None:
            result['spl'] = self.spl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spl') is not None:
            self.spl = m.get('spl')
        return self


class ConsumeProcessor(TeaModel):
    def __init__(
        self,
        configuration: ConsumeProcessorConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        processor_name: str = None,
        update_time: int = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.processor_name = processor_name
        self.update_time = update_time

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.processor_name is not None:
            result['processorName'] = self.processor_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ConsumeProcessorConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('processorName') is not None:
            self.processor_name = m.get('processorName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ConsumerGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: bool = None,
        timeout: int = None,
    ):
        self.name = name
        self.order = order
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class ETLConfigurationSink(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        datasets: List[str] = None,
        endpoint: str = None,
        logstore: str = None,
        name: str = None,
        project: str = None,
        role_arn: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.datasets = datasets
        self.endpoint = endpoint
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project = project
        # This parameter is required.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.datasets is not None:
            result['datasets'] = self.datasets
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.name is not None:
            result['name'] = self.name
        if self.project is not None:
            result['project'] = self.project
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('datasets') is not None:
            self.datasets = m.get('datasets')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        return self


class ETLConfiguration(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        from_time: int = None,
        lang: str = None,
        logstore: str = None,
        parameters: Dict[str, Any] = None,
        role_arn: str = None,
        script: str = None,
        sinks: List[ETLConfigurationSink] = None,
        to_time: int = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        # This parameter is required.
        self.from_time = from_time
        self.lang = lang
        # This parameter is required.
        self.logstore = logstore
        self.parameters = parameters
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.script = script
        # This parameter is required.
        self.sinks = sinks
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        if self.sinks:
            for k in self.sinks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.lang is not None:
            result['lang'] = self.lang
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.script is not None:
            result['script'] = self.script
        result['sinks'] = []
        if self.sinks is not None:
            for k in self.sinks:
                result['sinks'].append(k.to_map() if k else None)
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('script') is not None:
            self.script = m.get('script')
        self.sinks = []
        if m.get('sinks') is not None:
            for k in m.get('sinks'):
                temp_model = ETLConfigurationSink()
                self.sinks.append(temp_model.from_map(k))
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class ETL(TeaModel):
    def __init__(
        self,
        configuration: ETLConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        schedule_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        self.schedule_id = schedule_id
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ETLConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class EncryptUserCmkConf(TeaModel):
    def __init__(
        self,
        arn: str = None,
        cmk_key_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.arn = arn
        # This parameter is required.
        self.cmk_key_id = cmk_key_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.cmk_key_id is not None:
            result['cmk_key_id'] = self.cmk_key_id
        if self.region_id is not None:
            result['region_id'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('cmk_key_id') is not None:
            self.cmk_key_id = m.get('cmk_key_id')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        return self


class EncryptConf(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        encrypt_type: str = None,
        user_cmk_info: EncryptUserCmkConf = None,
    ):
        # This parameter is required.
        self.enable = enable
        self.encrypt_type = encrypt_type
        self.user_cmk_info = user_cmk_info

    def validate(self):
        if self.user_cmk_info:
            self.user_cmk_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.encrypt_type is not None:
            result['encrypt_type'] = self.encrypt_type
        if self.user_cmk_info is not None:
            result['user_cmk_info'] = self.user_cmk_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('encrypt_type') is not None:
            self.encrypt_type = m.get('encrypt_type')
        if m.get('user_cmk_info') is not None:
            temp_model = EncryptUserCmkConf()
            self.user_cmk_info = temp_model.from_map(m['user_cmk_info'])
        return self


class Histogram(TeaModel):
    def __init__(
        self,
        count: int = None,
        from_: int = None,
        progress: str = None,
        to: int = None,
    ):
        self.count = count
        self.from_ = from_
        self.progress = progress
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.from_ is not None:
            result['from'] = self.from_
        if self.progress is not None:
            result['progress'] = self.progress
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class IndexJsonKey(TeaModel):
    def __init__(
        self,
        alias: str = None,
        case_sensitive: bool = None,
        chn: bool = None,
        doc_value: bool = None,
        token: List[str] = None,
        type: str = None,
    ):
        self.alias = alias
        self.case_sensitive = case_sensitive
        self.chn = chn
        self.doc_value = doc_value
        self.token = token
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.doc_value is not None:
            result['doc_value'] = self.doc_value
        if self.token is not None:
            result['token'] = self.token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('doc_value') is not None:
            self.doc_value = m.get('doc_value')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class IndexKey(TeaModel):
    def __init__(
        self,
        alias: str = None,
        case_sensitive: bool = None,
        chn: bool = None,
        doc_value: bool = None,
        index_all: bool = None,
        json_keys: Dict[str, IndexJsonKey] = None,
        max_depth: int = None,
        token: List[str] = None,
        type: str = None,
    ):
        self.alias = alias
        self.case_sensitive = case_sensitive
        self.chn = chn
        self.doc_value = doc_value
        self.index_all = index_all
        self.json_keys = json_keys
        self.max_depth = max_depth
        self.token = token
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.json_keys:
            for v in self.json_keys.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.doc_value is not None:
            result['doc_value'] = self.doc_value
        if self.index_all is not None:
            result['index_all'] = self.index_all
        result['json_keys'] = {}
        if self.json_keys is not None:
            for k, v in self.json_keys.items():
                result['json_keys'][k] = v.to_map()
        if self.max_depth is not None:
            result['max_depth'] = self.max_depth
        if self.token is not None:
            result['token'] = self.token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('doc_value') is not None:
            self.doc_value = m.get('doc_value')
        if m.get('index_all') is not None:
            self.index_all = m.get('index_all')
        self.json_keys = {}
        if m.get('json_keys') is not None:
            for k, v in m.get('json_keys').items():
                temp_model = IndexJsonKey()
                self.json_keys[k] = temp_model.from_map(v)
        if m.get('max_depth') is not None:
            self.max_depth = m.get('max_depth')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class IngestProcessorConfiguration(TeaModel):
    def __init__(
        self,
        parse_fail: str = None,
        spl: str = None,
    ):
        self.parse_fail = parse_fail
        # This parameter is required.
        self.spl = spl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parse_fail is not None:
            result['parseFail'] = self.parse_fail
        if self.spl is not None:
            result['spl'] = self.spl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parseFail') is not None:
            self.parse_fail = m.get('parseFail')
        if m.get('spl') is not None:
            self.spl = m.get('spl')
        return self


class IngestProcessor(TeaModel):
    def __init__(
        self,
        configuration: IngestProcessorConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        processor_name: str = None,
        update_time: int = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.processor_name = processor_name
        self.update_time = update_time

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.processor_name is not None:
            result['processorName'] = self.processor_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = IngestProcessorConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('processorName') is not None:
            self.processor_name = m.get('processorName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class LogContent(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LogItem(TeaModel):
    def __init__(
        self,
        contents: List[LogContent] = None,
        time: int = None,
    ):
        # This parameter is required.
        self.contents = contents
        # This parameter is required.
        self.time = time

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = LogContent()
                self.contents.append(temp_model.from_map(k))
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class LogTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class LogGroup(TeaModel):
    def __init__(
        self,
        log_items: List[LogItem] = None,
        log_tags: List[LogTag] = None,
        source: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.log_items = log_items
        self.log_tags = log_tags
        self.source = source
        self.topic = topic

    def validate(self):
        if self.log_items:
            for k in self.log_items:
                if k:
                    k.validate()
        if self.log_tags:
            for k in self.log_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogItems'] = []
        if self.log_items is not None:
            for k in self.log_items:
                result['LogItems'].append(k.to_map() if k else None)
        result['LogTags'] = []
        if self.log_tags is not None:
            for k in self.log_tags:
                result['LogTags'].append(k.to_map() if k else None)
        if self.source is not None:
            result['Source'] = self.source
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_items = []
        if m.get('LogItems') is not None:
            for k in m.get('LogItems'):
                temp_model = LogItem()
                self.log_items.append(temp_model.from_map(k))
        self.log_tags = []
        if m.get('LogTags') is not None:
            for k in m.get('LogTags'):
                temp_model = LogTag()
                self.log_tags.append(temp_model.from_map(k))
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class LogGroupList(TeaModel):
    def __init__(
        self,
        log_group_list: List[LogGroup] = None,
    ):
        # This parameter is required.
        self.log_group_list = log_group_list

    def validate(self):
        if self.log_group_list:
            for k in self.log_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['logGroupList'] = []
        if self.log_group_list is not None:
            for k in self.log_group_list:
                result['logGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_group_list = []
        if m.get('logGroupList') is not None:
            for k in m.get('logGroupList'):
                temp_model = LogGroup()
                self.log_group_list.append(temp_model.from_map(k))
        return self


class LogtailConfigOutputDetail(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        logstore_name: str = None,
        region: str = None,
        telemetry_type: str = None,
    ):
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.logstore_name = logstore_name
        self.region = region
        self.telemetry_type = telemetry_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.region is not None:
            result['region'] = self.region
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        return self


class LogtailConfig(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        create_time: int = None,
        input_detail: Dict[str, Any] = None,
        input_type: str = None,
        last_modify_time: int = None,
        log_sample: str = None,
        output_detail: LogtailConfigOutputDetail = None,
        output_type: str = None,
    ):
        # This parameter is required.
        self.config_name = config_name
        self.create_time = create_time
        # This parameter is required.
        self.input_detail = input_detail
        # This parameter is required.
        self.input_type = input_type
        self.last_modify_time = last_modify_time
        self.log_sample = log_sample
        # This parameter is required.
        self.output_detail = output_detail
        # This parameter is required.
        self.output_type = output_type

    def validate(self):
        if self.output_detail:
            self.output_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.input_detail is not None:
            result['inputDetail'] = self.input_detail
        if self.input_type is not None:
            result['inputType'] = self.input_type
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.output_detail is not None:
            result['outputDetail'] = self.output_detail.to_map()
        if self.output_type is not None:
            result['outputType'] = self.output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('inputDetail') is not None:
            self.input_detail = m.get('inputDetail')
        if m.get('inputType') is not None:
            self.input_type = m.get('inputType')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('outputDetail') is not None:
            temp_model = LogtailConfigOutputDetail()
            self.output_detail = temp_model.from_map(m['outputDetail'])
        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')
        return self


class LogtailPipelineConfig(TeaModel):
    def __init__(
        self,
        aggregators: List[Dict[str, Any]] = None,
        config_name: str = None,
        create_time: int = None,
        flushers: List[Dict[str, Any]] = None,
        global_: Dict[str, Any] = None,
        inputs: List[Dict[str, Any]] = None,
        last_modify_time: int = None,
        log_sample: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        self.aggregators = aggregators
        # This parameter is required.
        self.config_name = config_name
        self.create_time = create_time
        # This parameter is required.
        self.flushers = flushers
        self.global_ = global_
        # This parameter is required.
        self.inputs = inputs
        self.last_modify_time = last_modify_time
        self.log_sample = log_sample
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.flushers is not None:
            result['flushers'] = self.flushers
        if self.global_ is not None:
            result['global'] = self.global_
        if self.inputs is not None:
            result['inputs'] = self.inputs
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')
        if m.get('global') is not None:
            self.global_ = m.get('global')
        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class MLDataParamAnnotationsValue(TeaModel):
    def __init__(
        self,
        annotated_by: str = None,
        update_time: int = None,
        results: List[Dict[str, str]] = None,
    ):
        self.annotated_by = annotated_by
        self.update_time = update_time
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotated_by is not None:
            result['annotatedBy'] = self.annotated_by
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.results is not None:
            result['results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotatedBy') is not None:
            self.annotated_by = m.get('annotatedBy')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('results') is not None:
            self.results = m.get('results')
        return self


class MLDataParamPredictionsValue(TeaModel):
    def __init__(
        self,
        annotated_by: str = None,
        update_time: int = None,
        results: List[Dict[str, str]] = None,
    ):
        self.annotated_by = annotated_by
        self.update_time = update_time
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotated_by is not None:
            result['annotatedBy'] = self.annotated_by
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.results is not None:
            result['results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotatedBy') is not None:
            self.annotated_by = m.get('annotatedBy')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('results') is not None:
            self.results = m.get('results')
        return self


class MLDataParam(TeaModel):
    def __init__(
        self,
        annotationdata_id: str = None,
        annotations: Dict[str, MLDataParamAnnotationsValue] = None,
        config: Dict[str, str] = None,
        create_time: int = None,
        data_hash: str = None,
        dataset_id: str = None,
        last_modify_time: int = None,
        predictions: Dict[str, MLDataParamPredictionsValue] = None,
        value: str = None,
        value_type: str = None,
    ):
        self.annotationdata_id = annotationdata_id
        self.annotations = annotations
        self.config = config
        self.create_time = create_time
        self.data_hash = data_hash
        self.dataset_id = dataset_id
        self.last_modify_time = last_modify_time
        self.predictions = predictions
        self.value = value
        self.value_type = value_type

    def validate(self):
        if self.annotations:
            for v in self.annotations.values():
                if v:
                    v.validate()
        if self.predictions:
            for v in self.predictions.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotationdata_id is not None:
            result['annotationdataId'] = self.annotationdata_id
        result['annotations'] = {}
        if self.annotations is not None:
            for k, v in self.annotations.items():
                result['annotations'][k] = v.to_map()
        if self.config is not None:
            result['config'] = self.config
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_hash is not None:
            result['dataHash'] = self.data_hash
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        result['predictions'] = {}
        if self.predictions is not None:
            for k, v in self.predictions.items():
                result['predictions'][k] = v.to_map()
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotationdataId') is not None:
            self.annotationdata_id = m.get('annotationdataId')
        self.annotations = {}
        if m.get('annotations') is not None:
            for k, v in m.get('annotations').items():
                temp_model = MLDataParamAnnotationsValue()
                self.annotations[k] = temp_model.from_map(v)
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataHash') is not None:
            self.data_hash = m.get('dataHash')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        self.predictions = {}
        if m.get('predictions') is not None:
            for k, v in m.get('predictions').items():
                temp_model = MLDataParamPredictionsValue()
                self.predictions[k] = temp_model.from_map(v)
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class MLDataSetParam(TeaModel):
    def __init__(
        self,
        create_by: str = None,
        create_time: int = None,
        data_type: str = None,
        dataset_id: str = None,
        description: str = None,
        label_id: str = None,
        last_modify_time: int = None,
        name: str = None,
        setting_type: str = None,
    ):
        self.create_by = create_by
        self.create_time = create_time
        self.data_type = data_type
        self.dataset_id = dataset_id
        self.description = description
        self.label_id = label_id
        self.last_modify_time = last_modify_time
        self.name = name
        self.setting_type = setting_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_by is not None:
            result['createBy'] = self.create_by
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.description is not None:
            result['description'] = self.description
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['name'] = self.name
        if self.setting_type is not None:
            result['settingType'] = self.setting_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createBy') is not None:
            self.create_by = m.get('createBy')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('settingType') is not None:
            self.setting_type = m.get('settingType')
        return self


class MLLabelParamSettings(TeaModel):
    def __init__(
        self,
        config: str = None,
        mode: str = None,
        type: str = None,
        version: str = None,
    ):
        self.config = config
        self.mode = mode
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.mode is not None:
            result['mode'] = self.mode
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class MLLabelParam(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        label_id: str = None,
        last_modify_time: int = None,
        name: str = None,
        settings: List[MLLabelParamSettings] = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.label_id = label_id
        self.last_modify_time = last_modify_time
        self.name = name
        self.settings = settings
        self.type = type

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.label_id is not None:
            result['labelId'] = self.label_id
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['name'] = self.name
        result['settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['settings'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.settings = []
        if m.get('settings') is not None:
            for k in m.get('settings'):
                temp_model = MLLabelParamSettings()
                self.settings.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MLServiceAnalysisParam(TeaModel):
    def __init__(
        self,
        input: List[Dict[str, str]] = None,
        parameter: Dict[str, str] = None,
    ):
        self.input = input
        self.parameter = parameter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.parameter is not None:
            result['parameter'] = self.parameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        return self


class MLServiceParamModel(TeaModel):
    def __init__(
        self,
        model_resource_id: str = None,
        model_resource_type: str = None,
    ):
        self.model_resource_id = model_resource_id
        self.model_resource_type = model_resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_resource_id is not None:
            result['modelResourceId'] = self.model_resource_id
        if self.model_resource_type is not None:
            result['modelResourceType'] = self.model_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelResourceId') is not None:
            self.model_resource_id = m.get('modelResourceId')
        if m.get('modelResourceType') is not None:
            self.model_resource_type = m.get('modelResourceType')
        return self


class MLServiceParamResource(TeaModel):
    def __init__(
        self,
        cpu_limit: int = None,
        gpu: int = None,
        memory_limit: int = None,
        replica: int = None,
    ):
        self.cpu_limit = cpu_limit
        self.gpu = gpu
        self.memory_limit = memory_limit
        self.replica = replica

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.gpu is not None:
            result['gpu'] = self.gpu
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.replica is not None:
            result['replica'] = self.replica
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('gpu') is not None:
            self.gpu = m.get('gpu')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        return self


class MLServiceParam(TeaModel):
    def __init__(
        self,
        description: str = None,
        model: MLServiceParamModel = None,
        name: str = None,
        resource: MLServiceParamResource = None,
        service_type: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.description = description
        self.model = model
        self.name = name
        self.resource = resource
        self.service_type = service_type
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.model:
            self.model.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.model is not None:
            result['model'] = self.model.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.status is not None:
            result['status'] = self.status
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('model') is not None:
            temp_model = MLServiceParamModel()
            self.model = temp_model.from_map(m['model'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resource') is not None:
            temp_model = MLServiceParamResource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class MaxComputeExportConfigurationSink(TeaModel):
    def __init__(
        self,
        fields: List[str] = None,
        odps_access_key_id: str = None,
        odps_access_secret: str = None,
        odps_endpoint: str = None,
        odps_project: str = None,
        odps_rolearn: str = None,
        odps_table: str = None,
        odps_tunnel_endpoint: str = None,
        partition_column: List[str] = None,
        partition_time_format: str = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.fields = fields
        self.odps_access_key_id = odps_access_key_id
        self.odps_access_secret = odps_access_secret
        # This parameter is required.
        self.odps_endpoint = odps_endpoint
        # This parameter is required.
        self.odps_project = odps_project
        self.odps_rolearn = odps_rolearn
        # This parameter is required.
        self.odps_table = odps_table
        # This parameter is required.
        self.odps_tunnel_endpoint = odps_tunnel_endpoint
        # This parameter is required.
        self.partition_column = partition_column
        # This parameter is required.
        self.partition_time_format = partition_time_format
        # This parameter is required.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.odps_access_key_id is not None:
            result['odpsAccessKeyId'] = self.odps_access_key_id
        if self.odps_access_secret is not None:
            result['odpsAccessSecret'] = self.odps_access_secret
        if self.odps_endpoint is not None:
            result['odpsEndpoint'] = self.odps_endpoint
        if self.odps_project is not None:
            result['odpsProject'] = self.odps_project
        if self.odps_rolearn is not None:
            result['odpsRolearn'] = self.odps_rolearn
        if self.odps_table is not None:
            result['odpsTable'] = self.odps_table
        if self.odps_tunnel_endpoint is not None:
            result['odpsTunnelEndpoint'] = self.odps_tunnel_endpoint
        if self.partition_column is not None:
            result['partitionColumn'] = self.partition_column
        if self.partition_time_format is not None:
            result['partitionTimeFormat'] = self.partition_time_format
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('odpsAccessKeyId') is not None:
            self.odps_access_key_id = m.get('odpsAccessKeyId')
        if m.get('odpsAccessSecret') is not None:
            self.odps_access_secret = m.get('odpsAccessSecret')
        if m.get('odpsEndpoint') is not None:
            self.odps_endpoint = m.get('odpsEndpoint')
        if m.get('odpsProject') is not None:
            self.odps_project = m.get('odpsProject')
        if m.get('odpsRolearn') is not None:
            self.odps_rolearn = m.get('odpsRolearn')
        if m.get('odpsTable') is not None:
            self.odps_table = m.get('odpsTable')
        if m.get('odpsTunnelEndpoint') is not None:
            self.odps_tunnel_endpoint = m.get('odpsTunnelEndpoint')
        if m.get('partitionColumn') is not None:
            self.partition_column = m.get('partitionColumn')
        if m.get('partitionTimeFormat') is not None:
            self.partition_time_format = m.get('partitionTimeFormat')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class MaxComputeExportConfiguration(TeaModel):
    def __init__(
        self,
        from_time: int = None,
        logstore: str = None,
        role_arn: str = None,
        sink: MaxComputeExportConfigurationSink = None,
        to_time: int = None,
    ):
        # This parameter is required.
        self.from_time = from_time
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.sink = sink
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.sink is not None:
            result['sink'] = self.sink.to_map()
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('sink') is not None:
            temp_model = MaxComputeExportConfigurationSink()
            self.sink = temp_model.from_map(m['sink'])
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class MaxComputeExport(TeaModel):
    def __init__(
        self,
        configuration: MaxComputeExportConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = MaxComputeExportConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class OSSExportConfigurationSink(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        buffer_interval: int = None,
        buffer_size: int = None,
        compression_type: str = None,
        content_detail: Dict[str, Any] = None,
        content_type: str = None,
        delay_sec: int = None,
        delay_seconds: int = None,
        endpoint: str = None,
        path_format: str = None,
        path_format_type: str = None,
        prefix: str = None,
        role_arn: str = None,
        suffix: str = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        self.buffer_interval = buffer_interval
        self.buffer_size = buffer_size
        self.compression_type = compression_type
        self.content_detail = content_detail
        self.content_type = content_type
        self.delay_sec = delay_sec
        self.delay_seconds = delay_seconds
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.path_format = path_format
        # This parameter is required.
        self.path_format_type = path_format_type
        self.prefix = prefix
        # This parameter is required.
        self.role_arn = role_arn
        self.suffix = suffix
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.buffer_interval is not None:
            result['bufferInterval'] = self.buffer_interval
        if self.buffer_size is not None:
            result['bufferSize'] = self.buffer_size
        if self.compression_type is not None:
            result['compressionType'] = self.compression_type
        if self.content_detail is not None:
            result['contentDetail'] = self.content_detail
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.delay_sec is not None:
            result['delaySec'] = self.delay_sec
        if self.delay_seconds is not None:
            result['delaySeconds'] = self.delay_seconds
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.path_format is not None:
            result['pathFormat'] = self.path_format
        if self.path_format_type is not None:
            result['pathFormatType'] = self.path_format_type
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('bufferInterval') is not None:
            self.buffer_interval = m.get('bufferInterval')
        if m.get('bufferSize') is not None:
            self.buffer_size = m.get('bufferSize')
        if m.get('compressionType') is not None:
            self.compression_type = m.get('compressionType')
        if m.get('contentDetail') is not None:
            self.content_detail = m.get('contentDetail')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('delaySec') is not None:
            self.delay_sec = m.get('delaySec')
        if m.get('delaySeconds') is not None:
            self.delay_seconds = m.get('delaySeconds')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('pathFormat') is not None:
            self.path_format = m.get('pathFormat')
        if m.get('pathFormatType') is not None:
            self.path_format_type = m.get('pathFormatType')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class OSSExportConfiguration(TeaModel):
    def __init__(
        self,
        from_time: int = None,
        logstore: str = None,
        role_arn: str = None,
        sink: OSSExportConfigurationSink = None,
        to_time: int = None,
    ):
        self.from_time = from_time
        self.logstore = logstore
        self.role_arn = role_arn
        self.sink = sink
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.sink is not None:
            result['sink'] = self.sink.to_map()
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('sink') is not None:
            temp_model = OSSExportConfigurationSink()
            self.sink = temp_model.from_map(m['sink'])
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class OSSExport(TeaModel):
    def __init__(
        self,
        configuration: OSSExportConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        schedule_id: str = None,
        status: str = None,
    ):
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        self.schedule_id = schedule_id
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSExportConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class OSSIngestionConfigurationSource(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        compression_codec: str = None,
        encoding: str = None,
        end_time: int = None,
        endpoint: str = None,
        format: Dict[str, Any] = None,
        interval: str = None,
        pattern: str = None,
        prefix: str = None,
        restore_object_enabled: bool = None,
        role_arn: str = None,
        start_time: int = None,
        time_field: str = None,
        time_format: str = None,
        time_pattern: str = None,
        time_zone: str = None,
        use_meta_index: bool = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        # This parameter is required.
        self.compression_codec = compression_codec
        # This parameter is required.
        self.encoding = encoding
        self.end_time = end_time
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.format = format
        # This parameter is required.
        self.interval = interval
        self.pattern = pattern
        self.prefix = prefix
        self.restore_object_enabled = restore_object_enabled
        self.role_arn = role_arn
        self.start_time = start_time
        self.time_field = time_field
        self.time_format = time_format
        self.time_pattern = time_pattern
        self.time_zone = time_zone
        # This parameter is required.
        self.use_meta_index = use_meta_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.compression_codec is not None:
            result['compressionCodec'] = self.compression_codec
        if self.encoding is not None:
            result['encoding'] = self.encoding
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.format is not None:
            result['format'] = self.format
        if self.interval is not None:
            result['interval'] = self.interval
        if self.pattern is not None:
            result['pattern'] = self.pattern
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.restore_object_enabled is not None:
            result['restoreObjectEnabled'] = self.restore_object_enabled
        if self.role_arn is not None:
            result['roleARN'] = self.role_arn
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.time_field is not None:
            result['timeField'] = self.time_field
        if self.time_format is not None:
            result['timeFormat'] = self.time_format
        if self.time_pattern is not None:
            result['timePattern'] = self.time_pattern
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.use_meta_index is not None:
            result['useMetaIndex'] = self.use_meta_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('compressionCodec') is not None:
            self.compression_codec = m.get('compressionCodec')
        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('pattern') is not None:
            self.pattern = m.get('pattern')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('restoreObjectEnabled') is not None:
            self.restore_object_enabled = m.get('restoreObjectEnabled')
        if m.get('roleARN') is not None:
            self.role_arn = m.get('roleARN')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timeField') is not None:
            self.time_field = m.get('timeField')
        if m.get('timeFormat') is not None:
            self.time_format = m.get('timeFormat')
        if m.get('timePattern') is not None:
            self.time_pattern = m.get('timePattern')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('useMetaIndex') is not None:
            self.use_meta_index = m.get('useMetaIndex')
        return self


class OSSIngestionConfiguration(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        source: OSSIngestionConfigurationSource = None,
    ):
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.source = source

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.source is not None:
            result['source'] = self.source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('source') is not None:
            temp_model = OSSIngestionConfigurationSource()
            self.source = temp_model.from_map(m['source'])
        return self


class OSSIngestion(TeaModel):
    def __init__(
        self,
        configuration: OSSIngestionConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        schedule: Schedule = None,
        schedule_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schedule = schedule
        self.schedule_id = schedule_id
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSIngestionConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ProcessorAssociate(TeaModel):
    def __init__(
        self,
        processor_id: str = None,
    ):
        # This parameter is required.
        self.processor_id = processor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processor_id is not None:
            result['processorId'] = self.processor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')
        return self


class ProjectSummary(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        project_name: str = None,
        region: str = None,
        resource_group_id: str = None,
        update_time: int = None,
    ):
        # This parameter is required.
        self.create_time = create_time
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.region is not None:
            result['region'] = self.region
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class SavedSearch(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        logstore: str = None,
        savedsearch_name: str = None,
        search_query: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.savedsearch_name = savedsearch_name
        # This parameter is required.
        self.search_query = search_query
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class ScheduledSQLConfiguration(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        dest_endpoint: str = None,
        dest_logstore: str = None,
        dest_project: str = None,
        dest_role_arn: str = None,
        from_time: int = None,
        from_time_expr: str = None,
        max_retries: int = None,
        max_run_time_in_seconds: int = None,
        parameters: Dict[str, Any] = None,
        resource_pool: str = None,
        role_arn: str = None,
        script: str = None,
        source_logstore: str = None,
        sql_type: str = None,
        to_time: int = None,
        to_time_expr: str = None,
    ):
        # This parameter is required.
        self.data_format = data_format
        # This parameter is required.
        self.dest_endpoint = dest_endpoint
        # This parameter is required.
        self.dest_logstore = dest_logstore
        # This parameter is required.
        self.dest_project = dest_project
        # This parameter is required.
        self.dest_role_arn = dest_role_arn
        # This parameter is required.
        self.from_time = from_time
        # This parameter is required.
        self.from_time_expr = from_time_expr
        # This parameter is required.
        self.max_retries = max_retries
        # This parameter is required.
        self.max_run_time_in_seconds = max_run_time_in_seconds
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.resource_pool = resource_pool
        # This parameter is required.
        self.role_arn = role_arn
        # This parameter is required.
        self.script = script
        # This parameter is required.
        self.source_logstore = source_logstore
        # This parameter is required.
        self.sql_type = sql_type
        # This parameter is required.
        self.to_time = to_time
        # This parameter is required.
        self.to_time_expr = to_time_expr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['dataFormat'] = self.data_format
        if self.dest_endpoint is not None:
            result['destEndpoint'] = self.dest_endpoint
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_role_arn is not None:
            result['destRoleArn'] = self.dest_role_arn
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.from_time_expr is not None:
            result['fromTimeExpr'] = self.from_time_expr
        if self.max_retries is not None:
            result['maxRetries'] = self.max_retries
        if self.max_run_time_in_seconds is not None:
            result['maxRunTimeInSeconds'] = self.max_run_time_in_seconds
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.resource_pool is not None:
            result['resourcePool'] = self.resource_pool
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.script is not None:
            result['script'] = self.script
        if self.source_logstore is not None:
            result['sourceLogstore'] = self.source_logstore
        if self.sql_type is not None:
            result['sqlType'] = self.sql_type
        if self.to_time is not None:
            result['toTime'] = self.to_time
        if self.to_time_expr is not None:
            result['toTimeExpr'] = self.to_time_expr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataFormat') is not None:
            self.data_format = m.get('dataFormat')
        if m.get('destEndpoint') is not None:
            self.dest_endpoint = m.get('destEndpoint')
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRoleArn') is not None:
            self.dest_role_arn = m.get('destRoleArn')
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('fromTimeExpr') is not None:
            self.from_time_expr = m.get('fromTimeExpr')
        if m.get('maxRetries') is not None:
            self.max_retries = m.get('maxRetries')
        if m.get('maxRunTimeInSeconds') is not None:
            self.max_run_time_in_seconds = m.get('maxRunTimeInSeconds')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('resourcePool') is not None:
            self.resource_pool = m.get('resourcePool')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('script') is not None:
            self.script = m.get('script')
        if m.get('sourceLogstore') is not None:
            self.source_logstore = m.get('sourceLogstore')
        if m.get('sqlType') is not None:
            self.sql_type = m.get('sqlType')
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        if m.get('toTimeExpr') is not None:
            self.to_time_expr = m.get('toTimeExpr')
        return self


class ScheduledSQL(TeaModel):
    def __init__(
        self,
        configuration: ScheduledSQLConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        schedule: Schedule = None,
        schedule_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schedule = schedule
        self.schedule_id = schedule_id
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ScheduledSQLConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class StoreViewStore(TeaModel):
    def __init__(
        self,
        project: str = None,
        query: str = None,
        store_name: str = None,
    ):
        # This parameter is required.
        self.project = project
        self.query = query
        # This parameter is required.
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project
        if self.query is not None:
            result['query'] = self.query
        if self.store_name is not None:
            result['storeName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('storeName') is not None:
            self.store_name = m.get('storeName')
        return self


class Ticket(TeaModel):
    def __init__(
        self,
        caller_uid: int = None,
        create_date: str = None,
        expiration_time: int = None,
        expire_date: str = None,
        extra: str = None,
        name: str = None,
        number: int = None,
        sharing_to: str = None,
        ticket: str = None,
        ticket_id: str = None,
        used_number: int = None,
        valid: bool = None,
    ):
        self.caller_uid = caller_uid
        self.create_date = create_date
        self.expiration_time = expiration_time
        self.expire_date = expire_date
        self.extra = extra
        self.name = name
        self.number = number
        self.sharing_to = sharing_to
        self.ticket = ticket
        self.ticket_id = ticket_id
        self.used_number = used_number
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        if self.create_date is not None:
            result['createDate'] = self.create_date
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date
        if self.extra is not None:
            result['extra'] = self.extra
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.sharing_to is not None:
            result['sharingTo'] = self.sharing_to
        if self.ticket is not None:
            result['ticket'] = self.ticket
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        if self.used_number is not None:
            result['usedNumber'] = self.used_number
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('sharingTo') is not None:
            self.sharing_to = m.get('sharingTo')
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        if m.get('usedNumber') is not None:
            self.used_number = m.get('usedNumber')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class Chart(TeaModel):
    def __init__(
        self,
        action: Dict[str, Any] = None,
        display: Dict[str, Any] = None,
        search: Dict[str, Any] = None,
        title: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.display = display
        # This parameter is required.
        self.search = search
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.display is not None:
            result['display'] = self.display
        if self.search is not None:
            result['search'] = self.search
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Dashboard(TeaModel):
    def __init__(
        self,
        attribute: Dict[str, str] = None,
        charts: List[Chart] = None,
        dashboard_name: str = None,
        description: str = None,
        display_name: str = None,
    ):
        self.attribute = attribute
        # This parameter is required.
        self.charts = charts
        # This parameter is required.
        self.dashboard_name = dashboard_name
        self.description = description
        # This parameter is required.
        self.display_name = display_name

    def validate(self):
        if self.charts:
            for k in self.charts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute
        result['charts'] = []
        if self.charts is not None:
            for k in self.charts:
                result['charts'].append(k.to_map() if k else None)
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        self.charts = []
        if m.get('charts') is not None:
            for k in m.get('charts'):
                temp_model = Chart()
                self.charts.append(temp_model.from_map(k))
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ExternalStore(TeaModel):
    def __init__(
        self,
        external_store_name: str = None,
        parameter: Dict[str, Any] = None,
        store_type: str = None,
    ):
        # This parameter is required.
        self.external_store_name = external_store_name
        # This parameter is required.
        self.parameter = parameter
        # This parameter is required.
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class IndexLine(TeaModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        chn: bool = None,
        exclude_keys: List[str] = None,
        include_keys: List[str] = None,
        token: List[str] = None,
    ):
        self.case_sensitive = case_sensitive
        self.chn = chn
        self.exclude_keys = exclude_keys
        self.include_keys = include_keys
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys
        if self.include_keys is not None:
            result['include_keys'] = self.include_keys
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')
        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class Index(TeaModel):
    def __init__(
        self,
        keys: Dict[str, IndexKey] = None,
        line: IndexLine = None,
        log_reduce: bool = None,
        log_reduce_black_list: List[str] = None,
        log_reduce_white_list: List[str] = None,
        max_text_len: int = None,
    ):
        self.keys = keys
        self.line = line
        self.log_reduce = log_reduce
        self.log_reduce_black_list = log_reduce_black_list
        self.log_reduce_white_list = log_reduce_white_list
        self.max_text_len = max_text_len

    def validate(self):
        if self.keys:
            for v in self.keys.values():
                if v:
                    v.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['keys'] = {}
        if self.keys is not None:
            for k, v in self.keys.items():
                result['keys'][k] = v.to_map()
        if self.line is not None:
            result['line'] = self.line.to_map()
        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce
        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list
        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list
        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.keys = {}
        if m.get('keys') is not None:
            for k, v in m.get('keys').items():
                temp_model = IndexKey()
                self.keys[k] = temp_model.from_map(v)
        if m.get('line') is not None:
            temp_model = IndexLine()
            self.line = temp_model.from_map(m['line'])
        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')
        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')
        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')
        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')
        return self


class LoggingLoggingDetails(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Logging(TeaModel):
    def __init__(
        self,
        logging_details: List[LoggingLoggingDetails] = None,
        logging_project: str = None,
    ):
        # This parameter is required.
        self.logging_details = logging_details
        # This parameter is required.
        self.logging_project = logging_project

    def validate(self):
        if self.logging_details:
            for k in self.logging_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k in self.logging_details:
                result['loggingDetails'].append(k.to_map() if k else None)
        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k in m.get('loggingDetails'):
                temp_model = LoggingLoggingDetails()
                self.logging_details.append(temp_model.from_map(k))
        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')
        return self


class Logstore(TeaModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        create_time: int = None,
        enable_tracking: bool = None,
        encrypt_conf: EncryptConf = None,
        hot_ttl: int = None,
        infrequent_access_ttl: int = None,
        last_modify_time: int = None,
        logstore_name: str = None,
        max_split_shard: int = None,
        mode: str = None,
        processor_id: str = None,
        product_type: str = None,
        shard_count: int = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        self.append_meta = append_meta
        self.auto_split = auto_split
        self.create_time = create_time
        self.enable_tracking = enable_tracking
        self.encrypt_conf = encrypt_conf
        self.hot_ttl = hot_ttl
        self.infrequent_access_ttl = infrequent_access_ttl
        self.last_modify_time = last_modify_time
        # This parameter is required.
        self.logstore_name = logstore_name
        self.max_split_shard = max_split_shard
        self.mode = mode
        self.processor_id = processor_id
        self.product_type = product_type
        # This parameter is required.
        self.shard_count = shard_count
        self.telemetry_type = telemetry_type
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.processor_id is not None:
            result['processorId'] = self.processor_id
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class Machine(TeaModel):
    def __init__(
        self,
        ip: str = None,
        last_heartbeat_time: int = None,
        machine_uniqueid: str = None,
        userdefined_id: str = None,
    ):
        self.ip = ip
        self.last_heartbeat_time = last_heartbeat_time
        self.machine_uniqueid = machine_uniqueid
        self.userdefined_id = userdefined_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.last_heartbeat_time is not None:
            result['lastHeartbeatTime'] = self.last_heartbeat_time
        if self.machine_uniqueid is not None:
            result['machine-uniqueid'] = self.machine_uniqueid
        if self.userdefined_id is not None:
            result['userdefined-id'] = self.userdefined_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('lastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('lastHeartbeatTime')
        if m.get('machine-uniqueid') is not None:
            self.machine_uniqueid = m.get('machine-uniqueid')
        if m.get('userdefined-id') is not None:
            self.userdefined_id = m.get('userdefined-id')
        return self


class MachineGroupGroupAttribute(TeaModel):
    def __init__(
        self,
        external_name: str = None,
        group_topic: str = None,
    ):
        self.external_name = external_name
        self.group_topic = group_topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')
        return self


class MachineGroup(TeaModel):
    def __init__(
        self,
        group_attribute: MachineGroupGroupAttribute = None,
        group_name: str = None,
        group_type: str = None,
        machine_identify_type: str = None,
        machine_list: List[str] = None,
    ):
        self.group_attribute = group_attribute
        # This parameter is required.
        self.group_name = group_name
        self.group_type = group_type
        # This parameter is required.
        self.machine_identify_type = machine_identify_type
        # This parameter is required.
        self.machine_list = machine_list

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type
        if self.machine_list is not None:
            result['machineList'] = self.machine_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = MachineGroupGroupAttribute()
            self.group_attribute = temp_model.from_map(m['groupAttribute'])
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')
        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')
        return self


class Project(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_redundancy_type: str = None,
        description: str = None,
        last_modify_time: str = None,
        owner: str = None,
        project_name: str = None,
        quota: Dict[str, Any] = None,
        region: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.data_redundancy_type = data_redundancy_type
        # This parameter is required.
        self.description = description
        self.last_modify_time = last_modify_time
        self.owner = owner
        # This parameter is required.
        self.project_name = project_name
        self.quota = quota
        self.region = region
        self.resource_group_id = resource_group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_redundancy_type is not None:
            result['dataRedundancyType'] = self.data_redundancy_type
        if self.description is not None:
            result['description'] = self.description
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.owner is not None:
            result['owner'] = self.owner
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.quota is not None:
            result['quota'] = self.quota
        if self.region is not None:
            result['region'] = self.region
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataRedundancyType') is not None:
            self.data_redundancy_type = m.get('dataRedundancyType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ServiceStatus(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        status: str = None,
    ):
        self.enabled = enabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class Shard(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        exclusive_end_key: str = None,
        inclusive_begin_key: str = None,
        shard_id: int = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.exclusive_end_key = exclusive_end_key
        self.inclusive_begin_key = inclusive_begin_key
        self.shard_id = shard_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.exclusive_end_key is not None:
            result['exclusiveEndKey'] = self.exclusive_end_key
        if self.inclusive_begin_key is not None:
            result['inclusiveBeginKey'] = self.inclusive_begin_key
        if self.shard_id is not None:
            result['shardID'] = self.shard_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('exclusiveEndKey') is not None:
            self.exclusive_end_key = m.get('exclusiveEndKey')
        if m.get('inclusiveBeginKey') is not None:
            self.inclusive_begin_key = m.get('inclusiveBeginKey')
        if m.get('shardID') is not None:
            self.shard_id = m.get('shardID')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ApplyConfigToMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Only PROJECT is supported. Set the value to PROJECT.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ConsumerGroupHeartBeatRequest(TeaModel):
    def __init__(
        self,
        body: List[int] = None,
        consumer: str = None,
    ):
        # The IDs of shards whose data is being consumed.
        # 
        # This parameter is required.
        self.body = body
        # The consumer.
        # 
        # This parameter is required.
        self.consumer = consumer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.consumer is not None:
            result['consumer'] = self.consumer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')
        return self


class ConsumerGroupHeartBeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[int] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ConsumerGroupUpdateCheckPointRequest(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        shard: int = None,
        consumer: str = None,
        force_success: bool = None,
    ):
        # The value of the checkpoint.
        # 
        # This parameter is required.
        self.checkpoint = checkpoint
        # The ID of the shard.
        # 
        # This parameter is required.
        self.shard = shard
        # The consumer.
        # 
        # This parameter is required.
        self.consumer = consumer
        # Specifies whether to enable forceful updates. Valid values:
        # 
        # *   true
        # *   false
        self.force_success = force_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint
        if self.shard is not None:
            result['shard'] = self.shard
        if self.consumer is not None:
            result['consumer'] = self.consumer
        if self.force_success is not None:
            result['forceSuccess'] = self.force_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')
        if m.get('forceSuccess') is not None:
            self.force_success = m.get('forceSuccess')
        return self


class ConsumerGroupUpdateCheckPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateAlertRequest(TeaModel):
    def __init__(
        self,
        configuration: AlertConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        schedule: Schedule = None,
    ):
        # The detailed configurations of the alert rule.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the alert rule.
        self.description = description
        # The display name of the alert rule.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The name of the alert rule. Make sure that the name is unique in a project.
        # 
        # This parameter is required.
        self.name = name
        # The scheduling configurations of the alert rule.
        # 
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = AlertConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        return self


class CreateAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateAnnotationDataSetRequest(TeaModel):
    def __init__(
        self,
        body: MLDataSetParam = None,
        dataset_id: str = None,
    ):
        # The data structure of the request.
        self.body = body
        # The unique identifier of the dataset.
        self.dataset_id = dataset_id

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLDataSetParam()
            self.body = temp_model.from_map(m['body'])
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        return self


class CreateAnnotationDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateAnnotationLabelRequest(TeaModel):
    def __init__(
        self,
        body: MLLabelParam = None,
    ):
        # The data structure of the request.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLLabelParam()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAnnotationLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateConfigRequest(TeaModel):
    def __init__(
        self,
        body: LogtailConfig = None,
    ):
        # The body of the request.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = LogtailConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        order: bool = None,
        timeout: int = None,
    ):
        # The name of the consumer group. The name must be unique in a project.
        # 
        # This parameter is required.
        self.consumer_group = consumer_group
        # Specifies whether to consume data in sequence. Valid values:
        # 
        # *   true
        # 
        #     *   In a shard, data is consumed in ascending order based on the value of the \\*\\*__tag__:__receive_time__\\*\\* field.
        #     *   If a shard is split, data in the original shard is consumed first. Then, data in the new shards is consumed at the same time.
        #     *   If shards are merged, data in the original shards is consumed first. Then, data in the new shard is consumed.
        # 
        # *   false Data in all shards is consumed at the same time. If a new shard is generated after a shard is split or after shards are merged, data in the new shard is immediately consumed.
        # 
        # This parameter is required.
        self.order = order
        # The timeout period. If the server does not receive heartbeats from a consumer within the timeout period, the server deletes the consumer. Unit: seconds.
        # 
        # This parameter is required.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['consumerGroup'] = self.consumer_group
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroup') is not None:
            self.consumer_group = m.get('consumerGroup')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateDashboardRequest(TeaModel):
    def __init__(
        self,
        body: Dashboard = None,
    ):
        # The data structure of the dashboard.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Dashboard()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateDownloadJobRequestConfigurationSink(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        compression_type: str = None,
        content_type: str = None,
        prefix: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # 对象存储桶
        self.bucket = bucket
        # 压缩格式
        # 
        # This parameter is required.
        self.compression_type = compression_type
        # 下载文件格式
        # 
        # This parameter is required.
        self.content_type = content_type
        self.prefix = prefix
        # 下载使用roleArn
        self.role_arn = role_arn
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.compression_type is not None:
            result['compressionType'] = self.compression_type
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('compressionType') is not None:
            self.compression_type = m.get('compressionType')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDownloadJobRequestConfiguration(TeaModel):
    def __init__(
        self,
        allow_in_complete: bool = None,
        from_time: int = None,
        logstore: str = None,
        power_sql: bool = None,
        query: str = None,
        sink: CreateDownloadJobRequestConfigurationSink = None,
        to_time: int = None,
    ):
        # This parameter is required.
        self.allow_in_complete = allow_in_complete
        # 起点时间戳（精确到秒）
        # 
        # This parameter is required.
        self.from_time = from_time
        # 源logstore
        # 
        # This parameter is required.
        self.logstore = logstore
        # 是否启用powerSql
        self.power_sql = power_sql
        # 查询语句
        # 
        # This parameter is required.
        self.query = query
        # 导出配置
        # 
        # This parameter is required.
        self.sink = sink
        # 结束时间戳（精确到秒）
        # 
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_in_complete is not None:
            result['allowInComplete'] = self.allow_in_complete
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.sink is not None:
            result['sink'] = self.sink.to_map()
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowInComplete') is not None:
            self.allow_in_complete = m.get('allowInComplete')
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sink') is not None:
            temp_model = CreateDownloadJobRequestConfigurationSink()
            self.sink = temp_model.from_map(m['sink'])
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class CreateDownloadJobRequest(TeaModel):
    def __init__(
        self,
        configuration: CreateDownloadJobRequestConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        # 下载配置
        # 
        # This parameter is required.
        self.configuration = configuration
        # 任务描述
        self.description = description
        # 任务显示名称
        # 
        # This parameter is required.
        self.display_name = display_name
        # 代表资源名称的资源属性字段
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = CreateDownloadJobRequestConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateDownloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateETLRequest(TeaModel):
    def __init__(
        self,
        configuration: ETLConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ETLConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateETLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateIndexRequest(TeaModel):
    def __init__(
        self,
        body: Index = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Index()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateLogStoreRequest(TeaModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        enable_tracking: bool = None,
        encrypt_conf: EncryptConf = None,
        hot_ttl: int = None,
        infrequent_access_ttl: int = None,
        logstore_name: str = None,
        max_split_shard: int = None,
        mode: str = None,
        processor_id: str = None,
        shard_count: int = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        # Specifies whether to record the **public IP address** and **log receiving time**. Default value: false. Valid values:
        # 
        # *   true********\
        # *   false********\
        self.append_meta = append_meta
        # Specifies whether to enable automatic sharding. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split
        # Specifies whether to enable the web tracking feature. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking
        # The data structure of the encryption configuration. The following parameters are included: `enable`, `encrypt_type`, and `user_cmk_info`. For more information, see [EncryptConf](https://help.aliyun.com/document_detail/409461.html).
        self.encrypt_conf = encrypt_conf
        # The retention period of data in the hot storage tier of the Logstore. Valid values: 7 to 3000. Unit: days.
        # 
        # After the retention period that is specified for the hot storage tier elapses, the data is moved to the Infrequent Access (IA) storage tier. For more information, see [Enable hot and cold-tiered storage for a Logstore](https://help.aliyun.com/document_detail/308645.html).
        self.hot_ttl = hot_ttl
        # The retention period of data in the IA storage tier of the Logstore. You must set this parameter to at least 30 days. After the data retention period that you specify for the IA storage tier elapses, the data is moved to the Archive storage tier.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The name of the Logstore. The name must meet the following requirements:
        # 
        # *   The name must be unique in a project.
        # *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards into which existing shards can be automatically split. Valid values: 1 to 256.
        # 
        # >  If you set autoSplit to true, you must specify this parameter.
        self.max_split_shard = max_split_shard
        # The type of the Logstore. Simple Log Service provides two types of Logstores: Standard Logstores and Query Logstores. Valid values:
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the amount of data is large, the log retention period is long, or log analysis is not required. If logs are stored for weeks or months, the log retention period is considered long.
        self.mode = mode
        self.processor_id = processor_id
        # The number of shards.
        # 
        # >  You cannot call the CreateLogStore operation to change the number of shards. You can call the SplitShard or MergeShards operation to change the number of shards.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        # The type of the observable data. Valid values:
        # 
        # *   **None** (default): log data
        # *   **Metrics**: metric data
        self.telemetry_type = telemetry_type
        # The retention period of data. Unit: days. Valid values: 1 to 3000. If you set this parameter to 3650, data is permanently stored.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.processor_id is not None:
            result['processorId'] = self.processor_id
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class CreateLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateLoggingRequestLoggingDetails(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        type: str = None,
    ):
        # The name of the Logstore to which service logs of the type are stored.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The type of service logs. Valid values:
        # 
        # *   consumergroup_log: the consumption delay logs of consumer groups.
        # *   logtail_alarm: the alert logs of Logtail.
        # *   operation_log: the operation logs.
        # *   logtail_profile: the collection logs of Logtail.
        # *   metering: the metering logs.
        # *   logtail_status: the status logs of Logtail.
        # *   scheduledsqlalert: the run logs of Scheduled SQL jobs.
        # *   etl_alert: the run logs of data transformation jobs.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateLoggingRequest(TeaModel):
    def __init__(
        self,
        logging_details: List[CreateLoggingRequestLoggingDetails] = None,
        logging_project: str = None,
    ):
        # The configurations of service logs.
        # 
        # This parameter is required.
        self.logging_details = logging_details
        # The name of the project to which service logs are stored.
        # 
        # This parameter is required.
        self.logging_project = logging_project

    def validate(self):
        if self.logging_details:
            for k in self.logging_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k in self.logging_details:
                result['loggingDetails'].append(k.to_map() if k else None)
        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k in m.get('loggingDetails'):
                temp_model = CreateLoggingRequestLoggingDetails()
                self.logging_details.append(temp_model.from_map(k))
        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')
        return self


class CreateLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateLogtailPipelineConfigRequest(TeaModel):
    def __init__(
        self,
        aggregators: List[Dict[str, Any]] = None,
        config_name: str = None,
        flushers: List[Dict[str, Any]] = None,
        global_: Dict[str, Any] = None,
        inputs: List[Dict[str, Any]] = None,
        log_sample: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        # The aggregation plug-ins.
        self.aggregators = aggregators
        # The name of the configuration.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The data output plug-ins.
        # 
        # This parameter is required.
        self.flushers = flushers
        # The global configuration.
        self.global_ = global_
        # The data source plug-ins.
        # 
        # This parameter is required.
        self.inputs = inputs
        # The sample log.
        self.log_sample = log_sample
        # The processing plug-ins.
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.flushers is not None:
            result['flushers'] = self.flushers
        if self.global_ is not None:
            result['global'] = self.global_
        if self.inputs is not None:
            result['inputs'] = self.inputs
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')
        if m.get('global') is not None:
            self.global_ = m.get('global')
        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class CreateLogtailPipelineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateMachineGroupRequestGroupAttribute(TeaModel):
    def __init__(
        self,
        external_name: str = None,
        group_topic: str = None,
    ):
        # The identifier of the external management system on which the machine group depends.
        self.external_name = external_name
        # The log topic of the machine group.
        self.group_topic = group_topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')
        return self


class CreateMachineGroupRequest(TeaModel):
    def __init__(
        self,
        group_attribute: CreateMachineGroupRequestGroupAttribute = None,
        group_name: str = None,
        group_type: str = None,
        machine_identify_type: str = None,
        machine_list: List[str] = None,
    ):
        # The attributes of the machine group.
        self.group_attribute = group_attribute
        # The name of the machine group. The name must meet the following requirements:
        # 
        # *   The name of each machine group in a project must be unique.
        # *   It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   It must start and end with a lowercase letter or a digit.
        # *   It must be 3 to 128 characters in length.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the machine group. The parameter can be left empty.
        self.group_type = group_type
        # The type of the machine group identifier. Valid values:
        # 
        # *   ip: The machine group uses IP addresses as identifiers.
        # *   userdefined: The machine group uses custom identifiers.
        # 
        # This parameter is required.
        self.machine_identify_type = machine_identify_type
        # The identifiers of machine group.
        # 
        # *   If you set machineIdentifyType to ip, enter the IP address of the machine.
        # *   If you set machineIdentifyType to userdefined, enter a custom identifier.
        # 
        # This parameter is required.
        self.machine_list = machine_list

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type
        if self.machine_list is not None:
            result['machineList'] = self.machine_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = CreateMachineGroupRequestGroupAttribute()
            self.group_attribute = temp_model.from_map(m['groupAttribute'])
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')
        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')
        return self


class CreateMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateMetricStoreRequest(TeaModel):
    def __init__(
        self,
        auto_split: bool = None,
        max_split_shard: int = None,
        metric_type: str = None,
        mode: str = None,
        name: str = None,
        shard_count: int = None,
        ttl: int = None,
    ):
        # Specifies whether to enable automatic sharding.
        self.auto_split = auto_split
        # The maximum number of shards into which existing shards can be automatically split. This parameter is valid only when you set the autoSplit parameter to true.
        self.max_split_shard = max_split_shard
        # The type of the metric data. Example: prometheus.
        self.metric_type = metric_type
        # The type of the Metricstore. For example, you can set the parameter to standard to query Standard Metricstores.
        self.mode = mode
        # The name of the Metricstore.
        # 
        # This parameter is required.
        self.name = name
        # The number of shards in the Metricstore.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        # The retention period of the metric data in the Metricstore. Unit: days.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class CreateMetricStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateOSSExportRequest(TeaModel):
    def __init__(
        self,
        configuration: OSSExportConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        # The configuration details of the job.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the job.
        self.description = description
        # The display name of the job.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The unique identifier of the OSS data shipping job.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSExportConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateOSSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateOSSHDFSExportRequest(TeaModel):
    def __init__(
        self,
        configuration: OSSExportConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        # The configuration details of the job.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the job.
        self.description = description
        # The display name of the job.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The unique identifier of the OSS data shipping job.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSExportConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateOSSHDFSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateOSSIngestionRequest(TeaModel):
    def __init__(
        self,
        configuration: OSSIngestionConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        schedule: Schedule = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        self.schedule = schedule

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSIngestionConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        return self


class CreateOSSIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateOssExternalStoreRequestParameterColumns(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the field.
        # 
        # This parameter is required.
        self.name = name
        # The data type of the field.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateOssExternalStoreRequestParameter(TeaModel):
    def __init__(
        self,
        accessid: str = None,
        accesskey: str = None,
        bucket: str = None,
        columns: List[CreateOssExternalStoreRequestParameterColumns] = None,
        endpoint: str = None,
        objects: List[str] = None,
    ):
        # The AccessKey ID.
        # 
        # This parameter is required.
        self.accessid = accessid
        # The AccessKey secret.
        # 
        # This parameter is required.
        self.accesskey = accesskey
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The associated fields.
        # 
        # This parameter is required.
        self.columns = columns
        # The OSS endpoint. For more information, see [Regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The associated OSS objects. Valid values of n: 1 to 100.
        # 
        # This parameter is required.
        self.objects = objects

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['accessid'] = self.accessid
        if self.accesskey is not None:
            result['accesskey'] = self.accesskey
        if self.bucket is not None:
            result['bucket'] = self.bucket
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.objects is not None:
            result['objects'] = self.objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessid') is not None:
            self.accessid = m.get('accessid')
        if m.get('accesskey') is not None:
            self.accesskey = m.get('accesskey')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = CreateOssExternalStoreRequestParameterColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('objects') is not None:
            self.objects = m.get('objects')
        return self


class CreateOssExternalStoreRequest(TeaModel):
    def __init__(
        self,
        external_store_name: str = None,
        parameter: CreateOssExternalStoreRequestParameter = None,
        store_type: str = None,
    ):
        # The name of the external store.
        # 
        # This parameter is required.
        self.external_store_name = external_store_name
        # The parameters of the external store.
        # 
        # This parameter is required.
        self.parameter = parameter
        # The type of the external store. Set the value to oss.
        # 
        # This parameter is required.
        self.store_type = store_type

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = CreateOssExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class CreateOssExternalStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        data_redundancy_type: str = None,
        description: str = None,
        project_name: str = None,
        resource_group_id: str = None,
    ):
        # Data redundancy type
        self.data_redundancy_type = data_redundancy_type
        # The description of the project.
        # 
        # This parameter is required.
        self.description = description
        # The name of the project. The name must be unique in a region. You cannot change the name after you create the project. The name must meet the following requirements:
        # 
        # *   The name must be unique.
        # *   It can contain only lowercase letters, digits, and hyphens (-).
        # *   It must start and end with a lowercase letter or a digit.
        # *   It must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_redundancy_type is not None:
            result['dataRedundancyType'] = self.data_redundancy_type
        if self.description is not None:
            result['description'] = self.description
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataRedundancyType') is not None:
            self.data_redundancy_type = m.get('dataRedundancyType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateRdsExternalStoreRequestParameter(TeaModel):
    def __init__(
        self,
        db: str = None,
        host: str = None,
        instance_id: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        table: str = None,
        username: str = None,
        vpc_id: str = None,
    ):
        # The name of the database in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.db = db
        # The internal or public endpoint of the ApsaraDB RDS for MySQL instance.
        self.host = host
        # The ID of the ApsaraDB RDS for MySQL instance.
        self.instance_id = instance_id
        # The password that is used to log on to the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.password = password
        # The internal or public port of the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.port = port
        # The region where the ApsaraDB RDS for MySQL instance resides. Valid values: cn-qingdao, cn-beijing, and cn-hangzhou.
        # 
        # This parameter is required.
        self.region = region
        # The name of the database table in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.table = table
        # The username that is used to log on to the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.username = username
        # The ID of the VPC to which the ApsaraDB RDS for MySQL instance belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['db'] = self.db
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instance-id'] = self.instance_id
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.region is not None:
            result['region'] = self.region
        if self.table is not None:
            result['table'] = self.table
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpc-id'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instance-id') is not None:
            self.instance_id = m.get('instance-id')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpc-id') is not None:
            self.vpc_id = m.get('vpc-id')
        return self


class CreateRdsExternalStoreRequest(TeaModel):
    def __init__(
        self,
        external_store_name: str = None,
        parameter: CreateRdsExternalStoreRequestParameter = None,
        store_type: str = None,
    ):
        # The name of the external store. The name must be unique in a project and must be different from Logstore names.
        # 
        # This parameter is required.
        self.external_store_name = external_store_name
        # The parameter struct.
        # 
        # This parameter is required.
        self.parameter = parameter
        # The storage type. Set the value to rds-vpc, which indicates an ApsaraDB RDS for MySQL database in a virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.store_type = store_type

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = CreateRdsExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class CreateRdsExternalStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateSavedSearchRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        logstore: str = None,
        savedsearch_name: str = None,
        search_query: str = None,
        topic: str = None,
    ):
        # The display name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The name of the Logstore to which the saved search belongs.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The name of the saved search. The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.savedsearch_name = savedsearch_name
        # The query statement of the saved search. A query statement consists of a search statement and an analytic statement in the `Search statement|Analytic statement` format. For more information, see [Log search overview](https://help.aliyun.com/document_detail/43772.html) and [Log analysis overview](https://help.aliyun.com/document_detail/53608.html).
        # 
        # This parameter is required.
        self.search_query = search_query
        # The topic of the logs.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class CreateSavedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateScheduledSQLRequest(TeaModel):
    def __init__(
        self,
        configuration: ScheduledSQLConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        schedule: Schedule = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ScheduledSQLConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        return self


class CreateScheduledSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateSqlInstanceRequest(TeaModel):
    def __init__(
        self,
        cu: int = None,
        use_as_default: bool = None,
    ):
        # The number of compute units (CUs). When you use the Dedicated SQL feature, CUs are used in parallel.
        # 
        # This parameter is required.
        self.cu = cu
        # Specifies whether to enable the Dedicated SQL feature for the project. If you set this parameter to true, the Dedicated SQL feature is enabled for the specified project and takes effect for all query statements that you execute in the project, including the query statements for alerts and dashboards.
        # 
        # This parameter is required.
        self.use_as_default = use_as_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        if self.use_as_default is not None:
            result['useAsDefault'] = self.use_as_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('useAsDefault') is not None:
            self.use_as_default = m.get('useAsDefault')
        return self


class CreateSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateStoreViewRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        store_type: str = None,
        stores: List[StoreViewStore] = None,
    ):
        # The name of the dataset.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (_).
        # *   The name must start with a lowercase letter.
        # *   The name must be 3 to 62 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The type of the dataset. Valid values: metricstore and logstore.
        # 
        # This parameter is required.
        self.store_type = store_type
        # The Logstores or Metricstores.
        # 
        # This parameter is required.
        self.stores = stores

    def validate(self):
        if self.stores:
            for k in self.stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.store_type is not None:
            result['storeType'] = self.store_type
        result['stores'] = []
        if self.stores is not None:
            for k in self.stores:
                result['stores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        self.stores = []
        if m.get('stores') is not None:
            for k in m.get('stores'):
                temp_model = StoreViewStore()
                self.stores.append(temp_model.from_map(k))
        return self


class CreateStoreViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        access_token_expiration_time: int = None,
        expiration_time: int = None,
    ):
        self.access_token_expiration_time = access_token_expiration_time
        # The validity period of the ticket that is used for logon-free access. Unit: seconds. Default value: 86400. Maximum value: 2592000. The value 86400 specifies one day.
        self.expiration_time = expiration_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_expiration_time is not None:
            result['accessTokenExpirationTime'] = self.access_token_expiration_time
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTokenExpirationTime') is not None:
            self.access_token_expiration_time = m.get('accessTokenExpirationTime')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(
        self,
        ticket: str = None,
    ):
        # The ticket that is used for logon-free access.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAnnotationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAnnotationDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAnnotationLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteCollectionPolicyRequest(TeaModel):
    def __init__(
        self,
        data_code: str = None,
        product_code: str = None,
    ):
        self.data_code = data_code
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class DeleteCollectionPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteDownloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteETLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteExternalStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLogtailPipelineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteMetricStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteOSSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteOSSHDFSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteOSSIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteProjectPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteSavedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteScheduledSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteStoreViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
    ):
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        local_name: str = None,
        region: str = None,
    ):
        self.internet_endpoint = internet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.local_name = local_name
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_endpoint is not None:
            result['internetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['intranetEndpoint'] = self.intranet_endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internetEndpoint') is not None:
            self.internet_endpoint = m.get('internetEndpoint')
        if m.get('intranetEndpoint') is not None:
            self.intranet_endpoint = m.get('intranetEndpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('regions') is not None:
            for k in m.get('regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DisableScheduledSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class EnableAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class EnableScheduledSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Alert = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Alert()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnnotationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MLDataParam = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MLDataParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnnotationDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MLDataSetParam = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MLDataSetParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnnotationLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MLLabelParam = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MLLabelParam()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppliedConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[str] = None,
        count: int = None,
    ):
        # The names of the Logtail configurations.
        self.configs = configs
        # The number of Logtail configurations.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['configs'] = self.configs
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetAppliedConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppliedConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppliedConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppliedMachineGroupsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        machinegroups: List[str] = None,
    ):
        # The number of returned machine groups.
        self.count = count
        # The names of the returned machine groups.
        self.machinegroups = machinegroups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.machinegroups is not None:
            result['machinegroups'] = self.machinegroups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('machinegroups') is not None:
            self.machinegroups = m.get('machinegroups')
        return self


class GetAppliedMachineGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppliedMachineGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAppliedMachineGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCheckPointRequest(TeaModel):
    def __init__(
        self,
        shard: int = None,
    ):
        # The shard ID.
        # 
        # *   If the specified shard does not exist, an empty list is returned.
        # *   If no shard ID is specified, the checkpoints of all shards are returned.
        self.shard = shard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shard is not None:
            result['shard'] = self.shard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        return self


class GetCheckPointResponseBody(TeaModel):
    def __init__(
        self,
        shard: int = None,
        checkpoint: str = None,
        update_time: int = None,
        consumer: str = None,
    ):
        # The shard ID.
        self.shard = shard
        # The value of the checkpoint.
        self.checkpoint = checkpoint
        # The time when the checkpoint was last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time
        # The consumer at the checkpoint.
        self.consumer = consumer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shard is not None:
            result['shard'] = self.shard
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.consumer is not None:
            result['consumer'] = self.consumer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shard') is not None:
            self.shard = m.get('shard')
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('consumer') is not None:
            self.consumer = m.get('consumer')
        return self


class GetCheckPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[GetCheckPointResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GetCheckPointResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetCollectionPolicyRequest(TeaModel):
    def __init__(
        self,
        data_code: str = None,
        product_code: str = None,
    ):
        self.data_code = data_code
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig(TeaModel):
    def __init__(
        self,
        dest_logstore: str = None,
        dest_project: str = None,
        dest_region: str = None,
        dest_ttl: int = None,
    ):
        self.dest_logstore = dest_logstore
        self.dest_project = dest_project
        self.dest_region = dest_region
        self.dest_ttl = dest_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyDataConfig(TeaModel):
    def __init__(
        self,
        data_project: str = None,
        data_region: str = None,
    ):
        self.data_project = data_project
        self.data_region = data_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_project is not None:
            result['dataProject'] = self.data_project
        if self.data_region is not None:
            result['dataRegion'] = self.data_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataProject') is not None:
            self.data_project = m.get('dataProject')
        if m.get('dataRegion') is not None:
            self.data_region = m.get('dataRegion')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        regions: List[str] = None,
        resource_mode: str = None,
        resource_tags: Dict[str, Any] = None,
    ):
        self.instance_ids = instance_ids
        self.regions = regions
        self.resource_mode = resource_mode
        self.resource_tags = resource_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.regions is not None:
            result['regions'] = self.regions
        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode
        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')
        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicyResourceDirectory(TeaModel):
    def __init__(
        self,
        account_group_type: str = None,
        members: List[str] = None,
    ):
        self.account_group_type = account_group_type
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_group_type is not None:
            result['accountGroupType'] = self.account_group_type
        if self.members is not None:
            result['members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountGroupType') is not None:
            self.account_group_type = m.get('accountGroupType')
        if m.get('members') is not None:
            self.members = m.get('members')
        return self


class GetCollectionPolicyResponseBodyCollectionPolicy(TeaModel):
    def __init__(
        self,
        centralize_config: GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig = None,
        centralize_enabled: bool = None,
        data_code: str = None,
        data_config: GetCollectionPolicyResponseBodyCollectionPolicyDataConfig = None,
        enabled: bool = None,
        internal_policy: bool = None,
        policy_config: GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig = None,
        policy_name: str = None,
        policy_uid: str = None,
        product_code: str = None,
        resource_directory: GetCollectionPolicyResponseBodyCollectionPolicyResourceDirectory = None,
    ):
        self.centralize_config = centralize_config
        self.centralize_enabled = centralize_enabled
        self.data_code = data_code
        self.data_config = data_config
        self.enabled = enabled
        self.internal_policy = internal_policy
        self.policy_config = policy_config
        self.policy_name = policy_name
        self.policy_uid = policy_uid
        self.product_code = product_code
        self.resource_directory = resource_directory

    def validate(self):
        if self.centralize_config:
            self.centralize_config.validate()
        if self.data_config:
            self.data_config.validate()
        if self.policy_config:
            self.policy_config.validate()
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()
        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.data_config is not None:
            result['dataConfig'] = self.data_config.to_map()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.internal_policy is not None:
            result['internalPolicy'] = self.internal_policy
        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.policy_uid is not None:
            result['policyUid'] = self.policy_uid
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_directory is not None:
            result['resourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centralizeConfig') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyCentralizeConfig()
            self.centralize_config = temp_model.from_map(m['centralizeConfig'])
        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('dataConfig') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyDataConfig()
            self.data_config = temp_model.from_map(m['dataConfig'])
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('internalPolicy') is not None:
            self.internal_policy = m.get('internalPolicy')
        if m.get('policyConfig') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyPolicyConfig()
            self.policy_config = temp_model.from_map(m['policyConfig'])
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyUid') is not None:
            self.policy_uid = m.get('policyUid')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceDirectory') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['resourceDirectory'])
        return self


class GetCollectionPolicyResponseBody(TeaModel):
    def __init__(
        self,
        collection_policy: GetCollectionPolicyResponseBodyCollectionPolicy = None,
    ):
        self.collection_policy = collection_policy

    def validate(self):
        if self.collection_policy:
            self.collection_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collection_policy is not None:
            result['collectionPolicy'] = self.collection_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectionPolicy') is not None:
            temp_model = GetCollectionPolicyResponseBodyCollectionPolicy()
            self.collection_policy = temp_model.from_map(m['collectionPolicy'])
        return self


class GetCollectionPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCollectionPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCollectionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LogtailConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LogtailConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContextLogsRequest(TeaModel):
    def __init__(
        self,
        back_lines: int = None,
        forward_lines: int = None,
        pack_id: str = None,
        pack_meta: str = None,
    ):
        # The number of logs that you want to obtain and are generated before the generation time of the start log. Valid values: `(0,100]`.
        # 
        # This parameter is required.
        self.back_lines = back_lines
        # The number of logs that you want to obtain and are generated after the generation time of the start log. Valid values: `(0,100]`.
        # 
        # This parameter is required.
        self.forward_lines = forward_lines
        # The unique identifier of the log group to which the start log belongs.
        # 
        # This parameter is required.
        self.pack_id = pack_id
        # The unique context identifier of the start log in the log group.
        # 
        # This parameter is required.
        self.pack_meta = pack_meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_lines is not None:
            result['back_lines'] = self.back_lines
        if self.forward_lines is not None:
            result['forward_lines'] = self.forward_lines
        if self.pack_id is not None:
            result['pack_id'] = self.pack_id
        if self.pack_meta is not None:
            result['pack_meta'] = self.pack_meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('back_lines') is not None:
            self.back_lines = m.get('back_lines')
        if m.get('forward_lines') is not None:
            self.forward_lines = m.get('forward_lines')
        if m.get('pack_id') is not None:
            self.pack_id = m.get('pack_id')
        if m.get('pack_meta') is not None:
            self.pack_meta = m.get('pack_meta')
        return self


class GetContextLogsResponseBody(TeaModel):
    def __init__(
        self,
        back_lines: int = None,
        forward_lines: int = None,
        logs: List[Dict[str, Any]] = None,
        progress: str = None,
        total_lines: int = None,
    ):
        # The number of logs that are generated before the generation time of the start log.
        self.back_lines = back_lines
        # The number of logs that are generated after the generation time of the start log.
        self.forward_lines = forward_lines
        # The logs that are returned.
        self.logs = logs
        # Indicates whether the query and analysis results are complete. Valid values:
        # 
        # *   Complete: The query is successful, and the complete query and analysis results are returned.
        # *   Incomplete: The query is successful, but the query and analysis results are incomplete. To obtain the complete results, you must repeat the request.
        self.progress = progress
        # The total number of logs that are returned. The logs include the start log that is specified in the request.
        self.total_lines = total_lines

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_lines is not None:
            result['back_lines'] = self.back_lines
        if self.forward_lines is not None:
            result['forward_lines'] = self.forward_lines
        if self.logs is not None:
            result['logs'] = self.logs
        if self.progress is not None:
            result['progress'] = self.progress
        if self.total_lines is not None:
            result['total_lines'] = self.total_lines
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('back_lines') is not None:
            self.back_lines = m.get('back_lines')
        if m.get('forward_lines') is not None:
            self.forward_lines = m.get('forward_lines')
        if m.get('logs') is not None:
            self.logs = m.get('logs')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('total_lines') is not None:
            self.total_lines = m.get('total_lines')
        return self


class GetContextLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetContextLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetContextLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCursorRequest(TeaModel):
    def __init__(
        self,
        from_: str = None,
    ):
        # The point in time that you want to use to query a cursor. Set the value to a UNIX timestamp or a string such as `begin` and `end`.
        # 
        # This parameter is required.
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        return self


class GetCursorResponseBody(TeaModel):
    def __init__(
        self,
        cursor: str = None,
    ):
        # The value of the cursor.
        self.cursor = cursor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class GetCursorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCursorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCursorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCursorTimeRequest(TeaModel):
    def __init__(
        self,
        cursor: str = None,
    ):
        # The cursor.
        # 
        # This parameter is required.
        self.cursor = cursor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class GetCursorTimeResponseBody(TeaModel):
    def __init__(
        self,
        cursor_time: str = None,
    ):
        # The server time that is queried based on the cursor. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.cursor_time = cursor_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor_time is not None:
            result['cursor_time'] = self.cursor_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor_time') is not None:
            self.cursor_time = m.get('cursor_time')
        return self


class GetCursorTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCursorTimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCursorTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Dashboard = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Dashboard()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadJobResponseBodyConfigurationSink(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        compression_type: str = None,
        content_type: str = None,
        prefix: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # 对象存储桶
        self.bucket = bucket
        # 压缩格式
        self.compression_type = compression_type
        # 下载文件格式
        self.content_type = content_type
        self.prefix = prefix
        # 下载使用roleArn
        self.role_arn = role_arn
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.compression_type is not None:
            result['compressionType'] = self.compression_type
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('compressionType') is not None:
            self.compression_type = m.get('compressionType')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDownloadJobResponseBodyConfiguration(TeaModel):
    def __init__(
        self,
        allow_in_complete: bool = None,
        from_time: int = None,
        logstore: str = None,
        power_sql: bool = None,
        query: str = None,
        sink: GetDownloadJobResponseBodyConfigurationSink = None,
        to_time: int = None,
    ):
        self.allow_in_complete = allow_in_complete
        # 起点时间戳（精确到秒）
        self.from_time = from_time
        # 源logstore
        self.logstore = logstore
        # 是否启用powerSql
        self.power_sql = power_sql
        # 查询语句
        self.query = query
        # 导出配置
        self.sink = sink
        # 结束时间戳（精确到秒）
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_in_complete is not None:
            result['allowInComplete'] = self.allow_in_complete
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.sink is not None:
            result['sink'] = self.sink.to_map()
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowInComplete') is not None:
            self.allow_in_complete = m.get('allowInComplete')
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sink') is not None:
            temp_model = GetDownloadJobResponseBodyConfigurationSink()
            self.sink = temp_model.from_map(m['sink'])
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class GetDownloadJobResponseBodyExecutionDetails(TeaModel):
    def __init__(
        self,
        check_sum: str = None,
        error_message: str = None,
        execute_time: int = None,
        file_path: str = None,
        file_size: int = None,
        log_count: int = None,
        progress: int = None,
    ):
        self.check_sum = check_sum
        # 下载错误信息
        self.error_message = error_message
        # 下载执行时间
        self.execute_time = execute_time
        # 下载结果链接
        self.file_path = file_path
        # 下载文件大小
        self.file_size = file_size
        # 下载日志条数
        self.log_count = log_count
        # 下载进度
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_sum is not None:
            result['checkSum'] = self.check_sum
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.execute_time is not None:
            result['executeTime'] = self.execute_time
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.log_count is not None:
            result['logCount'] = self.log_count
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkSum') is not None:
            self.check_sum = m.get('checkSum')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('logCount') is not None:
            self.log_count = m.get('logCount')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class GetDownloadJobResponseBody(TeaModel):
    def __init__(
        self,
        configuration: GetDownloadJobResponseBodyConfiguration = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        execution_details: GetDownloadJobResponseBodyExecutionDetails = None,
        name: str = None,
        status: str = None,
    ):
        # 下载配置
        self.configuration = configuration
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 任务描述
        self.description = description
        # 任务显示名称
        self.display_name = display_name
        # 任务执行细节
        self.execution_details = execution_details
        # 代表资源名称的资源属性字段
        self.name = name
        # 代表资源状态的资源属性字段
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.execution_details:
            self.execution_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.execution_details is not None:
            result['executionDetails'] = self.execution_details.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = GetDownloadJobResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('executionDetails') is not None:
            temp_model = GetDownloadJobResponseBodyExecutionDetails()
            self.execution_details = temp_model.from_map(m['executionDetails'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetDownloadJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDownloadJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDownloadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetETLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ETL = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ETL()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExternalStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExternalStore = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExternalStore()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHistogramsRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        query: str = None,
        to: int = None,
        topic: str = None,
    ):
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The search statement. Only search statements are supported. Analytic statements are not supported. For more information about the syntax of search statements, see [Log search overview](https://help.aliyun.com/document_detail/43772.html).
        self.query = query
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The topic of the logs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.query is not None:
            result['query'] = self.query
        if self.to is not None:
            result['to'] = self.to
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class GetHistogramsResponseBody(TeaModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
        count: int = None,
        progress: str = None,
    ):
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.from_ = from_
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned.
        self.to = to
        # The number of logs that are generated within the subinterval.
        self.count = count
        # Indicates whether the query and analysis results in the subinterval is complete. Valid values:
        # 
        # Complete: The query is successful, and the complete query and analysis results are returned.
        # 
        # Incomplete: The query is successful, but the query and analysis results are incomplete. To obtain the complete results, you must repeat the request.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.to is not None:
            result['to'] = self.to
        if self.count is not None:
            result['count'] = self.count
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class GetHistogramsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[GetHistogramsResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GetHistogramsResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetIndexResponseBodyLine(TeaModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        chn: bool = None,
        exclude_keys: List[str] = None,
        include_keys: List[str] = None,
        token: List[str] = None,
    ):
        # Indicates whether case sensitivity is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.case_sensitive = case_sensitive
        # Indicates whether Chinese characters are included. Valid values:
        # 
        # *   true
        # *   false
        self.chn = chn
        # The excluded fields.
        self.exclude_keys = exclude_keys
        # The included fields.
        self.include_keys = include_keys
        # The delimiters.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.chn is not None:
            result['chn'] = self.chn
        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys
        if self.include_keys is not None:
            result['include_keys'] = self.include_keys
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('chn') is not None:
            self.chn = m.get('chn')
        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')
        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetIndexResponseBody(TeaModel):
    def __init__(
        self,
        index_mode: str = None,
        keys: Dict[str, IndexKey] = None,
        last_modify_time: int = None,
        line: GetIndexResponseBodyLine = None,
        log_reduce: bool = None,
        log_reduce_black_list: List[str] = None,
        log_reduce_white_list: List[str] = None,
        max_text_len: int = None,
        storage: str = None,
        ttl: int = None,
    ):
        # The type of the index.
        self.index_mode = index_mode
        # The configurations of field indexes. A field index is in the key-value format in which the key specifies the name of the field and the value specifies the index configuration of the field.
        self.keys = keys
        # The time when the index configurations were last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # The configurations of full-text indexes.
        self.line = line
        # Indicates whether the log clustering feature is enabled.
        self.log_reduce = log_reduce
        # The fields in the blacklist that are used to cluster logs. This parameter is valid only if the log clustering feature is enabled.
        self.log_reduce_black_list = log_reduce_black_list
        # The fields in the whitelist that are used to cluster logs. This parameter is valid only if the log clustering feature is enabled.
        self.log_reduce_white_list = log_reduce_white_list
        # The maximum length of a field value that can be retained. Default value: 2048. Unit: bytes. The default value is equal to 2 KB. You can change the value of the max_text_len parameter. Valid values: 64 to 16384. Unit: bytes.
        self.max_text_len = max_text_len
        # The storage type. The value is fixed as pg.
        self.storage = storage
        # The lifecycle of the index file. Valid values: 7, 30, and 90. Unit: day.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.keys:
            for v in self.keys.values():
                if v:
                    v.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_mode is not None:
            result['index_mode'] = self.index_mode
        result['keys'] = {}
        if self.keys is not None:
            for k, v in self.keys.items():
                result['keys'][k] = v.to_map()
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.line is not None:
            result['line'] = self.line.to_map()
        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce
        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list
        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list
        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len
        if self.storage is not None:
            result['storage'] = self.storage
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index_mode') is not None:
            self.index_mode = m.get('index_mode')
        self.keys = {}
        if m.get('keys') is not None:
            for k, v in m.get('keys').items():
                temp_model = IndexKey()
                self.keys[k] = temp_model.from_map(v)
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('line') is not None:
            temp_model = GetIndexResponseBodyLine()
            self.line = temp_model.from_map(m['line'])
        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')
        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')
        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')
        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class GetIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Logstore = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Logstore()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogStoreMeteringModeResponseBody(TeaModel):
    def __init__(
        self,
        metering_mode: str = None,
    ):
        # The billing mode. Default value: ChargeByFunction. Valid values: ChargeByFunction and ChargeByDataIngest.
        self.metering_mode = metering_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')
        return self


class GetLogStoreMeteringModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogStoreMeteringModeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLogStoreMeteringModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Logging = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Logging()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogsRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        line: int = None,
        offset: int = None,
        power_sql: bool = None,
        query: str = None,
        reverse: bool = None,
        to: int = None,
        topic: str = None,
    ):
        # The beginning of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you specify the same value for the **from** and **to** parameters, the interval is invalid, and an error message is returned.
        # *   The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > To ensure that full data can be queried, specify a query time range that is accurate to the minute. If you also specify a time range in an analytic statement, Simple Log Service uses the time range specified in the analytic statement for query and analysis.
        # 
        # If you want to specify a time range that is accurate to the second in your analytic statement, you must use the from_unixtime or to_unixtime function to convert the time format. For more information about the functions, see [from_unixtime function](https://help.aliyun.com/document_detail/63451.html) and [to_unixtime function](https://help.aliyun.com/document_detail/63451.html). Examples:
        # 
        # *   `* | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1664186624) AND from_unixtime(__time__) < now()`
        # *   `* | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse(\\"2022-10-19 15:46:05\\", \\"%Y-%m-%d %H:%i:%s\\")) AND __time__ < to_unixtime(now())`
        # 
        # This parameter is required.
        self.from_ = from_
        # The maximum number of logs to return for the request. This parameter takes effect only when the query parameter is set to a search statement. Minimum value: 0. Maximum value: 100. Default value: 100. For more information, see [Perform paged queries](https://help.aliyun.com/document_detail/89994.html).
        self.line = line
        # The line from which the query starts. This parameter takes effect only when the query parameter is set to a search statement. Default value: 0. For more information, see [Perform paged queries](https://help.aliyun.com/document_detail/89994.html).
        self.offset = offset
        # Specifies whether to enable the Dedicated SQL feature. For more information, see [Enable Dedicated SQL](https://help.aliyun.com/document_detail/223777.html). Valid values:
        # 
        # *   true: enables the Dedicated SQL feature.
        # *   false (default): enables the Standard SQL feature.
        # 
        # You can use the powerSql or **query** parameter to configure Dedicated SQL.
        self.power_sql = power_sql
        # The search statement or the query statement. For more information, see [Log search overview](https://help.aliyun.com/document_detail/43772.html) and [Log analysis overview](https://help.aliyun.com/document_detail/53608.html). If you add `set session parallel_sql=true;` to the analytic statement in the query parameter, Dedicated SQL is used. For example, you can set the query parameter to `* | set session parallel_sql=true; select count(*) as pv`. For more information about common errors that may occur during log query and analysis, see [How do I resolve common errors that occur when I query and analyze logs?](https://help.aliyun.com/document_detail/61628.html)
        # 
        # > If you specify an analytic statement in the value of the query parameter, the line and offset parameters do not take effect. In this case, we recommend that you set the line and offset parameters to 0 and use the LIMIT clause to limit the number of logs to return on each page. For more information, see [Paged query](https://help.aliyun.com/document_detail/89994.html).
        self.query = query
        # Specifies whether to return logs in reverse chronological order of log timestamps. The log timestamps are accurate to the minute. Valid values:
        # 
        # *   true: returns logs in reverse chronological order of log timestamps.
        # *   false (default): returns logs in chronological order of log timestamps.
        # 
        # > 
        # 
        # *   The reverse parameter takes effect only when the query parameter is set to a search statement. The reverse parameter specifies the method used to sort returned logs.
        # *   If the query parameter is set to a query statement, the reverse parameter does not take effect. The method used to sort returned logs is specified by the ORDER BY clause in the analytic statement. If you use the keyword asc in the ORDER BY clause, the logs are sorted in chronological order. If you use the keyword desc in the ORDER BY clause, the logs are sorted in reverse chronological order. By default, asc is used in the ORDER BY clause.
        self.reverse = reverse
        # The end of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you specify the same value for the **from** and **to** parameters, the interval is invalid, and an error message is returned.
        # *   The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > To ensure that full data can be queried, specify a query time range that is accurate to the minute. If you also specify a time range in an analytic statement, Simple Log Service uses the time range specified in the analytic statement for query and analysis.
        # 
        # If you want to specify a time range that is accurate to the second in your analytic statement, you must use the from_unixtime or to_unixtime function to convert the time format. For more information about the functions, see [from_unixtime function](https://help.aliyun.com/document_detail/63451.html) and [to_unixtime function](https://help.aliyun.com/document_detail/63451.html). Examples:
        # 
        # *   `* | SELECT * FROM log WHERE from_unixtime(__time__) > from_unixtime(1664186624) AND from_unixtime(__time__) < now()`
        # *   `* | SELECT * FROM log WHERE __time__ > to_unixtime(date_parse(\\"2022-10-19 15:46:05\\", \\"%Y-%m-%d %H:%i:%s\\")) AND __time__ < to_unixtime(now())`
        # 
        # This parameter is required.
        self.to = to
        # The topic of the logs. The default value is an empty string. For more information, see [Topic](https://help.aliyun.com/document_detail/48881.html).
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.line is not None:
            result['line'] = self.line
        if self.offset is not None:
            result['offset'] = self.offset
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.reverse is not None:
            result['reverse'] = self.reverse
        if self.to is not None:
            result['to'] = self.to
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('line') is not None:
            self.line = m.get('line')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class GetLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Dict[str, Any]] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetLogsV2Headers(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept_encoding: str = None,
    ):
        self.common_headers = common_headers
        # The compression format.
        # 
        # *   For Java, Python, and Go, only the lz4 and gzip algorithms are supported for decompression.
        # *   For PHP, JavaScript, and C#, only the gzip algorithm is supported for decompression.
        # 
        # This parameter is required.
        self.accept_encoding = accept_encoding

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.accept_encoding is not None:
            result['Accept-Encoding'] = self.accept_encoding
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Accept-Encoding') is not None:
            self.accept_encoding = m.get('Accept-Encoding')
        return self


class GetLogsV2Request(TeaModel):
    def __init__(
        self,
        forward: bool = None,
        from_: int = None,
        highlight: bool = None,
        line: int = None,
        offset: int = None,
        power_sql: bool = None,
        query: str = None,
        reverse: bool = None,
        session: str = None,
        to: int = None,
        topic: str = None,
    ):
        # Specifies whether to page forward or backward for the scan-based query or phrase search.
        self.forward = forward
        # The beginning of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned. The value is a timestamp that follows the UNIX time format. It is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # Specifies whether to highlight the returned result.
        self.highlight = highlight
        # The maximum number of logs to return for the request. This parameter takes effect only when the query parameter is set to a search statement. Valid values: 0 to 100. Default value: 100.
        self.line = line
        # The line from which the query starts. This parameter takes effect only when the query parameter is set to a search statement. Default value: 0.
        self.offset = offset
        # Specifies whether to enable the SQL enhancement feature. By default, the feature is disabled.
        self.power_sql = power_sql
        # The search statement or query statement. For more information, see the "Log search overview" and "Log analysis overview" topics.
        # 
        # If you add set session parallel_sql=true; to the analytic statement in the query parameter, Dedicated SQL is used. Example: \\* | set session parallel_sql=true; select count(\\*) as pv.
        # 
        # Note: If you specify an analytic statement in the query parameter, the line and offset parameters do not take effect in this operation. In this case, we recommend that you set the line and offset parameters to 0 and use the LIMIT clause to specify the number of logs to return on each page. For more information, see the "Perform paged queries" topic.
        self.query = query
        # Specifies whether to return logs in reverse chronological order of log timestamps. The log timestamps are accurate to minutes. Valid values:
        # 
        # true: Logs are returned in reverse chronological order of log timestamps. false (default): Logs are returned in chronological order of log timestamps. Note: The reverse parameter takes effect only when the query parameter is set to a search statement. The reverse parameter specifies the method used to sort returned logs. If the query parameter is set to a query statement, the reverse parameter does not take effect. The method used to sort returned logs is specified by the ORDER BY clause in the analytic statement. If you use the keyword asc in the ORDER BY clause, the logs are sorted in chronological order. If you use the keyword desc in the ORDER BY clause, the logs are sorted in reverse chronological order. By default, asc is used in the ORDER BY clause.
        self.reverse = reverse
        # The parameter that is used to query data.
        self.session = session
        # The end of the time range to query. The value is the log time that is specified when log data is written.
        # 
        # The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the from parameter, but does not include the end time specified by the to parameter. If you specify the same value for the from and to parameters, the interval is invalid, and an error message is returned. The value is a timestamp that follows the UNIX time format. It is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The topic of the logs. Default value: double quotation marks ("").
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward is not None:
            result['forward'] = self.forward
        if self.from_ is not None:
            result['from'] = self.from_
        if self.highlight is not None:
            result['highlight'] = self.highlight
        if self.line is not None:
            result['line'] = self.line
        if self.offset is not None:
            result['offset'] = self.offset
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.reverse is not None:
            result['reverse'] = self.reverse
        if self.session is not None:
            result['session'] = self.session
        if self.to is not None:
            result['to'] = self.to
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forward') is not None:
            self.forward = m.get('forward')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('highlight') is not None:
            self.highlight = m.get('highlight')
        if m.get('line') is not None:
            self.line = m.get('line')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')
        if m.get('session') is not None:
            self.session = m.get('session')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class GetLogsV2ResponseBodyMetaPhraseQueryInfo(TeaModel):
    def __init__(
        self,
        begin_offset: int = None,
        end_offset: int = None,
        end_time: int = None,
        scan_all: bool = None,
    ):
        self.begin_offset = begin_offset
        self.end_offset = end_offset
        self.end_time = end_time
        self.scan_all = scan_all

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_offset is not None:
            result['beginOffset'] = self.begin_offset
        if self.end_offset is not None:
            result['endOffset'] = self.end_offset
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.scan_all is not None:
            result['scanAll'] = self.scan_all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginOffset') is not None:
            self.begin_offset = m.get('beginOffset')
        if m.get('endOffset') is not None:
            self.end_offset = m.get('endOffset')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('scanAll') is not None:
            self.scan_all = m.get('scanAll')
        return self


class GetLogsV2ResponseBodyMeta(TeaModel):
    def __init__(
        self,
        agg_query: str = None,
        column_types: List[str] = None,
        count: int = None,
        cpu_cores: int = None,
        cpu_sec: float = None,
        elapsed_millisecond: int = None,
        has_sql: bool = None,
        highlights: List[List[LogContent]] = None,
        is_accurate: bool = None,
        keys: List[str] = None,
        limited: int = None,
        mode: int = None,
        phrase_query_info: GetLogsV2ResponseBodyMetaPhraseQueryInfo = None,
        processed_bytes: int = None,
        processed_rows: int = None,
        progress: str = None,
        scan_bytes: int = None,
        telementry_type: str = None,
        terms: List[Dict[str, Any]] = None,
        where_query: str = None,
    ):
        # The SQL statement after | in the query statement.
        self.agg_query = agg_query
        self.column_types = column_types
        # The number of rows that are returned.
        self.count = count
        self.cpu_cores = cpu_cores
        self.cpu_sec = cpu_sec
        # The amount of time that is consumed by the request. Unit: milliseconds.
        self.elapsed_millisecond = elapsed_millisecond
        # Indicates whether the query is an SQL query.
        self.has_sql = has_sql
        self.highlights = highlights
        # Indicates whether the returned result is accurate to seconds.
        self.is_accurate = is_accurate
        # All keys in the query result.
        self.keys = keys
        self.limited = limited
        self.mode = mode
        self.phrase_query_info = phrase_query_info
        # The number of logs that are processed in the request.
        self.processed_bytes = processed_bytes
        # The number of rows that are processed in the request.
        self.processed_rows = processed_rows
        # Indicates whether the query result is complete. Valid values:
        # 
        # *   Complete: The query was successful, and the complete result is returned.
        # *   Incomplete: The query was successful, but the query result is incomplete. To obtain the complete result, you must call the operation again.
        self.progress = progress
        self.scan_bytes = scan_bytes
        # The type of observable data.
        self.telementry_type = telementry_type
        # All terms in the query statement.
        self.terms = terms
        # The part before | in the query statement.
        self.where_query = where_query

    def validate(self):
        if self.highlights:
            for k in self.highlights:
                for k1 in k:
                    if k1:
                        k1.validate()
        if self.phrase_query_info:
            self.phrase_query_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_query is not None:
            result['aggQuery'] = self.agg_query
        if self.column_types is not None:
            result['columnTypes'] = self.column_types
        if self.count is not None:
            result['count'] = self.count
        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores
        if self.cpu_sec is not None:
            result['cpuSec'] = self.cpu_sec
        if self.elapsed_millisecond is not None:
            result['elapsedMillisecond'] = self.elapsed_millisecond
        if self.has_sql is not None:
            result['hasSQL'] = self.has_sql
        result['highlights'] = []
        if self.highlights is not None:
            for k in self.highlights:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['highlights'].append(l1)
        if self.is_accurate is not None:
            result['isAccurate'] = self.is_accurate
        if self.keys is not None:
            result['keys'] = self.keys
        if self.limited is not None:
            result['limited'] = self.limited
        if self.mode is not None:
            result['mode'] = self.mode
        if self.phrase_query_info is not None:
            result['phraseQueryInfo'] = self.phrase_query_info.to_map()
        if self.processed_bytes is not None:
            result['processedBytes'] = self.processed_bytes
        if self.processed_rows is not None:
            result['processedRows'] = self.processed_rows
        if self.progress is not None:
            result['progress'] = self.progress
        if self.scan_bytes is not None:
            result['scanBytes'] = self.scan_bytes
        if self.telementry_type is not None:
            result['telementryType'] = self.telementry_type
        if self.terms is not None:
            result['terms'] = self.terms
        if self.where_query is not None:
            result['whereQuery'] = self.where_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggQuery') is not None:
            self.agg_query = m.get('aggQuery')
        if m.get('columnTypes') is not None:
            self.column_types = m.get('columnTypes')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')
        if m.get('cpuSec') is not None:
            self.cpu_sec = m.get('cpuSec')
        if m.get('elapsedMillisecond') is not None:
            self.elapsed_millisecond = m.get('elapsedMillisecond')
        if m.get('hasSQL') is not None:
            self.has_sql = m.get('hasSQL')
        self.highlights = []
        if m.get('highlights') is not None:
            for k in m.get('highlights'):
                l1 = []
                for k1 in k:
                    temp_model = LogContent()
                    l1.append(temp_model.from_map(k1))
                self.highlights.append(l1)
        if m.get('isAccurate') is not None:
            self.is_accurate = m.get('isAccurate')
        if m.get('keys') is not None:
            self.keys = m.get('keys')
        if m.get('limited') is not None:
            self.limited = m.get('limited')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('phraseQueryInfo') is not None:
            temp_model = GetLogsV2ResponseBodyMetaPhraseQueryInfo()
            self.phrase_query_info = temp_model.from_map(m['phraseQueryInfo'])
        if m.get('processedBytes') is not None:
            self.processed_bytes = m.get('processedBytes')
        if m.get('processedRows') is not None:
            self.processed_rows = m.get('processedRows')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('scanBytes') is not None:
            self.scan_bytes = m.get('scanBytes')
        if m.get('telementryType') is not None:
            self.telementry_type = m.get('telementryType')
        if m.get('terms') is not None:
            self.terms = m.get('terms')
        if m.get('whereQuery') is not None:
            self.where_query = m.get('whereQuery')
        return self


class GetLogsV2ResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, str]] = None,
        meta: GetLogsV2ResponseBodyMeta = None,
    ):
        # The returned result.
        self.data = data
        # The metadata of the returned data.
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('meta') is not None:
            temp_model = GetLogsV2ResponseBodyMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class GetLogsV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogsV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLogsV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogtailPipelineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LogtailPipelineConfig = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LogtailPipelineConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMLServiceResultsRequest(TeaModel):
    def __init__(
        self,
        allow_builtin: bool = None,
        body: MLServiceAnalysisParam = None,
        version: str = None,
    ):
        self.allow_builtin = allow_builtin
        self.body = body
        self.version = version

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_builtin is not None:
            result['allowBuiltin'] = self.allow_builtin
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowBuiltin') is not None:
            self.allow_builtin = m.get('allowBuiltin')
        if m.get('body') is not None:
            temp_model = MLServiceAnalysisParam()
            self.body = temp_model.from_map(m['body'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetMLServiceResultsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, str]] = None,
        status: Dict[str, str] = None,
    ):
        self.data = data
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetMLServiceResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMLServiceResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMLServiceResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MachineGroup = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MachineGroup()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetricStoreResponseBody(TeaModel):
    def __init__(
        self,
        auto_split: bool = None,
        create_time: int = None,
        last_modify_time: int = None,
        max_split_shard: int = None,
        metric_type: str = None,
        mode: str = None,
        name: str = None,
        shard_count: int = None,
        ttl: int = None,
    ):
        # Indicates whether the automatic sharding feature is enabled.
        self.auto_split = auto_split
        # The creation time. The value is a UNIX timestamp.
        self.create_time = create_time
        # The last update time. The value is a UNIX timestamp.
        self.last_modify_time = last_modify_time
        # The maximum number of shards into which existing shards can be automatically split.
        self.max_split_shard = max_split_shard
        # The metric type of the Metricstore. Example: prometheus.
        self.metric_type = metric_type
        # The specification type of the Metricstore. Example: standard.
        self.mode = mode
        # The name of the Metricstore.
        self.name = name
        # The number of shards.
        self.shard_count = shard_count
        # The retention period. Unit: days.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class GetMetricStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMetricStoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMetricStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetricStoreMeteringModeResponseBody(TeaModel):
    def __init__(
        self,
        metering_mode: str = None,
    ):
        # The billing mode. Default value: ChargeByFunction. Valid values: ChargeByFunction and ChargeByDataIngest.
        self.metering_mode = metering_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')
        return self


class GetMetricStoreMeteringModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMetricStoreMeteringModeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMetricStoreMeteringModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OSSExport = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OSSExport()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSHDFSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OSSExport = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OSSExport()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OSSIngestion = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OSSIngestion()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Project = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Project()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectLogsRequest(TeaModel):
    def __init__(
        self,
        power_sql: bool = None,
        query: str = None,
    ):
        # Specifies whether to enable the Dedicated SQL feature. For more information, see [Enable Dedicated SQL](https://help.aliyun.com/document_detail/223777.html). Valid values:
        # 
        # *   true
        # *   false (default): enables the Standard SQL feature.
        # 
        # You can use the powerSql or **query** parameter to configure Dedicated SQL.
        self.power_sql = power_sql
        # The standard SQL statement. In this example, the SQL statement queries the number of page views (PVs) from 2022-03-01 10:41:40 to 2022-03-01 10:56:40 in a Logstore whose name is nginx-moni.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class GetProjectLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Dict[str, str]] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetProjectPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetSavedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SavedSearch = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SavedSearch()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduledSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScheduledSQL = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScheduledSQL()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSlsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ServiceStatus = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ServiceStatus()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlInstanceResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        cu: int = None,
        create_time: int = None,
        update_time: int = None,
        use_as_default: bool = None,
    ):
        self.name = name
        self.cu = cu
        self.create_time = create_time
        self.update_time = update_time
        self.use_as_default = use_as_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.cu is not None:
            result['cu'] = self.cu
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.use_as_default is not None:
            result['useAsDefault'] = self.use_as_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('useAsDefault') is not None:
            self.use_as_default = m.get('useAsDefault')
        return self


class GetSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[GetSqlInstanceResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GetSqlInstanceResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetStoreViewResponseBody(TeaModel):
    def __init__(
        self,
        store_type: str = None,
        stores: List[StoreViewStore] = None,
    ):
        # The type of the dataset.
        # 
        # Valid values:
        # 
        # *   metricstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   logstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.store_type = store_type
        # The Logstores or Metricstores.
        self.stores = stores

    def validate(self):
        if self.stores:
            for k in self.stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        result['stores'] = []
        if self.stores is not None:
            for k in self.stores:
                result['stores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        self.stores = []
        if m.get('stores') is not None:
            for k in m.get('stores'):
                temp_model = StoreViewStore()
                self.stores.append(temp_model.from_map(k))
        return self


class GetStoreViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStoreViewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStoreViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoreViewIndexResponseBodyIndexes(TeaModel):
    def __init__(
        self,
        index: Index = None,
        logstore: str = None,
        project: str = None,
    ):
        # The index configurations of the Logstore.
        self.index = index
        # The name of the Logstore.
        self.logstore = logstore
        # The name of the project to which the Logstore belongs.
        self.project = project

    def validate(self):
        if self.index:
            self.index.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index.to_map()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            temp_model = Index()
            self.index = temp_model.from_map(m['index'])
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class GetStoreViewIndexResponseBody(TeaModel):
    def __init__(
        self,
        indexes: List[GetStoreViewIndexResponseBodyIndexes] = None,
    ):
        # The index configurations.
        self.indexes = indexes

    def validate(self):
        if self.indexes:
            for k in self.indexes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexes'] = []
        if self.indexes is not None:
            for k in self.indexes:
                result['indexes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.indexes = []
        if m.get('indexes') is not None:
            for k in m.get('indexes'):
                temp_model = GetStoreViewIndexResponseBodyIndexes()
                self.indexes.append(temp_model.from_map(k))
        return self


class GetStoreViewIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStoreViewIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStoreViewIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAlertsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[Alert] = None,
        total: int = None,
    ):
        # The number of alert rules that are returned.
        self.count = count
        # The alert rules.
        self.results = results
        # The total number of alert rules in the project.
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = Alert()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAlertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlertsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnnotationDataRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        size: int = None,
    ):
        # The line from which the query starts.
        self.offset = offset
        # The number of entries per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAnnotationDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[MLDataParam] = None,
        total: int = None,
    ):
        # The data returned.
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = MLDataParam()
                self.data.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnnotationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnnotationDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnnotationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnnotationDataSetsRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        size: int = None,
    ):
        # The line from which the query starts.
        self.offset = offset
        # The number of entries per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAnnotationDataSetsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[MLDataSetParam] = None,
        total: int = None,
    ):
        # The data returned.
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = MLDataSetParam()
                self.data.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnnotationDataSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnnotationDataSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnnotationDataSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnnotationLabelsRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        size: int = None,
    ):
        # The line from which the query starts.
        self.offset = offset
        # The number of entries per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAnnotationLabelsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[MLLabelParam] = None,
        total: int = None,
    ):
        # The data returned.
        self.data = data
        # The total number of tags that meet the query conditions.
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = MLLabelParam()
                self.data.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAnnotationLabelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnnotationLabelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAnnotationLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectionPoliciesRequest(TeaModel):
    def __init__(
        self,
        central_project: str = None,
        data_code: str = None,
        instance_id: str = None,
        offset: int = None,
        policy_name: str = None,
        product_code: str = None,
        size: int = None,
    ):
        self.central_project = central_project
        self.data_code = data_code
        self.instance_id = instance_id
        self.offset = offset
        self.policy_name = policy_name
        self.product_code = product_code
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.central_project is not None:
            result['centralProject'] = self.central_project
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.offset is not None:
            result['offset'] = self.offset
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centralProject') is not None:
            self.central_project = m.get('centralProject')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListCollectionPoliciesResponseBodyDataCentralizeConfig(TeaModel):
    def __init__(
        self,
        dest_logstore: str = None,
        dest_project: str = None,
        dest_region: str = None,
        dest_ttl: int = None,
    ):
        self.dest_logstore = dest_logstore
        self.dest_project = dest_project
        self.dest_region = dest_region
        # The data retention period for centralized storage. Unit: days.
        self.dest_ttl = dest_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')
        return self


class ListCollectionPoliciesResponseBodyDataDataConfig(TeaModel):
    def __init__(
        self,
        data_project: str = None,
        data_region: str = None,
    ):
        self.data_project = data_project
        self.data_region = data_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_project is not None:
            result['dataProject'] = self.data_project
        if self.data_region is not None:
            result['dataRegion'] = self.data_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataProject') is not None:
            self.data_project = m.get('dataProject')
        if m.get('dataRegion') is not None:
            self.data_region = m.get('dataRegion')
        return self


class ListCollectionPoliciesResponseBodyDataPolicyConfig(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        regions: List[str] = None,
        resource_mode: str = None,
        resource_tags: Dict[str, Any] = None,
    ):
        self.instance_ids = instance_ids
        self.regions = regions
        self.resource_mode = resource_mode
        self.resource_tags = resource_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.regions is not None:
            result['regions'] = self.regions
        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode
        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')
        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')
        return self


class ListCollectionPoliciesResponseBodyDataResourceDirectory(TeaModel):
    def __init__(
        self,
        account_group_type: str = None,
        members: List[str] = None,
    ):
        self.account_group_type = account_group_type
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_group_type is not None:
            result['accountGroupType'] = self.account_group_type
        if self.members is not None:
            result['members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountGroupType') is not None:
            self.account_group_type = m.get('accountGroupType')
        if m.get('members') is not None:
            self.members = m.get('members')
        return self


class ListCollectionPoliciesResponseBodyData(TeaModel):
    def __init__(
        self,
        centralize_config: ListCollectionPoliciesResponseBodyDataCentralizeConfig = None,
        centralize_enabled: bool = None,
        data_code: str = None,
        data_config: ListCollectionPoliciesResponseBodyDataDataConfig = None,
        enabled: bool = None,
        internal_policy: bool = None,
        policy_config: ListCollectionPoliciesResponseBodyDataPolicyConfig = None,
        policy_name: str = None,
        policy_uid: str = None,
        product_code: str = None,
        resource_directory: ListCollectionPoliciesResponseBodyDataResourceDirectory = None,
    ):
        # The configuration for centralized storage.
        self.centralize_config = centralize_config
        self.centralize_enabled = centralize_enabled
        self.data_code = data_code
        self.data_config = data_config
        self.enabled = enabled
        self.internal_policy = internal_policy
        self.policy_config = policy_config
        self.policy_name = policy_name
        self.policy_uid = policy_uid
        self.product_code = product_code
        self.resource_directory = resource_directory

    def validate(self):
        if self.centralize_config:
            self.centralize_config.validate()
        if self.data_config:
            self.data_config.validate()
        if self.policy_config:
            self.policy_config.validate()
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()
        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.data_config is not None:
            result['dataConfig'] = self.data_config.to_map()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.internal_policy is not None:
            result['internalPolicy'] = self.internal_policy
        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.policy_uid is not None:
            result['policyUid'] = self.policy_uid
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_directory is not None:
            result['resourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centralizeConfig') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataCentralizeConfig()
            self.centralize_config = temp_model.from_map(m['centralizeConfig'])
        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('dataConfig') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataDataConfig()
            self.data_config = temp_model.from_map(m['dataConfig'])
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('internalPolicy') is not None:
            self.internal_policy = m.get('internalPolicy')
        if m.get('policyConfig') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataPolicyConfig()
            self.policy_config = temp_model.from_map(m['policyConfig'])
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyUid') is not None:
            self.policy_uid = m.get('policyUid')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceDirectory') is not None:
            temp_model = ListCollectionPoliciesResponseBodyDataResourceDirectory()
            self.resource_directory = temp_model.from_map(m['resourceDirectory'])
        return self


class ListCollectionPoliciesResponseBodyStatisticsPolicySourceList(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_uid: str = None,
    ):
        self.policy_name = policy_name
        self.policy_uid = policy_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.policy_uid is not None:
            result['policyUid'] = self.policy_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyUid') is not None:
            self.policy_uid = m.get('policyUid')
        return self


class ListCollectionPoliciesResponseBodyStatistics(TeaModel):
    def __init__(
        self,
        policy_source_list: List[ListCollectionPoliciesResponseBodyStatisticsPolicySourceList] = None,
        product_code: str = None,
    ):
        self.policy_source_list = policy_source_list
        self.product_code = product_code

    def validate(self):
        if self.policy_source_list:
            for k in self.policy_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['policySourceList'] = []
        if self.policy_source_list is not None:
            for k in self.policy_source_list:
                result['policySourceList'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['productCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_source_list = []
        if m.get('policySourceList') is not None:
            for k in m.get('policySourceList'):
                temp_model = ListCollectionPoliciesResponseBodyStatisticsPolicySourceList()
                self.policy_source_list.append(temp_model.from_map(k))
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        return self


class ListCollectionPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        current_count: int = None,
        data: List[ListCollectionPoliciesResponseBodyData] = None,
        statistics: List[ListCollectionPoliciesResponseBodyStatistics] = None,
        total_count: int = None,
    ):
        self.current_count = current_count
        # The data of the policies that are matched against the query conditions. The data is returned based on paginated results.
        self.data = data
        self.statistics = statistics
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['currentCount'] = self.current_count
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        result['statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['statistics'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentCount') is not None:
            self.current_count = m.get('currentCount')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListCollectionPoliciesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        self.statistics = []
        if m.get('statistics') is not None:
            for k in m.get('statistics'):
                temp_model = ListCollectionPoliciesResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListCollectionPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCollectionPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCollectionPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRequest(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        logstore_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the Logtail configuration, which is used for fuzzy match.
        self.config_name = config_name
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The line from which the query starts. Default value: 0.
        # 
        # This parameter is required.
        self.offset = offset
        # The number of entries per page. Maximum value: 500.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListConfigResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[str] = None,
        count: int = None,
        total: int = None,
    ):
        # The Logtail configurations that are returned on the current page.
        self.configs = configs
        # The number of Logtail configurations that are returned on the current page.
        self.count = count
        # The total number of Logtail configurations that meet the query conditions.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['configs'] = self.configs
        if self.count is not None:
            result['count'] = self.count
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[ConsumerGroup] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ConsumerGroup()
                self.body.append(temp_model.from_map(k))
        return self


class ListDashboardRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        size: int = None,
    ):
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500. Default value: 500.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDashboardResponseBodyDashboardItems(TeaModel):
    def __init__(
        self,
        dashboard_name: str = None,
        display_name: str = None,
    ):
        # The dashboard ID. The ID must be unique in a project. Fuzzy search is supported. For example, if you enter da, all dashboards whose IDs start with da are queried.
        self.dashboard_name = dashboard_name
        # The display name of the dashboard.
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ListDashboardResponseBody(TeaModel):
    def __init__(
        self,
        dashboard_items: List[ListDashboardResponseBodyDashboardItems] = None,
        dashboards: List[str] = None,
    ):
        # The details of the dashboard.
        self.dashboard_items = dashboard_items
        # The queried dashboards. Each dashboard in the array is specified by dashboardName.
        self.dashboards = dashboards

    def validate(self):
        if self.dashboard_items:
            for k in self.dashboard_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dashboardItems'] = []
        if self.dashboard_items is not None:
            for k in self.dashboard_items:
                result['dashboardItems'].append(k.to_map() if k else None)
        if self.dashboards is not None:
            result['dashboards'] = self.dashboards
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboard_items = []
        if m.get('dashboardItems') is not None:
            for k in m.get('dashboardItems'):
                temp_model = ListDashboardResponseBodyDashboardItems()
                self.dashboard_items.append(temp_model.from_map(k))
        if m.get('dashboards') is not None:
            self.dashboards = m.get('dashboards')
        return self


class ListDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDashboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The domain name that is used to match custom domain names. For example, if you set domainName to `example.com`, the matched domain names are `a.example.com` and `b.example.com`.
        self.domain_name = domain_name
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Default value: 500. Maximum value: 500.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        domains: List[str] = None,
        total: int = None,
    ):
        # The number of domain names that are returned on the current page.
        self.count = count
        # The domain names.
        self.domains = domains
        # The total number of domain names that are returned.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.domains is not None:
            result['domains'] = self.domains
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDownloadJobsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListDownloadJobsResponseBodyResultsConfigurationSink(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        compression_type: str = None,
        content_type: str = None,
        prefix: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # 对象存储桶
        self.bucket = bucket
        # 压缩格式
        self.compression_type = compression_type
        # 下载文件格式
        self.content_type = content_type
        self.prefix = prefix
        # 下载使用roleArn
        self.role_arn = role_arn
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.compression_type is not None:
            result['compressionType'] = self.compression_type
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('compressionType') is not None:
            self.compression_type = m.get('compressionType')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDownloadJobsResponseBodyResultsConfiguration(TeaModel):
    def __init__(
        self,
        allow_in_complete: str = None,
        from_time: int = None,
        logstore: str = None,
        power_sql: bool = None,
        query: str = None,
        sink: ListDownloadJobsResponseBodyResultsConfigurationSink = None,
        to_time: int = None,
    ):
        self.allow_in_complete = allow_in_complete
        # 起点时间戳（精确到秒）
        self.from_time = from_time
        # 源logstore
        self.logstore = logstore
        # 是否启用powerSql
        self.power_sql = power_sql
        # 查询语句
        self.query = query
        # 导出配置
        self.sink = sink
        # 结束时间戳（精确到秒）
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_in_complete is not None:
            result['allowInComplete'] = self.allow_in_complete
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.power_sql is not None:
            result['powerSql'] = self.power_sql
        if self.query is not None:
            result['query'] = self.query
        if self.sink is not None:
            result['sink'] = self.sink.to_map()
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowInComplete') is not None:
            self.allow_in_complete = m.get('allowInComplete')
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sink') is not None:
            temp_model = ListDownloadJobsResponseBodyResultsConfigurationSink()
            self.sink = temp_model.from_map(m['sink'])
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class ListDownloadJobsResponseBodyResultsExecutionDetails(TeaModel):
    def __init__(
        self,
        check_sum: str = None,
        error_message: str = None,
        execute_time: int = None,
        file_path: str = None,
        file_size: int = None,
        log_count: int = None,
        progress: int = None,
    ):
        self.check_sum = check_sum
        # 下载错误信息
        self.error_message = error_message
        # 下载执行时间
        self.execute_time = execute_time
        # 下载结果链接
        self.file_path = file_path
        # 下载文件大小
        self.file_size = file_size
        # 下载日志条数
        self.log_count = log_count
        # 下载进度
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_sum is not None:
            result['checkSum'] = self.check_sum
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.execute_time is not None:
            result['executeTime'] = self.execute_time
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.log_count is not None:
            result['logCount'] = self.log_count
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkSum') is not None:
            self.check_sum = m.get('checkSum')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('logCount') is not None:
            self.log_count = m.get('logCount')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class ListDownloadJobsResponseBodyResults(TeaModel):
    def __init__(
        self,
        configuration: ListDownloadJobsResponseBodyResultsConfiguration = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        execution_details: ListDownloadJobsResponseBodyResultsExecutionDetails = None,
        name: str = None,
        status: str = None,
    ):
        # 下载配置
        self.configuration = configuration
        self.create_time = create_time
        # 任务描述
        self.description = description
        # 任务显示名称
        self.display_name = display_name
        # 任务执行细节
        self.execution_details = execution_details
        # 代表资源名称的资源属性字段
        self.name = name
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.execution_details:
            self.execution_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.execution_details is not None:
            result['executionDetails'] = self.execution_details.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ListDownloadJobsResponseBodyResultsConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('executionDetails') is not None:
            temp_model = ListDownloadJobsResponseBodyResultsExecutionDetails()
            self.execution_details = temp_model.from_map(m['executionDetails'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDownloadJobsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[ListDownloadJobsResponseBodyResults] = None,
        total: int = None,
    ):
        self.count = count
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = ListDownloadJobsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDownloadJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDownloadJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDownloadJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListETLsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListETLsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[ETL] = None,
        total: int = None,
    ):
        self.count = count
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = ETL()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListETLsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListETLsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListETLsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogStoresRequest(TeaModel):
    def __init__(
        self,
        logstore_name: str = None,
        mode: str = None,
        offset: int = None,
        size: int = None,
        telemetry_type: str = None,
    ):
        # The name of the Logstore. Fuzzy match is supported. For example, if you enter test, Logstores whose name contains test are returned.
        self.logstore_name = logstore_name
        # The type of the Logstore. Valid values: standard and query.
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the volume of data is large, the log retention period is long, or log analysis is not required. Log retention periods of weeks or months are considered long.
        self.mode = mode
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500. Default value: 500.
        self.size = size
        # The type of the data that you want to query. Valid values:
        # 
        # *   None: logs
        # *   Metrics: metrics
        self.telemetry_type = telemetry_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.mode is not None:
            result['mode'] = self.mode
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        return self


class ListLogStoresResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        logstores: List[str] = None,
        total: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The Logstores that meet the query conditions.
        self.logstores = logstores
        # The number of the Logstores that meet the query conditions.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.logstores is not None:
            result['logstores'] = self.logstores
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('logstores') is not None:
            self.logstores = m.get('logstores')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListLogStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogStoresResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogtailPipelineConfigRequest(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        logstore_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the Logtail pipeline configuration.
        self.config_name = config_name
        # The name of the Logstore.
        self.logstore_name = logstore_name
        # The line from which the query starts.
        self.offset = offset
        # The number of Logtail pipeline configurations per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListLogtailPipelineConfigResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[str] = None,
        count: int = None,
        total: int = None,
    ):
        # The Logtail pipeline configurations that are returned on the current page.
        self.configs = configs
        # The number of Logtail pipeline configurations that are returned on the current page.
        self.count = count
        # The total number of Logtail pipeline configurations in the current project.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['configs'] = self.configs
        if self.count is not None:
            result['count'] = self.count
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configs') is not None:
            self.configs = m.get('configs')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListLogtailPipelineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogtailPipelineConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogtailPipelineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMachineGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the machine group. This parameter is used to filter machine groups. Partial match is supported.
        self.group_name = group_name
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMachineGroupResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        machinegroups: List[str] = None,
        total: int = None,
    ):
        # The number of machine groups that are returned on the current page.
        self.count = count
        # The machine groups that meet the query conditions.
        self.machinegroups = machinegroups
        # The total number of machine groups that meet the query conditions.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.machinegroups is not None:
            result['machinegroups'] = self.machinegroups
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('machinegroups') is not None:
            self.machinegroups = m.get('machinegroups')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMachineGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMachineGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMachinesRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        size: int = None,
    ):
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Default value: 100. Maximum value: 500.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMachinesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        machines: List[Machine] = None,
        total: int = None,
    ):
        # The number of machines that are returned on the current page.
        self.count = count
        # The machines that are returned.
        self.machines = machines
        # The total number of machines.
        self.total = total

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = Machine()
                self.machines.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMachinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMachinesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMachinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMetricStoresRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        name: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The type of the Metricstore. For example, you can set the parameter to standard to query Standard Metricstores.
        self.mode = mode
        # The name of the Metricstore. Fuzzy search is supported. If you do not specify this parameter, all Metricstores are involved.
        self.name = name
        # The start position of the query.
        self.offset = offset
        # The number of entries per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMetricStoresResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        metricstores: List[str] = None,
        total: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The names of the Metricstores.
        self.metricstores = metricstores
        # The total number of queried Metricstores.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.metricstores is not None:
            result['metricstores'] = self.metricstores
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('metricstores') is not None:
            self.metricstores = m.get('metricstores')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMetricStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMetricStoresResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMetricStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOSSExportsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListOSSExportsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[OSSExport] = None,
        total: int = None,
    ):
        self.count = count
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = OSSExport()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListOSSExportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOSSExportsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOSSExportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOSSHDFSExportsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListOSSHDFSExportsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[OSSExport] = None,
        total: int = None,
    ):
        self.count = count
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = OSSExport()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListOSSHDFSExportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOSSHDFSExportsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOSSHDFSExportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOSSIngestionsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListOSSIngestionsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[OSSIngestion] = None,
        total: int = None,
    ):
        # The number of OSS data import jobs that are returned.
        self.count = count
        # The OSS data import jobs.
        self.results = results
        # The total number of OSS data import jobs in the project.
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = OSSIngestion()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListOSSIngestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOSSIngestionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOSSIngestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(
        self,
        fetch_quota: bool = None,
        offset: int = None,
        project_name: str = None,
        resource_group_id: str = None,
        size: int = None,
    ):
        self.fetch_quota = fetch_quota
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The name of the project.
        self.project_name = project_name
        self.resource_group_id = resource_group_id
        # The number of entries per page. Default value: 100. This operation can return up to 500 projects.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_quota is not None:
            result['fetchQuota'] = self.fetch_quota
        if self.offset is not None:
            result['offset'] = self.offset
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fetchQuota') is not None:
            self.fetch_quota = m.get('fetchQuota')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        projects: List[Project] = None,
        total: int = None,
    ):
        # The number of returned projects on the current page.
        self.count = count
        # The projects that meet the query conditions.
        self.projects = projects
        # The total number of projects that meet the query conditions.
        self.total = total

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSavedSearchRequest(TeaModel):
    def __init__(
        self,
        offset: int = None,
        size: int = None,
    ):
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListSavedSearchResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        savedsearch_items: List[SavedSearch] = None,
        total: int = None,
    ):
        # The number of saved searches returned on the current page.
        self.count = count
        # The saved searches.
        self.savedsearch_items = savedsearch_items
        # The total number of saved searches that meet the query conditions.
        self.total = total

    def validate(self):
        if self.savedsearch_items:
            for k in self.savedsearch_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['savedsearchItems'] = []
        if self.savedsearch_items is not None:
            for k in self.savedsearch_items:
                result['savedsearchItems'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.savedsearch_items = []
        if m.get('savedsearchItems') is not None:
            for k in m.get('savedsearchItems'):
                temp_model = SavedSearch()
                self.savedsearch_items.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListSavedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSavedSearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSavedSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledSQLsRequest(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The name of the Logstore.
        self.logstore = logstore
        self.offset = offset
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListScheduledSQLsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        results: List[ScheduledSQL] = None,
        total: int = None,
    ):
        self.count = count
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = ScheduledSQL()
                self.results.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListScheduledSQLsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduledSQLsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScheduledSQLsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Shard] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Shard()
                self.body.append(temp_model.from_map(k))
        return self


class ListStoreViewsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        offset: int = None,
        size: int = None,
        store_type: str = None,
    ):
        # The dataset name that is used for fuzzy match.
        self.name = name
        # The offset of the datasets to return. Default value: 0.
        self.offset = offset
        # The number of datasets to return. Default value: 100.
        self.size = size
        # The type of the datasets to return. By default, datasets are not filtered by type.
        # 
        # Valid values:
        # 
        # *   metricstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   logstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class ListStoreViewsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        storeviews: List[str] = None,
        total: int = None,
    ):
        # The number of returned datasets.
        self.count = count
        # The dataset names.
        self.storeviews = storeviews
        # The total number of datasets in the project.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.storeviews is not None:
            result['storeviews'] = self.storeviews
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('storeviews') is not None:
            self.storeviews = m.get('storeviews')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListStoreViewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStoreViewsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStoreViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that you want to use to filter resources. For example, if you set the key to `"test-key"`, only resources to which the key is added are returned.``
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag that you want to use to filter resources. If you set the value to null, resources are filtered based only on the key of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tags: List[ListTagResourcesRequestTags] = None,
    ):
        # The IDs of the resources whose tags you want to query. You must specify at least one of resourceId and tags.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   project
        # *   logstore
        # *   dashboard
        # *   MachineGroup
        # *   LogtailConfig
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to use to filter resources based on exact match. Each tag is a key-value pair. You must specify at least one of resourceId and tags.
        # 
        # You can enter up to 20 tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        # The IDs of the resources whose tags you want to query. You must specify at least one of resourceId and tags.
        self.resource_id_shrink = resource_id_shrink
        # The type of the resource. Valid values:
        # 
        # *   project
        # *   logstore
        # *   dashboard
        # *   MachineGroup
        # *   LogtailConfig
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to use to filter resources based on exact match. Each tag is a key-value pair. You must specify at least one of resourceId and tags.
        # 
        # You can enter up to 20 tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The returned tags.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['tagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['tagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.tag_resources = []
        if m.get('tagResources') is not None:
            for k in m.get('tagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeShardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Shard] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Shard()
                self.body.append(temp_model.from_map(k))
        return self


class OpenSlsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PullLogsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept_encoding: str = None,
    ):
        self.common_headers = common_headers
        self.accept_encoding = accept_encoding

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.accept_encoding is not None:
            result['Accept-Encoding'] = self.accept_encoding
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Accept-Encoding') is not None:
            self.accept_encoding = m.get('Accept-Encoding')
        return self


class PullLogsRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        cursor: str = None,
        end_cursor: str = None,
        query: str = None,
    ):
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.cursor = cursor
        self.end_cursor = end_cursor
        # The SPL statement that is used to filter data. For more information, see [SPL instructions](https://help.aliyun.com/document_detail/2536530.html).
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.end_cursor is not None:
            result['end_cursor'] = self.end_cursor
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('end_cursor') is not None:
            self.end_cursor = m.get('end_cursor')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class PullLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LogGroupList = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LogGroupList()
            self.body = temp_model.from_map(m['body'])
        return self


class PutAnnotationDataRequest(TeaModel):
    def __init__(
        self,
        annotationdata_id: str = None,
        ml_data_param: MLDataParam = None,
        raw_log: List[Dict[str, str]] = None,
    ):
        # The unique identifier of the data.
        self.annotationdata_id = annotationdata_id
        # The data structure of the request.
        self.ml_data_param = ml_data_param
        # The raw log data.
        self.raw_log = raw_log

    def validate(self):
        if self.ml_data_param:
            self.ml_data_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotationdata_id is not None:
            result['annotationdataId'] = self.annotationdata_id
        if self.ml_data_param is not None:
            result['mlDataParam'] = self.ml_data_param.to_map()
        if self.raw_log is not None:
            result['rawLog'] = self.raw_log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotationdataId') is not None:
            self.annotationdata_id = m.get('annotationdataId')
        if m.get('mlDataParam') is not None:
            temp_model = MLDataParam()
            self.ml_data_param = temp_model.from_map(m['mlDataParam'])
        if m.get('rawLog') is not None:
            self.raw_log = m.get('rawLog')
        return self


class PutAnnotationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutLogsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_log_compresstype: str = None,
    ):
        self.common_headers = common_headers
        # The compression format. lz4 and gzip are supported.
        # 
        # This parameter is required.
        self.x_log_compresstype = x_log_compresstype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_log_compresstype is not None:
            result['x-log-compresstype'] = self.x_log_compresstype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-log-compresstype') is not None:
            self.x_log_compresstype = m.get('x-log-compresstype')
        return self


class PutLogsRequest(TeaModel):
    def __init__(
        self,
        body: LogGroup = None,
    ):
        # The compressed Protobuf data.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = LogGroup()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutProjectPolicyRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The project policy.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PutProjectPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutProjectTransferAccelerationRequest(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # This parameter is required.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class PutProjectTransferAccelerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutWebtrackingRequest(TeaModel):
    def __init__(
        self,
        logs: List[Dict[str, str]] = None,
        source: str = None,
        tags: Dict[str, str] = None,
        topic: str = None,
    ):
        # The logs. Each element is a JSON object that indicates a log.
        # 
        # >  **Note**: The time in a log that is collected by using the web tracking feature is the time at which Simple Log Service receives the log. You do not need to configure the __time__ field for each log. If this field exists, it is overwritten by the time at which Simple Log Service receives the log.
        # 
        # This parameter is required.
        self.logs = logs
        # The source of the logs.
        # 
        # This parameter is required.
        self.source = source
        # The tags of the logs.
        self.tags = tags
        # The topic of the logs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['__logs__'] = self.logs
        if self.source is not None:
            result['__source__'] = self.source
        if self.tags is not None:
            result['__tags__'] = self.tags
        if self.topic is not None:
            result['__topic__'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('__logs__') is not None:
            self.logs = m.get('__logs__')
        if m.get('__source__') is not None:
            self.source = m.get('__source__')
        if m.get('__tags__') is not None:
            self.tags = m.get('__tags__')
        if m.get('__topic__') is not None:
            self.topic = m.get('__topic__')
        return self


class PutWebtrackingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RefreshTokenRequest(TeaModel):
    def __init__(
        self,
        access_token_expiration_time: int = None,
        ticket: str = None,
    ):
        self.access_token_expiration_time = access_token_expiration_time
        # The ticket that is used for logon-free access.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_expiration_time is not None:
            result['accessTokenExpirationTime'] = self.access_token_expiration_time
        if self.ticket is not None:
            result['ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTokenExpirationTime') is not None:
            self.access_token_expiration_time = m.get('accessTokenExpirationTime')
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')
        return self


class RefreshTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
    ):
        self.access_token = access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        return self


class RefreshTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveConfigFromMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SplitShardRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        shard_count: int = None,
    ):
        # The position where the shard is split.
        self.key = key
        # The number of new shards that are generated after splitting.
        self.shard_count = shard_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        return self


class SplitShardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[Shard] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Shard()
                self.body.append(temp_model.from_map(k))
        return self


class StartETLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StartOSSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StartOSSHDFSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StartOSSIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StopETLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StopOSSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StopOSSHDFSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StopOSSIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class TagResourcesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The key must meet the following requirements:
        # 
        # *   The key must be `1 to 128` characters in length.
        # *   The key cannot contain `http://` or `https://`.
        # *   The key cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag. The value must meet the following requirements:
        # 
        # *   The value must be `1 to 128` characters in length.
        # *   The value cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tags: List[TagResourcesRequestTags] = None,
    ):
        # The resource IDs. You can specify only one resource and add tags to the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   project
        # *   logstore
        # *   dashboard
        # *   machinegroup
        # *   logtailconfig
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to add to the resource. You can specify up to 20 tags in each call. Each tag is a key-value pair.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = TagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tags: List[str] = None,
    ):
        # Specifies whether to unbind all tags. Default value: false. Valid values:
        # 
        # *   false: unbinds only the tags that match the value of tags.
        # *   true: unbinds all tags that are bound to the resource.
        self.all = all
        # The resource IDs. Each time you call this operation, you can unbind tags only from a single resource. Therefore, you can enter only one resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   project
        # *   logstore
        # *   dashboard
        # *   machinegroup
        # *   logtailconfig
        self.resource_type = resource_type
        # The tag keys. If you set all to false, only the tags that match the value of this parameter are unbound.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateAlertRequest(TeaModel):
    def __init__(
        self,
        configuration: AlertConfiguration = None,
        description: str = None,
        display_name: str = None,
        schedule: Schedule = None,
    ):
        # The detailed configurations of the alert rule.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the alert rule.
        self.description = description
        # The display name of the alert rule.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The scheduling settings of the alert rule.
        # 
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = AlertConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        return self


class UpdateAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateAnnotationDataSetRequest(TeaModel):
    def __init__(
        self,
        body: MLDataSetParam = None,
    ):
        # The data structure of the request.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLDataSetParam()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnnotationDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateAnnotationLabelRequest(TeaModel):
    def __init__(
        self,
        body: MLLabelParam = None,
    ):
        # The data structure of the request.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MLLabelParam()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnnotationLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateConfigRequest(TeaModel):
    def __init__(
        self,
        body: LogtailConfig = None,
    ):
        # The body of the request.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = LogtailConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        order: bool = None,
        timeout: int = None,
    ):
        # Specifies whether to consume data in sequence. Valid values:
        # 
        # *   true: If a shard is split, the data in the original shard is consumed first. Then, the data in the new shards is consumed at the same time. If shards are merged, the data in the original shards is consumed first. Then, the data in the new shard is consumed.
        # *   false: The data in all shards is consumed at the same time. If a new shard is generated after a shard is split or shards are merged, the data in the new shard is immediately consumed.
        self.order = order
        # The timeout period. If Simple Log Service does not receive heartbeats from a consumer within the timeout period, Simple Log Service deletes the consumer. Unit: seconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateDashboardRequest(TeaModel):
    def __init__(
        self,
        attribute: Dict[str, str] = None,
        charts: List[Chart] = None,
        dashboard_name: str = None,
        description: str = None,
        display_name: str = None,
    ):
        # The attribute values of the dashboard.
        self.attribute = attribute
        # The charts on the dashboard.
        # 
        # This parameter is required.
        self.charts = charts
        # The name of the dashboard.
        # 
        # This parameter is required.
        self.dashboard_name = dashboard_name
        # The description of the dashboard.
        self.description = description
        # The display name of the dashboard.
        # 
        # This parameter is required.
        self.display_name = display_name

    def validate(self):
        if self.charts:
            for k in self.charts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['attribute'] = self.attribute
        result['charts'] = []
        if self.charts is not None:
            for k in self.charts:
                result['charts'].append(k.to_map() if k else None)
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        self.charts = []
        if m.get('charts') is not None:
            for k in m.get('charts'):
                temp_model = Chart()
                self.charts.append(temp_model.from_map(k))
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class UpdateDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateETLRequest(TeaModel):
    def __init__(
        self,
        configuration: ETLConfiguration = None,
        description: str = None,
        display_name: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.display_name = display_name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ETLConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class UpdateETLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateIndexRequest(TeaModel):
    def __init__(
        self,
        body: Index = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Index()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateLogStoreRequest(TeaModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        enable_tracking: bool = None,
        encrypt_conf: EncryptConf = None,
        hot_ttl: int = None,
        infrequent_access_ttl: int = None,
        logstore_name: str = None,
        max_split_shard: int = None,
        mode: str = None,
        shard_count: int = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        # Specifies whether to record public IP addresses. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.append_meta = append_meta
        # Specifies whether to enable automatic sharding. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split
        # Specifies whether to enable the web tracking feature. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking
        # The data structure of the encryption configuration.
        self.encrypt_conf = encrypt_conf
        # The retention period of data in the hot storage tier of the Logstore. Valid values: 7 to 3000. Unit: days. After the retention period that is specified for the hot storage tier elapses, the data is moved to the Infrequent Access (IA) storage tier. For more information, see [Enable hot and cold-tiered storage for a Logstore](https://help.aliyun.com/document_detail/308645.html).
        self.hot_ttl = hot_ttl
        # The retention period of data in the IA storage tier of the Logstore. You must set this parameter to at least 30 days. After the data retention period that you specify for the IA storage tier elapses, the data is moved to the Archive storage tier.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards into which existing shards can be automatically split. Valid values: 1 to 256.
        # 
        # >  If you set autoSplit to true, you must specify maxSplitShard.
        self.max_split_shard = max_split_shard
        # The type of the Logstore. Simple Log Service provides two types of Logstores: Standard Logstores and Query Logstores. Valid values:
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the amount of data is large, the log retention period is long, or log analysis is not required. If logs are stored for weeks or months, the log retention period is considered long.
        self.mode = mode
        # The number of shards.
        # 
        # >  You cannot call the UpdateLogStore operation to change the number of shards. You can call the SplitShard or MergeShards operation to change the number of shards.
        self.shard_count = shard_count
        # The type of the observable data. Valid values:
        # 
        # *   None (default): log data.
        # *   Metrics: metric data.
        self.telemetry_type = telemetry_type
        # The retention period of data. Unit: days. Valid values: 1 to 3650. If you set this parameter to 3650, logs are permanently stored.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking
        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()
        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl
        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl
        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.shard_count is not None:
            result['shardCount'] = self.shard_count
        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')
        if m.get('encrypt_conf') is not None:
            temp_model = EncryptConf()
            self.encrypt_conf = temp_model.from_map(m['encrypt_conf'])
        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')
        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')
        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')
        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class UpdateLogStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateLogStoreEncryptionRequestUserCmkInfo(TeaModel):
    def __init__(
        self,
        key_id: str = None,
        region_id: str = None,
        role_arn: str = None,
    ):
        self.key_id = key_id
        self.region_id = region_id
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['keyId'] = self.key_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        return self


class UpdateLogStoreEncryptionRequest(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        encrypt_type: str = None,
        user_cmk_info: UpdateLogStoreEncryptionRequestUserCmkInfo = None,
    ):
        # This parameter is required.
        self.enable = enable
        self.encrypt_type = encrypt_type
        self.user_cmk_info = user_cmk_info

    def validate(self):
        if self.user_cmk_info:
            self.user_cmk_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.encrypt_type is not None:
            result['encryptType'] = self.encrypt_type
        if self.user_cmk_info is not None:
            result['userCmkInfo'] = self.user_cmk_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('encryptType') is not None:
            self.encrypt_type = m.get('encryptType')
        if m.get('userCmkInfo') is not None:
            temp_model = UpdateLogStoreEncryptionRequestUserCmkInfo()
            self.user_cmk_info = temp_model.from_map(m['userCmkInfo'])
        return self


class UpdateLogStoreEncryptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateLogStoreMeteringModeRequest(TeaModel):
    def __init__(
        self,
        metering_mode: str = None,
    ):
        # The billing mode. Valid values: ChargeByFunction and ChargeByDataIngest. Default value: ChargeByFunction. The value ChargeByFunction specifies the pay-by-feature billing mode. The value ChargeByDataIngest specifies the pay-by-ingested-data billing mode.
        # 
        # This parameter is required.
        self.metering_mode = metering_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')
        return self


class UpdateLogStoreMeteringModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateLoggingRequestLoggingDetails(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        type: str = None,
    ):
        # The name of the Logstore to which you want to save service logs.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The type of service logs. Valid values:
        # 
        # *   consumergroup_log: the consumption delay logs of consumer groups.
        # *   logtail_alarm: the alert logs of Logtail.
        # *   operation_log: the operation logs.
        # *   logtail_profile: the collection logs of Logtail.
        # *   metering: the metering logs.
        # *   logtail_status: the status logs of Logtail.
        # *   scheduledsqlalert: the operational logs of Scheduled SQL jobs.
        # *   etl_alert: the operational logs of data transformation jobs.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateLoggingRequest(TeaModel):
    def __init__(
        self,
        logging_details: List[UpdateLoggingRequestLoggingDetails] = None,
        logging_project: str = None,
    ):
        # The configurations of service logs.
        # 
        # This parameter is required.
        self.logging_details = logging_details
        # The name of the project to which you want to save service logs.
        # 
        # This parameter is required.
        self.logging_project = logging_project

    def validate(self):
        if self.logging_details:
            for k in self.logging_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k in self.logging_details:
                result['loggingDetails'].append(k.to_map() if k else None)
        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k in m.get('loggingDetails'):
                temp_model = UpdateLoggingRequestLoggingDetails()
                self.logging_details.append(temp_model.from_map(k))
        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')
        return self


class UpdateLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateLogtailPipelineConfigRequest(TeaModel):
    def __init__(
        self,
        aggregators: List[Dict[str, Any]] = None,
        config_name: str = None,
        flushers: List[Dict[str, Any]] = None,
        global_: Dict[str, Any] = None,
        inputs: List[Dict[str, Any]] = None,
        log_sample: str = None,
        processors: List[Dict[str, Any]] = None,
    ):
        # The aggregation plug-ins.
        # 
        # >  This parameter takes effect only when extended plug-ins are used. You can use only one aggregation plug-in.
        self.aggregators = aggregators
        # The name of the configuration.
        # 
        # >  The value of this parameter must be the same as the value of configName in the outer layer.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The output plug-ins.
        # 
        # >  You can use only one Simple Log Service output plug-in.
        # 
        # This parameter is required.
        self.flushers = flushers
        # The global settings.
        # 
        # **\
        # 
        # ****\
        self.global_ = global_
        # The input plug-ins.
        # 
        # >  You can configure only one input plug-in.
        # 
        # This parameter is required.
        self.inputs = inputs
        # The sample log. You can specify multiple sample logs.
        self.log_sample = log_sample
        # The processing plug-ins.
        # 
        # >  Logtail supports native plug-ins and extended plug-ins for data processing. For more information, see [Logtail plug-ins overview](https://help.aliyun.com/document_detail/64957.html).
        # 
        # > 
        # 
        # *   You can use native plug-ins only to collect text logs.
        # 
        # *   You cannot add native plug-ins and extended plug-ins at the same time.
        # 
        # *   When you add native plug-ins, take note of the following items:
        # 
        #     *   You must add one of the following Logtail plug-ins for data processing as the first plug-in: Data Parsing (Regex Mode), Data Parsing (Delimiter Mode), Data Parsing (JSON Mode), Data Parsing (NGINX Mode), Data Parsing (Apache Mode), and Data Parsing (IIS Mode).
        #     *   After you add the first plug-in, you can add one Time Parsing plug-in, one Data Filtering plug-in, and multiple Data Masking plug-ins.
        self.processors = processors

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators
        if self.config_name is not None:
            result['configName'] = self.config_name
        if self.flushers is not None:
            result['flushers'] = self.flushers
        if self.global_ is not None:
            result['global'] = self.global_
        if self.inputs is not None:
            result['inputs'] = self.inputs
        if self.log_sample is not None:
            result['logSample'] = self.log_sample
        if self.processors is not None:
            result['processors'] = self.processors
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')
        if m.get('configName') is not None:
            self.config_name = m.get('configName')
        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')
        if m.get('global') is not None:
            self.global_ = m.get('global')
        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')
        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        return self


class UpdateLogtailPipelineConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateMachineGroupRequestGroupAttribute(TeaModel):
    def __init__(
        self,
        external_name: str = None,
        group_topic: str = None,
    ):
        # The identifier of the external management system on which the machine group depends. This parameter is empty by default.
        self.external_name = external_name
        # The topic of the machine group. This parameter is empty by default.
        self.group_topic = group_topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')
        return self


class UpdateMachineGroupRequest(TeaModel):
    def __init__(
        self,
        group_attribute: UpdateMachineGroupRequestGroupAttribute = None,
        group_name: str = None,
        group_type: str = None,
        machine_identify_type: str = None,
        machine_list: List[str] = None,
    ):
        # The attribute of the machine group. This parameter is empty by default.
        self.group_attribute = group_attribute
        # The name of the machine group.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the machine group. Set the value to an empty string.
        self.group_type = group_type
        # The identifier type of the machine group. Valid values:
        # 
        # *   ip: The machine group uses IP addresses as identifiers.
        # *   userdefined: The machine group uses custom identifiers.
        # 
        # This parameter is required.
        self.machine_identify_type = machine_identify_type
        # The identifiers of the machines in the machine group.
        # 
        # *   If you set machineIdentifyType to ip, enter the IP addresses of the machines.
        # *   If you set machineIdentifyType to userdefined, enter a custom identifier.
        # 
        # This parameter is required.
        self.machine_list = machine_list

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type
        if self.machine_list is not None:
            result['machineList'] = self.machine_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = UpdateMachineGroupRequestGroupAttribute()
            self.group_attribute = temp_model.from_map(m['groupAttribute'])
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')
        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')
        return self


class UpdateMachineGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateMachineGroupMachineRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        body: List[str] = None,
    ):
        # The operation on the machine. Valid values: add and delete. A value of add specifies to add the machine to the machine group. A value of delete specifies to remove the machine from the machine group.
        self.action = action
        # The machines to be added or removed.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateMachineGroupMachineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateMetricStoreRequest(TeaModel):
    def __init__(
        self,
        auto_split: bool = None,
        max_split_shard: int = None,
        mode: str = None,
        ttl: int = None,
    ):
        # Specifies whether to enable automatic sharding.
        self.auto_split = auto_split
        # The maximum number of shards into which existing shards can be automatically split. This parameter is valid only when you set the autoSplit parameter to true.
        self.max_split_shard = max_split_shard
        # The type of the Metricstore.
        self.mode = mode
        # The retention period of the metric data. Unit: days.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split
        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard
        if self.mode is not None:
            result['mode'] = self.mode
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')
        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class UpdateMetricStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateMetricStoreMeteringModeRequest(TeaModel):
    def __init__(
        self,
        metering_mode: str = None,
    ):
        # This parameter is required.
        self.metering_mode = metering_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')
        return self


class UpdateMetricStoreMeteringModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateOSSExportRequest(TeaModel):
    def __init__(
        self,
        configuration: OSSExportConfiguration = None,
        description: str = None,
        display_name: str = None,
    ):
        # The configuration details of the job.
        self.configuration = configuration
        # The description of the job.
        self.description = description
        # The display name of the job.
        self.display_name = display_name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSExportConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class UpdateOSSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateOSSHDFSExportRequest(TeaModel):
    def __init__(
        self,
        configuration: OSSExportConfiguration = None,
        description: str = None,
        display_name: str = None,
    ):
        # The configuration details of the job.
        self.configuration = configuration
        # The description of the job.
        self.description = description
        # The display name of the job.
        self.display_name = display_name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSExportConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class UpdateOSSHDFSExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateOSSIngestionRequest(TeaModel):
    def __init__(
        self,
        configuration: OSSIngestionConfiguration = None,
        description: str = None,
        display_name: str = None,
        schedule: Schedule = None,
    ):
        # The configurations of the OSS data import job.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the OSS data import job.
        self.description = description
        # The display name of the OSS data import job.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The scheduling type. By default, you do not need to specify this parameter. If you want to import data at regular intervals, such as importing data every Monday at 08: 00., you can specify a cron expression.
        self.schedule = schedule

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = OSSIngestionConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        return self


class UpdateOSSIngestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateOssExternalStoreRequestParameterColumns(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the field.
        # 
        # This parameter is required.
        self.name = name
        # The type of the field.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateOssExternalStoreRequestParameter(TeaModel):
    def __init__(
        self,
        accessid: str = None,
        accesskey: str = None,
        bucket: str = None,
        columns: List[UpdateOssExternalStoreRequestParameterColumns] = None,
        endpoint: str = None,
        objects: List[str] = None,
    ):
        # The AccessKey ID of your account.
        # 
        # This parameter is required.
        self.accessid = accessid
        # The AccessKey secret of your account.
        # 
        # This parameter is required.
        self.accesskey = accesskey
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The fields that are associated to the external store.
        # 
        # This parameter is required.
        self.columns = columns
        # The Object Storage Service (OSS) endpoint.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The names of the OSS objects that are associated to the external store.
        # 
        # This parameter is required.
        self.objects = objects

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['accessid'] = self.accessid
        if self.accesskey is not None:
            result['accesskey'] = self.accesskey
        if self.bucket is not None:
            result['bucket'] = self.bucket
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.objects is not None:
            result['objects'] = self.objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessid') is not None:
            self.accessid = m.get('accessid')
        if m.get('accesskey') is not None:
            self.accesskey = m.get('accesskey')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = UpdateOssExternalStoreRequestParameterColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('objects') is not None:
            self.objects = m.get('objects')
        return self


class UpdateOssExternalStoreRequest(TeaModel):
    def __init__(
        self,
        external_store_name: str = None,
        parameter: UpdateOssExternalStoreRequestParameter = None,
        store_type: str = None,
    ):
        # The name of the external store.
        # 
        # This parameter is required.
        self.external_store_name = external_store_name
        # The parameters that are configured for the external store.
        # 
        # This parameter is required.
        self.parameter = parameter
        # The type of the external store. Set the value to oss.
        # 
        # This parameter is required.
        self.store_type = store_type

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = UpdateOssExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class UpdateOssExternalStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        # The description of the project. The default value is an empty string.
        # 
        # This parameter is required.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateRdsExternalStoreRequestParameter(TeaModel):
    def __init__(
        self,
        db: str = None,
        host: str = None,
        instance_id: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        table: str = None,
        username: str = None,
        vpc_id: str = None,
    ):
        # The name of the database in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.db = db
        # The internal or public endpoint of the ApsaraDB RDS for MySQL instance.
        self.host = host
        # The ID of the ApsaraDB RDS for MySQL instance.
        self.instance_id = instance_id
        # The password that is used to log on to the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.password = password
        # The internal or public port of the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.port = port
        # The region where the ApsaraDB RDS for MySQL instance resides. Valid values: cn-qingdao, cn-beijing, and cn-hangzhou.
        # 
        # This parameter is required.
        self.region = region
        # The name of the database table in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.table = table
        # The username that is used to log on to the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.username = username
        # The ID of the VPC to which the ApsaraDB RDS for MySQL instance belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['db'] = self.db
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instance-id'] = self.instance_id
        if self.password is not None:
            result['password'] = self.password
        if self.port is not None:
            result['port'] = self.port
        if self.region is not None:
            result['region'] = self.region
        if self.table is not None:
            result['table'] = self.table
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpc-id'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instance-id') is not None:
            self.instance_id = m.get('instance-id')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpc-id') is not None:
            self.vpc_id = m.get('vpc-id')
        return self


class UpdateRdsExternalStoreRequest(TeaModel):
    def __init__(
        self,
        external_store_name: str = None,
        parameter: UpdateRdsExternalStoreRequestParameter = None,
        store_type: str = None,
    ):
        # The name of the external store.
        # 
        # This parameter is required.
        self.external_store_name = external_store_name
        # The parameter struct.
        # 
        # This parameter is required.
        self.parameter = parameter
        # The storage type. Set the value to rds-vpc, which indicates an ApsaraDB RDS for MySQL database in a virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.store_type = store_type

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')
        if m.get('parameter') is not None:
            temp_model = UpdateRdsExternalStoreRequestParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class UpdateRdsExternalStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateSavedSearchRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        logstore: str = None,
        savedsearch_name: str = None,
        search_query: str = None,
        topic: str = None,
    ):
        # The display name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The name of the Logstore to which the saved search belongs.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The name of the saved search. The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.savedsearch_name = savedsearch_name
        # The query statement of the saved search. A query statement consists of a search statement and an analytic statement in the Search statement|Analytic statement format. For more information, see [Log search overview](https://help.aliyun.com/document_detail/43772.html) and [Log analysis overview](https://help.aliyun.com/document_detail/53608.html).
        # 
        # This parameter is required.
        self.search_query = search_query
        # The topic of the logs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class UpdateSavedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateScheduledSQLRequest(TeaModel):
    def __init__(
        self,
        configuration: ScheduledSQLConfiguration = None,
        description: str = None,
        display_name: str = None,
        schedule: Schedule = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.schedule = schedule

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = ScheduledSQLConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['schedule'])
        return self


class UpdateScheduledSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateSqlInstanceRequest(TeaModel):
    def __init__(
        self,
        cu: int = None,
        use_as_default: bool = None,
    ):
        # This parameter is required.
        self.cu = cu
        # This parameter is required.
        self.use_as_default = use_as_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        if self.use_as_default is not None:
            result['useAsDefault'] = self.use_as_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('useAsDefault') is not None:
            self.use_as_default = m.get('useAsDefault')
        return self


class UpdateSqlInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateStoreViewRequest(TeaModel):
    def __init__(
        self,
        store_type: str = None,
        stores: List[StoreViewStore] = None,
    ):
        # The type of the dataset.
        # 
        # Valid values:
        # 
        # *   metricstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   logstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.store_type = store_type
        # The Logstores or Metricstores.
        # 
        # This parameter is required.
        self.stores = stores

    def validate(self):
        if self.stores:
            for k in self.stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_type is not None:
            result['storeType'] = self.store_type
        result['stores'] = []
        if self.stores is not None:
            for k in self.stores:
                result['stores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        self.stores = []
        if m.get('stores') is not None:
            for k in m.get('stores'):
                temp_model = StoreViewStore()
                self.stores.append(temp_model.from_map(k))
        return self


class UpdateStoreViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpsertCollectionPolicyRequestCentralizeConfig(TeaModel):
    def __init__(
        self,
        dest_logstore: str = None,
        dest_project: str = None,
        dest_region: str = None,
        dest_ttl: int = None,
    ):
        self.dest_logstore = dest_logstore
        self.dest_project = dest_project
        self.dest_region = dest_region
        self.dest_ttl = dest_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_logstore is not None:
            result['destLogstore'] = self.dest_logstore
        if self.dest_project is not None:
            result['destProject'] = self.dest_project
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        if self.dest_ttl is not None:
            result['destTTL'] = self.dest_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destLogstore') is not None:
            self.dest_logstore = m.get('destLogstore')
        if m.get('destProject') is not None:
            self.dest_project = m.get('destProject')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        if m.get('destTTL') is not None:
            self.dest_ttl = m.get('destTTL')
        return self


class UpsertCollectionPolicyRequestDataConfig(TeaModel):
    def __init__(
        self,
        data_region: str = None,
    ):
        self.data_region = data_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_region is not None:
            result['dataRegion'] = self.data_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataRegion') is not None:
            self.data_region = m.get('dataRegion')
        return self


class UpsertCollectionPolicyRequestPolicyConfig(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        regions: List[str] = None,
        resource_mode: str = None,
        resource_tags: Dict[str, Any] = None,
    ):
        self.instance_ids = instance_ids
        self.regions = regions
        # This parameter is required.
        self.resource_mode = resource_mode
        self.resource_tags = resource_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.regions is not None:
            result['regions'] = self.regions
        if self.resource_mode is not None:
            result['resourceMode'] = self.resource_mode
        if self.resource_tags is not None:
            result['resourceTags'] = self.resource_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('resourceMode') is not None:
            self.resource_mode = m.get('resourceMode')
        if m.get('resourceTags') is not None:
            self.resource_tags = m.get('resourceTags')
        return self


class UpsertCollectionPolicyRequestResourceDirectory(TeaModel):
    def __init__(
        self,
        account_group_type: str = None,
        members: List[str] = None,
    ):
        self.account_group_type = account_group_type
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_group_type is not None:
            result['accountGroupType'] = self.account_group_type
        if self.members is not None:
            result['members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountGroupType') is not None:
            self.account_group_type = m.get('accountGroupType')
        if m.get('members') is not None:
            self.members = m.get('members')
        return self


class UpsertCollectionPolicyRequest(TeaModel):
    def __init__(
        self,
        centralize_config: UpsertCollectionPolicyRequestCentralizeConfig = None,
        centralize_enabled: bool = None,
        data_code: str = None,
        data_config: UpsertCollectionPolicyRequestDataConfig = None,
        enabled: bool = None,
        policy_config: UpsertCollectionPolicyRequestPolicyConfig = None,
        policy_name: str = None,
        product_code: str = None,
        resource_directory: UpsertCollectionPolicyRequestResourceDirectory = None,
    ):
        self.centralize_config = centralize_config
        self.centralize_enabled = centralize_enabled
        # This parameter is required.
        self.data_code = data_code
        self.data_config = data_config
        # This parameter is required.
        self.enabled = enabled
        # This parameter is required.
        self.policy_config = policy_config
        # This parameter is required.
        self.policy_name = policy_name
        # This parameter is required.
        self.product_code = product_code
        self.resource_directory = resource_directory

    def validate(self):
        if self.centralize_config:
            self.centralize_config.validate()
        if self.data_config:
            self.data_config.validate()
        if self.policy_config:
            self.policy_config.validate()
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centralize_config is not None:
            result['centralizeConfig'] = self.centralize_config.to_map()
        if self.centralize_enabled is not None:
            result['centralizeEnabled'] = self.centralize_enabled
        if self.data_code is not None:
            result['dataCode'] = self.data_code
        if self.data_config is not None:
            result['dataConfig'] = self.data_config.to_map()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.policy_config is not None:
            result['policyConfig'] = self.policy_config.to_map()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.resource_directory is not None:
            result['resourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centralizeConfig') is not None:
            temp_model = UpsertCollectionPolicyRequestCentralizeConfig()
            self.centralize_config = temp_model.from_map(m['centralizeConfig'])
        if m.get('centralizeEnabled') is not None:
            self.centralize_enabled = m.get('centralizeEnabled')
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')
        if m.get('dataConfig') is not None:
            temp_model = UpsertCollectionPolicyRequestDataConfig()
            self.data_config = temp_model.from_map(m['dataConfig'])
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('policyConfig') is not None:
            temp_model = UpsertCollectionPolicyRequestPolicyConfig()
            self.policy_config = temp_model.from_map(m['policyConfig'])
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('resourceDirectory') is not None:
            temp_model = UpsertCollectionPolicyRequestResourceDirectory()
            self.resource_directory = temp_model.from_map(m['resourceDirectory'])
        return self


class UpsertCollectionPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


