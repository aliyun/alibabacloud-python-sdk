# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class CheckDcdnProjectExistResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.CheckDcdnProjectExistResponseBodyContent = None,
        request_id: str = None,
    ):
        # The returned results.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.CheckDcdnProjectExistResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckDcdnProjectExistResponseBodyContent(DaraModel):
    def __init__(
        self,
        exist: str = None,
    ):
        # Indicates whether the real-time log delivery project exists. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.exist = exist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exist is not None:
            result['Exist'] = self.exist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')

        return self

