# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class QuerySecurityCheckReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySecurityCheckReportResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySecurityCheckReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySecurityCheckReportResponseBodyData(DaraModel):
    def __init__(
        self,
        cloud_security_guide: int = None,
        config_check_number: int = None,
        contact_check_number: int = None,
        risk_event_number: int = None,
        sas_check_number: int = None,
        security_status: int = None,
        suggestion_text: str = None,
    ):
        self.cloud_security_guide = cloud_security_guide
        self.config_check_number = config_check_number
        self.contact_check_number = contact_check_number
        self.risk_event_number = risk_event_number
        self.sas_check_number = sas_check_number
        self.security_status = security_status
        self.suggestion_text = suggestion_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_security_guide is not None:
            result['CloudSecurityGuide'] = self.cloud_security_guide

        if self.config_check_number is not None:
            result['ConfigCheckNumber'] = self.config_check_number

        if self.contact_check_number is not None:
            result['ContactCheckNumber'] = self.contact_check_number

        if self.risk_event_number is not None:
            result['RiskEventNumber'] = self.risk_event_number

        if self.sas_check_number is not None:
            result['SasCheckNumber'] = self.sas_check_number

        if self.security_status is not None:
            result['SecurityStatus'] = self.security_status

        if self.suggestion_text is not None:
            result['SuggestionText'] = self.suggestion_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudSecurityGuide') is not None:
            self.cloud_security_guide = m.get('CloudSecurityGuide')

        if m.get('ConfigCheckNumber') is not None:
            self.config_check_number = m.get('ConfigCheckNumber')

        if m.get('ContactCheckNumber') is not None:
            self.contact_check_number = m.get('ContactCheckNumber')

        if m.get('RiskEventNumber') is not None:
            self.risk_event_number = m.get('RiskEventNumber')

        if m.get('SasCheckNumber') is not None:
            self.sas_check_number = m.get('SasCheckNumber')

        if m.get('SecurityStatus') is not None:
            self.security_status = m.get('SecurityStatus')

        if m.get('SuggestionText') is not None:
            self.suggestion_text = m.get('SuggestionText')

        return self

