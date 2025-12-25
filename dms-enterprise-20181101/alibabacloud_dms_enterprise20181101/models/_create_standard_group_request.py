# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStandardGroupRequest(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        description: str = None,
        group_name: str = None,
        tid: int = None,
    ):
        # The type of the database engine. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        # 
        # This parameter is required.
        self.db_type = db_type
        # The description of the security rule set.
        # 
        # This parameter is required.
        self.description = description
        # The name of the security rule set.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The ID of the tenant.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

