# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApiDestinationResponseBody(DaraModel):
    def __init__(
        self,
        api_destination_name: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # api-destination-name
        self.api_destination_name = api_destination_name
        # The response code. If the request is successful, Success is returned.
        self.code = code
        # The returned message. If the request is successful, success is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

