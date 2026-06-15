# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetTuneProposalByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTuneProposalByIdResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTuneProposalByIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTuneProposalByIdResponseBodyData(DaraModel):
    def __init__(
        self,
        json_content: str = None,
    ):
        self.json_content = json_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_content is not None:
            result['JsonContent'] = self.json_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonContent') is not None:
            self.json_content = m.get('JsonContent')

        return self

