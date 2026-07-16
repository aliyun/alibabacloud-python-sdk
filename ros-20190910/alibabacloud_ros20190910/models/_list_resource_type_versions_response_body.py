# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListResourceTypeVersionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_versions: List[main_models.ListResourceTypeVersionsResponseBodyResourceTypeVersions] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The versions of the resource types.
        self.resource_type_versions = resource_type_versions

    def validate(self):
        if self.resource_type_versions:
            for v1 in self.resource_type_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceTypeVersions'] = []
        if self.resource_type_versions is not None:
            for k1 in self.resource_type_versions:
                result['ResourceTypeVersions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_type_versions = []
        if m.get('ResourceTypeVersions') is not None:
            for k1 in m.get('ResourceTypeVersions'):
                temp_model = main_models.ListResourceTypeVersionsResponseBodyResourceTypeVersions()
                self.resource_type_versions.append(temp_model.from_map(k1))

        return self

class ListResourceTypeVersionsResponseBodyResourceTypeVersions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        entity_type: str = None,
        is_default_version: bool = None,
        provider: str = None,
        resource_type: str = None,
        update_time: str = None,
        version_id: str = None,
    ):
        # The time when the version was created. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The description of the version.
        self.description = description
        # The entity type. Only Module may be returned.
        self.entity_type = entity_type
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   true
        # *   false
        self.is_default_version = is_default_version
        # The provider of the resource type. Valid values:
        # 
        # *   ROS: ROS
        # *   Self: yourself
        self.provider = provider
        # The resource type.
        self.resource_type = resource_type
        # The time when the version was updated. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.update_time = update_time
        # The version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

