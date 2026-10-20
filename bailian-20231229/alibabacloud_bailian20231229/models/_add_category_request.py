# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCategoryRequest(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        category_type: str = None,
        connector_id: str = None,
        parent_category_id: str = None,
    ):
        # The category name. The name must be 1 to 20 characters in length and can contain characters in the Unicode letter category, including letters, Chinese characters, and digits. The name can also contain colons (:), underscores (_), periods (.), or hyphens (-).
        # 
        # This parameter is required.
        self.category_name = category_name
        # The category type. Valid values:
        # - UNSTRUCTURED: category.
        # 
        # This parameter is required.
        self.category_type = category_type
        # The instance ID of the data connector (Connector). Obtain this value from the Model Studio console.
        self.connector_id = connector_id
        # The ID of the parent category. The new category is created under this parent category. If this parameter is left empty, a first-level category is created.
        self.parent_category_id = parent_category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.parent_category_id is not None:
            result['ParentCategoryId'] = self.parent_category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ParentCategoryId') is not None:
            self.parent_category_id = m.get('ParentCategoryId')

        return self

