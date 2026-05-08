# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketing_event20210101 import models as main_models
from darabonba.model import DaraModel

class QueryQwenConferenceSgTicketSearchPopResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryQwenConferenceSgTicketSearchPopResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryQwenConferenceSgTicketSearchPopResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryQwenConferenceSgTicketSearchPopResponseBodyData(DaraModel):
    def __init__(
        self,
        company_name: str = None,
        ext_fields: str = None,
        first_name: str = None,
        last_name: str = None,
        submit_id: int = None,
        ticket_token: str = None,
    ):
        self.company_name = company_name
        self.ext_fields = ext_fields
        self.first_name = first_name
        self.last_name = last_name
        self.submit_id = submit_id
        self.ticket_token = ticket_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.ext_fields is not None:
            result['ExtFields'] = self.ext_fields

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id

        if self.ticket_token is not None:
            result['TicketToken'] = self.ticket_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('ExtFields') is not None:
            self.ext_fields = m.get('ExtFields')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')

        if m.get('TicketToken') is not None:
            self.ticket_token = m.get('TicketToken')

        return self

