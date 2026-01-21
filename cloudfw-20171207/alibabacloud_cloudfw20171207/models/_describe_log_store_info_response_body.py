# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeLogStoreInfoResponseBody(DaraModel):
    def __init__(
        self,
        info_list: List[main_models.DescribeLogStoreInfoResponseBodyInfoList] = None,
        log_modify_quota: int = None,
        log_store_name: str = None,
        log_version: int = None,
        project_name: str = None,
        quota: int = None,
        region_id: str = None,
        request_id: str = None,
        task_id: str = None,
        total_quota: int = None,
        ttl: int = None,
        used: int = None,
    ):
        self.info_list = info_list
        self.log_modify_quota = log_modify_quota
        # The name of the SLS LogStore in the log service.
        self.log_store_name = log_store_name
        self.log_version = log_version
        # The Project name of the log service.
        self.project_name = project_name
        # Available log storage capacity. Unit: Byte.
        self.quota = quota
        # The region ID for log delivery.
        self.region_id = region_id
        # The ID of this request.
        self.request_id = request_id
        self.task_id = task_id
        self.total_quota = total_quota
        # Log storage duration. Unit: days.
        self.ttl = ttl
        # Used storage capacity. Unit: Byte.
        # 
        # > The statistics of the log service have a delay of approximately two hours.
        self.used = used

    def validate(self):
        if self.info_list:
            for v1 in self.info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InfoList'] = []
        if self.info_list is not None:
            for k1 in self.info_list:
                result['InfoList'].append(k1.to_map() if k1 else None)

        if self.log_modify_quota is not None:
            result['LogModifyQuota'] = self.log_modify_quota

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_version is not None:
            result['LogVersion'] = self.log_version

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.used is not None:
            result['Used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info_list = []
        if m.get('InfoList') is not None:
            for k1 in m.get('InfoList'):
                temp_model = main_models.DescribeLogStoreInfoResponseBodyInfoList()
                self.info_list.append(temp_model.from_map(k1))

        if m.get('LogModifyQuota') is not None:
            self.log_modify_quota = m.get('LogModifyQuota')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogVersion') is not None:
            self.log_version = m.get('LogVersion')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

class DescribeLogStoreInfoResponseBodyInfoList(DaraModel):
    def __init__(
        self,
        log_store_name: str = None,
        max_split_shard: int = None,
        project_name: str = None,
        quota: int = None,
        region_id: str = None,
        shard: int = None,
        site: str = None,
        ttl: int = None,
        used: int = None,
    ):
        self.log_store_name = log_store_name
        self.max_split_shard = max_split_shard
        self.project_name = project_name
        self.quota = quota
        self.region_id = region_id
        self.shard = shard
        self.site = site
        self.ttl = ttl
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.max_split_shard is not None:
            result['MaxSplitShard'] = self.max_split_shard

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.shard is not None:
            result['Shard'] = self.shard

        if self.site is not None:
            result['Site'] = self.site

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.used is not None:
            result['Used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('MaxSplitShard') is not None:
            self.max_split_shard = m.get('MaxSplitShard')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Shard') is not None:
            self.shard = m.get('Shard')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

