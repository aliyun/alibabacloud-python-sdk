# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateOpsItemResponseBody(DaraModel):
    def __init__(
        self,
        ops_item: main_models.CreateOpsItemResponseBodyOpsItem = None,
        request_id: str = None,
    ):
        # The information about the O\\&M item.
        self.ops_item = ops_item
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = main_models.CreateOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m.get('OpsItem'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOpsItemResponseBodyOpsItem(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        category: str = None,
        create_date: str = None,
        created_by: str = None,
        description: str = None,
        last_modified_by: str = None,
        ops_item_id: str = None,
        priority: int = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
        update_date: str = None,
    ):
        # The attributes of the O\\&M item.
        self.attributes = attributes
        # The category of the O\\&M item.
        self.category = category
        # The time when the O\\&M item was created.
        self.create_date = create_date
        # The user who created the O\\&M item.
        self.created_by = created_by
        # The description of the O\\&M item.
        self.description = description
        # The user who last modified the O\\&M item.
        self.last_modified_by = last_modified_by
        # The ID of the O\\&M item.
        self.ops_item_id = ops_item_id
        # The priority of the O\\&M item.
        self.priority = priority
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ARNs of the associated resources.
        self.resources = resources
        # The severity level of the O\\&M item.
        self.severity = severity
        # The solutions.
        self.solutions = solutions
        # The source business of the O\\&M item.
        self.source = source
        # The state of the O\\&M item.
        self.status = status
        # The tags of the O\\&M item.
        self.tags = tags
        # The title of the O\\&M item.
        self.title = title
        # The time when the O\\&M item was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.category is not None:
            result['Category'] = self.category

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.description is not None:
            result['Description'] = self.description

        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by

        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.solutions is not None:
            result['Solutions'] = self.solutions

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')

        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

