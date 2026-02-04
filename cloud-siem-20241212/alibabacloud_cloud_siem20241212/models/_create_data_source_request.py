# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class CreateDataSourceRequest(DaraModel):
    def __init__(
        self,
        data_source_from: str = None,
        data_source_ids: List[str] = None,
        data_source_name: str = None,
        data_source_recognize_enabled: bool = None,
        data_source_recognizer: str = None,
        data_source_references: List[str] = None,
        data_source_stores: List[main_models.CreateDataSourceRequestDataSourceStores] = None,
        data_source_template_id: str = None,
        data_source_type: str = None,
        lang: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        log_user_id: int = None,
        order: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.data_source_from = data_source_from
        self.data_source_ids = data_source_ids
        self.data_source_name = data_source_name
        self.data_source_recognize_enabled = data_source_recognize_enabled
        self.data_source_recognizer = data_source_recognizer
        self.data_source_references = data_source_references
        self.data_source_stores = data_source_stores
        self.data_source_template_id = data_source_template_id
        self.data_source_type = data_source_type
        self.lang = lang
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        self.log_user_id = log_user_id
        self.order = order
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

        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_recognize_enabled is not None:
            result['DataSourceRecognizeEnabled'] = self.data_source_recognize_enabled

        if self.data_source_recognizer is not None:
            result['DataSourceRecognizer'] = self.data_source_recognizer

        if self.data_source_references is not None:
            result['DataSourceReferences'] = self.data_source_references

        result['DataSourceStores'] = []
        if self.data_source_stores is not None:
            for k1 in self.data_source_stores:
                result['DataSourceStores'].append(k1.to_map() if k1 else None)

        if self.data_source_template_id is not None:
            result['DataSourceTemplateId'] = self.data_source_template_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

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

        if self.order is not None:
            result['Order'] = self.order

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceFrom') is not None:
            self.data_source_from = m.get('DataSourceFrom')

        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceRecognizeEnabled') is not None:
            self.data_source_recognize_enabled = m.get('DataSourceRecognizeEnabled')

        if m.get('DataSourceRecognizer') is not None:
            self.data_source_recognizer = m.get('DataSourceRecognizer')

        if m.get('DataSourceReferences') is not None:
            self.data_source_references = m.get('DataSourceReferences')

        self.data_source_stores = []
        if m.get('DataSourceStores') is not None:
            for k1 in m.get('DataSourceStores'):
                temp_model = main_models.CreateDataSourceRequestDataSourceStores()
                self.data_source_stores.append(temp_model.from_map(k1))

        if m.get('DataSourceTemplateId') is not None:
            self.data_source_template_id = m.get('DataSourceTemplateId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

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

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

class CreateDataSourceRequestDataSourceStores(DaraModel):
    def __init__(
        self,
        data_source_store_from: str = None,
        data_source_store_id: str = None,
        data_source_store_status: str = None,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
    ):
        self.data_source_store_from = data_source_store_from
        self.data_source_store_id = data_source_store_id
        self.data_source_store_status = data_source_store_status
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

        if self.data_source_store_status is not None:
            result['DataSourceStoreStatus'] = self.data_source_store_status

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

        if m.get('DataSourceStoreStatus') is not None:
            self.data_source_store_status = m.get('DataSourceStoreStatus')

        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        return self

