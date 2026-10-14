# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        edition: int = None,
        enabled: int = None,
        expire_end_time: int = None,
        expire_start_time: int = None,
        instance_ids: List[str] = None,
        ip: str = None,
        page_number: str = None,
        page_size: str = None,
        remark: str = None,
        resource_group_id: str = None,
        status: List[int] = None,
        tag: List[main_models.DescribeInstancesRequestTag] = None,
    ):
        # The mitigation plan edition of the Anti-DDoS Pro or Anti-DDoS Premium instance to query. Valid values:
        # 
        # - **0**: Anti-DDoS Pro and Anti-DDoS Premium (outside the Chinese mainland) Insurance edition.
        # - **1**: Anti-DDoS Pro and Anti-DDoS Premium (outside the Chinese mainland) Unlimited edition.
        # - **2**: Anti-DDoS Pro and Anti-DDoS Premium (outside the Chinese mainland) acceleration line.
        # - **9**: Anti-DDoS Pro and Anti-DDoS Premium (the Chinese mainland) Professional Edition.
        self.edition = edition
        # The service traffic forwarding status of the Anti-DDoS Pro or Anti-DDoS Premium instance to query. Valid values:
        # 
        # - **0**: Service traffic forwarding is stopped.
        # - **1**: Service traffic forwarding is normal.
        self.enabled = enabled
        # The latest expiration time of the Anti-DDoS Pro or Anti-DDoS Premium instances to query. This means that only instances whose expiration time is earlier than the value of **ExpireEndTime** are queried. The value is a UNIX timestamp in milliseconds.
        self.expire_end_time = expire_end_time
        # The earliest expiration time of the Anti-DDoS Pro or Anti-DDoS Premium instances to query. This means that only instances whose expiration time is later than the value of **ExpireStartTime** are queried. The value is a UNIX timestamp in milliseconds.
        self.expire_start_time = expire_start_time
        # The IDs of the Anti-DDoS Pro or Anti-DDoS Premium instances to query. You can specify up to 200 Anti-DDoS Pro or Anti-DDoS Premium instances.
        self.instance_ids = instance_ids
        # The IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance to query.
        self.ip = ip
        # The page number for paging.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of instances per page for paging. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The remark of the Anti-DDoS Pro or Anti-DDoS Premium instance to query. Fuzzy match is supported.
        self.remark = remark
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the default resource group is used.
        self.resource_group_id = resource_group_id
        # The statuses of the Anti-DDoS Pro or Anti-DDoS Premium instances to query. You can specify up to 2 Anti-DDoS Pro or Anti-DDoS Premium instance statuses.
        self.status = status
        # The tags attached to the Anti-DDoS Pro or Anti-DDoS Premium instances to query.
        self.tag = tag

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
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.expire_end_time is not None:
            result['ExpireEndTime'] = self.expire_end_time

        if self.expire_start_time is not None:
            result['ExpireStartTime'] = self.expire_start_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExpireEndTime') is not None:
            self.expire_end_time = m.get('ExpireEndTime')

        if m.get('ExpireStartTime') is not None:
            self.expire_start_time = m.get('ExpireStartTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key attached to the Anti-DDoS Pro or Anti-DDoS Premium instance to query. Maximum value of N: 200, which means you can specify up to 200 tag keys. The configuration rules are as follows:
        # 
        # - Each tag consists of a tag key (**Key**) and a tag value (**Value**), separated by a comma (,).
        # - Tags are separated by commas (,).
        # 
        # > The tag key (**Key**) and tag value (**Value**) must appear in pairs.
        self.key = key
        # The tag value attached to the Anti-DDoS Pro or Anti-DDoS Premium instance to query. Maximum value of N: 200, which means you can specify up to 200 tag values. The configuration rules are as follows:
        # 
        # - Each tag consists of a tag key (**Key**) and a tag value (**Value**), separated by a comma (,).
        # - Tags are separated by commas (,).
        # 
        # > The tag key (**Key**) and tag value (**Value**) must appear in pairs.
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

