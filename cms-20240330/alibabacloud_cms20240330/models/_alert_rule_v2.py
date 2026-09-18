# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleV2(DaraModel):
    def __init__(
        self,
        action_integration_config: main_models.ActionIntegrationConfig = None,
        annotations: Dict[str, str] = None,
        arms_integration_config: main_models.ArmsIntegrationConfig = None,
        biz_source: str = None,
        condition_config: main_models.ConditionConfigUnified = None,
        content_template: str = None,
        created_at: str = None,
        datasource_config: main_models.DatasourceConfigUnified = None,
        datasource_type: str = None,
        display_name: str = None,
        enabled: bool = None,
        labels: Dict[str, str] = None,
        managed_by: str = None,
        notify_config: main_models.NotifyConfigUnified = None,
        notify_strategy_id: str = None,
        observe_resource_config: main_models.ObserveResourceConfig = None,
        observe_resource_global_scope: bool = None,
        observe_resource_list: List[str] = None,
        observe_resource_type: str = None,
        partition_key: str = None,
        query_config: main_models.QueryConfigUnified = None,
        rca_config: main_models.AlertRuleRcaConfig = None,
        region_id: str = None,
        schedule_config: main_models.ScheduleConfigUnified = None,
        severity_levels: str = None,
        status: str = None,
        updated_at: str = None,
        uuid: str = None,
        workspace: str = None,
    ):
        # The action integration configuration.
        self.action_integration_config = action_integration_config
        # The annotations.
        self.annotations = annotations
        # The Application Real-Time Monitoring Service (ARMS) integration configuration.
        self.arms_integration_config = arms_integration_config
        # The business source (read-only, such as managed_service_for_prometheus, umodel, application_insights, cloud_monitoring, or sls).
        self.biz_source = biz_source
        # The detection condition configuration aggregation (Prometheus simple, UModel, APM simple, or APM composite).
        self.condition_config = condition_config
        # The content template.
        self.content_template = content_template
        # The creation time (read-only), in ISO 8601 format.
        self.created_at = created_at
        # The datasource config aggregation (PROMETHEUS, UMODEL, and APM share a single object, with fields selected based on type).
        self.datasource_config = datasource_config
        # The data source type (read-only, derived).
        self.datasource_type = datasource_type
        # The display name.
        self.display_name = display_name
        # Indicates whether the alert rule is enabled.
        self.enabled = enabled
        # The labels.
        self.labels = labels
        # The rule manager (read-only). An empty value indicates a user-created rule. A non-empty value indicates the rule is created and managed by the corresponding cloud service.
        self.managed_by = managed_by
        # The notification configuration aggregation (currently only DIRECT_NOTIFY, corresponding to DirectNotifyConfig).
        self.notify_config = notify_config
        # The notification policy ID (read-only, derived, the first entry in the notification policy list).
        self.notify_strategy_id = notify_strategy_id
        # The observable resource configuration.
        self.observe_resource_config = observe_resource_config
        # **[Deprecated]** Indicates whether the rule takes effect on all resources of this type (read-only, derived). For new integrations, use observeResourceConfig.relationType to check whether the value is ALL for equivalent semantics.
        self.observe_resource_global_scope = observe_resource_global_scope
        # The list of observable resource IDs (read-only, derived).
        self.observe_resource_list = observe_resource_list
        # **[Deprecated]** The observable resource type (read-only, derived). For new integrations, use observeResourceConfig.entityType instead.
        self.observe_resource_type = observe_resource_type
        # The partition key (read-only, maintained by the system for rule routing and sharding).
        self.partition_key = partition_key
        # The query configuration aggregation (PROMETHEUS_SINGLE_QUERY, UMODEL_METRICSET_QUERY, or APM_MULTI_QUERY).
        self.query_config = query_config
        # The Root Cause Analysis (RCA) configuration.
        self.rca_config = rca_config
        # The region ID (aligned with V1 AlertRule.regionId. Priority: regionId in the request body > callerRegionId from the gateway).
        self.region_id = region_id
        # The scheduling configuration aggregation (currently only FIXED is supported).
        self.schedule_config = schedule_config
        # The severity levels covered by this rule, comma-separated (read-only, derived. Same format as the filter.severityLevels query parameter).
        self.severity_levels = severity_levels
        # The alert status (read-only).
        self.status = status
        # The update time (read-only), in ISO 8601 format.
        self.updated_at = updated_at
        # The rule UUID (system-generated, read-only).
        self.uuid = uuid
        # The workspace.
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
        if self.observe_resource_config:
            self.observe_resource_config.validate()
        if self.query_config:
            self.query_config.validate()
        if self.rca_config:
            self.rca_config.validate()
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

        if self.biz_source is not None:
            result['bizSource'] = self.biz_source

        if self.condition_config is not None:
            result['conditionConfig'] = self.condition_config.to_map()

        if self.content_template is not None:
            result['contentTemplate'] = self.content_template

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

        if self.managed_by is not None:
            result['managedBy'] = self.managed_by

        if self.notify_config is not None:
            result['notifyConfig'] = self.notify_config.to_map()

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id

        if self.observe_resource_config is not None:
            result['observeResourceConfig'] = self.observe_resource_config.to_map()

        if self.observe_resource_global_scope is not None:
            result['observeResourceGlobalScope'] = self.observe_resource_global_scope

        if self.observe_resource_list is not None:
            result['observeResourceList'] = self.observe_resource_list

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type

        if self.partition_key is not None:
            result['partitionKey'] = self.partition_key

        if self.query_config is not None:
            result['queryConfig'] = self.query_config.to_map()

        if self.rca_config is not None:
            result['rcaConfig'] = self.rca_config.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.schedule_config is not None:
            result['scheduleConfig'] = self.schedule_config.to_map()

        if self.severity_levels is not None:
            result['severityLevels'] = self.severity_levels

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

        if m.get('bizSource') is not None:
            self.biz_source = m.get('bizSource')

        if m.get('conditionConfig') is not None:
            temp_model = main_models.ConditionConfigUnified()
            self.condition_config = temp_model.from_map(m.get('conditionConfig'))

        if m.get('contentTemplate') is not None:
            self.content_template = m.get('contentTemplate')

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

        if m.get('managedBy') is not None:
            self.managed_by = m.get('managedBy')

        if m.get('notifyConfig') is not None:
            temp_model = main_models.NotifyConfigUnified()
            self.notify_config = temp_model.from_map(m.get('notifyConfig'))

        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')

        if m.get('observeResourceConfig') is not None:
            temp_model = main_models.ObserveResourceConfig()
            self.observe_resource_config = temp_model.from_map(m.get('observeResourceConfig'))

        if m.get('observeResourceGlobalScope') is not None:
            self.observe_resource_global_scope = m.get('observeResourceGlobalScope')

        if m.get('observeResourceList') is not None:
            self.observe_resource_list = m.get('observeResourceList')

        if m.get('observeResourceType') is not None:
            self.observe_resource_type = m.get('observeResourceType')

        if m.get('partitionKey') is not None:
            self.partition_key = m.get('partitionKey')

        if m.get('queryConfig') is not None:
            temp_model = main_models.QueryConfigUnified()
            self.query_config = temp_model.from_map(m.get('queryConfig'))

        if m.get('rcaConfig') is not None:
            temp_model = main_models.AlertRuleRcaConfig()
            self.rca_config = temp_model.from_map(m.get('rcaConfig'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('scheduleConfig') is not None:
            temp_model = main_models.ScheduleConfigUnified()
            self.schedule_config = temp_model.from_map(m.get('scheduleConfig'))

        if m.get('severityLevels') is not None:
            self.severity_levels = m.get('severityLevels')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

