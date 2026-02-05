# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListAllTenantBindNumberBindingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAllTenantBindNumberBindingResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.ListAllTenantBindNumberBindingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAllTenantBindNumberBindingResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAllTenantBindNumberBindingResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListAllTenantBindNumberBindingResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class ListAllTenantBindNumberBindingResponseBodyDataList(DaraModel):
    def __init__(
        self,
        billing_type: str = None,
        binding_id: str = None,
        instance_name_list: List[str] = None,
        number: str = None,
        serialized_params: str = None,
        trunk_name: str = None,
    ):
        self.billing_type = billing_type
        self.binding_id = binding_id
        self.instance_name_list = instance_name_list
        self.number = number
        self.serialized_params = serialized_params
        self.trunk_name = trunk_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type

        if self.binding_id is not None:
            result['BindingId'] = self.binding_id

        if self.instance_name_list is not None:
            result['InstanceNameList'] = self.instance_name_list

        if self.number is not None:
            result['Number'] = self.number

        if self.serialized_params is not None:
            result['SerializedParams'] = self.serialized_params

        if self.trunk_name is not None:
            result['TrunkName'] = self.trunk_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')

        if m.get('BindingId') is not None:
            self.binding_id = m.get('BindingId')

        if m.get('InstanceNameList') is not None:
            self.instance_name_list = m.get('InstanceNameList')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('SerializedParams') is not None:
            self.serialized_params = m.get('SerializedParams')

        if m.get('TrunkName') is not None:
            self.trunk_name = m.get('TrunkName')

        return self

