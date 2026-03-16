# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        business_channel: str = None,
        description: str = None,
        group_name: str = None,
        parent_group_id: str = None,
        solution_id: str = None,
    ):
        self.biz_type = biz_type
        self.business_channel = business_channel
        # The description of the user group.
        self.description = description
        self.group_name = group_name
        # > This parameter is not publicly available.
        self.parent_group_id = parent_group_id
        # > This parameter is not publicly available.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.parent_group_id is not None:
            result['ParentGroupId'] = self.parent_group_id

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ParentGroupId') is not None:
            self.parent_group_id = m.get('ParentGroupId')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        return self

