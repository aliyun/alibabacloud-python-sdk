# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        templates: List[main_models.ListTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        # The page number of the template list.  
        # Start value: 1.
        self.page_number = page_number
        # The number of entries per page in a paginated query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of templates.
        self.templates = templates
        # The total number of templates.
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        additional_info: Dict[str, Any] = None,
        create_time: str = None,
        description: str = None,
        owner_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: List[main_models.ListTemplatesResponseBodyTemplatesTags] = None,
        template_arn: str = None,
        template_id: str = None,
        template_name: str = None,
        template_url: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        # Supplementary information for public templates.
        self.additional_info = additional_info
        # Creation time.
        self.create_time = create_time
        # Template description.
        self.description = description
        # ID of the Alibaba Cloud account to which the template belongs.
        self.owner_id = owner_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The sharing type of the template.
        # 
        # Values:
        # - Private: The template is owned by the user themselves.
        # - Shared: The template is shared by other users.
        self.share_type = share_type
        # Tags of the template.
        self.tags = tags
        # The ARN of the template.
        self.template_arn = template_arn
        # Template ID.
        self.template_id = template_id
        # Template name.
        self.template_name = template_name
        # Link to the template
        self.template_url = template_url
        # Latest template version name.
        self.template_version = template_version
        # The last update time of the template.
        self.update_time = update_time

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
        if self.additional_info is not None:
            result['AdditionalInfo'] = self.additional_info

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalInfo') is not None:
            self.additional_info = m.get('AdditionalInfo')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTemplatesResponseBodyTemplatesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListTemplatesResponseBodyTemplatesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key of the template.
        self.key = key
        # Tag value of the template.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

