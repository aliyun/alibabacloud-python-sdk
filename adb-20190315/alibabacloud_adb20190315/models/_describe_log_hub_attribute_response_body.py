# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeLogHubAttributeResponseBody(DaraModel):
    def __init__(
        self,
        loghub_info: main_models.DescribeLogHubAttributeResponseBodyLoghubInfo = None,
        request_id: str = None,
    ):
        # The log collection information.
        self.loghub_info = loghub_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.loghub_info:
            self.loghub_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loghub_info is not None:
            result['LoghubInfo'] = self.loghub_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoghubInfo') is not None:
            temp_model = main_models.DescribeLogHubAttributeResponseBodyLoghubInfo()
            self.loghub_info = temp_model.from_map(m.get('LoghubInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogHubAttributeResponseBodyLoghubInfo(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbtype: str = None,
        delay: int = None,
        deliver_name: str = None,
        deliver_time: str = None,
        description: str = None,
        filter_dirty_data: bool = None,
        log_hub_stores: main_models.DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores = None,
        log_store_name: str = None,
        message: str = None,
        project_name: str = None,
        region_id: str = None,
        schema_name: str = None,
        sync_status: str = None,
        table_name: str = None,
        user_name: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The database type.
        self.dbtype = dbtype
        # The synchronization latency, which is the latency between the latest update time of the synchronization job and the current system time. Unit: seconds.
        self.delay = delay
        # The name of the log shipping job.
        self.deliver_name = deliver_name
        # The log shipping time.
        self.deliver_time = deliver_time
        # The description.
        self.description = description
        # Indicates whether dirty data is filtered.
        self.filter_dirty_data = filter_dirty_data
        self.log_hub_stores = log_hub_stores
        # The name of the Logstore.
        self.log_store_name = log_store_name
        # The returned message.
        self.message = message
        # The name of the Simple Log Service project.
        self.project_name = project_name
        # The region ID.
        self.region_id = region_id
        # The name of the database.
        self.schema_name = schema_name
        # The synchronization status.
        self.sync_status = sync_status
        # The name of the table.
        self.table_name = table_name
        # The name of the database account.
        self.user_name = user_name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.log_hub_stores:
            self.log_hub_stores.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.deliver_name is not None:
            result['DeliverName'] = self.deliver_name

        if self.deliver_time is not None:
            result['DeliverTime'] = self.deliver_time

        if self.description is not None:
            result['Description'] = self.description

        if self.filter_dirty_data is not None:
            result['FilterDirtyData'] = self.filter_dirty_data

        if self.log_hub_stores is not None:
            result['LogHubStores'] = self.log_hub_stores.to_map()

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.message is not None:
            result['Message'] = self.message

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DeliverName') is not None:
            self.deliver_name = m.get('DeliverName')

        if m.get('DeliverTime') is not None:
            self.deliver_time = m.get('DeliverTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FilterDirtyData') is not None:
            self.filter_dirty_data = m.get('FilterDirtyData')

        if m.get('LogHubStores') is not None:
            temp_model = main_models.DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores()
            self.log_hub_stores = temp_model.from_map(m.get('LogHubStores'))

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStores(DaraModel):
    def __init__(
        self,
        log_hub_store: List[main_models.DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore] = None,
    ):
        self.log_hub_store = log_hub_store

    def validate(self):
        if self.log_hub_store:
            for v1 in self.log_hub_store:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogHubStore'] = []
        if self.log_hub_store is not None:
            for k1 in self.log_hub_store:
                result['LogHubStore'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_hub_store = []
        if m.get('LogHubStore') is not None:
            for k1 in m.get('LogHubStore'):
                temp_model = main_models.DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore()
                self.log_hub_store.append(temp_model.from_map(k1))

        return self

class DescribeLogHubAttributeResponseBodyLoghubInfoLogHubStoresLogHubStore(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        log_key: str = None,
    ):
        self.field_key = field_key
        self.log_key = log_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_key is not None:
            result['FieldKey'] = self.field_key

        if self.log_key is not None:
            result['LogKey'] = self.log_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')

        if m.get('LogKey') is not None:
            self.log_key = m.get('LogKey')

        return self

