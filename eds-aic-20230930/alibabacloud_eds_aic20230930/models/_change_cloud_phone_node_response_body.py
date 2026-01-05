# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ChangeCloudPhoneNodeResponseBody(DaraModel):
    def __init__(
        self,
        node_infos: List[main_models.ChangeCloudPhoneNodeResponseBodyNodeInfos] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.node_infos = node_infos
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.node_infos:
            for v1 in self.node_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k1 in self.node_infos:
                result['NodeInfos'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k1 in m.get('NodeInfos'):
                temp_model = main_models.ChangeCloudPhoneNodeResponseBodyNodeInfos()
                self.node_infos.append(temp_model.from_map(k1))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ChangeCloudPhoneNodeResponseBodyNodeInfos(DaraModel):
    def __init__(
        self,
        instance_infos: List[main_models.ChangeCloudPhoneNodeResponseBodyNodeInfosInstanceInfos] = None,
        node_id: str = None,
        share_data_volume: int = None,
    ):
        self.instance_infos = instance_infos
        self.node_id = node_id
        self.share_data_volume = share_data_volume

    def validate(self):
        if self.instance_infos:
            for v1 in self.instance_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceInfos'] = []
        if self.instance_infos is not None:
            for k1 in self.instance_infos:
                result['InstanceInfos'].append(k1.to_map() if k1 else None)

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.share_data_volume is not None:
            result['ShareDataVolume'] = self.share_data_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_infos = []
        if m.get('InstanceInfos') is not None:
            for k1 in m.get('InstanceInfos'):
                temp_model = main_models.ChangeCloudPhoneNodeResponseBodyNodeInfosInstanceInfos()
                self.instance_infos.append(temp_model.from_map(k1))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ShareDataVolume') is not None:
            self.share_data_volume = m.get('ShareDataVolume')

        return self

class ChangeCloudPhoneNodeResponseBodyNodeInfosInstanceInfos(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        phone_data_volume: int = None,
    ):
        self.instance_id = instance_id
        self.phone_data_volume = phone_data_volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        return self

