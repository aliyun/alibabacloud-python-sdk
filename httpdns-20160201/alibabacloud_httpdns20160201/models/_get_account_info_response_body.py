# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_httpdns20160201 import models as main_models
from darabonba.model import DaraModel

class GetAccountInfoResponseBody(DaraModel):
    def __init__(
        self,
        account_info: main_models.GetAccountInfoResponseBodyAccountInfo = None,
        request_id: str = None,
    ):
        self.account_info = account_info
        self.request_id = request_id

    def validate(self):
        if self.account_info:
            self.account_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_info is not None:
            result['AccountInfo'] = self.account_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountInfo') is not None:
            temp_model = main_models.GetAccountInfoResponseBodyAccountInfo()
            self.account_info = temp_model.from_map(m.get('AccountInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccountInfoResponseBodyAccountInfo(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        doh_enabled: bool = None,
        doh_resolve_all_enabled: bool = None,
        month_doh_resolve_count: int = None,
        month_free_count: int = None,
        month_http_aes_resolve_count: int = None,
        month_https_aes_resolve_count: int = None,
        month_https_resolve_count: int = None,
        month_resolve_count: int = None,
        package_count: int = None,
        sign_secret: str = None,
        signed_count: int = None,
        unsigned_count: int = None,
        unsigned_enabled: bool = None,
        user_status: int = None,
    ):
        self.account_id = account_id
        self.doh_enabled = doh_enabled
        self.doh_resolve_all_enabled = doh_resolve_all_enabled
        self.month_doh_resolve_count = month_doh_resolve_count
        self.month_free_count = month_free_count
        self.month_http_aes_resolve_count = month_http_aes_resolve_count
        self.month_https_aes_resolve_count = month_https_aes_resolve_count
        self.month_https_resolve_count = month_https_resolve_count
        self.month_resolve_count = month_resolve_count
        self.package_count = package_count
        self.sign_secret = sign_secret
        self.signed_count = signed_count
        self.unsigned_count = unsigned_count
        self.unsigned_enabled = unsigned_enabled
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.doh_enabled is not None:
            result['DohEnabled'] = self.doh_enabled

        if self.doh_resolve_all_enabled is not None:
            result['DohResolveAllEnabled'] = self.doh_resolve_all_enabled

        if self.month_doh_resolve_count is not None:
            result['MonthDohResolveCount'] = self.month_doh_resolve_count

        if self.month_free_count is not None:
            result['MonthFreeCount'] = self.month_free_count

        if self.month_http_aes_resolve_count is not None:
            result['MonthHttpAesResolveCount'] = self.month_http_aes_resolve_count

        if self.month_https_aes_resolve_count is not None:
            result['MonthHttpsAesResolveCount'] = self.month_https_aes_resolve_count

        if self.month_https_resolve_count is not None:
            result['MonthHttpsResolveCount'] = self.month_https_resolve_count

        if self.month_resolve_count is not None:
            result['MonthResolveCount'] = self.month_resolve_count

        if self.package_count is not None:
            result['PackageCount'] = self.package_count

        if self.sign_secret is not None:
            result['SignSecret'] = self.sign_secret

        if self.signed_count is not None:
            result['SignedCount'] = self.signed_count

        if self.unsigned_count is not None:
            result['UnsignedCount'] = self.unsigned_count

        if self.unsigned_enabled is not None:
            result['UnsignedEnabled'] = self.unsigned_enabled

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DohEnabled') is not None:
            self.doh_enabled = m.get('DohEnabled')

        if m.get('DohResolveAllEnabled') is not None:
            self.doh_resolve_all_enabled = m.get('DohResolveAllEnabled')

        if m.get('MonthDohResolveCount') is not None:
            self.month_doh_resolve_count = m.get('MonthDohResolveCount')

        if m.get('MonthFreeCount') is not None:
            self.month_free_count = m.get('MonthFreeCount')

        if m.get('MonthHttpAesResolveCount') is not None:
            self.month_http_aes_resolve_count = m.get('MonthHttpAesResolveCount')

        if m.get('MonthHttpsAesResolveCount') is not None:
            self.month_https_aes_resolve_count = m.get('MonthHttpsAesResolveCount')

        if m.get('MonthHttpsResolveCount') is not None:
            self.month_https_resolve_count = m.get('MonthHttpsResolveCount')

        if m.get('MonthResolveCount') is not None:
            self.month_resolve_count = m.get('MonthResolveCount')

        if m.get('PackageCount') is not None:
            self.package_count = m.get('PackageCount')

        if m.get('SignSecret') is not None:
            self.sign_secret = m.get('SignSecret')

        if m.get('SignedCount') is not None:
            self.signed_count = m.get('SignedCount')

        if m.get('UnsignedCount') is not None:
            self.unsigned_count = m.get('UnsignedCount')

        if m.get('UnsignedEnabled') is not None:
            self.unsigned_enabled = m.get('UnsignedEnabled')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

