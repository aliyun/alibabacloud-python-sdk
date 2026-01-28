# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTransferInListRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        simple_transfer_in_status: str = None,
        submission_end_date: int = None,
        submission_start_date: int = None,
        user_client_ip: str = None,
    ):
        self.domain_name = domain_name
        self.lang = lang
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.simple_transfer_in_status = simple_transfer_in_status
        self.submission_end_date = submission_end_date
        self.submission_start_date = submission_start_date
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status

        if self.submission_end_date is not None:
            result['SubmissionEndDate'] = self.submission_end_date

        if self.submission_start_date is not None:
            result['SubmissionStartDate'] = self.submission_start_date

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')

        if m.get('SubmissionEndDate') is not None:
            self.submission_end_date = m.get('SubmissionEndDate')

        if m.get('SubmissionStartDate') is not None:
            self.submission_start_date = m.get('SubmissionStartDate')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

