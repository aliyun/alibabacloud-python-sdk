# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafServiceResponseBody(DaraModel):
    def __init__(
        self,
        edition: str = None,
        enabled: str = None,
        opening_time: str = None,
        request_billing_type: str = None,
        request_id: str = None,
        rule_billing_type: str = None,
        status: str = None,
    ):
        # The edition of WAF.
        self.edition = edition
        # The status of WAF. Valid values:
        # 
        # *   on
        # *   off
        self.enabled = enabled
        # The time when WAF was enabled.
        self.opening_time = opening_time
        # The metering method for requests.
        self.request_billing_type = request_billing_type
        # The ID of the request.
        self.request_id = request_id
        # The metering method for rules. You are charged for the number of SeCUs.
        self.rule_billing_type = rule_billing_type
        # The status of WAF. Valid values:
        # 
        # *   Normal
        # *   WaitForExpire
        # *   Expired
        # *   Released
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time

        if self.request_billing_type is not None:
            result['RequestBillingType'] = self.request_billing_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_billing_type is not None:
            result['RuleBillingType'] = self.rule_billing_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')

        if m.get('RequestBillingType') is not None:
            self.request_billing_type = m.get('RequestBillingType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleBillingType') is not None:
            self.rule_billing_type = m.get('RuleBillingType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

