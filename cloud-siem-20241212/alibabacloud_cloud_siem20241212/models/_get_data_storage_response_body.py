# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetDataStorageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataStorageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataStorageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataStorageResponseBodyData(DaraModel):
    def __init__(
        self,
        cold_storage_used_capacity: float = None,
        data_storage_region_id: str = None,
        data_storage_region_permission: str = None,
        data_storage_total_capacity: int = None,
        data_storage_used_capacity: float = None,
        data_storage_used_capacity_detail: str = None,
        log_project: str = None,
        normalization_log_stores: List[main_models.GetDataStorageResponseBodyDataNormalizationLogStores] = None,
        normalization_log_views: List[main_models.GetDataStorageResponseBodyDataNormalizationLogViews] = None,
        sas_log_stores: List[main_models.GetDataStorageResponseBodyDataSasLogStores] = None,
        unused_log_stores: List[main_models.GetDataStorageResponseBodyDataUnusedLogStores] = None,
    ):
        self.cold_storage_used_capacity = cold_storage_used_capacity
        self.data_storage_region_id = data_storage_region_id
        self.data_storage_region_permission = data_storage_region_permission
        self.data_storage_total_capacity = data_storage_total_capacity
        self.data_storage_used_capacity = data_storage_used_capacity
        self.data_storage_used_capacity_detail = data_storage_used_capacity_detail
        self.log_project = log_project
        self.normalization_log_stores = normalization_log_stores
        self.normalization_log_views = normalization_log_views
        self.sas_log_stores = sas_log_stores
        self.unused_log_stores = unused_log_stores

    def validate(self):
        if self.normalization_log_stores:
            for v1 in self.normalization_log_stores:
                 if v1:
                    v1.validate()
        if self.normalization_log_views:
            for v1 in self.normalization_log_views:
                 if v1:
                    v1.validate()
        if self.sas_log_stores:
            for v1 in self.sas_log_stores:
                 if v1:
                    v1.validate()
        if self.unused_log_stores:
            for v1 in self.unused_log_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_storage_used_capacity is not None:
            result['ColdStorageUsedCapacity'] = self.cold_storage_used_capacity

        if self.data_storage_region_id is not None:
            result['DataStorageRegionId'] = self.data_storage_region_id

        if self.data_storage_region_permission is not None:
            result['DataStorageRegionPermission'] = self.data_storage_region_permission

        if self.data_storage_total_capacity is not None:
            result['DataStorageTotalCapacity'] = self.data_storage_total_capacity

        if self.data_storage_used_capacity is not None:
            result['DataStorageUsedCapacity'] = self.data_storage_used_capacity

        if self.data_storage_used_capacity_detail is not None:
            result['DataStorageUsedCapacityDetail'] = self.data_storage_used_capacity_detail

        if self.log_project is not None:
            result['LogProject'] = self.log_project

        result['NormalizationLogStores'] = []
        if self.normalization_log_stores is not None:
            for k1 in self.normalization_log_stores:
                result['NormalizationLogStores'].append(k1.to_map() if k1 else None)

        result['NormalizationLogViews'] = []
        if self.normalization_log_views is not None:
            for k1 in self.normalization_log_views:
                result['NormalizationLogViews'].append(k1.to_map() if k1 else None)

        result['SasLogStores'] = []
        if self.sas_log_stores is not None:
            for k1 in self.sas_log_stores:
                result['SasLogStores'].append(k1.to_map() if k1 else None)

        result['UnusedLogStores'] = []
        if self.unused_log_stores is not None:
            for k1 in self.unused_log_stores:
                result['UnusedLogStores'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdStorageUsedCapacity') is not None:
            self.cold_storage_used_capacity = m.get('ColdStorageUsedCapacity')

        if m.get('DataStorageRegionId') is not None:
            self.data_storage_region_id = m.get('DataStorageRegionId')

        if m.get('DataStorageRegionPermission') is not None:
            self.data_storage_region_permission = m.get('DataStorageRegionPermission')

        if m.get('DataStorageTotalCapacity') is not None:
            self.data_storage_total_capacity = m.get('DataStorageTotalCapacity')

        if m.get('DataStorageUsedCapacity') is not None:
            self.data_storage_used_capacity = m.get('DataStorageUsedCapacity')

        if m.get('DataStorageUsedCapacityDetail') is not None:
            self.data_storage_used_capacity_detail = m.get('DataStorageUsedCapacityDetail')

        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        self.normalization_log_stores = []
        if m.get('NormalizationLogStores') is not None:
            for k1 in m.get('NormalizationLogStores'):
                temp_model = main_models.GetDataStorageResponseBodyDataNormalizationLogStores()
                self.normalization_log_stores.append(temp_model.from_map(k1))

        self.normalization_log_views = []
        if m.get('NormalizationLogViews') is not None:
            for k1 in m.get('NormalizationLogViews'):
                temp_model = main_models.GetDataStorageResponseBodyDataNormalizationLogViews()
                self.normalization_log_views.append(temp_model.from_map(k1))

        self.sas_log_stores = []
        if m.get('SasLogStores') is not None:
            for k1 in m.get('SasLogStores'):
                temp_model = main_models.GetDataStorageResponseBodyDataSasLogStores()
                self.sas_log_stores.append(temp_model.from_map(k1))

        self.unused_log_stores = []
        if m.get('UnusedLogStores') is not None:
            for k1 in m.get('UnusedLogStores'):
                temp_model = main_models.GetDataStorageResponseBodyDataUnusedLogStores()
                self.unused_log_stores.append(temp_model.from_map(k1))

        return self

class GetDataStorageResponseBodyDataUnusedLogStores(DaraModel):
    def __init__(
        self,
        log_store_name: str = None,
        log_store_ttl: int = None,
        used_capacity: float = None,
    ):
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

class GetDataStorageResponseBodyDataSasLogStores(DaraModel):
    def __init__(
        self,
        log_code: str = None,
        log_delivery_group: str = None,
        log_delivery_permission: str = None,
        log_delivery_status: str = None,
        log_delivery_update_time: str = None,
        log_name: str = None,
        log_search_conditions: str = None,
        log_store_existed: bool = None,
        log_store_name: str = None,
        log_store_ttl: int = None,
        used_capacity: float = None,
    ):
        self.log_code = log_code
        self.log_delivery_group = log_delivery_group
        self.log_delivery_permission = log_delivery_permission
        self.log_delivery_status = log_delivery_status
        self.log_delivery_update_time = log_delivery_update_time
        self.log_name = log_name
        self.log_search_conditions = log_search_conditions
        self.log_store_existed = log_store_existed
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_delivery_group is not None:
            result['LogDeliveryGroup'] = self.log_delivery_group

        if self.log_delivery_permission is not None:
            result['LogDeliveryPermission'] = self.log_delivery_permission

        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status

        if self.log_delivery_update_time is not None:
            result['LogDeliveryUpdateTime'] = self.log_delivery_update_time

        if self.log_name is not None:
            result['LogName'] = self.log_name

        if self.log_search_conditions is not None:
            result['LogSearchConditions'] = self.log_search_conditions

        if self.log_store_existed is not None:
            result['LogStoreExisted'] = self.log_store_existed

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogDeliveryGroup') is not None:
            self.log_delivery_group = m.get('LogDeliveryGroup')

        if m.get('LogDeliveryPermission') is not None:
            self.log_delivery_permission = m.get('LogDeliveryPermission')

        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')

        if m.get('LogDeliveryUpdateTime') is not None:
            self.log_delivery_update_time = m.get('LogDeliveryUpdateTime')

        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')

        if m.get('LogSearchConditions') is not None:
            self.log_search_conditions = m.get('LogSearchConditions')

        if m.get('LogStoreExisted') is not None:
            self.log_store_existed = m.get('LogStoreExisted')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

class GetDataStorageResponseBodyDataNormalizationLogViews(DaraModel):
    def __init__(
        self,
        activity_name: str = None,
        category_name: str = None,
        detection_rule_reference_count: int = None,
        detection_rule_reference_product_ids: List[str] = None,
        log_search_conditions: str = None,
        log_store_name: str = None,
        log_view_existed: bool = None,
        log_view_name: str = None,
    ):
        self.activity_name = activity_name
        self.category_name = category_name
        self.detection_rule_reference_count = detection_rule_reference_count
        self.detection_rule_reference_product_ids = detection_rule_reference_product_ids
        self.log_search_conditions = log_search_conditions
        self.log_store_name = log_store_name
        self.log_view_existed = log_view_existed
        self.log_view_name = log_view_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.detection_rule_reference_count is not None:
            result['DetectionRuleReferenceCount'] = self.detection_rule_reference_count

        if self.detection_rule_reference_product_ids is not None:
            result['DetectionRuleReferenceProductIds'] = self.detection_rule_reference_product_ids

        if self.log_search_conditions is not None:
            result['LogSearchConditions'] = self.log_search_conditions

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_view_existed is not None:
            result['LogViewExisted'] = self.log_view_existed

        if self.log_view_name is not None:
            result['LogViewName'] = self.log_view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('DetectionRuleReferenceCount') is not None:
            self.detection_rule_reference_count = m.get('DetectionRuleReferenceCount')

        if m.get('DetectionRuleReferenceProductIds') is not None:
            self.detection_rule_reference_product_ids = m.get('DetectionRuleReferenceProductIds')

        if m.get('LogSearchConditions') is not None:
            self.log_search_conditions = m.get('LogSearchConditions')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogViewExisted') is not None:
            self.log_view_existed = m.get('LogViewExisted')

        if m.get('LogViewName') is not None:
            self.log_view_name = m.get('LogViewName')

        return self

class GetDataStorageResponseBodyDataNormalizationLogStores(DaraModel):
    def __init__(
        self,
        log_store_name: str = None,
        log_store_ttl: int = None,
        used_capacity: float = None,
    ):
        self.log_store_name = log_store_name
        self.log_store_ttl = log_store_ttl
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.log_store_ttl is not None:
            result['LogStoreTtl'] = self.log_store_ttl

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('LogStoreTtl') is not None:
            self.log_store_ttl = m.get('LogStoreTtl')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

