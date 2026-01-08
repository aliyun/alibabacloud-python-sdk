# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatappPhoneNumberMetricRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        end: int = None,
        granularity: str = None,
        isv_code: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start: int = None,
    ):
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end = end
        # The granularity of the metric.
        # 
        # Valid values:
        # 
        # *   DAILY
        # *   HALF_HOUR
        self.granularity = granularity
        # The independent software vendor (ISV) verification code, which is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        self.owner_id = owner_id
        # The business phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.end is not None:
            result['End'] = self.end

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

