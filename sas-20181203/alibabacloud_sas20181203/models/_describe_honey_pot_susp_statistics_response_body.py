# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeHoneyPotSuspStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        susp_honey_pot_statistics_response: List[main_models.DescribeHoneyPotSuspStatisticsResponseBodySuspHoneyPotStatisticsResponse] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the top 5 VPCs or assets for which alerts are most frequently generated.
        self.susp_honey_pot_statistics_response = susp_honey_pot_statistics_response

    def validate(self):
        if self.susp_honey_pot_statistics_response:
            for v1 in self.susp_honey_pot_statistics_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SuspHoneyPotStatisticsResponse'] = []
        if self.susp_honey_pot_statistics_response is not None:
            for k1 in self.susp_honey_pot_statistics_response:
                result['SuspHoneyPotStatisticsResponse'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.susp_honey_pot_statistics_response = []
        if m.get('SuspHoneyPotStatisticsResponse') is not None:
            for k1 in m.get('SuspHoneyPotStatisticsResponse'):
                temp_model = main_models.DescribeHoneyPotSuspStatisticsResponseBodySuspHoneyPotStatisticsResponse()
                self.susp_honey_pot_statistics_response.append(temp_model.from_map(k1))

        return self

class DescribeHoneyPotSuspStatisticsResponseBodySuspHoneyPotStatisticsResponse(DaraModel):
    def __init__(
        self,
        count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        type: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The total number of alerts that are generated for the asset.
        self.count = count
        # The ID of the server.
        # 
        # > This parameter is returned only when **StatisticsKeyType** is set to **uuid**.
        self.instance_id = instance_id
        # The name of the server.
        # 
        # > This parameter is returned only when **StatisticsKeyType** is set to **uuid**.
        self.instance_name = instance_name
        # The type of the asset. Valid values:
        # 
        # *   **vpcInstanceId**: VPC
        # *   **uuid**: server
        self.type = type
        # The ID of the VPC.
        # 
        # > This parameter is returned only when **StatisticsKeyType** is set to **vpcInstanceId**.
        self.vpc_id = vpc_id
        # The name of the VPC.
        # 
        # > This parameter is returned only when **StatisticsKeyType** is set to **vpcInstanceId**.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.type is not None:
            result['Type'] = self.type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

