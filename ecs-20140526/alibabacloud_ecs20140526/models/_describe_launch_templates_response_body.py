# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeLaunchTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        launch_template_sets: main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSets = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried launch templates.
        self.launch_template_sets = launch_template_sets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of launch templates.
        self.total_count = total_count

    def validate(self):
        if self.launch_template_sets:
            self.launch_template_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_template_sets is not None:
            result['LaunchTemplateSets'] = self.launch_template_sets.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateSets') is not None:
            temp_model = main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSets()
            self.launch_template_sets = temp_model.from_map(m.get('LaunchTemplateSets'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLaunchTemplatesResponseBodyLaunchTemplateSets(DaraModel):
    def __init__(
        self,
        launch_template_set: List[main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSet] = None,
    ):
        self.launch_template_set = launch_template_set

    def validate(self):
        if self.launch_template_set:
            for v1 in self.launch_template_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LaunchTemplateSet'] = []
        if self.launch_template_set is not None:
            for k1 in self.launch_template_set:
                result['LaunchTemplateSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.launch_template_set = []
        if m.get('LaunchTemplateSet') is not None:
            for k1 in m.get('LaunchTemplateSet'):
                temp_model = main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSet()
                self.launch_template_set.append(temp_model.from_map(k1))

        return self

class DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSet(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        created_by: str = None,
        default_version_number: int = None,
        latest_version_number: int = None,
        launch_template_id: str = None,
        launch_template_name: str = None,
        modified_time: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSetTags = None,
    ):
        # The time when the launch template was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that created the launch template.
        self.created_by = created_by
        # The default version number of the launch template.
        self.default_version_number = default_version_number
        # The latest version number of the launch template.
        self.latest_version_number = latest_version_number
        # The ID of the launch template.
        self.launch_template_id = launch_template_id
        # The name of the launch template.
        self.launch_template_name = launch_template_name
        # The time when a version was added to or deleted from the launch template.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The ID of the resource group to which the launch template belongs.
        self.resource_group_id = resource_group_id
        # The tags of the launch template.
        # 
        # >  You can only call API operations to add tags to and query the tags of a launch template. You cannot add tags to or view the tags of a launch template in the ECS console.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.default_version_number is not None:
            result['DefaultVersionNumber'] = self.default_version_number

        if self.latest_version_number is not None:
            result['LatestVersionNumber'] = self.latest_version_number

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('DefaultVersionNumber') is not None:
            self.default_version_number = m.get('DefaultVersionNumber')

        if m.get('LatestVersionNumber') is not None:
            self.latest_version_number = m.get('LatestVersionNumber')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSetTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLaunchTemplatesResponseBodyLaunchTemplateSetsLaunchTemplateSetTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag value of the launch template.
        self.tag_key = tag_key
        # The tag key of the launch template.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

