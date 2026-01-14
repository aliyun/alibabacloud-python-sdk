# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetDocParsingResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDocParsingResultResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned result.
        self.data = data
        # ID of the request
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetDocParsingResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDocParsingResultResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
    ):
        # - The parsed content of the document.
        # - The format (markdown or json) is determined by the returnFormat parameter. For specific format details, refer to: [json return structure](https://www.alibabacloud.com/help/en/energy-expert/developer-reference/interface-attached-information#b644b6255cojj)
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        return self

