# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabaseInstancesResponseBody(DaraModel):
    def __init__(
        self,
        database_instances: List[main_models.DescribeDatabaseInstancesResponseBodyDatabaseInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the lightweight database instances.
        self.database_instances = database_instances
        # The page number for a paged query.
        self.page_number = page_number
        # The number of entries per page in the lightweight database instance list.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.database_instances:
            for v1 in self.database_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabaseInstances'] = []
        if self.database_instances is not None:
            for k1 in self.database_instances:
                result['DatabaseInstances'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_instances = []
        if m.get('DatabaseInstances') is not None:
            for k1 in m.get('DatabaseInstances'):
                temp_model = main_models.DescribeDatabaseInstancesResponseBodyDatabaseInstances()
                self.database_instances.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDatabaseInstancesResponseBodyDatabaseInstances(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        charge_type: str = None,
        cpu: str = None,
        creation_time: str = None,
        database_instance_edition: str = None,
        database_instance_id: str = None,
        database_instance_name: str = None,
        database_instance_status: str = None,
        database_version: str = None,
        expired_time: str = None,
        memory: str = None,
        private_connection: str = None,
        public_connection: str = None,
        region_id: str = None,
        storage: int = None,
        super_account_name: str = None,
    ):
        # The business status of the instance. Valid values:
        # 
        # - normal: Normal.
        # - expired: Expired.
        # - overdue: Overdue payment.
        self.business_status = business_status
        # The billing method of the lightweight database instance. Only the subscription billing method is supported. Set the value to PrePaid.
        # 
        # Default value: PrePaid.
        self.charge_type = charge_type
        # The number of vCPUs.
        self.cpu = cpu
        # The time when the instance was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC+0.
        self.creation_time = creation_time
        # The plan ID of the lightweight database instance. Valid values:
        # 
        # - swas.db.c1m1s25: CNY 35 per month.
        # 
        # - swas.db.c1m2s80: CNY 100 per month.
        # 
        # - swas.db.c2m4s120: CNY 200 per month.
        # - swas.db.c2m8s240: CNY 300 per month.
        self.database_instance_edition = database_instance_edition
        # The instance ID of the lightweight database.
        self.database_instance_id = database_instance_id
        # The name of the lightweight database instance.
        self.database_instance_name = database_instance_name
        # The status of the lightweight database instance. Valid values:
        # 
        # - Pending: The instance is being created.
        # - Restarting: The instance is being restarted.
        # - Running: The instance is running.
        # - Stopping: The instance is being stopped.
        # - Stopped: The instance is stopped.
        # - UPGRADING: The instance is being upgraded.
        # - DISABLED: The instance is disabled.
        self.database_instance_status = database_instance_status
        # The database version. Valid values:
        # 
        # - 5.7: MySQL 5.7.
        # - 8.0: MySQL 8.0.
        self.database_version = database_version
        # The time when the instance expires. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC+0.
        # 
        # > The expiration time displayed in the console is 8 hours ahead of the UTC time.
        self.expired_time = expired_time
        # The memory size. Unit: GB.
        self.memory = memory
        # The internal endpoint.
        self.private_connection = private_connection
        # The public endpoint.
        # 
        # > This parameter is returned only if a public endpoint is applied for. You can call the [AllocatePublicConnection](https://help.aliyun.com/document_detail/451413.html) operation to apply for a public endpoint.
        self.public_connection = public_connection
        # The region ID of the lightweight database instance.
        self.region_id = region_id
        # The capacity of the ESSD cloud disk. Unit: GB.
        self.storage = storage
        # The name of the privileged account of the lightweight database instance.
        self.super_account_name = super_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.database_instance_edition is not None:
            result['DatabaseInstanceEdition'] = self.database_instance_edition

        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.database_instance_name is not None:
            result['DatabaseInstanceName'] = self.database_instance_name

        if self.database_instance_status is not None:
            result['DatabaseInstanceStatus'] = self.database_instance_status

        if self.database_version is not None:
            result['DatabaseVersion'] = self.database_version

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.private_connection is not None:
            result['PrivateConnection'] = self.private_connection

        if self.public_connection is not None:
            result['PublicConnection'] = self.public_connection

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.super_account_name is not None:
            result['SuperAccountName'] = self.super_account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DatabaseInstanceEdition') is not None:
            self.database_instance_edition = m.get('DatabaseInstanceEdition')

        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('DatabaseInstanceName') is not None:
            self.database_instance_name = m.get('DatabaseInstanceName')

        if m.get('DatabaseInstanceStatus') is not None:
            self.database_instance_status = m.get('DatabaseInstanceStatus')

        if m.get('DatabaseVersion') is not None:
            self.database_version = m.get('DatabaseVersion')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('PrivateConnection') is not None:
            self.private_connection = m.get('PrivateConnection')

        if m.get('PublicConnection') is not None:
            self.public_connection = m.get('PublicConnection')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('SuperAccountName') is not None:
            self.super_account_name = m.get('SuperAccountName')

        return self

