# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class AppendCasesRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        cases: List[main_models.AppendCasesRequestCases] = None,
        instance_id: str = None,
    ):
        # The outbound call task ID.
        # 
        # This parameter is required.
        self.campaign_id = campaign_id
        # The list of contacts.
        # 
        # This parameter is required.
        self.cases = cases
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.cases:
            for v1 in self.cases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        result['Cases'] = []
        if self.cases is not None:
            for k1 in self.cases:
                result['Cases'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        self.cases = []
        if m.get('Cases') is not None:
            for k1 in m.get('Cases'):
                temp_model = main_models.AppendCasesRequestCases()
                self.cases.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self



class AppendCasesRequestCases(DaraModel):
    def __init__(
        self,
        custom_variables: str = None,
        phone_number: str = None,
        priority: int = None,
        reference_id: str = None,
    ):
        # The custom variables defined by the customer. The value is a JSON object that contains up to 10 properties. The name and value of each property are defined by the customer.
        self.custom_variables = custom_variables
        # The phone number of the contact.
        self.phone_number = phone_number
        # The priority.
        self.priority = priority
        # The business system ID of the contact.
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        return self

