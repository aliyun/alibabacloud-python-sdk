# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormFsUsedDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        fs_capacity: str = None,
        fs_capacity_cold: str = None,
        fs_capacity_hot: str = None,
        fs_used_cold: str = None,
        fs_used_cold_on_lindorm_search: str = None,
        fs_used_cold_on_lindorm_tsdb: str = None,
        fs_used_cold_on_lindorm_table: str = None,
        fs_used_hot: str = None,
        fs_used_hot_on_lindorm_search: str = None,
        fs_used_hot_on_lindorm_tsdb: str = None,
        fs_used_hot_on_lindorm_table: str = None,
        fs_used_on_lindorm_search: str = None,
        fs_used_on_lindorm_tsdb: str = None,
        fs_used_on_lindorm_table: str = None,
        fs_used_on_lindorm_table_data: str = None,
        fs_used_on_lindorm_table_wal: str = None,
        lstorage_usage_list: List[main_models.GetLindormFsUsedDetailResponseBodyLStorageUsageList] = None,
        request_id: str = None,
        valid: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The total storage space of the cluster. Unit: bytes.
        self.fs_capacity = fs_capacity
        # The cold storage space of the cluster. Unit: bytes.
        self.fs_capacity_cold = fs_capacity_cold
        # The hot storage space of the cluster. Unit: bytes.
        self.fs_capacity_hot = fs_capacity_hot
        # The cold storage usage of the cluster. Unit: bytes.
        self.fs_used_cold = fs_used_cold
        # The cold storage usage of the table data of the search engine. Unit: bytes.
        self.fs_used_cold_on_lindorm_search = fs_used_cold_on_lindorm_search
        # The cold storage usage of the table data of the time series engine. Unit: bytes.
        self.fs_used_cold_on_lindorm_tsdb = fs_used_cold_on_lindorm_tsdb
        # The cold storage usage of the table data of the wide table engine. Unit: bytes.
        self.fs_used_cold_on_lindorm_table = fs_used_cold_on_lindorm_table
        # The hot storage usage of the cluster. Unit: bytes.
        self.fs_used_hot = fs_used_hot
        # The hot storage usage of the table data of the search engine. Unit: bytes.
        self.fs_used_hot_on_lindorm_search = fs_used_hot_on_lindorm_search
        # The hot storage usage of the table data of the time series engine. Unit: bytes.
        self.fs_used_hot_on_lindorm_tsdb = fs_used_hot_on_lindorm_tsdb
        # The hot storage usage of the table data of the wide table engine. Unit: bytes.
        self.fs_used_hot_on_lindorm_table = fs_used_hot_on_lindorm_table
        # The storage usage of the search engine. Unit: bytes.
        self.fs_used_on_lindorm_search = fs_used_on_lindorm_search
        # The storage usage of the time series engine. Unit: bytes.
        self.fs_used_on_lindorm_tsdb = fs_used_on_lindorm_tsdb
        # The space usage of the wide table engine. Unit: bytes.
        self.fs_used_on_lindorm_table = fs_used_on_lindorm_table
        # The storage usage of the table data of the wide table engine. Unit: bytes.
        self.fs_used_on_lindorm_table_data = fs_used_on_lindorm_table_data
        # The storage usage of the log data of the wide table engine. Unit: bytes.
        self.fs_used_on_lindorm_table_wal = fs_used_on_lindorm_table_wal
        # If the version of the underlying storage engine is 4.1.9 or later, the storage usage values returned for the LStorageUsageList parameter prevail. Storage details are returned based on the storage type.
        self.lstorage_usage_list = lstorage_usage_list
        # The request ID. Each request has a unique ID. You can use the request ID to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the return value is valid. Valid values: true and false. If a value of false is returned, you must provide the request ID for troubleshooting.
        self.valid = valid

    def validate(self):
        if self.lstorage_usage_list:
            for v1 in self.lstorage_usage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.fs_capacity is not None:
            result['FsCapacity'] = self.fs_capacity

        if self.fs_capacity_cold is not None:
            result['FsCapacityCold'] = self.fs_capacity_cold

        if self.fs_capacity_hot is not None:
            result['FsCapacityHot'] = self.fs_capacity_hot

        if self.fs_used_cold is not None:
            result['FsUsedCold'] = self.fs_used_cold

        if self.fs_used_cold_on_lindorm_search is not None:
            result['FsUsedColdOnLindormSearch'] = self.fs_used_cold_on_lindorm_search

        if self.fs_used_cold_on_lindorm_tsdb is not None:
            result['FsUsedColdOnLindormTSDB'] = self.fs_used_cold_on_lindorm_tsdb

        if self.fs_used_cold_on_lindorm_table is not None:
            result['FsUsedColdOnLindormTable'] = self.fs_used_cold_on_lindorm_table

        if self.fs_used_hot is not None:
            result['FsUsedHot'] = self.fs_used_hot

        if self.fs_used_hot_on_lindorm_search is not None:
            result['FsUsedHotOnLindormSearch'] = self.fs_used_hot_on_lindorm_search

        if self.fs_used_hot_on_lindorm_tsdb is not None:
            result['FsUsedHotOnLindormTSDB'] = self.fs_used_hot_on_lindorm_tsdb

        if self.fs_used_hot_on_lindorm_table is not None:
            result['FsUsedHotOnLindormTable'] = self.fs_used_hot_on_lindorm_table

        if self.fs_used_on_lindorm_search is not None:
            result['FsUsedOnLindormSearch'] = self.fs_used_on_lindorm_search

        if self.fs_used_on_lindorm_tsdb is not None:
            result['FsUsedOnLindormTSDB'] = self.fs_used_on_lindorm_tsdb

        if self.fs_used_on_lindorm_table is not None:
            result['FsUsedOnLindormTable'] = self.fs_used_on_lindorm_table

        if self.fs_used_on_lindorm_table_data is not None:
            result['FsUsedOnLindormTableData'] = self.fs_used_on_lindorm_table_data

        if self.fs_used_on_lindorm_table_wal is not None:
            result['FsUsedOnLindormTableWAL'] = self.fs_used_on_lindorm_table_wal

        result['LStorageUsageList'] = []
        if self.lstorage_usage_list is not None:
            for k1 in self.lstorage_usage_list:
                result['LStorageUsageList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('FsCapacity') is not None:
            self.fs_capacity = m.get('FsCapacity')

        if m.get('FsCapacityCold') is not None:
            self.fs_capacity_cold = m.get('FsCapacityCold')

        if m.get('FsCapacityHot') is not None:
            self.fs_capacity_hot = m.get('FsCapacityHot')

        if m.get('FsUsedCold') is not None:
            self.fs_used_cold = m.get('FsUsedCold')

        if m.get('FsUsedColdOnLindormSearch') is not None:
            self.fs_used_cold_on_lindorm_search = m.get('FsUsedColdOnLindormSearch')

        if m.get('FsUsedColdOnLindormTSDB') is not None:
            self.fs_used_cold_on_lindorm_tsdb = m.get('FsUsedColdOnLindormTSDB')

        if m.get('FsUsedColdOnLindormTable') is not None:
            self.fs_used_cold_on_lindorm_table = m.get('FsUsedColdOnLindormTable')

        if m.get('FsUsedHot') is not None:
            self.fs_used_hot = m.get('FsUsedHot')

        if m.get('FsUsedHotOnLindormSearch') is not None:
            self.fs_used_hot_on_lindorm_search = m.get('FsUsedHotOnLindormSearch')

        if m.get('FsUsedHotOnLindormTSDB') is not None:
            self.fs_used_hot_on_lindorm_tsdb = m.get('FsUsedHotOnLindormTSDB')

        if m.get('FsUsedHotOnLindormTable') is not None:
            self.fs_used_hot_on_lindorm_table = m.get('FsUsedHotOnLindormTable')

        if m.get('FsUsedOnLindormSearch') is not None:
            self.fs_used_on_lindorm_search = m.get('FsUsedOnLindormSearch')

        if m.get('FsUsedOnLindormTSDB') is not None:
            self.fs_used_on_lindorm_tsdb = m.get('FsUsedOnLindormTSDB')

        if m.get('FsUsedOnLindormTable') is not None:
            self.fs_used_on_lindorm_table = m.get('FsUsedOnLindormTable')

        if m.get('FsUsedOnLindormTableData') is not None:
            self.fs_used_on_lindorm_table_data = m.get('FsUsedOnLindormTableData')

        if m.get('FsUsedOnLindormTableWAL') is not None:
            self.fs_used_on_lindorm_table_wal = m.get('FsUsedOnLindormTableWAL')

        self.lstorage_usage_list = []
        if m.get('LStorageUsageList') is not None:
            for k1 in m.get('LStorageUsageList'):
                temp_model = main_models.GetLindormFsUsedDetailResponseBodyLStorageUsageList()
                self.lstorage_usage_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

class GetLindormFsUsedDetailResponseBodyLStorageUsageList(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        disk_type: str = None,
        used: str = None,
        used_lindorm_column_3: str = None,
        used_lindorm_message_3: str = None,
        used_lindorm_search: str = None,
        used_lindorm_spark: str = None,
        used_lindorm_table: str = None,
        used_lindorm_tsdb: str = None,
        used_lindorm_vector_3: str = None,
        used_other: str = None,
    ):
        # The total storage capacity. Unit: bytes.
        self.capacity = capacity
        # The storage type of the cluster. Valid values:
        # 
        # *   StandardCloudStorage
        # *   PerformanceCloudStorage
        # *   CapacityCloudStorage
        # *   LocalSsdStorage
        # *   LocalHddStorage
        # *   LocalEbsStorage
        self.disk_type = disk_type
        # The storage usage. Unit: bytes.
        self.used = used
        self.used_lindorm_column_3 = used_lindorm_column_3
        self.used_lindorm_message_3 = used_lindorm_message_3
        # The storage usage of the search engine. Unit: bytes.
        self.used_lindorm_search = used_lindorm_search
        # The storage usage of the compute engine. Unit: bytes.
        self.used_lindorm_spark = used_lindorm_spark
        # The storage usage of the wide table engine. Unit: bytes.
        self.used_lindorm_table = used_lindorm_table
        # The storage usage of the time series engine. Unit: bytes.
        self.used_lindorm_tsdb = used_lindorm_tsdb
        self.used_lindorm_vector_3 = used_lindorm_vector_3
        # The storage usage of other resources, such as logs and recycle bins. Unit: bytes.
        self.used_other = used_other

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_lindorm_column_3 is not None:
            result['UsedLindormColumn3'] = self.used_lindorm_column_3

        if self.used_lindorm_message_3 is not None:
            result['UsedLindormMessage3'] = self.used_lindorm_message_3

        if self.used_lindorm_search is not None:
            result['UsedLindormSearch'] = self.used_lindorm_search

        if self.used_lindorm_spark is not None:
            result['UsedLindormSpark'] = self.used_lindorm_spark

        if self.used_lindorm_table is not None:
            result['UsedLindormTable'] = self.used_lindorm_table

        if self.used_lindorm_tsdb is not None:
            result['UsedLindormTsdb'] = self.used_lindorm_tsdb

        if self.used_lindorm_vector_3 is not None:
            result['UsedLindormVector3'] = self.used_lindorm_vector_3

        if self.used_other is not None:
            result['UsedOther'] = self.used_other

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedLindormColumn3') is not None:
            self.used_lindorm_column_3 = m.get('UsedLindormColumn3')

        if m.get('UsedLindormMessage3') is not None:
            self.used_lindorm_message_3 = m.get('UsedLindormMessage3')

        if m.get('UsedLindormSearch') is not None:
            self.used_lindorm_search = m.get('UsedLindormSearch')

        if m.get('UsedLindormSpark') is not None:
            self.used_lindorm_spark = m.get('UsedLindormSpark')

        if m.get('UsedLindormTable') is not None:
            self.used_lindorm_table = m.get('UsedLindormTable')

        if m.get('UsedLindormTsdb') is not None:
            self.used_lindorm_tsdb = m.get('UsedLindormTsdb')

        if m.get('UsedLindormVector3') is not None:
            self.used_lindorm_vector_3 = m.get('UsedLindormVector3')

        if m.get('UsedOther') is not None:
            self.used_other = m.get('UsedOther')

        return self

