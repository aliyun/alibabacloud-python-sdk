# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckServiceDeployableRequest(DaraModel):
    def __init__(
        self,
        post_paid_amount: str = None,
        pre_paid_amount: str = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # Total amount of postpaid.
        self.post_paid_amount = post_paid_amount
        # Total amount of prepayment.
        self.pre_paid_amount = pre_paid_amount
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        self.template_name = template_name
        # The trial type of the service instance. Valid values:
        # 
        # *   **Trial**: Trials are supported.
        # *   **NotTrial**: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.post_paid_amount is not None:
            result['PostPaidAmount'] = self.post_paid_amount

        if self.pre_paid_amount is not None:
            result['PrePaidAmount'] = self.pre_paid_amount

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.trial_type is not None:
            result['TrialType'] = self.trial_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostPaidAmount') is not None:
            self.post_paid_amount = m.get('PostPaidAmount')

        if m.get('PrePaidAmount') is not None:
            self.pre_paid_amount = m.get('PrePaidAmount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')

        return self

