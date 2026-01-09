# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class AlertConfiguration(DaraModel):
    def __init__(
        self,
        annotations: List[main_models.AlertTag] = None,
        auto_annotation: bool = None,
        condition_configuration: main_models.ConditionConfiguration = None,
        dashboard: str = None,
        group_configuration: main_models.GroupConfiguration = None,
        join_configurations: List[main_models.JoinConfiguration] = None,
        labels: List[main_models.AlertTag] = None,
        mute_until: int = None,
        no_data_fire: bool = None,
        no_data_severity: int = None,
        policy_configuration: main_models.PolicyConfiguration = None,
        query_list: List[main_models.AlertQuery] = None,
        send_resolved: bool = None,
        severity_configurations: List[main_models.SeverityConfiguration] = None,
        sink_alerthub: main_models.SinkAlerthubConfiguration = None,
        sink_cms: main_models.SinkCmsConfiguration = None,
        sink_event_store: main_models.SinkEventStoreConfiguration = None,
        tags: List[str] = None,
        template_configuration: main_models.TemplateConfiguration = None,
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
            for v1 in self.annotations:
                 if v1:
                    v1.validate()
        if self.condition_configuration:
            self.condition_configuration.validate()
        if self.group_configuration:
            self.group_configuration.validate()
        if self.join_configurations:
            for v1 in self.join_configurations:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.policy_configuration:
            self.policy_configuration.validate()
        if self.query_list:
            for v1 in self.query_list:
                 if v1:
                    v1.validate()
        if self.severity_configurations:
            for v1 in self.severity_configurations:
                 if v1:
                    v1.validate()
        if self.sink_alerthub:
            self.sink_alerthub.validate()
        if self.sink_cms:
            self.sink_cms.validate()
        if self.sink_event_store:
            self.sink_event_store.validate()
        if self.template_configuration:
            self.template_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['annotations'].append(k1.to_map() if k1 else None)

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
            for k1 in self.join_configurations:
                result['joinConfigurations'].append(k1.to_map() if k1 else None)

        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

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
            for k1 in self.query_list:
                result['queryList'].append(k1.to_map() if k1 else None)

        if self.send_resolved is not None:
            result['sendResolved'] = self.send_resolved

        result['severityConfigurations'] = []
        if self.severity_configurations is not None:
            for k1 in self.severity_configurations:
                result['severityConfigurations'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('annotations'):
                temp_model = main_models.AlertTag()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('autoAnnotation') is not None:
            self.auto_annotation = m.get('autoAnnotation')

        if m.get('conditionConfiguration') is not None:
            temp_model = main_models.ConditionConfiguration()
            self.condition_configuration = temp_model.from_map(m.get('conditionConfiguration'))

        if m.get('dashboard') is not None:
            self.dashboard = m.get('dashboard')

        if m.get('groupConfiguration') is not None:
            temp_model = main_models.GroupConfiguration()
            self.group_configuration = temp_model.from_map(m.get('groupConfiguration'))

        self.join_configurations = []
        if m.get('joinConfigurations') is not None:
            for k1 in m.get('joinConfigurations'):
                temp_model = main_models.JoinConfiguration()
                self.join_configurations.append(temp_model.from_map(k1))

        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.AlertTag()
                self.labels.append(temp_model.from_map(k1))

        if m.get('muteUntil') is not None:
            self.mute_until = m.get('muteUntil')

        if m.get('noDataFire') is not None:
            self.no_data_fire = m.get('noDataFire')

        if m.get('noDataSeverity') is not None:
            self.no_data_severity = m.get('noDataSeverity')

        if m.get('policyConfiguration') is not None:
            temp_model = main_models.PolicyConfiguration()
            self.policy_configuration = temp_model.from_map(m.get('policyConfiguration'))

        self.query_list = []
        if m.get('queryList') is not None:
            for k1 in m.get('queryList'):
                temp_model = main_models.AlertQuery()
                self.query_list.append(temp_model.from_map(k1))

        if m.get('sendResolved') is not None:
            self.send_resolved = m.get('sendResolved')

        self.severity_configurations = []
        if m.get('severityConfigurations') is not None:
            for k1 in m.get('severityConfigurations'):
                temp_model = main_models.SeverityConfiguration()
                self.severity_configurations.append(temp_model.from_map(k1))

        if m.get('sinkAlerthub') is not None:
            temp_model = main_models.SinkAlerthubConfiguration()
            self.sink_alerthub = temp_model.from_map(m.get('sinkAlerthub'))

        if m.get('sinkCms') is not None:
            temp_model = main_models.SinkCmsConfiguration()
            self.sink_cms = temp_model.from_map(m.get('sinkCms'))

        if m.get('sinkEventStore') is not None:
            temp_model = main_models.SinkEventStoreConfiguration()
            self.sink_event_store = temp_model.from_map(m.get('sinkEventStore'))

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('templateConfiguration') is not None:
            temp_model = main_models.TemplateConfiguration()
            self.template_configuration = temp_model.from_map(m.get('templateConfiguration'))

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

