# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBatchShrinkRequest(DaraModel):
    def __init__(
        self,
        actions_shrink: str = None,
        id: str = None,
        input_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
    ):
        # A list of data processing templates.
        self.actions_shrink = actions_shrink
        # The ID of the batch processing task. For more information, see [Create a batch processing task](https://help.aliyun.com/document_detail/606694.html).
        # 
        # This parameter is required.
        self.id = id
        # The data source configuration.
        self.input_shrink = input_shrink
        # The project name. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Custom tags used to search for and filter asynchronous tasks.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

