# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        log_infos: main_models.DescribeLogConfigResponseBodyLogInfos = None,
        request_id: str = None,
    ):
        # Info of the log config.
        self.log_infos = log_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogInfos') is not None:
            temp_model = main_models.DescribeLogConfigResponseBodyLogInfos()
            self.log_infos = temp_model.from_map(m.get('LogInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogConfigResponseBodyLogInfos(DaraModel):
    def __init__(
        self,
        log_info: List[main_models.DescribeLogConfigResponseBodyLogInfosLogInfo] = None,
    ):
        self.log_info = log_info

    def validate(self):
        if self.log_info:
            for v1 in self.log_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogInfo'] = []
        if self.log_info is not None:
            for k1 in self.log_info:
                result['LogInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_info = []
        if m.get('LogInfo') is not None:
            for k1 in m.get('LogInfo'):
                temp_model = main_models.DescribeLogConfigResponseBodyLogInfosLogInfo()
                self.log_info.append(temp_model.from_map(k1))

        return self

class DescribeLogConfigResponseBodyLogInfosLogInfo(DaraModel):
    def __init__(
        self,
        log_type: str = None,
        region_id: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
    ):
        # The log type.
        self.log_type = log_type
        # The region ID of the Logstore.
        self.region_id = region_id
        # The name of the Logstore in Log Service.
        self.sls_log_store = sls_log_store
        # The name of the Log Service project.
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        return self

