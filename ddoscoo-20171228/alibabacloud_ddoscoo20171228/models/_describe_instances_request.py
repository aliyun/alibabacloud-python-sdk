# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        edition: int = None,
        enabled: int = None,
        expire_end_time: int = None,
        expire_start_time: int = None,
        instance_ids: str = None,
        ip: str = None,
        page_no: str = None,
        page_size: str = None,
        remark: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        status: List[int] = None,
        tag: List[main_models.DescribeInstancesRequestTag] = None,
    ):
        self.edition = edition
        self.enabled = enabled
        self.expire_end_time = expire_end_time
        self.expire_start_time = expire_start_time
        self.instance_ids = instance_ids
        self.ip = ip
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        self.status = status
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

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

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

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

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
        self.key = key
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

