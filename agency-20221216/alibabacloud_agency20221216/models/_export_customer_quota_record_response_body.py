# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class ExportCustomerQuotaRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ExportCustomerQuotaRecordResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # Code
        self.code = code
        # Data
        self.data = data
        # Description
        self.msg = msg
        # ID of the Request
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
            temp_model = main_models.ExportCustomerQuotaRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ExportCustomerQuotaRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        cost: int = None,
        id: int = None,
    ):
        # Estimated duration, in minutes.
        self.cost = cost
        # ID of Export task
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['Cost'] = self.cost

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

