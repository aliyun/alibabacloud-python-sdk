# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetIcpFilingInfoForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetIcpFilingInfoForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetIcpFilingInfoForPartnerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIcpFilingInfoForPartnerResponseBodyData(DaraModel):
    def __init__(
        self,
        icp_number: str = None,
        recorded: bool = None,
        site_record_number: str = None,
    ):
        self.icp_number = icp_number
        self.recorded = recorded
        self.site_record_number = site_record_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number

        if self.recorded is not None:
            result['Recorded'] = self.recorded

        if self.site_record_number is not None:
            result['SiteRecordNumber'] = self.site_record_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')

        if m.get('Recorded') is not None:
            self.recorded = m.get('Recorded')

        if m.get('SiteRecordNumber') is not None:
            self.site_record_number = m.get('SiteRecordNumber')

        return self

