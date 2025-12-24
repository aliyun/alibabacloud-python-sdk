# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class CreateMessageGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateMessageGroupResponseBodyResult = None,
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
            temp_model = main_models.CreateMessageGroupResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CreateMessageGroupResponseBodyResult(DaraModel):
    def __init__(
        self,
        extension: Dict[str, Any] = None,
        group_id: str = None,
    ):
        # The extended field.
        self.extension = extension
        # The ID of the message group.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        return self

