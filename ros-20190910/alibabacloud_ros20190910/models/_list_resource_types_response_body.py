# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListResourceTypesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_summaries: List[main_models.ListResourceTypesResponseBodyResourceTypeSummaries] = None,
        resource_types: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The resource type summaries.
        self.resource_type_summaries = resource_type_summaries
        # The array of resource types.
        self.resource_types = resource_types

    def validate(self):
        if self.resource_type_summaries:
            for v1 in self.resource_type_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceTypeSummaries'] = []
        if self.resource_type_summaries is not None:
            for k1 in self.resource_type_summaries:
                result['ResourceTypeSummaries'].append(k1.to_map() if k1 else None)

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_type_summaries = []
        if m.get('ResourceTypeSummaries') is not None:
            for k1 in m.get('ResourceTypeSummaries'):
                temp_model = main_models.ListResourceTypesResponseBodyResourceTypeSummaries()
                self.resource_type_summaries.append(temp_model.from_map(k1))

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

class ListResourceTypesResponseBodyResourceTypeSummaries(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_version_id: str = None,
        description: str = None,
        entity_type: str = None,
        latest_version_id: str = None,
        provider: str = None,
        resource_type: str = None,
        total_version_count: int = None,
        update_time: str = None,
    ):
        # The creation time. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The ID of the default version.
        self.default_version_id = default_version_id
        # The description of the resource type.
        self.description = description
        # The entity type. Valid values:
        # 
        # *   Resource: regular resources.
        # *   DataSource: DataSource resources.
        # *   Module: modules.
        self.entity_type = entity_type
        # The ID of the latest version.
        self.latest_version_id = latest_version_id
        # The provider of the resource type. Valid values:
        # 
        # *   ROS: The resource type is provided by ROS.
        # *   Self: The resource type is provided by you.
        self.provider = provider
        # The resource type.
        self.resource_type = resource_type
        # The number of versions.
        self.total_version_count = total_version_count
        # The update time. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_version_id is not None:
            result['DefaultVersionId'] = self.default_version_id

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.latest_version_id is not None:
            result['LatestVersionId'] = self.latest_version_id

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.total_version_count is not None:
            result['TotalVersionCount'] = self.total_version_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultVersionId') is not None:
            self.default_version_id = m.get('DefaultVersionId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('LatestVersionId') is not None:
            self.latest_version_id = m.get('LatestVersionId')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TotalVersionCount') is not None:
            self.total_version_count = m.get('TotalVersionCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

