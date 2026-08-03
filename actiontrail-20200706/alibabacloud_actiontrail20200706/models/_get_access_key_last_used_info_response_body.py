# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccessKeyLastUsedInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        account_id: str = None,
        account_type: str = None,
        detail: str = None,
        owner_id: str = None,
        request_id: str = None,
        service_name: str = None,
        service_name_cn: str = None,
        service_name_en: str = None,
        source: str = None,
        used_timestamp: int = None,
        user_name: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The Alibaba Cloud account ID.
        self.account_id = account_id
        # The type of the account to which the AccessKey pair belongs.
        self.account_type = account_type
        # The event details.
        self.detail = detail
        # The ID of the account to which the AccessKey pair belongs.
        self.owner_id = owner_id
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The Alibaba Cloud service that was last accessed.
        # 
        # This parameter is required.
        self.service_name = service_name
        # The Chinese name of the Alibaba Cloud service that was last accessed.
        self.service_name_cn = service_name_cn
        # The English name of the Alibaba Cloud service that was last accessed.
        self.service_name_en = service_name_en
        # The source of the last usage record.
        self.source = source
        # The timestamp when the AccessKey pair was last used. Unit: milliseconds.
        # 
        # This parameter is required.
        self.used_timestamp = used_timestamp
        # The name of the account to which the AccessKey pair belongs.
        # 
        # If the value of the AccountType parameter is root-account, the value of the UserName parameter is root. If the value of the AccountType parameter is ram-user, the value of the UserName parameter is the name of a RAM user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_name_cn is not None:
            result['ServiceNameCn'] = self.service_name_cn

        if self.service_name_en is not None:
            result['ServiceNameEn'] = self.service_name_en

        if self.source is not None:
            result['Source'] = self.source

        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceNameCn') is not None:
            self.service_name_cn = m.get('ServiceNameCn')

        if m.get('ServiceNameEn') is not None:
            self.service_name_en = m.get('ServiceNameEn')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

