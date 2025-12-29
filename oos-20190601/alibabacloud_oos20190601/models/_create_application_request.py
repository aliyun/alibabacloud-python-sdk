# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        alarm_config: main_models.CreateApplicationRequestAlarmConfig = None,
        application_source: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The configurations of application alerts.
        self.alarm_config = alarm_config
        # The source of application.
        self.application_source = application_source
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the application.
        self.description = description
        # The application name.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the Compute Nest service that corresponds to the application template.
        self.service_id = service_id
        # The tags.
        self.tags = tags

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()

        if self.application_source is not None:
            result['ApplicationSource'] = self.application_source

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = main_models.CreateApplicationRequestAlarmConfig()
            self.alarm_config = temp_model.from_map(m.get('AlarmConfig'))

        if m.get('ApplicationSource') is not None:
            self.application_source = m.get('ApplicationSource')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class CreateApplicationRequestAlarmConfig(DaraModel):
    def __init__(
        self,
        contact_groups: List[str] = None,
        health_check_url: str = None,
        template_ids: List[str] = None,
    ):
        # The alert contact groups.
        self.contact_groups = contact_groups
        # The health check URL of the application.
        self.health_check_url = health_check_url
        # The alert templates.
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        return self

