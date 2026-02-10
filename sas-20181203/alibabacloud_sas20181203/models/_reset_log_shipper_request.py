# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ResetLogShipperRequest(DaraModel):
    def __init__(
        self,
        hot_ttl: int = None,
        log_meta_list: List[main_models.ResetLogShipperRequestLogMetaList] = None,
        ttl: int = None,
    ):
        # The global retention period of hot data.
        # 
        # >  The value of this parameter must be at least 7 and smaller than the log retention period. Unit: days.
        self.hot_ttl = hot_ttl
        # The settings of the log analysis feature.
        self.log_meta_list = log_meta_list
        # The global log retention period.
        # 
        # >  This parameter is supported only when the log analysis feature uses the pay-as-you-go billing method.
        self.ttl = ttl

    def validate(self):
        if self.log_meta_list:
            for v1 in self.log_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hot_ttl is not None:
            result['HotTtl'] = self.hot_ttl

        result['LogMetaList'] = []
        if self.log_meta_list is not None:
            for k1 in self.log_meta_list:
                result['LogMetaList'].append(k1.to_map() if k1 else None)

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotTtl') is not None:
            self.hot_ttl = m.get('HotTtl')

        self.log_meta_list = []
        if m.get('LogMetaList') is not None:
            for k1 in m.get('LogMetaList'):
                temp_model = main_models.ResetLogShipperRequestLogMetaList()
                self.log_meta_list.append(temp_model.from_map(k1))

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class ResetLogShipperRequestLogMetaList(DaraModel):
    def __init__(
        self,
        config_log_store: str = None,
        hot_ttl: int = None,
        status: str = None,
        ttl: int = None,
    ):
        # The Logstore that you want to configure.
        # 
        # >  You can call the [DescribeLogMeta](~~DescribeLogMeta~~) operation to query the Logstore.
        self.config_log_store = config_log_store
        # The retention period of hot data in the Logstore.
        # 
        # >  The value of this parameter must be at least 7 and smaller than the log retention period. Unit: days. If you specify this parameter for the Logstore, the global retention period of hot data specified by the HotTtl parameter is overwritten.
        self.hot_ttl = hot_ttl
        # The status of the log analysis feature. Valid values:
        # 
        # *   **disabled**
        # *   **enabled**
        self.status = status
        # The log retention period of the Logstore.
        # 
        # >  If you specify this parameter for the Logstore, the global log retention period specified by the Ttl parameter is overwritten.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_log_store is not None:
            result['ConfigLogStore'] = self.config_log_store

        if self.hot_ttl is not None:
            result['HotTtl'] = self.hot_ttl

        if self.status is not None:
            result['Status'] = self.status

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigLogStore') is not None:
            self.config_log_store = m.get('ConfigLogStore')

        if m.get('HotTtl') is not None:
            self.hot_ttl = m.get('HotTtl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

