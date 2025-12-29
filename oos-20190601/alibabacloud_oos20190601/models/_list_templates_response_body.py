# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        templates: List[main_models.ListTemplatesResponseBodyTemplates] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The template metadata.
        self.templates = templates

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class ListTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        category: str = None,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        has_trigger: bool = None,
        hash: str = None,
        is_favorite: bool = None,
        popularity: int = None,
        publisher: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
        template_version: str = None,
        total_execution_count: int = None,
        updated_by: str = None,
        updated_date: str = None,
        version_name: str = None,
    ):
        # The template type.
        self.category = category
        # The template constraints.
        self.constraints = constraints
        # The user who created the template.
        self.created_by = created_by
        # The creation time of the template.
        self.created_date = created_date
        # The template description.
        self.description = description
        # Indicates whether the template was configured with a trigger.
        self.has_trigger = has_trigger
        # The SHA256 value of the template content.
        self.hash = hash
        # Indicates whether the template is added to favorites.
        self.is_favorite = is_favorite
        # The popularity of the public template. Valid values: **1-10**. A greater value indicates higher popularity. If **ShareType** is set to **Private**, the value of this parameter is `-1`.
        # 
        # >  This parameter is valid only if **ShareType** is set to **Public**.
        self.popularity = popularity
        # The user who published the template.
        self.publisher = publisher
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. The share type of a template created by a user is **Private**. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        self.share_type = share_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The template format. The system automatically determines whether the format of the template is JSON or YAML.
        self.template_format = template_format
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The template type.
        self.template_type = template_type
        # The template version. The version contains the letter v and a number. The number starts from 1.
        self.template_version = template_version
        # The number of times for which the private template is executed. If **ShareType** is set to **Public**, the value of this parameter is `-1`.
        # 
        # >  This parameter is valid only if **ShareType** is set to **Private**.
        self.total_execution_count = total_execution_count
        # The user who last updated the template.
        self.updated_by = updated_by
        # The time when the template was last updated.
        self.updated_date = updated_date
        # The version name.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger

        if self.hash is not None:
            result['Hash'] = self.hash

        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite

        if self.popularity is not None:
            result['Popularity'] = self.popularity

        if self.publisher is not None:
            result['Publisher'] = self.publisher

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.total_execution_count is not None:
            result['TotalExecutionCount'] = self.total_execution_count

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')

        if m.get('Hash') is not None:
            self.hash = m.get('Hash')

        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')

        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')

        if m.get('Publisher') is not None:
            self.publisher = m.get('Publisher')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TotalExecutionCount') is not None:
            self.total_execution_count = m.get('TotalExecutionCount')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

