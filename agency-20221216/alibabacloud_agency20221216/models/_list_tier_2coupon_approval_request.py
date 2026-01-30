# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTier2CouponApprovalRequest(DaraModel):
    def __init__(
        self,
        application_sheet_id: str = None,
        approval_status: str = None,
        current_page: int = None,
        page_size: int = None,
        t_2partner_name: str = None,
        t_2partner_uid: int = None,
    ):
        self.application_sheet_id = application_sheet_id
        self.approval_status = approval_status
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        self.t_2partner_name = t_2partner_name
        self.t_2partner_uid = t_2partner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_sheet_id is not None:
            result['ApplicationSheetId'] = self.application_sheet_id

        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.t_2partner_name is not None:
            result['T2PartnerName'] = self.t_2partner_name

        if self.t_2partner_uid is not None:
            result['T2PartnerUid'] = self.t_2partner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationSheetId') is not None:
            self.application_sheet_id = m.get('ApplicationSheetId')

        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('T2PartnerName') is not None:
            self.t_2partner_name = m.get('T2PartnerName')

        if m.get('T2PartnerUid') is not None:
            self.t_2partner_uid = m.get('T2PartnerUid')

        return self

