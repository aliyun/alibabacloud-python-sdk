# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceRiskLevelsResponseBody(DaraModel):
    def __init__(
        self,
        instance_risks: List[main_models.DescribeInstanceRiskLevelsResponseBodyInstanceRisks] = None,
        request_id: str = None,
    ):
        # The information about the instances.
        self.instance_risks = instance_risks
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_risks:
            for v1 in self.instance_risks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRisks'] = []
        if self.instance_risks is not None:
            for k1 in self.instance_risks:
                result['InstanceRisks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_risks = []
        if m.get('InstanceRisks') is not None:
            for k1 in m.get('InstanceRisks'):
                temp_model = main_models.DescribeInstanceRiskLevelsResponseBodyInstanceRisks()
                self.instance_risks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceRiskLevelsResponseBodyInstanceRisks(DaraModel):
    def __init__(
        self,
        details: List[main_models.DescribeInstanceRiskLevelsResponseBodyInstanceRisksDetails] = None,
        instance_id: str = None,
        level: str = None,
    ):
        # The risk levels of the Elastic Compute Service (ECS) instance.
        self.details = details
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id
        # The risk levels. Valid values:
        # 
        # *   **medium**
        self.level = level

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeInstanceRiskLevelsResponseBodyInstanceRisksDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

class DescribeInstanceRiskLevelsResponseBodyInstanceRisksDetails(DaraModel):
    def __init__(
        self,
        ip: str = None,
        level: str = None,
        type: str = None,
    ):
        # The IP addresses of servers.
        self.ip = ip
        # The risk levels. Valid values:
        # 
        # *   **medium**
        self.level = level
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.level is not None:
            result['Level'] = self.level

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

