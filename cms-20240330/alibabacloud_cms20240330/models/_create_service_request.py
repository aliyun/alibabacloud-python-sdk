# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateServiceRequest(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        description: str = None,
        display_name: str = None,
        pid: str = None,
        resource_group_id: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        tags: List[main_models.CreateServiceRequestTags] = None,
    ):
        # Extended attributes.
        self.attributes = attributes
        # Service description, only valid when `serviceType=RUM`.
        self.description = description
        # Display name, only valid when `serviceType=RUM`.
        self.display_name = display_name
        # Application ID, generally not required to be specified.
        self.pid = pid
        self.resource_group_id = resource_group_id
        # Service name
        # 
        # This parameter is required.
        self.service_name = service_name
        # Service status, not required for service creation.
        self.service_status = service_status
        # Service type
        # 
        # This parameter is required.
        self.service_type = service_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.pid is not None:
            result['pid'] = self.pid

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.service_status is not None:
            result['serviceStatus'] = self.service_status

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('pid') is not None:
            self.pid = m.get('pid')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateServiceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateServiceRequestTags(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

