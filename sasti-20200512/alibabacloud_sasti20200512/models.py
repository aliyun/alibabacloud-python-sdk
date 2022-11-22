# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class DescribeDomainReportRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        field: str = None,
    ):
        self.domain = domain
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.field is not None:
            result['Field'] = self.field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        return self


class DescribeDomainReportResponseBody(TeaModel):
    def __init__(
        self,
        attack_cnt_by_threat_type: str = None,
        attack_preference_top_5: str = None,
        basic: str = None,
        confidence: str = None,
        context: str = None,
        domain: str = None,
        group: str = None,
        intelligences: str = None,
        request_id: str = None,
        scenario: str = None,
        ssl_cert: str = None,
        threat_level: str = None,
        threat_types: str = None,
        whois: str = None,
    ):
        self.attack_cnt_by_threat_type = attack_cnt_by_threat_type
        self.attack_preference_top_5 = attack_preference_top_5
        self.basic = basic
        self.confidence = confidence
        self.context = context
        self.domain = domain
        self.group = group
        self.intelligences = intelligences
        self.request_id = request_id
        self.scenario = scenario
        self.ssl_cert = ssl_cert
        self.threat_level = threat_level
        self.threat_types = threat_types
        self.whois = whois

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_cnt_by_threat_type is not None:
            result['AttackCntByThreatType'] = self.attack_cnt_by_threat_type
        if self.attack_preference_top_5 is not None:
            result['AttackPreferenceTop5'] = self.attack_preference_top_5
        if self.basic is not None:
            result['Basic'] = self.basic
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.context is not None:
            result['Context'] = self.context
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.group is not None:
            result['Group'] = self.group
        if self.intelligences is not None:
            result['Intelligences'] = self.intelligences
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.ssl_cert is not None:
            result['SslCert'] = self.ssl_cert
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_types is not None:
            result['ThreatTypes'] = self.threat_types
        if self.whois is not None:
            result['Whois'] = self.whois
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackCntByThreatType') is not None:
            self.attack_cnt_by_threat_type = m.get('AttackCntByThreatType')
        if m.get('AttackPreferenceTop5') is not None:
            self.attack_preference_top_5 = m.get('AttackPreferenceTop5')
        if m.get('Basic') is not None:
            self.basic = m.get('Basic')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Intelligences') is not None:
            self.intelligences = m.get('Intelligences')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('SslCert') is not None:
            self.ssl_cert = m.get('SslCert')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatTypes') is not None:
            self.threat_types = m.get('ThreatTypes')
        if m.get('Whois') is not None:
            self.whois = m.get('Whois')
        return self


class DescribeDomainReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


