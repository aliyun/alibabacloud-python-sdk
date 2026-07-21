# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportDesktopGroupInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The download URL of the exported shared cloud desktop list file. The exported file contains the following details of shared cloud desktops:
        # 
        # - Shared cloud desktop ID/name
        # - Office network ID/name
        # - Shared cloud desktop template
        # - CPU/memory
        # - System cloud disk/data cloud disk
        # - Security policy name
        # - Number of currently authorized users
        # - Billing method
        # - Creation time
        # - Expiration time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

