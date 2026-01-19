# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppResponseBody(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
        tag_status: bool = None,
    ):
        # The unique ID of the application.
        self.app_id = app_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the tag exists. If the value is **true**, the tag exists. If the value is **false**, the tag does not exist.
        self.tag_status = tag_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_status is not None:
            result['TagStatus'] = self.tag_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagStatus') is not None:
            self.tag_status = m.get('TagStatus')

        return self

