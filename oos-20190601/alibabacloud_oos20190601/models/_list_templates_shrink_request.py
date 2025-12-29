# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        created_by: str = None,
        created_date_after: str = None,
        created_date_before: str = None,
        has_trigger: bool = None,
        is_example: bool = None,
        is_favorite: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags_shrink: str = None,
        template_format: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The type of the template. Valid values include TimerTrigger, EventTrigger, AlarmTrigger, and Other.
        self.category = category
        # The creator of the template.
        # 
        # *   To query the template provided by Alibaba Cloud, set this parameter to **ACS**.
        # *   To query the template created by a user, set this parameter to the **ID** of the template or the **name of the user** who creates the template.
        self.created_by = created_by
        # Specifies to query the template that is created at or later than the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm:ssZ format.
        self.created_date_after = created_date_after
        # Specifies to query the template that is created at or before the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm::ssZ format.
        self.created_date_before = created_date_before
        # Specifies whether to query the template that is configured with a trigger.
        self.has_trigger = has_trigger
        # Specifies whether the template is an example template.
        self.is_example = is_example
        # Specifies whether the template is added to favorites.
        self.is_favorite = is_favorite
        # The number of entries per page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region in which you want to query templates.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        self.share_type = share_type
        # The field that is used to sort the templates to be queried. Valid values:
        # 
        # *   **TotalExecutionCount** (default): The system sorts the returned templates based on the total number of times that the templates are used.
        # *   **Popularity**: The system sorts the returned templates based on the popularity of the templates.
        # *   **TemplateName**: The system sorts the returned templates based on the names of the templates.
        # *   **CreatedDate**: The system sorts the returned templates based on the points in time when the templates are created.
        # *   **UpdatedDate**: The system sorts the returned templates based on the points in time when the templates are updated.
        self.sort_field = sort_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink
        # The format of the template. Valid values:
        # 
        # *   **JSON**
        # *   **YAML**
        self.template_format = template_format
        # The name of the template. All templates whose names contain the specified template name are to be returned.
        self.template_name = template_name
        # The type of the template. Valid values:
        # 
        # *   Automation: the template for automated tasks.
        # *   State: the template for configuration inventories.
        # *   Package: the template for software packages.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after

        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before

        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger

        if self.is_example is not None:
            result['IsExample'] = self.is_example

        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')

        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')

        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')

        if m.get('IsExample') is not None:
            self.is_example = m.get('IsExample')

        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

