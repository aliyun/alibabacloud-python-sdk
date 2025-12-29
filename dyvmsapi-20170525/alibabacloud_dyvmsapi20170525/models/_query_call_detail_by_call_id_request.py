# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCallDetailByCallIdRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        owner_id: int = None,
        prod_id: int = None,
        query_date: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The unique ID of the call.
        # 
        # > 
        # 
        # *   The CallId parameter is included in the response parameters of the outbound call operation that you call to initiate a call.
        # 
        # *   The date when the call specified by CallId is started must be the same as the date specified by QueryDate.
        # 
        # *   The value of CallId must match the value of ProdId.
        # 
        # This parameter is required.
        self.call_id = call_id
        self.owner_id = owner_id
        # The service ID. Valid values:
        # 
        # *   **11000000300006**: voice notification. You can call the [SingleCallByVoice](https://help.aliyun.com/document_detail/393517.html) operation to send a voice notification of the voice notification file type to the specified number.
        # *   **11010000138001**: voice verification code. You can call the [SingleCallByTts](https://help.aliyun.com/document_detail/393519.html) operation to send a voice verification code or a text-to-speech (TTS) voice notification to the specified number.
        # *   **11000000300005**: IVR. You can call the [IvrCall](https://help.aliyun.com/document_detail/393521.html) operation to initiate an interactive voice call to the specified number.
        # *   **11000000300009**: Session Initiation Protocol (SIP) call.
        # *   **11030000180001**: intelligent outbound call.
        # 
        # This parameter is required.
        self.prod_id = prod_id
        # The time at which call details are queried. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > The system queries the call records that are generated within 24 hours after the specified point in time. For example, if you specify the time 20:00:01 on November 21, 2022, the system queries the call records that are generated for the specified call ID from 20:00:01 on November 21, 2022, to 20:00:01 on November 22, 2022.
        # 
        # This parameter is required.
        self.query_date = query_date
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_id is not None:
            result['ProdId'] = self.prod_id

        if self.query_date is not None:
            result['QueryDate'] = self.query_date

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')

        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

