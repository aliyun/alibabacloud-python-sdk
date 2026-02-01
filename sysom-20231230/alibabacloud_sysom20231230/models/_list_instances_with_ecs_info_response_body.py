# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListInstancesWithEcsInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListInstancesWithEcsInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInstancesWithEcsInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListInstancesWithEcsInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_tag: List[main_models.ListInstancesWithEcsInfoResponseBodyDataInstanceTag] = None,
        kernel_version: str = None,
        os_arch: str = None,
        os_health_score: str = None,
        os_name: str = None,
        private_ip: str = None,
        public_ip: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_tag = instance_tag
        self.kernel_version = kernel_version
        self.os_arch = os_arch
        self.os_health_score = os_health_score
        self.os_name = os_name
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.status = status

    def validate(self):
        if self.instance_tag:
            for v1 in self.instance_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.instance_name is not None:
            result['instance_name'] = self.instance_name

        result['instance_tag'] = []
        if self.instance_tag is not None:
            for k1 in self.instance_tag:
                result['instance_tag'].append(k1.to_map() if k1 else None)

        if self.kernel_version is not None:
            result['kernel_version'] = self.kernel_version

        if self.os_arch is not None:
            result['os_arch'] = self.os_arch

        if self.os_health_score is not None:
            result['os_health_score'] = self.os_health_score

        if self.os_name is not None:
            result['os_name'] = self.os_name

        if self.private_ip is not None:
            result['private_ip'] = self.private_ip

        if self.public_ip is not None:
            result['public_ip'] = self.public_ip

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['resource_group_name'] = self.resource_group_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')

        self.instance_tag = []
        if m.get('instance_tag') is not None:
            for k1 in m.get('instance_tag'):
                temp_model = main_models.ListInstancesWithEcsInfoResponseBodyDataInstanceTag()
                self.instance_tag.append(temp_model.from_map(k1))

        if m.get('kernel_version') is not None:
            self.kernel_version = m.get('kernel_version')

        if m.get('os_arch') is not None:
            self.os_arch = m.get('os_arch')

        if m.get('os_health_score') is not None:
            self.os_health_score = m.get('os_health_score')

        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')

        if m.get('private_ip') is not None:
            self.private_ip = m.get('private_ip')

        if m.get('public_ip') is not None:
            self.public_ip = m.get('public_ip')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('resource_group_name') is not None:
            self.resource_group_name = m.get('resource_group_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListInstancesWithEcsInfoResponseBodyDataInstanceTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key

        if self.tag_value is not None:
            result['tag_value'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')

        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')

        return self

