# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSubPartnerListRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        sub_partner_company_name: str = None,
        sub_partner_pid: str = None,
    ):
        # The page number, starting from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The company name of the secondary partner.
        self.sub_partner_company_name = sub_partner_company_name
        # The PID of the secondary partner.
        self.sub_partner_pid = sub_partner_pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sub_partner_company_name is not None:
            result['SubPartnerCompanyName'] = self.sub_partner_company_name

        if self.sub_partner_pid is not None:
            result['SubPartnerPid'] = self.sub_partner_pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SubPartnerCompanyName') is not None:
            self.sub_partner_company_name = m.get('SubPartnerCompanyName')

        if m.get('SubPartnerPid') is not None:
            self.sub_partner_pid = m.get('SubPartnerPid')

        return self

