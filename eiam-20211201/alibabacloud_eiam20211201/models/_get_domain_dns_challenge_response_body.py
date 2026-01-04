# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetDomainDnsChallengeResponseBody(DaraModel):
    def __init__(
        self,
        domain_dns_challenge: main_models.GetDomainDnsChallengeResponseBodyDomainDnsChallenge = None,
        request_id: str = None,
    ):
        # The DNS challenge records.
        self.domain_dns_challenge = domain_dns_challenge
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_dns_challenge:
            self.domain_dns_challenge.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_dns_challenge is not None:
            result['DomainDnsChallenge'] = self.domain_dns_challenge.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainDnsChallenge') is not None:
            temp_model = main_models.GetDomainDnsChallengeResponseBodyDomainDnsChallenge()
            self.domain_dns_challenge = temp_model.from_map(m.get('DomainDnsChallenge'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDomainDnsChallengeResponseBodyDomainDnsChallenge(DaraModel):
    def __init__(
        self,
        dns_challenge_name: str = None,
        dns_challenge_value: str = None,
        dns_type: str = None,
    ):
        # The name of the DNS challenge record.
        self.dns_challenge_name = dns_challenge_name
        # The value of the DNS challenge record.
        self.dns_challenge_value = dns_challenge_value
        # The type of the DNS challenge record.
        self.dns_type = dns_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_challenge_name is not None:
            result['DnsChallengeName'] = self.dns_challenge_name

        if self.dns_challenge_value is not None:
            result['DnsChallengeValue'] = self.dns_challenge_value

        if self.dns_type is not None:
            result['DnsType'] = self.dns_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsChallengeName') is not None:
            self.dns_challenge_name = m.get('DnsChallengeName')

        if m.get('DnsChallengeValue') is not None:
            self.dns_challenge_value = m.get('DnsChallengeValue')

        if m.get('DnsType') is not None:
            self.dns_type = m.get('DnsType')

        return self

