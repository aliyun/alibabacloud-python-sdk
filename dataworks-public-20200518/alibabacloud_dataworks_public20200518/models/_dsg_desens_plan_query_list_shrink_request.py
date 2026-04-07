# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgDesensPlanQueryListShrinkRequest(DaraModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_name: str = None,
        scene_id: int = None,
        status: int = None,
        columns_shrink: str = None,
        data_type: str = None,
        empty_not_desesn: str = None,
    ):
        # The owner of the data masking rule.
        self.owner = owner
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the sensitive field.
        self.rule_name = rule_name
        # The ID of the level-2 data masking scenario. You can call the [DsgSceneQuerySceneListByName](https://help.aliyun.com/document_detail/2786322.html) operation to query the list of IDs.
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # The status of the data masking rule. Valid values:
        # 
        # *   0: expired
        # *   1: effective
        self.status = status
        self.columns_shrink = columns_shrink
        self.data_type = data_type
        self.empty_not_desesn = empty_not_desesn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        if self.columns_shrink is not None:
            result['columns'] = self.columns_shrink

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.empty_not_desesn is not None:
            result['emptyNotDesesn'] = self.empty_not_desesn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('columns') is not None:
            self.columns_shrink = m.get('columns')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('emptyNotDesesn') is not None:
            self.empty_not_desesn = m.get('emptyNotDesesn')

        return self

