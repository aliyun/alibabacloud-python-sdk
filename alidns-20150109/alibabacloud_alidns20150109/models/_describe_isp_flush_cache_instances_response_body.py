# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeIspFlushCacheInstancesResponseBody(DaraModel):
    def __init__(
        self,
        isp_flush_cache_instances: List[main_models.DescribeIspFlushCacheInstancesResponseBodyIspFlushCacheInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.isp_flush_cache_instances = isp_flush_cache_instances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.isp_flush_cache_instances:
            for v1 in self.isp_flush_cache_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspFlushCacheInstances'] = []
        if self.isp_flush_cache_instances is not None:
            for k1 in self.isp_flush_cache_instances:
                result['IspFlushCacheInstances'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_flush_cache_instances = []
        if m.get('IspFlushCacheInstances') is not None:
            for k1 in m.get('IspFlushCacheInstances'):
                temp_model = main_models.DescribeIspFlushCacheInstancesResponseBodyIspFlushCacheInstances()
                self.isp_flush_cache_instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeIspFlushCacheInstancesResponseBodyIspFlushCacheInstances(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        expire_timestamp: int = None,
        instance_id: str = None,
        instance_name: str = None,
        isp: str = None,
        quota_info: main_models.DescribeIspFlushCacheInstancesResponseBodyIspFlushCacheInstancesQuotaInfo = None,
        status: str = None,
        version_code: str = None,
    ):
        self.expire_time = expire_time
        self.expire_timestamp = expire_timestamp
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isp = isp
        self.quota_info = quota_info
        self.status = status
        self.version_code = version_code

    def validate(self):
        if self.quota_info:
            self.quota_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.quota_info is not None:
            result['QuotaInfo'] = self.quota_info.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('QuotaInfo') is not None:
            temp_model = main_models.DescribeIspFlushCacheInstancesResponseBodyIspFlushCacheInstancesQuotaInfo()
            self.quota_info = temp_model.from_map(m.get('QuotaInfo'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class DescribeIspFlushCacheInstancesResponseBodyIspFlushCacheInstancesQuotaInfo(DaraModel):
    def __init__(
        self,
        instance_quota: int = None,
        instance_quota_used: int = None,
    ):
        self.instance_quota = instance_quota
        self.instance_quota_used = instance_quota_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_quota is not None:
            result['InstanceQuota'] = self.instance_quota

        if self.instance_quota_used is not None:
            result['InstanceQuotaUsed'] = self.instance_quota_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceQuota') is not None:
            self.instance_quota = m.get('InstanceQuota')

        if m.get('InstanceQuotaUsed') is not None:
            self.instance_quota_used = m.get('InstanceQuotaUsed')

        return self

