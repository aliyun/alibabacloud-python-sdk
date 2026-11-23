# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MosQueryRegistrationInfoRequest(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        checkin_status: str = None,
        keyword: str = None,
        page: str = None,
        page_size: str = None,
        qr_code: str = None,
    ):
        self.activity_id = activity_id
        self.checkin_status = checkin_status
        self.keyword = keyword
        self.page = page
        self.page_size = page_size
        self.qr_code = qr_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.checkin_status is not None:
            result['CheckinStatus'] = self.checkin_status

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.qr_code is not None:
            result['QrCode'] = self.qr_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('CheckinStatus') is not None:
            self.checkin_status = m.get('CheckinStatus')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')

        return self

