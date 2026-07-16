# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListTagResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: List[main_models.ListTagResponseBodyData] = None,
        data_size: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The page size.
        self.current_page = current_page
        # The returned data.
        self.data = data
        # The actual number of records returned on the current page.
        self.data_size = data_size
        # The error message, if any.
        self.message = message
        # The page size.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. true: The call was successful. false: The call failed.
        self.success = success
        # The total number of records that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTagResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTagResponseBodyData(DaraModel):
    def __init__(
        self,
        child_count: int = None,
        create_time: int = None,
        description: str = None,
        level: int = None,
        modify_time: int = None,
        name: str = None,
        parent_tag_id: int = None,
        path: List[str] = None,
        tag_id: int = None,
    ):
        # The number of direct child nodes.
        self.child_count = child_count
        # The time when the label was created.
        self.create_time = create_time
        # The label description.
        self.description = description
        # The level of the current node.
        self.level = level
        # The time when the label was last modified.
        self.modify_time = modify_time
        # The label name.
        self.name = name
        # The ID of the parent label node.
        self.parent_tag_id = parent_tag_id
        # The node path.
        self.path = path
        # The label ID.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_count is not None:
            result['ChildCount'] = self.child_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.level is not None:
            result['Level'] = self.level

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_tag_id is not None:
            result['ParentTagId'] = self.parent_tag_id

        if self.path is not None:
            result['Path'] = self.path

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildCount') is not None:
            self.child_count = m.get('ChildCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentTagId') is not None:
            self.parent_tag_id = m.get('ParentTagId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

