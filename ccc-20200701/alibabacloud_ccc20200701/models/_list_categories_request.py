# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCategoriesRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        instance_id: str = None,
        type: str = None,
    ):
        # The ID of the ticket category. Specify this parameter to return information about the subcategories of the specified category. If you leave this parameter empty, information about all categories in the instance is returned.
        self.category_id = category_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The category type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

