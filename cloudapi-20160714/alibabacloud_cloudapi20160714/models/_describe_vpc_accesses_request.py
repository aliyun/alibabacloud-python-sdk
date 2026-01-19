# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcAccessesRequest(DaraModel):
    def __init__(
        self,
        accurate_query: bool = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        port: str = None,
        security_token: str = None,
        tag: List[main_models.DescribeVpcAccessesRequestTag] = None,
        vpc_access_id: str = None,
        vpc_id: str = None,
    ):
        # Whether to conduct precise queries
        self.accurate_query = accurate_query
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the authorization. The name must be unique.
        self.name = name
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The service port.
        self.port = port
        self.security_token = security_token
        # The port number.
        self.tag = tag
        # The ID of the VPC authorization.
        self.vpc_access_id = vpc_access_id
        # The ID of the VPC.
        self.vpc_id = vpc_id

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
        if self.accurate_query is not None:
            result['AccurateQuery'] = self.accurate_query

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccurateQuery') is not None:
            self.accurate_query = m.get('AccurateQuery')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVpcAccessesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeVpcAccessesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

