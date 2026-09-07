# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class AddKnowledgeUploadUserResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AddKnowledgeUploadUserResponseBodyData = None,
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
            temp_model = main_models.AddKnowledgeUploadUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddKnowledgeUploadUserResponseBodyData(DaraModel):
    def __init__(
        self,
        file_location: str = None,
        message: str = None,
        skipped: List[main_models.AddKnowledgeUploadUserResponseBodyDataSkipped] = None,
        success: bool = None,
        written: int = None,
    ):
        # The location of the knowledge base file.
        self.file_location = file_location
        # The prompt message.
        self.message = message
        # The list of skipped users.
        self.skipped = skipped
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success
        # The number of users that were successfully added.
        self.written = written

    def validate(self):
        if self.skipped:
            for v1 in self.skipped:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.message is not None:
            result['Message'] = self.message

        result['Skipped'] = []
        if self.skipped is not None:
            for k1 in self.skipped:
                result['Skipped'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.written is not None:
            result['Written'] = self.written

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.skipped = []
        if m.get('Skipped') is not None:
            for k1 in m.get('Skipped'):
                temp_model = main_models.AddKnowledgeUploadUserResponseBodyDataSkipped()
                self.skipped.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Written') is not None:
            self.written = m.get('Written')

        return self

class AddKnowledgeUploadUserResponseBodyDataSkipped(DaraModel):
    def __init__(
        self,
        reason: str = None,
        user: str = None,
    ):
        # The reason why the user was skipped.
        self.reason = reason
        # The username of the authorized user.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

