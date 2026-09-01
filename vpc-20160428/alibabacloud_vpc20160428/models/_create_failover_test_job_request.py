# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateFailoverTestJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        job_duration: int = None,
        job_type: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the failover test job.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: sends the request without creating the failover test node. The system checks the AccessKey validity, Resource Access Management (RAM) user authorization, and required parameters. If the check fails, the corresponding error is returned. If the check passes, the DryRunOperation error code is returned.
        # - **false** (default): sends a Normal request. After the check passes, a 2xx HTTP status code is returned and the failover test job is created.
        self.dry_run = dry_run
        # The duration of the failover test job. Unit: minutes. Valid values: **1 to 4320**.
        # 
        # This parameter is required.
        self.job_duration = job_duration
        # The failover test job type. Valid values:
        # 
        # - **StartNow**: starts immediately. The test job starts executing immediately after it is created.
        # 
        # - **StartLater**: does not start. Only creates the test job without executing it.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The name of the failover test job.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the failover test job.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query region IDs.
        self.region_id = region_id
        # The list of test resource IDs. You can add up to 16 test resources.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        # The type of the test resource. Valid values: **PHYSICALCONNECTION**: Express Connect circuit.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.job_duration is not None:
            result['JobDuration'] = self.job_duration

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('JobDuration') is not None:
            self.job_duration = m.get('JobDuration')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

