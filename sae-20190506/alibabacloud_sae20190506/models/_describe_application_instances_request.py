# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationInstancesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        group_id: str = None,
        instance_id: str = None,
        page_size: int = None,
        pipeline_id: str = None,
        reverse: bool = None,
    ):
        # d700e680-aa4d-4ec1-afc2-6566b5ff\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.app_id = app_id
        # 1
        self.current_page = current_page
        # b2a8a925-477a-4ed7-b825-d5e22500\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the application instance.
        self.instance_id = instance_id
        # 10
        self.page_size = page_size
        self.pipeline_id = pipeline_id
        # true
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        return self

