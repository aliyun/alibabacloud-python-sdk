# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVerifySDKResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_url: str = None,
    ):
        # The ID of this request.
        self.request_id = request_id
        # The SDK download URL. When not empty, it indicates that the generation is complete.
        self.sdk_url = sdk_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')

        return self

