# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTransferDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        from_user_id: int = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        target_user_id: int = None,
        transfer_type: str = None,
    ):
        # Specifies the domain name for which you want to view the transfer record.
        self.domain_name = domain_name
        # The user ID from which the domain name was transferred to the current account.
        self.from_user_id = from_user_id
        # The language.
        self.lang = lang
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The user ID to which the domain name was transferred from the current account.
        self.target_user_id = target_user_id
        # The transfer type. Valid values:
        # 
        # *   IN: The domain name was transferred to the current account.
        # *   OUT: The domain name was transferred from the current account.
        # 
        # This parameter is required.
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')

        return self

