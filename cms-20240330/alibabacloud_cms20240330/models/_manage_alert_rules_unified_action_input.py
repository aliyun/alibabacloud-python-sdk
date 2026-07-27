# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ManageAlertRulesUnifiedActionInput(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_integration_config: main_models.ActionIntegrationConfig = None,
        annotations: Dict[str, str] = None,
        arms_integration_config: main_models.ArmsIntegrationConfig = None,
        biz_source: str = None,
        condition_config: main_models.ConditionConfigUnified = None,
        content_template: str = None,
        datasource_config: main_models.DatasourceConfigUnified = None,
        display_name: str = None,
        enabled: bool = None,
        labels: Dict[str, str] = None,
        notify_config: main_models.NotifyConfigUnified = None,
        observe_resource_config: main_models.ObserveResourceConfig = None,
        observe_resource_instance_id: str = None,
        observe_resource_type: str = None,
        query_config: main_models.QueryConfigUnified = None,
        rca_config: main_models.AlertRuleRcaConfig = None,
        region_id: str = None,
        schedule_config: main_models.ScheduleConfigUnified = None,
        uuid: str = None,
        uuid_list: List[str] = None,
        workspace: str = None,
    ):
        # This parameter is required.
        self.action = action
        self.action_integration_config = action_integration_config
        self.annotations = annotations
        self.arms_integration_config = arms_integration_config
        self.biz_source = biz_source
        self.condition_config = condition_config
        self.content_template = content_template
        self.datasource_config = datasource_config
        self.display_name = display_name
        self.enabled = enabled
        self.labels = labels
        self.notify_config = notify_config
        self.observe_resource_config = observe_resource_config
        self.observe_resource_instance_id = observe_resource_instance_id
        self.observe_resource_type = observe_resource_type
        self.query_config = query_config
        self.rca_config = rca_config
        self.region_id = region_id
        self.schedule_config = schedule_config
        self.uuid = uuid
        self.uuid_list = uuid_list
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
        if self.action is not None:
            result['action'] = self.action

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

        if self.datasource_config is not None:
            result['datasourceConfig'] = self.datasource_config.to_map()

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.labels is not None:
            result['labels'] = self.labels

        if self.notify_config is not None:
            result['notifyConfig'] = self.notify_config.to_map()

        if self.observe_resource_config is not None:
            result['observeResourceConfig'] = self.observe_resource_config.to_map()

        if self.observe_resource_instance_id is not None:
            result['observeResourceInstanceId'] = self.observe_resource_instance_id

        if self.observe_resource_type is not None:
            result['observeResourceType'] = self.observe_resource_type

        if self.query_config is not None:
            result['queryConfig'] = self.query_config.to_map()

        if self.rca_config is not None:
            result['rcaConfig'] = self.rca_config.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.schedule_config is not None:
            result['scheduleConfig'] = self.schedule_config.to_map()

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.uuid_list is not None:
            result['uuidList'] = self.uuid_list

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

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

        if m.get('datasourceConfig') is not None:
            temp_model = main_models.DatasourceConfigUnified()
            self.datasource_config = temp_model.from_map(m.get('datasourceConfig'))

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('notifyConfig') is not None:
            temp_model = main_models.NotifyConfigUnified()
            self.notify_config = temp_model.from_map(m.get('notifyConfig'))

        if m.get('observeResourceConfig') is not None:
            temp_model = main_models.ObserveResourceConfig()
            self.observe_resource_config = temp_model.from_map(m.get('observeResourceConfig'))

        if m.get('observeResourceInstanceId') is not None:
            self.observe_resource_instance_id = m.get('observeResourceInstanceId')

        if m.get('observeResourceType') is not None:
            self.observe_resource_type = m.get('observeResourceType')

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

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('uuidList') is not None:
            self.uuid_list = m.get('uuidList')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

