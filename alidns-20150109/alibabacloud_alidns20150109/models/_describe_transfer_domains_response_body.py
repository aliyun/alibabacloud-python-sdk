# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeTransferDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domain_transfers: main_models.DescribeTransferDomainsResponseBodyDomainTransfers = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain names that were transferred between accounts.
        self.domain_transfers = domain_transfers
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domain_transfers:
            self.domain_transfers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_transfers is not None:
            result['DomainTransfers'] = self.domain_transfers.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainTransfers') is not None:
            temp_model = main_models.DescribeTransferDomainsResponseBodyDomainTransfers()
            self.domain_transfers = temp_model.from_map(m.get('DomainTransfers'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTransferDomainsResponseBodyDomainTransfers(DaraModel):
    def __init__(
        self,
        domain_transfer: List[main_models.DescribeTransferDomainsResponseBodyDomainTransfersDomainTransfer] = None,
    ):
        self.domain_transfer = domain_transfer

    def validate(self):
        if self.domain_transfer:
            for v1 in self.domain_transfer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainTransfer'] = []
        if self.domain_transfer is not None:
            for k1 in self.domain_transfer:
                result['DomainTransfer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_transfer = []
        if m.get('DomainTransfer') is not None:
            for k1 in m.get('DomainTransfer'):
                temp_model = main_models.DescribeTransferDomainsResponseBodyDomainTransfersDomainTransfer()
                self.domain_transfer.append(temp_model.from_map(k1))

        return self

class DescribeTransferDomainsResponseBodyDomainTransfersDomainTransfer(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        domain_name: str = None,
        from_user_id: int = None,
        id: int = None,
        target_user_id: int = None,
    ):
        # The time when the domain name was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the domain name was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The domain name.
        self.domain_name = domain_name
        # The user ID from which the domain name was transferred.
        self.from_user_id = from_user_id
        # The ID of the domain name that was transferred.
        self.id = id
        # The user ID to which the domain name was transferred.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id

        if self.id is not None:
            result['Id'] = self.id

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

