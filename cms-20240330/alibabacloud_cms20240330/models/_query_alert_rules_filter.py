# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryAlertRulesFilter(DaraModel):
    def __init__(
        self,
        biz_source: main_models.BizSourceFilter = None,
        datasource_type: main_models.DatasourceTypeFilter = None,
        display_name: main_models.DisplayNameFilter = None,
        enabled: main_models.EnabledFilter = None,
        labels: main_models.LabelsFilter = None,
        notification_channels: main_models.NotificationChannelsFilter = None,
        notify_strategy_id: main_models.NotifyStrategyIdFilter = None,
        observe_resource_config: main_models.ObserveResourceConfigFilter = None,
        observe_resource_global_scope: main_models.ObserveResourceGlobalScopeFilter = None,
        observe_resource_instance_id: str = None,
        observe_resource_list: main_models.ObserveResourceListFilter = None,
        observe_resource_type: main_models.ObserveResourceTypeFilter = None,
        partition_key: main_models.PartitionKeyFilter = None,
        severity_levels: main_models.SeverityLevelsFilter = None,
        status: main_models.StatusFilter = None,
        uuid: main_models.UuidFilter = None,
    ):
        self.biz_source = biz_source
        self.datasource_type = datasource_type
        self.display_name = display_name
        self.enabled = enabled
        self.labels = labels
        self.notification_channels = notification_channels
        self.notify_strategy_id = notify_strategy_id
        self.observe_resource_config = observe_resource_config
        self.observe_resource_global_scope = observe_resource_global_scope
        self.observe_resource_instance_id = observe_resource_instance_id
        self.observe_resource_list = observe_resource_list
        self.observe_resource_type = observe_resource_type
        self.partition_key = partition_key
        self.severity_levels = severity_levels
        self.status = status
        self.uuid = uuid

    def validate(self):
        if self.biz_source:
            self.biz_source.validate()
        if self.datasource_type:
            self.datasource_type.validate()
        if self.display_name:
            self.display_name.validate()
        if self.enabled:
            self.enabled.validate()
        if self.labels:
            self.labels.validate()
        if self.notification_channels:
            self.notification_channels.validate()
        if self.notify_strategy_id:
            self.notify_strategy_id.validate()
        if self.observe_resource_config:
            self.observe_resource_config.validate()
        if self.observe_resource_global_scope:
            self.observe_resource_global_scope.validate()
        if self.observe_resource_list:
            self.observe_resource_list.validate()
        if self.observe_resource_type:
            self.observe_resource_type.validate()
        if self.partition_key:
            self.partition_key.validate()
        if self.severity_levels:
            self.severity_levels.validate()
        if self.status:
            self.status.validate()
        if self.uuid:
            self.uuid.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_source is not None:
            result['bizSource'] = self.biz_source.to_map()

        if self.datasource_type is not None:
            result['datasourceType'] = self.datasource_type.to_map()

        if self.display_name is not None:
            result['displayName'] = self.display_name.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled.to_map()

        if self.labels is not None:
            result['labels'] = self.labels.to_map()

        if self.notification_channels is not None:
            result['notificationChannels'] = self.notification_channels.to_map()

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id.to_map()

        if self.observe_resource_config is not None:
            result['observeResourceConfig'] = self.observe_resource_config.to_map()

        if self.observe_resource_global_scope is not None:
            result['observeResourceGlobalScope'] = self.observe_resource_global_scope.to_map()

        if self.observe_resource_instance_id is not None:
            result['observeResourceInstanceId'] = self.observe_resource_instance_id

        if self.observe_resource_list is not None:
            result['observeResourceList'] = self.observe_resource_list.to_map()

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type.to_map()

        if self.partition_key is not None:
            result['partitionKey'] = self.partition_key.to_map()

        if self.severity_levels is not None:
            result['severityLevels'] = self.severity_levels.to_map()

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.uuid is not None:
            result['uuid'] = self.uuid.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizSource') is not None:
            temp_model = main_models.BizSourceFilter()
            self.biz_source = temp_model.from_map(m.get('bizSource'))

        if m.get('datasourceType') is not None:
            temp_model = main_models.DatasourceTypeFilter()
            self.datasource_type = temp_model.from_map(m.get('datasourceType'))

        if m.get('displayName') is not None:
            temp_model = main_models.DisplayNameFilter()
            self.display_name = temp_model.from_map(m.get('displayName'))

        if m.get('enabled') is not None:
            temp_model = main_models.EnabledFilter()
            self.enabled = temp_model.from_map(m.get('enabled'))

        if m.get('labels') is not None:
            temp_model = main_models.LabelsFilter()
            self.labels = temp_model.from_map(m.get('labels'))

        if m.get('notificationChannels') is not None:
            temp_model = main_models.NotificationChannelsFilter()
            self.notification_channels = temp_model.from_map(m.get('notificationChannels'))

        if m.get('notifyStrategyId') is not None:
            temp_model = main_models.NotifyStrategyIdFilter()
            self.notify_strategy_id = temp_model.from_map(m.get('notifyStrategyId'))

        if m.get('observeResourceConfig') is not None:
            temp_model = main_models.ObserveResourceConfigFilter()
            self.observe_resource_config = temp_model.from_map(m.get('observeResourceConfig'))

        if m.get('observeResourceGlobalScope') is not None:
            temp_model = main_models.ObserveResourceGlobalScopeFilter()
            self.observe_resource_global_scope = temp_model.from_map(m.get('observeResourceGlobalScope'))

        if m.get('observeResourceInstanceId') is not None:
            self.observe_resource_instance_id = m.get('observeResourceInstanceId')

        if m.get('observeResourceList') is not None:
            temp_model = main_models.ObserveResourceListFilter()
            self.observe_resource_list = temp_model.from_map(m.get('observeResourceList'))

        if m.get('observeResourceType') is not None:
            temp_model = main_models.ObserveResourceTypeFilter()
            self.observe_resource_type = temp_model.from_map(m.get('observeResourceType'))

        if m.get('partitionKey') is not None:
            temp_model = main_models.PartitionKeyFilter()
            self.partition_key = temp_model.from_map(m.get('partitionKey'))

        if m.get('severityLevels') is not None:
            temp_model = main_models.SeverityLevelsFilter()
            self.severity_levels = temp_model.from_map(m.get('severityLevels'))

        if m.get('status') is not None:
            temp_model = main_models.StatusFilter()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('uuid') is not None:
            temp_model = main_models.UuidFilter()
            self.uuid = temp_model.from_map(m.get('uuid'))

        return self

