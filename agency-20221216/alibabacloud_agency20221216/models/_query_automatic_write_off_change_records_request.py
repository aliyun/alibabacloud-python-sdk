# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAutomaticWriteOffChangeRecordsRequest(DaraModel):
    def __init__(
        self,
        customer_uid: int = None,
        end_date: str = None,
        language: str = None,
        page_no: int = None,
        page_size: int = None,
        start_date: str = None,
    ):
        # The customer UID.
        # 
        # This parameter is required.
        self.customer_uid = customer_uid
        # The end date.
        # Format: yyyy-MM-dd.
        self.end_date = end_date
        # The language. If you do not specify this parameter, English is used by default. Valid values:
        # - en: English.
        # - zh: Chinese.
        # - ja: Japanese.
        self.language = language
        # The page number. Pages start from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The start date.
        # Format: yyyy-MM-dd.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.language is not None:
            result['Language'] = self.language

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

