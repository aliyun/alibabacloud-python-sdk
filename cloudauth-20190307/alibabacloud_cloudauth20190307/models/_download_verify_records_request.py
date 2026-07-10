# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadVerifyRecordsRequest(DaraModel):
    def __init__(
        self,
        biz_param: str = None,
        product_type: str = None,
    ):
        # The query conditions in JSON string format. The following fields are included:
        # - **DownloadMode (String)**: the download mode.
        #   - Example: sync
        # - **InvokeType (String)**: the product plan, which corresponds to **ProductType**.
        # - **SceneIdList (List<Long>)**: the list of scene IDs.
        # - **StatisticsType (String)**: the statistics type. Valid values:
        #   - day
        #   - month
        # - **StartDate (String)**: the query start time.
        #   - Example: 2025-09-17 00:00:00 +0800
        # - **EndDate (String)**: the query end time.
        #   - Example: 2025-10-16 23:59:59 +0800
        # - **ProductProgramList**: the list of product codes under the product plan to query.
        #   - Example: ["FINANCE_FACE_VERIFY","MFVC"]
        # - **Code (information verification API)**: Valid values:
        #   - **ID_CARD_2_META**: ID card two-factor verification
        #   - **ID_PERIOD**: ID card validity period verification
        #   - **MOBILE_ONLINE_LENGTH**: mobile number online duration
        #   - **MOBILE_ONLINE_STATUS**: mobile number online status
        #   - **MOBILE_3_META_SIMPLE**: mobile number three-factor verification (basic)
        #   - **MOBILE_3_META**: mobile number three-factor verification (detailed)
        #   - **MOBILE_2_META**: mobile number two-factor verification
        #   - **BANK_CARD_N_META**: bank card verification (detailed)
        #   - **MOBILE_DETECT**: phone number detection 
        #   - **VEHICLE_N_META**: vehicle element verification (enhanced)
        #   - **VEHICLE_PENTA_INFO**: vehicle five-element information recognition
        #   - **VEHICLE_LICENSE_INFO**: vehicle information recognition
        #   - **VEHICLE_INSURE_DATE**: vehicle insurance date query
        #   - **VEHICLE_CHECK**: vehicle element verification
        # - **ProductCode (information verification)**: same as Code.
        self.biz_param = biz_param
        # The product type. Valid values:
        # - **FINANCE_VERIFY**: financial-grade ID Verification
        # - **SMART_VERIFY**: enhanced ID Verification (discontinued)
        # - **FACE_VERIFY**: ID Verification (discontinued)
        # - **INFO_CHECK_STATISTICS**: information verification.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

