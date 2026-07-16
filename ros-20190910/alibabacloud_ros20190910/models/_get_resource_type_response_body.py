# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetResourceTypeResponseBody(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        create_time: str = None,
        default_version_id: str = None,
        description: str = None,
        entity_type: str = None,
        is_default_version: bool = None,
        latest_version_id: str = None,
        properties: Dict[str, Any] = None,
        provider: str = None,
        request_id: str = None,
        resource_type: str = None,
        support_drift_detection: bool = None,
        support_scratch_detection: bool = None,
        template_body: str = None,
        total_version_count: int = None,
        update_time: str = None,
    ):
        # The type of the resource.
        self.attributes = attributes
        # The creation time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The default version ID.
        # 
        # > This parameter is returned only if the resource type is queried.
        self.default_version_id = default_version_id
        # The description of the resource type.
        self.description = description
        # The entity type. Valid values:
        # 
        # *   Resource: regular resource. For more information, see [Resources](https://help.aliyun.com/document_detail/28863.html).
        # *   DataSource: DataSource resource. For more information, see [DataSource resources](https://help.aliyun.com/document_detail/404753.html).
        # *   module: module.
        self.entity_type = entity_type
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > This parameter is returned only if a specific version of the resource type is queried.
        self.is_default_version = is_default_version
        # The latest version ID.
        # 
        # > This parameter is returned only if the resource type is queried.
        self.latest_version_id = latest_version_id
        # Indicates whether the resource supports drift detection. Default value: false. Valid values:
        # 
        # *   true: Drift detection is supported.
        # *   false: Drift detection is not supported.
        self.properties = properties
        # The provider of the resource type. Valid values:
        # 
        # *   ROS: The resource type is provided by Resource Orchestration Service (ROS).
        # *   Self: The resource type is provided by you.
        self.provider = provider
        # The attributes of the resource.
        self.request_id = request_id
        # The properties of the resource.
        self.resource_type = resource_type
        # Indicates whether the resource supports scratch detection. Default value: false. Valid values:
        # 
        # *   true: Scratch detection is supported.
        # *   false: Scratch detection is not supported.
        self.support_drift_detection = support_drift_detection
        # The entity type. Valid values:
        # 
        # *   Resource: resources other than DataSource resources. For more information, see [Resources](https://help.aliyun.com/document_detail/28863.html).
        # *   DataSource: DataSource resources.
        self.support_scratch_detection = support_scratch_detection
        # The template content in the module.
        # 
        # > This parameter is returned only if a specific version of the resource type is queried.
        self.template_body = template_body
        # The total number of versions.
        # 
        # > This parameter is returned only if the resource type is queried.
        self.total_version_count = total_version_count
        # The update time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_version_id is not None:
            result['DefaultVersionId'] = self.default_version_id

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version

        if self.latest_version_id is not None:
            result['LatestVersionId'] = self.latest_version_id

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.support_drift_detection is not None:
            result['SupportDriftDetection'] = self.support_drift_detection

        if self.support_scratch_detection is not None:
            result['SupportScratchDetection'] = self.support_scratch_detection

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.total_version_count is not None:
            result['TotalVersionCount'] = self.total_version_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultVersionId') is not None:
            self.default_version_id = m.get('DefaultVersionId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')

        if m.get('LatestVersionId') is not None:
            self.latest_version_id = m.get('LatestVersionId')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SupportDriftDetection') is not None:
            self.support_drift_detection = m.get('SupportDriftDetection')

        if m.get('SupportScratchDetection') is not None:
            self.support_scratch_detection = m.get('SupportScratchDetection')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TotalVersionCount') is not None:
            self.total_version_count = m.get('TotalVersionCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

