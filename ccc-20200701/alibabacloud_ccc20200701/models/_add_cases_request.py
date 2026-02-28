# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class AddCasesRequest(DaraModel):
    def __init__(
        self,
        campaign_id: str = None,
        case_list: List[main_models.AddCasesRequestCaseList] = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.campaign_id = campaign_id
        self.case_list = case_list
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.case_list:
            for v1 in self.case_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        result['CaseList'] = []
        if self.case_list is not None:
            for k1 in self.case_list:
                result['CaseList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        self.case_list = []
        if m.get('CaseList') is not None:
            for k1 in m.get('CaseList'):
                temp_model = main_models.AddCasesRequestCaseList()
                self.case_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self



class AddCasesRequestCaseList(DaraModel):
    def __init__(
        self,
        caller: str = None,
        custom_variables: str = None,
        masked_callee: str = None,
        phone_number: str = None,
        reference_id: str = None,
    ):
        self.caller = caller
        self.custom_variables = custom_variables
        self.masked_callee = masked_callee
        self.phone_number = phone_number
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

