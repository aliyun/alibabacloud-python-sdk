# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class OpenStructMvDetailModel(DaraModel):
    def __init__(
        self,
        base_table_infos: List[main_models.OpenStructMvDetailModelBaseTableInfos] = None,
        base_table_names: List[List[str]] = None,
        enable_delay_alert: int = None,
        enable_failure_alert: int = None,
        explicit_hit: int = None,
        first_refresh_time: str = None,
        implicit_hit: int = None,
        is_inactive: bool = None,
        latency_tolerance: int = None,
        local_size: int = None,
        query_rewrite_enabled: bool = None,
        refresh_interval: str = None,
        refresh_state: str = None,
        remote_size: int = None,
        resource_group: str = None,
        table_engine: str = None,
        updated_at: str = None,
    ):
        self.base_table_infos = base_table_infos
        self.base_table_names = base_table_names
        self.enable_delay_alert = enable_delay_alert
        self.enable_failure_alert = enable_failure_alert
        self.explicit_hit = explicit_hit
        self.first_refresh_time = first_refresh_time
        self.implicit_hit = implicit_hit
        self.is_inactive = is_inactive
        self.latency_tolerance = latency_tolerance
        self.local_size = local_size
        self.query_rewrite_enabled = query_rewrite_enabled
        self.refresh_interval = refresh_interval
        self.refresh_state = refresh_state
        self.remote_size = remote_size
        self.resource_group = resource_group
        self.table_engine = table_engine
        self.updated_at = updated_at

    def validate(self):
        if self.base_table_infos:
            for v1 in self.base_table_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaseTableInfos'] = []
        if self.base_table_infos is not None:
            for k1 in self.base_table_infos:
                result['BaseTableInfos'].append(k1.to_map() if k1 else None)

        if self.base_table_names is not None:
            result['BaseTableNames'] = self.base_table_names

        if self.enable_delay_alert is not None:
            result['EnableDelayAlert'] = self.enable_delay_alert

        if self.enable_failure_alert is not None:
            result['EnableFailureAlert'] = self.enable_failure_alert

        if self.explicit_hit is not None:
            result['ExplicitHit'] = self.explicit_hit

        if self.first_refresh_time is not None:
            result['FirstRefreshTime'] = self.first_refresh_time

        if self.implicit_hit is not None:
            result['ImplicitHit'] = self.implicit_hit

        if self.is_inactive is not None:
            result['IsInactive'] = self.is_inactive

        if self.latency_tolerance is not None:
            result['LatencyTolerance'] = self.latency_tolerance

        if self.local_size is not None:
            result['LocalSize'] = self.local_size

        if self.query_rewrite_enabled is not None:
            result['QueryRewriteEnabled'] = self.query_rewrite_enabled

        if self.refresh_interval is not None:
            result['RefreshInterval'] = self.refresh_interval

        if self.refresh_state is not None:
            result['RefreshState'] = self.refresh_state

        if self.remote_size is not None:
            result['RemoteSize'] = self.remote_size

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.table_engine is not None:
            result['TableEngine'] = self.table_engine

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.base_table_infos = []
        if m.get('BaseTableInfos') is not None:
            for k1 in m.get('BaseTableInfos'):
                temp_model = main_models.OpenStructMvDetailModelBaseTableInfos()
                self.base_table_infos.append(temp_model.from_map(k1))

        if m.get('BaseTableNames') is not None:
            self.base_table_names = m.get('BaseTableNames')

        if m.get('EnableDelayAlert') is not None:
            self.enable_delay_alert = m.get('EnableDelayAlert')

        if m.get('EnableFailureAlert') is not None:
            self.enable_failure_alert = m.get('EnableFailureAlert')

        if m.get('ExplicitHit') is not None:
            self.explicit_hit = m.get('ExplicitHit')

        if m.get('FirstRefreshTime') is not None:
            self.first_refresh_time = m.get('FirstRefreshTime')

        if m.get('ImplicitHit') is not None:
            self.implicit_hit = m.get('ImplicitHit')

        if m.get('IsInactive') is not None:
            self.is_inactive = m.get('IsInactive')

        if m.get('LatencyTolerance') is not None:
            self.latency_tolerance = m.get('LatencyTolerance')

        if m.get('LocalSize') is not None:
            self.local_size = m.get('LocalSize')

        if m.get('QueryRewriteEnabled') is not None:
            self.query_rewrite_enabled = m.get('QueryRewriteEnabled')

        if m.get('RefreshInterval') is not None:
            self.refresh_interval = m.get('RefreshInterval')

        if m.get('RefreshState') is not None:
            self.refresh_state = m.get('RefreshState')

        if m.get('RemoteSize') is not None:
            self.remote_size = m.get('RemoteSize')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('TableEngine') is not None:
            self.table_engine = m.get('TableEngine')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

class OpenStructMvDetailModelBaseTableInfos(DaraModel):
    def __init__(
        self,
        base_table_is_mv: bool = None,
        schema_name: str = None,
        table_engine: str = None,
        table_name: str = None,
    ):
        self.base_table_is_mv = base_table_is_mv
        self.schema_name = schema_name
        self.table_engine = table_engine
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_table_is_mv is not None:
            result['BaseTableIsMv'] = self.base_table_is_mv

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_engine is not None:
            result['TableEngine'] = self.table_engine

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseTableIsMv') is not None:
            self.base_table_is_mv = m.get('BaseTableIsMv')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableEngine') is not None:
            self.table_engine = m.get('TableEngine')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

