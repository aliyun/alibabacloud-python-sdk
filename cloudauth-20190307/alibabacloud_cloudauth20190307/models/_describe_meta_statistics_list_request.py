# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetaStatisticsListRequest(DaraModel):
    def __init__(
        self,
        api: str = None,
        end_date: int = None,
        start_date: int = None,
    ):
        # The commodity code. Valid values:
        # - **ID_CARD_2_META**: ID card two-element verification
        # - **ID_PERIOD**: ID card validity period verification
        # - **MOBILE_ONLINE_LENGTH**: mobile number online duration
        # - **MOBILE_ONLINE_STATUS**: mobile number online status
        # - **MOBILE_3_META_SIMPLE**: mobile number three-element verification (simple edition)
        # - **MOBILE_3_META**: mobile number three-element verification (detailed edition)
        # - **MOBILE_2_META**: mobile number two-element verification
        # - **BANK_CARD_N_META**: bank card verification (detailed edition)
        # - **MOBILE_DETECT**: phone number detection
        # - **VEHICLE_N_META**: vehicle element verification (enhanced edition)
        # - **VEHICLE_PENTA_INFO**: vehicle five-element information recognition
        # - **VEHICLE_LICENSE_INFO**: vehicle information recognition
        # - **VEHICLE_INSURE_DATE**: vehicle insurance date query
        # - **VEHICLE_CHECK**: vehicle element verification.
        # 
        # This parameter is required.
        self.api = api
        # The end time of the query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The start time of the query. The value is a UNIX timestamp. Unit: milliseconds.
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
        if self.api is not None:
            result['Api'] = self.api

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

