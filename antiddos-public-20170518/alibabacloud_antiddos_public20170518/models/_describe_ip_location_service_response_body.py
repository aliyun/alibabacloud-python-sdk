# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeIpLocationServiceResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.DescribeIpLocationServiceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The details of the asset.
        self.instance = instance
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.DescribeIpLocationServiceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIpLocationServiceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        region: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The type of the asset. Valid values:
        # 
        # - **ecs**: an ECS instance.
        # 
        # - **slb**: an SLB instance.
        # 
        # - **eip**: an EIP.
        # 
        # - **ipv6**: an IPv6 gateway.
        # 
        # - **swas**: a simple application server.
        # 
        # - **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # 
        # - **ga_basic**: a Global Accelerator (GA) instance.
        self.instance_type = instance_type
        # The IP address of the asset.
        self.internet_ip = internet_ip
        # The region to which the public IP address of the asset belongs.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

