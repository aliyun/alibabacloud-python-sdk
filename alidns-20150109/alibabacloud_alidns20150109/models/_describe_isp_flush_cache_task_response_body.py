# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeIspFlushCacheTaskResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        domain_name: str = None,
        flush_cache_results: List[main_models.DescribeIspFlushCacheTaskResponseBodyFlushCacheResults] = None,
        instance_id: str = None,
        instance_name: str = None,
        isp: str = None,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.domain_name = domain_name
        self.flush_cache_results = flush_cache_results
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isp = isp
        self.request_id = request_id
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.flush_cache_results:
            for v1 in self.flush_cache_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        result['FlushCacheResults'] = []
        if self.flush_cache_results is not None:
            for k1 in self.flush_cache_results:
                result['FlushCacheResults'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        self.flush_cache_results = []
        if m.get('FlushCacheResults') is not None:
            for k1 in m.get('FlushCacheResults'):
                temp_model = main_models.DescribeIspFlushCacheTaskResponseBodyFlushCacheResults()
                self.flush_cache_results.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class DescribeIspFlushCacheTaskResponseBodyFlushCacheResults(DaraModel):
    def __init__(
        self,
        dns_nodes: List[main_models.DescribeIspFlushCacheTaskResponseBodyFlushCacheResultsDnsNodes] = None,
        province: str = None,
    ):
        self.dns_nodes = dns_nodes
        self.province = province

    def validate(self):
        if self.dns_nodes:
            for v1 in self.dns_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DnsNodes'] = []
        if self.dns_nodes is not None:
            for k1 in self.dns_nodes:
                result['DnsNodes'].append(k1.to_map() if k1 else None)

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_nodes = []
        if m.get('DnsNodes') is not None:
            for k1 in m.get('DnsNodes'):
                temp_model = main_models.DescribeIspFlushCacheTaskResponseBodyFlushCacheResultsDnsNodes()
                self.dns_nodes.append(temp_model.from_map(k1))

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

class DescribeIspFlushCacheTaskResponseBodyFlushCacheResultsDnsNodes(DaraModel):
    def __init__(
        self,
        answers: List[main_models.DescribeIspFlushCacheTaskResponseBodyFlushCacheResultsDnsNodesAnswers] = None,
        node_ip: str = None,
        sp_name: str = None,
        status: str = None,
    ):
        self.answers = answers
        self.node_ip = node_ip
        self.sp_name = sp_name
        self.status = status

    def validate(self):
        if self.answers:
            for v1 in self.answers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Answers'] = []
        if self.answers is not None:
            for k1 in self.answers:
                result['Answers'].append(k1.to_map() if k1 else None)

        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip

        if self.sp_name is not None:
            result['SpName'] = self.sp_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answers = []
        if m.get('Answers') is not None:
            for k1 in m.get('Answers'):
                temp_model = main_models.DescribeIspFlushCacheTaskResponseBodyFlushCacheResultsDnsNodesAnswers()
                self.answers.append(temp_model.from_map(k1))

        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')

        if m.get('SpName') is not None:
            self.sp_name = m.get('SpName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeIspFlushCacheTaskResponseBodyFlushCacheResultsDnsNodesAnswers(DaraModel):
    def __init__(
        self,
        name: str = None,
        record: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.name = name
        self.record = record
        self.ttl = ttl
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.record is not None:
            result['Record'] = self.record

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Record') is not None:
            self.record = m.get('Record')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

