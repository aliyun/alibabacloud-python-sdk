# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobPlansShrinkRequest(DaraModel):
    def __init__(
        self,
        has_template: bool = None,
        job_plan_name: str = None,
        job_plan_type: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        tag_shrink: str = None,
        template_id: str = None,
        workspace_id: str = None,
    ):
        # Specifies whether to filter by template association. Valid values:
        # - true: Returns only scenario-specific job plans that have a template.
        # - false: Returns only general-purpose job plans that do not have a template.
        # 
        # If this parameter is not specified, no filtering is applied. If both this parameter and TemplateId are specified, the value of TemplateId takes precedence.
        self.has_template = has_template
        # The name of the job plan.
        self.job_plan_name = job_plan_name
        # The type of the job plan.
        self.job_plan_type = job_plan_type
        # The sort order.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The field by which to sort the results.
        self.sort_by = sort_by
        # The list of tags.
        self.tag_shrink = tag_shrink
        # The distillation template ID. Filters results to return only scenario-specific tasks that use the specified template.
        self.template_id = template_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_template is not None:
            result['HasTemplate'] = self.has_template

        if self.job_plan_name is not None:
            result['JobPlanName'] = self.job_plan_name

        if self.job_plan_type is not None:
            result['JobPlanType'] = self.job_plan_type

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasTemplate') is not None:
            self.has_template = m.get('HasTemplate')

        if m.get('JobPlanName') is not None:
            self.job_plan_name = m.get('JobPlanName')

        if m.get('JobPlanType') is not None:
            self.job_plan_type = m.get('JobPlanType')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

