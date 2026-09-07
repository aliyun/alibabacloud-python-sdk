# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class RemoveKnowledgeTagsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.RemoveKnowledgeTagsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.RemoveKnowledgeTagsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RemoveKnowledgeTagsResponseBodyData(DaraModel):
    def __init__(
        self,
        file_location: str = None,
        message: str = None,
        removed: int = None,
        success: bool = None,
    ):
        # The location of the knowledge base file.
        self.file_location = file_location
        # The message returned by the operation.
        self.message = message
        # The number of tags that were successfully deleted.
        self.removed = removed
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.message is not None:
            result['Message'] = self.message

        if self.removed is not None:
            result['Removed'] = self.removed

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Removed') is not None:
            self.removed = m.get('Removed')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

