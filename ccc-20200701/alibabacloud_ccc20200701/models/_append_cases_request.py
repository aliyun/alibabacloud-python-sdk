# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class AppendCasesRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        instance_id: str = None,
        body: List[main_models.AppendCasesRequestBody] = None,
    ):
        # The predictive outbound campaign ID.
        # 
        # This parameter is required.
        self.campaign_id = campaign_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of outbound call cases in the request body.
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.AppendCasesRequestBody()
                self.body.append(temp_model.from_map(k1))

        return self

class AppendCasesRequestBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        caller: str = None,
        custom_variables: str = None,
        masked_callee: str = None,
        phone_number: str = None,
        reference_id: str = None,
    ):
        # The agent ID of the specified agent to which the call is transferred. If this field is not empty, the system transfers the call to the specified agent. If this field is empty, the system assigns the call to an idle agent in the skill group.
        self.agent_id = agent_id
        # The caller number. If this field is not empty, the outbound call system preferentially uses the provided number as the caller to initiate the call. If this field is empty, the system automatically selects a caller number.
        self.caller = caller
        # The custom variables defined by the customer. The value is a JSON object that contains up to 10 properties. The name and value of each property are defined by the customer.
        self.custom_variables = custom_variables
        # The masked callee number. If this field is not empty, the callee number is masked based on custom rules defined by the customer. You only need to enter the masked callee number. If a masked callee number is used, the masked number is displayed in certain scenarios, and the actual callee number cannot be viewed.
        self.masked_callee = masked_callee
        # The phone number of the contact.
        self.phone_number = phone_number
        # The business ID, which is the identifier in the customer\\"s business system and is used for integration scenarios.
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables

        if self.masked_callee is not None:
            result['MaskedCallee'] = self.masked_callee

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')

        if m.get('MaskedCallee') is not None:
            self.masked_callee = m.get('MaskedCallee')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        return self

