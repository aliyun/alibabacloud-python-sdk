# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceRiskLevelsRequest(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstanceRiskLevelsRequestInstances] = None,
        lang: str = None,
    ):
        # The information about the instances.
        self.instances = instances
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstanceRiskLevelsRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

class DescribeInstanceRiskLevelsRequestInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        internet_ip: List[str] = None,
        intranet_ip: str = None,
        uuid: str = None,
    ):
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id
        # The public IP addresses of instances.
        self.internet_ip = internet_ip
        # The private IP address of the instance.
        self.intranet_ip = intranet_ip
        # The UUID of the instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

