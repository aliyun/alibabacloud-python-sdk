# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifySqlLogConfigRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        enable_audit: bool = None,
        filters: List[main_models.ModifySqlLogConfigRequestFilters] = None,
        hot_retention: int = None,
        instance_id: str = None,
        request_enable: bool = None,
        retention: int = None,
    ):
        # Specifies whether to enable DAS Enterprise Edition. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is required if you want to enable DAS Enterprise Edition. By default, the latest version of DAS Enterprise Edition that supports the database instance is enabled.
        self.enable = enable
        self.enable_audit = enable_audit
        # A reserved parameter.
        self.filters = filters
        # The number of days for which the SQL Explorer and Audit data is stored in hot storage. Valid values: 1 to 7.
        # 
        # >  This parameter is required if only DAS Enterprise Edition V3 can be enabled for the database instance.
        self.hot_retention = hot_retention
        # The ID of the database instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable the SQL Explorer feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is required if only DAS Enterprise Edition V3 can be enabled for the database instance.
        self.request_enable = request_enable
        # The total storage duration of the SQL Explorer and Audit data. Unit: day. Valid values:
        # 
        # *   7
        # *   30
        # *   180
        # *   365
        # 
        # >  If you want to enable DAS Enterprise Edition V3, the value of this parameter must be greater than or equal to 30.
        self.retention = retention

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.hot_retention is not None:
            result['HotRetention'] = self.hot_retention

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_enable is not None:
            result['RequestEnable'] = self.request_enable

        if self.retention is not None:
            result['Retention'] = self.retention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ModifySqlLogConfigRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('HotRetention') is not None:
            self.hot_retention = m.get('HotRetention')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestEnable') is not None:
            self.request_enable = m.get('RequestEnable')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        return self

class ModifySqlLogConfigRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # A reserved parameter.
        self.key = key
        # A reserved parameter.
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

