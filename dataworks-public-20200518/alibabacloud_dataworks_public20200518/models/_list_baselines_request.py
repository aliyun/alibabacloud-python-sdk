# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBaselinesRequest(DaraModel):
    def __init__(
        self,
        baseline_types: str = None,
        enable: bool = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        priority: str = None,
        project_id: int = None,
        search_text: str = None,
    ):
        # The type of the baseline. Valid values: DAILY and HOURLY. You can specify multiple types. Separate multiple types with commas (,).
        self.baseline_types = baseline_types
        # Specifies whether to enable the baseline. Valid values: true and false.
        self.enable = enable
        # The owner.
        self.owner = owner
        # The page number. Pages start from page 1. Default value: 1. Maximum value: 30.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The priority of the baseline. Valid values: {1,3,5,7,8}.
        self.priority = priority
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The keyword in the baseline name, which is used to search for the baseline.
        self.search_text = search_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_types is not None:
            result['BaselineTypes'] = self.baseline_types

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineTypes') is not None:
            self.baseline_types = m.get('BaselineTypes')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        return self

