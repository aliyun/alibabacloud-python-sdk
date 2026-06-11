# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleV2(DaraModel):
    def __init__(
        self,
        action_integration_config: main_models.ActionIntegrationConfig = None,
        annotations: Dict[str, str] = None,
        arms_integration_config: main_models.ArmsIntegrationConfig = None,
        condition_config: main_models.ConditionConfigUnified = None,
        content_template: str = None,
        covered_severity_levels: str = None,
        created_at: str = None,
        datasource_config: main_models.DatasourceConfigUnified = None,
        datasource_type: str = None,
        display_name: str = None,
        enabled: bool = None,
        labels: Dict[str, str] = None,
        notify_config: main_models.NotifyConfigUnified = None,
        observe_resource_global_scope: bool = None,
        observe_resource_list: str = None,
        observe_resource_type: str = None,
        query_config: main_models.QueryConfigUnified = None,
        schedule_config: main_models.ScheduleConfigUnified = None,
        status: str = None,
        updated_at: str = None,
        uuid: str = None,
        workspace: str = None,
    ):
        # Configuration for action integrations, such as webhooks, that execute when an alert is triggered.
        self.action_integration_config = action_integration_config
        # A set of key-value pairs that serve as annotations, providing additional, non-identifying information, such as a description or a runbook link.
        self.annotations = annotations
        # The configuration for integrating the alert rule with Application Real-Time Monitoring Service (ARMS).
        self.arms_integration_config = arms_integration_config
        # The configuration for the conditions that trigger an alert.
        self.condition_config = condition_config
        # The template for the alert notification content.
        self.content_template = content_template
        self.covered_severity_levels = covered_severity_levels
        # The time the alert rule was created.
        self.created_at = created_at
        # The configuration for the data source to be evaluated.
        self.datasource_config = datasource_config
        # The data source type. Examples: `sls`, `prometheus`.
        self.datasource_type = datasource_type
        # The user-defined display name for the alert rule.
        self.display_name = display_name
        # Indicates whether the alert rule is active. Set to `true` to enable the rule, or `false` to disable it.
        self.enabled = enabled
        # A set of key-value pairs that serve as labels to filter and group alert rules.
        self.labels = labels
        # The configuration for sending notifications when an alert is triggered.
        self.notify_config = notify_config
        # Indicates whether the alert rule monitors all resources of the specified type. If `true`, the rule applies globally within the workspace.
        self.observe_resource_global_scope = observe_resource_global_scope
        # A list of specific resource IDs to monitor, used only when `observeResourceGlobalScope` is `false`.
        self.observe_resource_list = observe_resource_list
        # The type of resource that the alert rule monitors.
        self.observe_resource_type = observe_resource_type
        # The configuration for querying and processing data from the data source.
        self.query_config = query_config
        # The configuration for how often the alert rule is evaluated.
        self.schedule_config = schedule_config
        # The current status of the alert rule. Examples: `RUNNING`, `STOPPED`.
        self.status = status
        # The time the alert rule was last updated.
        self.updated_at = updated_at
        # The unique identifier for the alert rule.
        self.uuid = uuid
        # The ID of the workspace that contains the alert rule.
        self.workspace = workspace

    def validate(self):
        if self.action_integration_config:
            self.action_integration_config.validate()
        if self.arms_integration_config:
            self.arms_integration_config.validate()
        if self.condition_config:
            self.condition_config.validate()
        if self.datasource_config:
            self.datasource_config.validate()
        if self.notify_config:
            self.notify_config.validate()
        if self.query_config:
            self.query_config.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_integration_config is not None:
            result['actionIntegrationConfig'] = self.action_integration_config.to_map()

        if self.annotations is not None:
            result['annotations'] = self.annotations

        if self.arms_integration_config is not None:
            result['armsIntegrationConfig'] = self.arms_integration_config.to_map()

        if self.condition_config is not None:
            result['conditionConfig'] = self.condition_config.to_map()

        if self.content_template is not None:
            result['contentTemplate'] = self.content_template

        if self.covered_severity_levels is not None:
            result['coveredSeverityLevels'] = self.covered_severity_levels

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.datasource_config is not None:
            result['datasourceConfig'] = self.datasource_config.to_map()

        if self.datasource_type is not None:
            result['datasourceType'] = self.datasource_type

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.labels is not None:
            result['labels'] = self.labels

        if self.notify_config is not None:
            result['notifyConfig'] = self.notify_config.to_map()

        if self.observe_resource_global_scope is not None:
            result['observeResourceGlobalScope'] = self.observe_resource_global_scope

        if self.observe_resource_list is not None:
            result['observeResourceList'] = self.observe_resource_list

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type

        if self.query_config is not None:
            result['queryConfig'] = self.query_config.to_map()

        if self.schedule_config is not None:
            result['scheduleConfig'] = self.schedule_config.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionIntegrationConfig') is not None:
            temp_model = main_models.ActionIntegrationConfig()
            self.action_integration_config = temp_model.from_map(m.get('actionIntegrationConfig'))

        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')

        if m.get('armsIntegrationConfig') is not None:
            temp_model = main_models.ArmsIntegrationConfig()
            self.arms_integration_config = temp_model.from_map(m.get('armsIntegrationConfig'))

        if m.get('conditionConfig') is not None:
            temp_model = main_models.ConditionConfigUnified()
            self.condition_config = temp_model.from_map(m.get('conditionConfig'))

        if m.get('contentTemplate') is not None:
            self.content_template = m.get('contentTemplate')

        if m.get('coveredSeverityLevels') is not None:
            self.covered_severity_levels = m.get('coveredSeverityLevels')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('datasourceConfig') is not None:
            temp_model = main_models.DatasourceConfigUnified()
            self.datasource_config = temp_model.from_map(m.get('datasourceConfig'))

        if m.get('datasourceType') is not None:
            self.datasource_type = m.get('datasourceType')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('notifyConfig') is not None:
            temp_model = main_models.NotifyConfigUnified()
            self.notify_config = temp_model.from_map(m.get('notifyConfig'))

        if m.get('observeResourceGlobalScope') is not None:
            self.observe_resource_global_scope = m.get('observeResourceGlobalScope')

        if m.get('observeResourceList') is not None:
            self.observe_resource_list = m.get('observeResourceList')

        if m.get('observeResourceType') is not None:
            self.observe_resource_type = m.get('observeResourceType')

        if m.get('queryConfig') is not None:
            temp_model = main_models.QueryConfigUnified()
            self.query_config = temp_model.from_map(m.get('queryConfig'))

        if m.get('scheduleConfig') is not None:
            temp_model = main_models.ScheduleConfigUnified()
            self.schedule_config = temp_model.from_map(m.get('scheduleConfig'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

