# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobPasswordRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        endpoint: str = None,
        password: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
        user_name: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration, data synchronization, or change tracking instance.
        # 
        # >  You can call the [DescribeMigrationJobs](https://help.aliyun.com/document_detail/208139.html), [DescribeSubscriptionInstances](https://help.aliyun.com/document_detail/49442.html), or [DescribeSynchronizationJobs](https://help.aliyun.com/document_detail/49454.html) operation to query the instance ID
        self.dts_instance_id = dts_instance_id
        # The ID of the DTS task. The DTS task can be a data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The database to which the password belongs. Valid values:
        # 
        # *   **src**: source database.
        # *   **dest**: destination database.
        # 
        # >  This parameter is required.
        self.endpoint = endpoint
        # The new password.
        # 
        # >  This parameter is required and cannot be set to a value that is the same as the current password.
        self.password = password
        # The ID of the region where the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Synchronization direction, with values:
        # - **Forward** (default): Forward. - **Reverse**: Reverse.
        self.synchronization_direction = synchronization_direction
        # The account of the source or destination database.
        # 
        # >  This parameter is required.
        self.user_name = user_name
        # Whether it is a seamless integration (Zero-ETL) task, the value can be:
        # - **false**: No. - **true**: Yes.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

