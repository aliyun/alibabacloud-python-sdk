# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class GetMessageGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetMessageGroupResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetMessageGroupResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetMessageGroupResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator_id: str = None,
        extension: Dict[str, Any] = None,
        group_id: str = None,
        is_mute_all: bool = None,
        status: int = None,
    ):
        # The time when the message group was created. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the creator.
        self.creator_id = creator_id
        # The extended field.
        self.extension = extension
        # The ID of the message group.
        self.group_id = group_id
        # Indicates whether the message group is muted.
        # 
        # *   true: The message group is muted.
        # *   false: The message group is not muted.
        self.is_mute_all = is_mute_all
        # The status of the message group. The default value is **1**, which indicates that the message group is normal.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.is_mute_all is not None:
            result['IsMuteAll'] = self.is_mute_all

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsMuteAll') is not None:
            self.is_mute_all = m.get('IsMuteAll')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

