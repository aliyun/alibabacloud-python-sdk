# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListOutboundCallRestrictionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListOutboundCallRestrictionsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The list of variable values in the error message.
        self.params = params
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.ListOutboundCallRestrictionsResponseBodyData()
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

class ListOutboundCallRestrictionsResponseBodyData(DaraModel):
    def __init__(
        self,
        outbound_call_restrictions: List[main_models.ListOutboundCallRestrictionsResponseBodyDataOutboundCallRestrictions] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data list.
        self.outbound_call_restrictions = outbound_call_restrictions
        # The page number, starting from 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records that match the conditions.
        self.total_count = total_count

    def validate(self):
        if self.outbound_call_restrictions:
            for v1 in self.outbound_call_restrictions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OutboundCallRestrictions'] = []
        if self.outbound_call_restrictions is not None:
            for k1 in self.outbound_call_restrictions:
                result['OutboundCallRestrictions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outbound_call_restrictions = []
        if m.get('OutboundCallRestrictions') is not None:
            for k1 in m.get('OutboundCallRestrictions'):
                temp_model = main_models.ListOutboundCallRestrictionsResponseBodyDataOutboundCallRestrictions()
                self.outbound_call_restrictions.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOutboundCallRestrictionsResponseBodyDataOutboundCallRestrictions(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        creator: str = None,
        number: str = None,
        policy: int = None,
        remark: str = None,
        restriction_id: str = None,
    ):
        # The creation time, in millisecond-level timestamp.
        self.created_time = created_time
        # The creator.
        self.creator = creator
        # The phone number.
        self.number = number
        # The policy. Valid values:
        # 0: blacklist.
        # 1: whitelist.
        self.policy = policy
        # The remark.
        self.remark = remark
        # The outbound call restriction ID.
        self.restriction_id = restriction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.number is not None:
            result['Number'] = self.number

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.restriction_id is not None:
            result['RestrictionId'] = self.restriction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RestrictionId') is not None:
            self.restriction_id = m.get('RestrictionId')

        return self

