# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateAndroidInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
        instance_group_infos: List[main_models.CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos] = None,
        network_package_order_model: main_models.CreateAndroidInstanceGroupResponseBodyNetworkPackageOrderModel = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The instance groups.
        self.instance_group_infos = instance_group_infos
        self.network_package_order_model = network_package_order_model
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_group_infos:
            for v1 in self.instance_group_infos:
                 if v1:
                    v1.validate()
        if self.network_package_order_model:
            self.network_package_order_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids

        result['InstanceGroupInfos'] = []
        if self.instance_group_infos is not None:
            for k1 in self.instance_group_infos:
                result['InstanceGroupInfos'].append(k1.to_map() if k1 else None)

        if self.network_package_order_model is not None:
            result['NetworkPackageOrderModel'] = self.network_package_order_model.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        self.instance_group_infos = []
        if m.get('InstanceGroupInfos') is not None:
            for k1 in m.get('InstanceGroupInfos'):
                temp_model = main_models.CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos()
                self.instance_group_infos.append(temp_model.from_map(k1))

        if m.get('NetworkPackageOrderModel') is not None:
            temp_model = main_models.CreateAndroidInstanceGroupResponseBodyNetworkPackageOrderModel()
            self.network_package_order_model = temp_model.from_map(m.get('NetworkPackageOrderModel'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAndroidInstanceGroupResponseBodyNetworkPackageOrderModel(DaraModel):
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

class CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos(DaraModel):
    def __init__(
        self,
        instance_group_id: str = None,
        instance_ids: List[str] = None,
    ):
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The IDs of the instances.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

