# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class GetApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.GetApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        alarm_config: main_models.GetApplicationResponseBodyApplicationAlarmConfig = None,
        application_source: str = None,
        application_type: str = None,
        create_date: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        tags: Dict[str, Any] = None,
        update_date: str = None,
    ):
        # The configurations of application alerts.
        self.alarm_config = alarm_config
        # The source of application.
        self.application_source = application_source
        # The type of the application.
        # 
        # Valid values:
        # 
        # *   ComputeNest
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Custom
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DingTalk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.application_type = application_type
        # The time when the application was created.
        self.create_date = create_date
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the Compute Nest service that corresponds to the application template.
        self.service_id = service_id
        # The tags.
        self.tags = tags
        # The time when the application was updated.
        self.update_date = update_date

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

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplicationAlarmConfig()
            self.alarm_config = temp_model.from_map(m.get('AlarmConfig'))

        if m.get('ApplicationSource') is not None:
            self.application_source = m.get('ApplicationSource')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class GetApplicationResponseBodyApplicationAlarmConfig(DaraModel):
    def __init__(
        self,
        contact_groups: List[str] = None,
        health_check_url: str = None,
        template_ids: List[str] = None,
    ):
        # The alert contact list.
        self.contact_groups = contact_groups
        # The health check URL of the application.
        self.health_check_url = health_check_url
        # The ID of the alert template.
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

