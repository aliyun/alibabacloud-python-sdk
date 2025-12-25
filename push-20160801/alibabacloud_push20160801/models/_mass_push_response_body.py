# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class MassPushResponseBody(DaraModel):
    def __init__(
        self,
        message_ids: main_models.MassPushResponseBodyMessageIds = None,
        request_id: str = None,
    ):
        self.message_ids = message_ids
        self.request_id = request_id

    def validate(self):
        if self.message_ids:
            self.message_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_ids is not None:
            result['MessageIds'] = self.message_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageIds') is not None:
            temp_model = main_models.MassPushResponseBodyMessageIds()
            self.message_ids = temp_model.from_map(m.get('MessageIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class MassPushResponseBodyMessageIds(DaraModel):
    def __init__(
        self,
        message_id: List[str] = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

