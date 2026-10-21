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
        # The detailed information returned.
        self.data = data
        # The request ID.
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
        delivery_settings: main_models.GetDataStorageResponseBodyDataDeliverySettings = None,
        delivery_settings_error: str = None,
        log_project: str = None,
        log_project_state: str = None,
        log_project_state_change_allowed: bool = None,
        log_service_disabled: bool = None,
        normalization_log_stores: List[main_models.GetDataStorageResponseBodyDataNormalizationLogStores] = None,
        normalization_log_views: List[main_models.GetDataStorageResponseBodyDataNormalizationLogViews] = None,
        record_log_stores: List[main_models.GetDataStorageResponseBodyDataRecordLogStores] = None,
        sas_log_stores: List[main_models.GetDataStorageResponseBodyDataSasLogStores] = None,
        unused_log_stores: List[main_models.GetDataStorageResponseBodyDataUnusedLogStores] = None,
    ):
        # The amount of cold storage used for user logs.
        self.cold_storage_used_capacity = cold_storage_used_capacity
        # The storage region of user logs.
        self.data_storage_region_id = data_storage_region_id
        # Specifies whether the storage region can be modified. By default, the region cannot be modified. You can contact the product manager to reset the region, and the region can be reset only once. Valid values:
        # - allow: The region can be modified.
        # - deny: The region cannot be modified.
        self.data_storage_region_permission = data_storage_region_permission
        # The storage capacity purchased for subscription.
        self.data_storage_total_capacity = data_storage_total_capacity
        # The amount of storage used in user log management.
        self.data_storage_used_capacity = data_storage_used_capacity
        # The storage usage details of the log management user.
        self.data_storage_used_capacity_detail = data_storage_used_capacity_detail
        # The multi-account delivery settings for the current storage resources. Returned when the query is successful. If the read operation fails, see DeliverySettingsError.
        self.delivery_settings = delivery_settings
        # The read error code for the optional multi-account delivery settings. If the read operation fails, DELIVERY_SETTINGS_UNAVAILABLE is returned. If the read operation is successful, this field is empty or not returned, and does not affect other storage fields.
        self.delivery_settings_error = delivery_settings_error
        # The name of the Simple Log Service project where user logs are stored.
        self.log_project = log_project
        # The status of the log project.
        self.log_project_state = log_project_state
        # Specifies whether the status of the log project can be changed.
        self.log_project_state_change_allowed = log_project_state_change_allowed
        # Specifies whether Simple Log Service is disabled.
        self.log_service_disabled = log_service_disabled
        # The details of the Logstores for normalized data.
        self.normalization_log_stores = normalization_log_stores
        # The details of the normalized datasets.
        self.normalization_log_views = normalization_log_views
        # The list of Record Logstores.
        self.record_log_stores = record_log_stores
        # The storage details of raw logs in Security Center.
        self.sas_log_stores = sas_log_stores
        # The list of legacy Logstores in SIEM V1.
        self.unused_log_stores = unused_log_stores

    def validate(self):
        if self.delivery_settings:
            self.delivery_settings.validate()
        if self.normalization_log_stores:
            for v1 in self.normalization_log_stores:
                 if v1:
                    v1.validate()
        if self.normalization_log_views:
            for v1 in self.normalization_log_views:
                 if v1:
                    v1.validate()
        if self.record_log_stores:
            for v1 in self.record_log_stores:
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

        if self.delivery_settings is not None:
            result['DeliverySettings'] = self.delivery_settings.to_map()

        if self.delivery_settings_error is not None:
            result['DeliverySettingsError'] = self.delivery_settings_error

        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.log_project_state is not None:
            result['LogProjectState'] = self.log_project_state

        if self.log_project_state_change_allowed is not None:
            result['LogProjectStateChangeAllowed'] = self.log_project_state_change_allowed

        if self.log_service_disabled is not None:
            result['LogServiceDisabled'] = self.log_service_disabled

        result['NormalizationLogStores'] = []
        if self.normalization_log_stores is not None:
            for k1 in self.normalization_log_stores:
                result['NormalizationLogStores'].append(k1.to_map() if k1 else None)

        result['NormalizationLogViews'] = []
        if self.normalization_log_views is not None:
            for k1 in self.normalization_log_views:
                result['NormalizationLogViews'].append(k1.to_map() if k1 else None)

        result['RecordLogStores'] = []
        if self.record_log_stores is not None:
            for k1 in self.record_log_stores:
                result['RecordLogStores'].append(k1.to_map() if k1 else None)

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

        if m.get('DeliverySettings') is not None:
            temp_model = main_models.GetDataStorageResponseBodyDataDeliverySettings()
            self.delivery_settings = temp_model.from_map(m.get('DeliverySettings'))

        if m.get('DeliverySettingsError') is not None:
            self.delivery_settings_error = m.get('DeliverySettingsError')

        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('LogProjectState') is not None:
            self.log_project_state = m.get('LogProjectState')

        if m.get('LogProjectStateChangeAllowed') is not None:
            self.log_project_state_change_allowed = m.get('LogProjectStateChangeAllowed')

        if m.get('LogServiceDisabled') is not None:
            self.log_service_disabled = m.get('LogServiceDisabled')

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

        self.record_log_stores = []
        if m.get('RecordLogStores') is not None:
            for k1 in m.get('RecordLogStores'):
                temp_model = main_models.GetDataStorageResponseBodyDataRecordLogStores()
                self.record_log_stores.append(temp_model.from_map(k1))

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
        # The name of the Logstore.
        self.log_store_name = log_store_name
        # The data retention period.
        self.log_store_ttl = log_store_ttl
        # The amount of hot storage used.
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
        account_deliveries: List[main_models.GetDataStorageResponseBodyDataSasLogStoresAccountDeliveries] = None,
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
        # The delivery records of this log type expanded by source account, including the current account and member accounts with existing records.
        self.account_deliveries = account_deliveries
        # The log code.
        self.log_code = log_code
        # The group to which the log belongs. Valid values:
        # - host: Host logs.
        # - security: Security logs.
        self.log_delivery_group = log_delivery_group
        # Specifies whether the log delivery switch can be operated. Log delivery is unavailable if the service is not purchased. Valid values:
        # - allow: Allowed.
        # - deny: Not allowed.
        self.log_delivery_permission = log_delivery_permission
        # The log delivery status. Valid values:
        # - enable: Log delivery is enabled.
        # - disable: Log delivery is disabled.
        self.log_delivery_status = log_delivery_status
        # The time of the last log delivery operation. The format is YYYY-MM-DDTHH:mm:ss.
        self.log_delivery_update_time = log_delivery_update_time
        # The log name.
        self.log_name = log_name
        # The default query conditions for the log. When multiple logs are stored in a single Logstore, you must use query conditions to perform a log query for a specific log.
        self.log_search_conditions = log_search_conditions
        # Indicates whether the Logstore where the log is stored exists. Valid values:
        # - true: Exists.
        # - false: Does not exist.
        self.log_store_existed = log_store_existed
        # The name of the Logstore where the log is stored.
        self.log_store_name = log_store_name
        # The storage duration of the Logstore where the log is stored. The minimum storage duration is 30 days.
        self.log_store_ttl = log_store_ttl
        # The amount of hot storage used.
        self.used_capacity = used_capacity

    def validate(self):
        if self.account_deliveries:
            for v1 in self.account_deliveries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountDeliveries'] = []
        if self.account_deliveries is not None:
            for k1 in self.account_deliveries:
                result['AccountDeliveries'].append(k1.to_map() if k1 else None)

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
        self.account_deliveries = []
        if m.get('AccountDeliveries') is not None:
            for k1 in m.get('AccountDeliveries'):
                temp_model = main_models.GetDataStorageResponseBodyDataSasLogStoresAccountDeliveries()
                self.account_deliveries.append(temp_model.from_map(k1))

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

class GetDataStorageResponseBodyDataSasLogStoresAccountDeliveries(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        is_da_account: bool = None,
        log_delivery_status: str = None,
        log_delivery_update_time: str = None,
    ):
        # The UID of the source cloud account. This field is an int64 number.
        self.account_id = account_id
        # The display name of the source account. If the name is not obtained, the account UID string is used.
        self.account_name = account_name
        # Indicates whether the account is the current management or target account (the current account). A value of true indicates the current account. A value of false indicates a member source account.
        self.is_da_account = is_da_account
        # The recorded delivery status of the source account. Valid values:
        # - enable: Enabled.
        # - disable: Disabled.
        self.log_delivery_status = log_delivery_status
        # The last update time of the delivery status for the source account. If no record is generated, this field is empty or not returned.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.log_delivery_update_time = log_delivery_update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.is_da_account is not None:
            result['IsDaAccount'] = self.is_da_account

        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status

        if self.log_delivery_update_time is not None:
            result['LogDeliveryUpdateTime'] = self.log_delivery_update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('IsDaAccount') is not None:
            self.is_da_account = m.get('IsDaAccount')

        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')

        if m.get('LogDeliveryUpdateTime') is not None:
            self.log_delivery_update_time = m.get('LogDeliveryUpdateTime')

        return self

class GetDataStorageResponseBodyDataRecordLogStores(DaraModel):
    def __init__(
        self,
        log_store_name: str = None,
        log_store_ttl: int = None,
        used_capacity: float = None,
    ):
        # The name of the Logstore.
        self.log_store_name = log_store_name
        # The TTL of the Logstore.
        self.log_store_ttl = log_store_ttl
        # The used capacity of the Logstore.
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
        # The log type of the normalized logs.
        self.activity_name = activity_name
        # The category of the normalized logs.
        self.category_name = category_name
        # The number of times this normalized dataset is referenced in Threat Analysis and Response.
        self.detection_rule_reference_count = detection_rule_reference_count
        # The list of products that reference this normalized dataset in Threat Analysis and Response.
        self.detection_rule_reference_product_ids = detection_rule_reference_product_ids
        # The query statement used to query log types in the normalized dataset.
        self.log_search_conditions = log_search_conditions
        # The Logstore where Threat Analysis and Response stores normalized logs.
        self.log_store_name = log_store_name
        # Specifies whether the normalized dataset exists. Valid values:
        # - true: The dataset exists.
        # - false: The dataset does not exist.
        self.log_view_existed = log_view_existed
        # The name of the normalized dataset.
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
        # The name of the Logstore that stores normalized data.
        self.log_store_name = log_store_name
        # The storage duration of the normalized data.
        self.log_store_ttl = log_store_ttl
        # The amount of hot storage used.
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

class GetDataStorageResponseBodyDataDeliverySettings(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.GetDataStorageResponseBodyDataDeliverySettingsAccounts] = None,
        can_configure: bool = None,
        configuration_version: int = None,
        da_account_id: str = None,
        enabled: bool = None,
        initialized: bool = None,
        prerequisite_enabled: bool = None,
        target_project: str = None,
        target_region: str = None,
        types: List[main_models.GetDataStorageResponseBodyDataDeliverySettingsTypes] = None,
        unavailable_reason: str = None,
    ):
        # The account directory of the current account and managed member accounts.
        self.accounts = accounts
        # Specifies whether the current account meets the conditions for delivery setting operations. This is determined based on authorization, target project availability, capacity orders, and the current account identity. The PrerequisiteEnabled parameter must also be met.
        self.can_configure = can_configure
        # The current version of the delivery settings. When you modify multi-account configurations or specify member delivery, pass this value back as ConfigurationVersion. You must query this value again after each modification and cannot use a fixed example value.
        self.configuration_version = configuration_version
        # The UID of the current management and delivery target account, which is a decimal string. This is also the current account that is permanently retained in the account selection list.
        self.da_account_id = da_account_id
        # The master switch for the saved multi-account centralized delivery. A value of true indicates that the switch is turned on. A value of false indicates that the switch is turned off.
        self.enabled = enabled
        # Specifies whether the initialization of the account scope and automatic inclusion settings is completed when the feature is enabled for the first time.
        self.initialized = initialized
        # Specifies whether the prerequisite of enabling multi-account security management in Security Center is met.
        self.prerequisite_enabled = prerequisite_enabled
        # The name of the current Simple Log Service project for centralized delivery. When you modify multi-account settings or specify member delivery, pass this value back as the TargetProject request parameter.
        self.target_project = target_project
        # The region ID of the current Simple Log Service project for centralized delivery.
        self.target_region = target_region
        # The account selection, automatic inclusion settings, and existing delivery status categorized by log type.
        self.types = types
        # The reason code for being unconfigurable. Valid values: DA_UNAUTHORIZED (the management account is not authorized), TARGET_PROJECT_UNAVAILABLE (the target project is unavailable), LOG_CAPACITY_UNAVAILABLE (no valid capacity order exists), and NOT_CURRENT_ACCOUNT (the operation is not performed by the current account). This field is empty or not returned if the conditions are met.
        self.unavailable_reason = unavailable_reason

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()
        if self.types:
            for v1 in self.types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.can_configure is not None:
            result['CanConfigure'] = self.can_configure

        if self.configuration_version is not None:
            result['ConfigurationVersion'] = self.configuration_version

        if self.da_account_id is not None:
            result['DaAccountId'] = self.da_account_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.initialized is not None:
            result['Initialized'] = self.initialized

        if self.prerequisite_enabled is not None:
            result['PrerequisiteEnabled'] = self.prerequisite_enabled

        if self.target_project is not None:
            result['TargetProject'] = self.target_project

        if self.target_region is not None:
            result['TargetRegion'] = self.target_region

        result['Types'] = []
        if self.types is not None:
            for k1 in self.types:
                result['Types'].append(k1.to_map() if k1 else None)

        if self.unavailable_reason is not None:
            result['UnavailableReason'] = self.unavailable_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.GetDataStorageResponseBodyDataDeliverySettingsAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('CanConfigure') is not None:
            self.can_configure = m.get('CanConfigure')

        if m.get('ConfigurationVersion') is not None:
            self.configuration_version = m.get('ConfigurationVersion')

        if m.get('DaAccountId') is not None:
            self.da_account_id = m.get('DaAccountId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Initialized') is not None:
            self.initialized = m.get('Initialized')

        if m.get('PrerequisiteEnabled') is not None:
            self.prerequisite_enabled = m.get('PrerequisiteEnabled')

        if m.get('TargetProject') is not None:
            self.target_project = m.get('TargetProject')

        if m.get('TargetRegion') is not None:
            self.target_region = m.get('TargetRegion')

        self.types = []
        if m.get('Types') is not None:
            for k1 in m.get('Types'):
                temp_model = main_models.GetDataStorageResponseBodyDataDeliverySettingsTypes()
                self.types.append(temp_model.from_map(k1))

        if m.get('UnavailableReason') is not None:
            self.unavailable_reason = m.get('UnavailableReason')

        return self

class GetDataStorageResponseBodyDataDeliverySettingsTypes(DaraModel):
    def __init__(
        self,
        auto_include_new_accounts: bool = None,
        executions: List[main_models.GetDataStorageResponseBodyDataDeliverySettingsTypesExecutions] = None,
        log_code: str = None,
        selected_account_ids: List[str] = None,
    ):
        # Specifies whether to automatically add subsequent new and available managed members to the selection scope of this log type.
        self.auto_include_new_accounts = auto_include_new_accounts
        # The status list of existing source delivery records for this log type.
        self.executions = executions
        # The unique identifier of the log type, which corresponds to UpdateDataStorageDelivery.LogCode.
        self.log_code = log_code
        # The array of UIDs of the selected source accounts for this log type, including the current account. The response is a JSON string array. When you write an array(simple) request, you must serialize it into comma-separated values.
        self.selected_account_ids = selected_account_ids

    def validate(self):
        if self.executions:
            for v1 in self.executions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_include_new_accounts is not None:
            result['AutoIncludeNewAccounts'] = self.auto_include_new_accounts

        result['Executions'] = []
        if self.executions is not None:
            for k1 in self.executions:
                result['Executions'].append(k1.to_map() if k1 else None)

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.selected_account_ids is not None:
            result['SelectedAccountIds'] = self.selected_account_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncludeNewAccounts') is not None:
            self.auto_include_new_accounts = m.get('AutoIncludeNewAccounts')

        self.executions = []
        if m.get('Executions') is not None:
            for k1 in m.get('Executions'):
                temp_model = main_models.GetDataStorageResponseBodyDataDeliverySettingsTypesExecutions()
                self.executions.append(temp_model.from_map(k1))

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('SelectedAccountIds') is not None:
            self.selected_account_ids = m.get('SelectedAccountIds')

        return self

class GetDataStorageResponseBodyDataDeliverySettingsTypesExecutions(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        error_code: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The UID of the source account for this delivery record, which is a decimal string.
        self.account_id = account_id
        # A reserved compatibility field. The current implementation does not populate historical execution error codes, so this field is usually empty or not returned. If execution fails, read the error code returned by the corresponding write operation.
        self.error_code = error_code
        # The recorded delivery status. RUNNING indicates that the status is recorded as enabled after the last successful operation. STOPPED indicates that the status is recorded as disabled. This field does not indicate real-time log arrival.
        self.status = status
        # The last update time of the delivery status, which is a UNIX timestamp in milliseconds. This field is empty or not returned if the record has no update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetDataStorageResponseBodyDataDeliverySettingsAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        authorized: bool = None,
        da_account: bool = None,
    ):
        # The UID of the source Alibaba Cloud account, which is a decimal string.
        self.account_id = account_id
        # The display name of the account. If the name is missing, the UID string is returned.
        self.account_name = account_name
        # Specifies whether the account has the authorization required for log delivery. This parameter must be set to true when you add a selected member.
        self.authorized = authorized
        # Specifies whether the account is the current management and delivery target account, which is the current account.
        self.da_account = da_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.authorized is not None:
            result['Authorized'] = self.authorized

        if self.da_account is not None:
            result['DaAccount'] = self.da_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')

        if m.get('DaAccount') is not None:
            self.da_account = m.get('DaAccount')

        return self

