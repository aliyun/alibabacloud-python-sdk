# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class GetEndpointAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetEndpointAttributeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the response.
        self.status = status
        # Indicates whether the request was successful.
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

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetEndpointAttributeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEndpointAttributeResponseBodyData(DaraModel):
    def __init__(
        self,
        cidr_list: List[main_models.GetEndpointAttributeResponseBodyDataCidrList] = None,
        endpoint_enabled: bool = None,
    ):
        # The list of CIDR blocks.
        self.cidr_list = cidr_list
        # Indicates whether the endpoint is enabled.
        self.endpoint_enabled = endpoint_enabled

    def validate(self):
        if self.cidr_list:
            for v1 in self.cidr_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CidrList'] = []
        if self.cidr_list is not None:
            for k1 in self.cidr_list:
                result['CidrList'].append(k1.to_map() if k1 else None)

        if self.endpoint_enabled is not None:
            result['EndpointEnabled'] = self.endpoint_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cidr_list = []
        if m.get('CidrList') is not None:
            for k1 in m.get('CidrList'):
                temp_model = main_models.GetEndpointAttributeResponseBodyDataCidrList()
                self.cidr_list.append(temp_model.from_map(k1))

        if m.get('EndpointEnabled') is not None:
            self.endpoint_enabled = m.get('EndpointEnabled')

        return self

class GetEndpointAttributeResponseBodyDataCidrList(DaraModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr: str = None,
        create_time: int = None,
    ):
        # The access control list (ACL) policy. Valid value:
        # 
        # - **allow**: The endpoint allows access from the specified CIDR block. This is the only supported value.
        self.acl_strategy = acl_strategy
        # The CIDR block.
        self.cidr = cidr
        # The time when the CIDR block was created.
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        return self

