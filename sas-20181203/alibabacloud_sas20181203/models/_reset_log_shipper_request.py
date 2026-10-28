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
        # The global data retention period in the hot storage tier.
        # 
        # > Valid values: greater than or equal to 7 days and less than the log retention period.
        self.hot_ttl = hot_ttl
        # The configuration information for log analysis in Security Center.
        self.log_meta_list = log_meta_list
        # The global log retention period in days.
        # 
        # > This parameter is supported only in the pay-as-you-go billing mode for logs.
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
        # The Logstore to be configured.
        # > You can call the [DescribeLogMeta](~~DescribeLogMeta~~) operation to obtain the value of this parameter.
        self.config_log_store = config_log_store
        # The data retention period in the hot storage tier of the Logstore.
        # 
        # > Valid values: greater than or equal to 7 days and less than the log retention period. Specifying the data retention period in the hot storage tier for a single Logstore overrides the global settings.
        self.hot_ttl = hot_ttl
        # The current enabling status. Valid values:
        # - **disabled**: The feature is disabled.
        # - **enabled**: The feature is enabled.
        self.status = status
        # The log retention period of the Logstore in days.
        # 
        # > Specifying the log retention period for a single Logstore overrides the global settings.
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

