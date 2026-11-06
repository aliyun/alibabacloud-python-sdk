# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListCorpNumbersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCorpNumbersResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned by the API.
        self.message = message
        # The list of variable values in the error message.
        self.params = params
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListCorpNumbersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCorpNumbersResponseBodyData(DaraModel):
    def __init__(
        self,
        corp_numbers: List[main_models.ListCorpNumbersResponseBodyDataCorpNumbers] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of tenant numbers.
        self.corp_numbers = corp_numbers
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.corp_numbers:
            for v1 in self.corp_numbers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CorpNumbers'] = []
        if self.corp_numbers is not None:
            for k1 in self.corp_numbers:
                result['CorpNumbers'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.corp_numbers = []
        if m.get('CorpNumbers') is not None:
            for k1 in m.get('CorpNumbers'):
                temp_model = main_models.ListCorpNumbersResponseBodyDataCorpNumbers()
                self.corp_numbers.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCorpNumbersResponseBodyDataCorpNumbers(DaraModel):
    def __init__(
        self,
        instance_names: List[str] = None,
        number: str = None,
        sip_trunk_id: str = None,
        sip_trunk_name: str = None,
    ):
        # The list of instance names associated with the number.
        self.instance_names = instance_names
        # The phone number.
        self.number = number
        # The SIP trunk ID.
        self.sip_trunk_id = sip_trunk_id
        # The SIP trunk name.
        self.sip_trunk_name = sip_trunk_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_names is not None:
            result['InstanceNames'] = self.instance_names

        if self.number is not None:
            result['Number'] = self.number

        if self.sip_trunk_id is not None:
            result['SipTrunkId'] = self.sip_trunk_id

        if self.sip_trunk_name is not None:
            result['SipTrunkName'] = self.sip_trunk_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceNames') is not None:
            self.instance_names = m.get('InstanceNames')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('SipTrunkId') is not None:
            self.sip_trunk_id = m.get('SipTrunkId')

        if m.get('SipTrunkName') is not None:
            self.sip_trunk_name = m.get('SipTrunkName')

        return self

