# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class SetVpcAccessRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        security_token: str = None,
        tag: List[main_models.SetVpcAccessRequestTag] = None,
        vpc_id: str = None,
        vpc_target_host_name: str = None,
    ):
        # The description of the VPC.
        self.description = description
        # The ID of an ECS or SLB instance in the VPC.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the authorization. The name must be unique.
        # 
        # This parameter is required.
        self.name = name
        # The port number that corresponds to the instance.
        # 
        # This parameter is required.
        self.port = port
        self.security_token = security_token
        # The tag of objects that match the rule. You can specify multiple tags.
        self.tag = tag
        # The ID of the VPC. The VPC must be an available one that belongs to the same account as the API.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The host of the backend service.
        self.vpc_target_host_name = vpc_target_host_name

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_target_host_name is not None:
            result['VpcTargetHostName'] = self.vpc_target_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.SetVpcAccessRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcTargetHostName') is not None:
            self.vpc_target_host_name = m.get('VpcTargetHostName')

        return self

class SetVpcAccessRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

