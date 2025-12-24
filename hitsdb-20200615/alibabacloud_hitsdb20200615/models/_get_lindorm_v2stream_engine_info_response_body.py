# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormV2StreamEngineInfoResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
        resource_group_list: List[main_models.GetLindormV2StreamEngineInfoResponseBodyResourceGroupList] = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id
        self.resource_group_list = resource_group_list

    def validate(self):
        if self.resource_group_list:
            for v1 in self.resource_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceGroupList'] = []
        if self.resource_group_list is not None:
            for k1 in self.resource_group_list:
                result['ResourceGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_group_list = []
        if m.get('ResourceGroupList') is not None:
            for k1 in m.get('ResourceGroupList'):
                temp_model = main_models.GetLindormV2StreamEngineInfoResponseBodyResourceGroupList()
                self.resource_group_list.append(temp_model.from_map(k1))

        return self

class GetLindormV2StreamEngineInfoResponseBodyResourceGroupList(DaraModel):
    def __init__(
        self,
        jm_ip_list: List[str] = None,
        quantity: int = None,
        resource_group_name: str = None,
        sg_ip_list: List[str] = None,
        spec: str = None,
        spec_id: str = None,
        status: str = None,
    ):
        self.jm_ip_list = jm_ip_list
        self.quantity = quantity
        self.resource_group_name = resource_group_name
        self.sg_ip_list = sg_ip_list
        self.spec = spec
        self.spec_id = spec_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jm_ip_list is not None:
            result['JmIpList'] = self.jm_ip_list

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.sg_ip_list is not None:
            result['SgIpList'] = self.sg_ip_list

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.spec_id is not None:
            result['SpecId'] = self.spec_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JmIpList') is not None:
            self.jm_ip_list = m.get('JmIpList')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('SgIpList') is not None:
            self.sg_ip_list = m.get('SgIpList')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

