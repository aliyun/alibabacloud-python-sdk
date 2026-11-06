# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class UpdateDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_stores: List[main_models.UpdateDataSourceRequestDataSourceStores] = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        order_field: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_id = data_source_id
        self.data_source_name = data_source_name
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_stores = data_source_stores
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.order_field = order_field
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        if self.data_source_stores:
            for v1 in self.data_source_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_from is not None:
            result['DataSourceFrom'] = self.data_source_from

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled

        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k1 in self.data_source_stores:
                result['DataSourceStores'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')

        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k1 in m.get('DataSourceStores'):
                temp_model = main_models.UpdateDataSourceRequestDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

class UpdateDataSourceRequestDataSourceStores(DaraModel):
    def __init__(
        self,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
    ):
        self.data_source_store_from = data_source_store_from
        self.data_source_store_id = data_source_store_id
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_store_from is not None:
            result['DataSourceStoreFrom'] = self.data_source_store_from

        if self.data_source_store_id is not None:
            result['DataSourceStoreId'] = self.data_source_store_id

        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceStoreFrom') is not None:
            self.data_source_store_from = m.get('DataSourceStoreFrom')

        if m.get('DataSourceStoreId') is not None:
            self.data_source_store_id = m.get('DataSourceStoreId')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        return self

