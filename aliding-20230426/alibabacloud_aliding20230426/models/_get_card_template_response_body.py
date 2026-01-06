# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetCardTemplateResponseBody(DaraModel):
    def __init__(
        self,
        common_variable_list: List[main_models.GetCardTemplateResponseBodyCommonVariableList] = None,
        request_id: str = None,
        status: str = None,
        template_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.common_variable_list = common_variable_list
        self.request_id = request_id
        self.status = status
        self.template_id = template_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.common_variable_list:
            for v1 in self.common_variable_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['commonVariableList'] = []
        if self.common_variable_list is not None:
            for k1 in self.common_variable_list:
                result['commonVariableList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_variable_list = []
        if m.get('commonVariableList') is not None:
            for k1 in m.get('commonVariableList'):
                temp_model = main_models.GetCardTemplateResponseBodyCommonVariableList()
                self.common_variable_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetCardTemplateResponseBodyCommonVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        if_private_filed: bool = None,
        name: str = None,
        type: str = None,
    ):
        self.description = description
        # Id
        self.id = id
        self.if_private_filed = if_private_filed
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.if_private_filed is not None:
            result['IfPrivateFiled'] = self.if_private_filed

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IfPrivateFiled') is not None:
            self.if_private_filed = m.get('IfPrivateFiled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

