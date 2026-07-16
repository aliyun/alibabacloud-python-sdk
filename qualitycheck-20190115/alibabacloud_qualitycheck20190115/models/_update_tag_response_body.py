# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class UpdateTagResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateTagResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Other values indicate failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The returned result.
        self.data = data
        # The error message returned when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateTagResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateTagResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        modify_time: int = None,
        name: str = None,
        parent_tag_id: int = None,
        tag_id: int = None,
    ):
        # The time when the label node was created.
        self.create_time = create_time
        # The label description.
        self.description = description
        # The time when the label node was last modified.
        self.modify_time = modify_time
        # The label name.
        self.name = name
        # The ID of the parent label node.
        self.parent_tag_id = parent_tag_id
        # The label ID.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_tag_id is not None:
            result['ParentTagId'] = self.parent_tag_id

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentTagId') is not None:
            self.parent_tag_id = m.get('ParentTagId')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

