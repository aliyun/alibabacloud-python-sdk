# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkflowsShrinkRequest(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        ids_shrink: str = None,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        tags_shrink: str = None,
        trigger_type: str = None,
    ):
        # The environment of the workspace. Valid values:
        # 
        # *   Prod: production environment
        # *   Dev: development environment
        self.env_type = env_type
        # The IDs of the workflows. You can query multiple workflows at a time by workflow ID.
        self.ids_shrink = ids_shrink
        # The name of the workflow. Fuzzy match is supported.
        self.name = name
        # The account ID of the workflow owner.
        self.owner = owner
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The field used for sorting. Fields such as TriggerTime and StartedTime are supported. The value of this parameter is in the Sort field + Sort by (Desc/Asc) format. By default, results are sorted in ascending order. Valid values:
        # 
        # *   ModifyTime (Desc/Asc)
        # *   CreateTime (Desc/Asc)
        # *   Id (Desc/Asc)
        # 
        # Default value: Id Desc.
        self.sort_by = sort_by
        self.tags_shrink = tags_shrink
        # The trigger type.
        # 
        # *   Scheduler
        # *   Manual
        # *   TriggerWorkflow
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

