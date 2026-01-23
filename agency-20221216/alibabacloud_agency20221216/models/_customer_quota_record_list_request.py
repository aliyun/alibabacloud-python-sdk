# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomerQuotaRecordListRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        end_user_pk: int = None,
        language: str = None,
        operation_type: str = None,
        page_no: int = None,
        page_size: int = None,
        start_date: str = None,
    ):
        # End Date Format: yyyy-MM-dd
        # 
        # This parameter is required.
        self.end_date = end_date
        # Customer UID
        # 
        # This parameter is required.
        self.end_user_pk = end_user_pk
        # Multilingual Parameters, the default language is English.</br>
        # en: English</br>
        # zh: Chinese</br>
        # ja: Japanese </br>
        self.language = language
        # Operation Type Enum</br>
        # all All types</br>
        # quota_create Create quota</br>
        # quota_amount_adjust Adjust the amount of quota</br>
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # Pagination, current page number, starting from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # Pagination, record number on each page. Maximum 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Start Date Format: yyyy-MM-dd
        # 
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.end_user_pk is not None:
            result['EndUserPk'] = self.end_user_pk

        if self.language is not None:
            result['Language'] = self.language

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('EndUserPk') is not None:
            self.end_user_pk = m.get('EndUserPk')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

