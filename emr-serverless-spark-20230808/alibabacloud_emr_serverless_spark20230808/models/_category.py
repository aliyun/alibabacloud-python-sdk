# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Category(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        modifier: int = None,
        name: str = None,
        parent_biz_id: str = None,
        type: str = None,
    ):
        # The folder ID.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # The ID of the user who creates the folder.
        # 
        # This parameter is required.
        self.creator = creator
        # The time when the folder was created.
        # 
        # This parameter is required.
        self.gmt_created = gmt_created
        # The time when the folder was last updated.
        # 
        # This parameter is required.
        self.gmt_modified = gmt_modified
        # The ID of the user who last modifies the folder.
        # 
        # This parameter is required.
        self.modifier = modifier
        # The name of the folder.
        # 
        # This parameter is required.
        self.name = name
        # The parent folder ID.
        self.parent_biz_id = parent_biz_id
        # The type of the folder.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.creator is not None:
            result['creator'] = self.creator

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.name is not None:
            result['name'] = self.name

        if self.parent_biz_id is not None:
            result['parentBizId'] = self.parent_biz_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentBizId') is not None:
            self.parent_biz_id = m.get('parentBizId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

