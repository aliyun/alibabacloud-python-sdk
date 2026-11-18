# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class CreateTairAIGatewayInstanceResponseBody(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        instance_id: str = None,
        instance_results: main_models.CreateTairAIGatewayInstanceResponseBodyInstanceResults = None,
        node_id: str = None,
        order_id: int = None,
        region_id: str = None,
        request_id: str = None,
        success_count: int = None,
        total_count: int = None,
        vcluster_id: str = None,
        vk_name: str = None,
        zone_id: str = None,
    ):
        # The number of instances that failed to be created in a batch. This parameter is not returned when a single instance is created.
        self.fail_count = fail_count
        # The instance ID.
        self.instance_id = instance_id
        self.instance_results = instance_results
        # **[Deprecated]** This parameter is deprecated. The ID of the virtual node.
        self.node_id = node_id
        # The order ID.
        self.order_id = order_id
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The number of instances successfully created in a batch. This parameter is not returned when a single instance is created.
        self.success_count = success_count
        # The total number of instances created in a batch. This parameter is not returned when a single instance is created.
        self.total_count = total_count
        # **[Deprecated]** This parameter is deprecated. The ID of the virtual cluster.
        self.vcluster_id = vcluster_id
        # **[Deprecated]** This parameter is deprecated. The instance ID of the VCluster virtual cluster where the VNode resides.
        self.vk_name = vk_name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.instance_results:
            self.instance_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_results is not None:
            result['InstanceResults'] = self.instance_results.to_map()

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vcluster_id is not None:
            result['VClusterId'] = self.vcluster_id

        if self.vk_name is not None:
            result['VkName'] = self.vk_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceResults') is not None:
            temp_model = main_models.CreateTairAIGatewayInstanceResponseBodyInstanceResults()
            self.instance_results = temp_model.from_map(m.get('InstanceResults'))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VClusterId') is not None:
            self.vcluster_id = m.get('VClusterId')

        if m.get('VkName') is not None:
            self.vk_name = m.get('VkName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateTairAIGatewayInstanceResponseBodyInstanceResults(DaraModel):
    def __init__(
        self,
        instance_results: List[main_models.CreateTairAIGatewayInstanceResponseBodyInstanceResultsInstanceResults] = None,
    ):
        self.instance_results = instance_results

    def validate(self):
        if self.instance_results:
            for v1 in self.instance_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['instanceResults'] = []
        if self.instance_results is not None:
            for k1 in self.instance_results:
                result['instanceResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_results = []
        if m.get('instanceResults') is not None:
            for k1 in m.get('instanceResults'):
                temp_model = main_models.CreateTairAIGatewayInstanceResponseBodyInstanceResultsInstanceResults()
                self.instance_results.append(temp_model.from_map(k1))

        return self

class CreateTairAIGatewayInstanceResponseBodyInstanceResultsInstanceResults(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance_id: str = None,
        order_id: int = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.instance_id = instance_id
        self.order_id = order_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

