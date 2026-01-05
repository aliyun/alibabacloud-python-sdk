# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateCloudPhoneNodeResponseBody(DaraModel):
    def __init__(
        self,
        network_package_order_model: main_models.CreateCloudPhoneNodeResponseBodyNetworkPackageOrderModel = None,
        node_infos: List[main_models.CreateCloudPhoneNodeResponseBodyNodeInfos] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.network_package_order_model = network_package_order_model
        # The cloud phone matrixes.
        self.node_infos = node_infos
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.network_package_order_model:
            self.network_package_order_model.validate()
        if self.node_infos:
            for v1 in self.node_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_package_order_model is not None:
            result['NetworkPackageOrderModel'] = self.network_package_order_model.to_map()

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
        if m.get('NetworkPackageOrderModel') is not None:
            temp_model = main_models.CreateCloudPhoneNodeResponseBodyNetworkPackageOrderModel()
            self.network_package_order_model = temp_model.from_map(m.get('NetworkPackageOrderModel'))

        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k1 in m.get('NodeInfos'):
                temp_model = main_models.CreateCloudPhoneNodeResponseBodyNodeInfos()
                self.node_infos.append(temp_model.from_map(k1))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCloudPhoneNodeResponseBodyNodeInfos(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        node_id: str = None,
    ):
        # The IDs of the cloud phone instances.
        self.instance_ids = instance_ids
        # The ID of the cloud phone matrix.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class CreateCloudPhoneNodeResponseBodyNetworkPackageOrderModel(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        bandwidth_package_order_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_order_id = bandwidth_package_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_order_id is not None:
            result['BandwidthPackageOrderId'] = self.bandwidth_package_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageOrderId') is not None:
            self.bandwidth_package_order_id = m.get('BandwidthPackageOrderId')

        return self

