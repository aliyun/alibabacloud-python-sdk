# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListTemplatesRequest(DaraModel):
    def __init__(
        self,
        filters: List[main_models.ListTemplatesRequestFilters] = None,
        include_tags: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tag: List[main_models.ListTemplatesRequestTag] = None,
        template_name: str = None,
    ):
        # Filter.
        self.filters = filters
        # Whether to query tag information. Values:  
        # 
        # - Enabled: Query.  
        # - Disabled (default): Do not query.
        self.include_tags = include_tags
        # The page number of the template list.  
        # Start value: 1.  
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paginated query.  
        # Value range: 1~50.  
        # Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.  
        # For more information about resource groups, see [What is a Resource Group](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        # The sharing type of the template.  
        # 
        # Values:  
        # - Private (default): The template is owned by the user.  
        # - Shared: The template is shared by other users.  
        # - Official: The template is officially shared.
        self.share_type = share_type
        # Tags. A maximum of 20 tags are supported.
        self.tag = tag
        # The name of the template. This parameter is effective only when ShareType is Private.  
        # The length must not exceed 255 characters and must start with a digit or a letter. It can contain digits, letters, hyphens (-), and underscores (_).
        self.template_name = template_name

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListTemplatesRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTemplatesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class ListTemplatesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. This parameter is effective only when ShareType is Private.  
        # 
        # A maximum of 20 tag keys are supported.
        self.key = key
        # The value of the tag. This parameter is effective only when ShareType is Private.  
        # 
        # A maximum of 20 tag values are supported.
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

class ListTemplatesRequestFilters(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The name of the filter. You can choose one or more names for the query. Value range:  
        # 
        # - Categories: Template categories  
        # - DeployTypes: Deployment types  
        # - ApplicationScenes: Application scenarios  
        # - BasicServices: Basic services  
        # - ResourceTypes: Resource types  
        # - TemplateNames: Template names
        self.name = name
        # The list of filter values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

