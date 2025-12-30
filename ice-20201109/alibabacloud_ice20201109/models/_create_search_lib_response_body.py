# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSearchLibResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        search_lib_name: str = None,
        success: str = None,
    ):
        # The status code returned.
        self.code = code
        # The ID of the request.
        self.request_id = request_id
        # The name of the search library.
        self.search_lib_name = search_lib_name
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

