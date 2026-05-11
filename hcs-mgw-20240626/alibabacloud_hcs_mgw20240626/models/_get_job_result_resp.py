# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobResultResp(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        copied_object_count: int = None,
        copied_object_size: int = None,
        failed_object_count: int = None,
        inv_access_id: str = None,
        inv_access_secret: str = None,
        inv_bucket: str = None,
        inv_domain: str = None,
        inv_location: str = None,
        inv_path: str = None,
        inv_region_id: str = None,
        ready_retry: str = None,
        skipped_object_count: int = None,
        skipped_object_size: int = None,
        total_object_count: int = None,
        total_object_size: int = None,
        version: str = None,
    ):
        # The type of the data address created based on the files that failed to be migrated. This parameter is required if you create a data address.
        self.address_type = address_type
        # The number of files that are migrated. The number includes the number of files that are successfully migrated and the number of files that are skipped.
        self.copied_object_count = copied_object_count
        # The data size of files that are migrated.
        self.copied_object_size = copied_object_size
        # The number of files that failed to be migrated.
        self.failed_object_count = failed_object_count
        # The AccessKey ID that is used to access the bucket in which the inventory list of files that failed to be migrated resides. This parameter is required if you create a data address.
        self.inv_access_id = inv_access_id
        # The AccessKey secret that is used to access the bucket in which the inventory list of files that failed to be migrated resides. This parameter is required if you create a data address.
        self.inv_access_secret = inv_access_secret
        # The name of the bucket in which the inventory list of files that failed to be migrated resides. This parameter is required if you create a data address.
        self.inv_bucket = inv_bucket
        # The domain name of the bucket in which the inventory list of files that failed to be migrated resides. This parameter is required if you create a data address.
        self.inv_domain = inv_domain
        # The type of the bucket in which the inventory list of files that failed to be migrated resides. This parameter is required if you create a data address.
        self.inv_location = inv_location
        # The inventory list of files that failed to be migrated. This parameter is required if you create a data address.
        self.inv_path = inv_path
        # The region ID of the bucket in which the inventory list of files that failed to be migrated resides. This parameter is required if you create a data address.
        self.inv_region_id = inv_region_id
        # Indicates whether the files that failed to be migrated can be migrated again.\\
        # Valid values: NoNeed, Ready, and NotReady.
        self.ready_retry = ready_retry
        self.skipped_object_count = skipped_object_count
        self.skipped_object_size = skipped_object_size
        # The total number of files.
        self.total_object_count = total_object_count
        # The total data size of files.
        self.total_object_size = total_object_size
        # The task ID.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.copied_object_count is not None:
            result['CopiedObjectCount'] = self.copied_object_count

        if self.copied_object_size is not None:
            result['CopiedObjectSize'] = self.copied_object_size

        if self.failed_object_count is not None:
            result['FailedObjectCount'] = self.failed_object_count

        if self.inv_access_id is not None:
            result['InvAccessId'] = self.inv_access_id

        if self.inv_access_secret is not None:
            result['InvAccessSecret'] = self.inv_access_secret

        if self.inv_bucket is not None:
            result['InvBucket'] = self.inv_bucket

        if self.inv_domain is not None:
            result['InvDomain'] = self.inv_domain

        if self.inv_location is not None:
            result['InvLocation'] = self.inv_location

        if self.inv_path is not None:
            result['InvPath'] = self.inv_path

        if self.inv_region_id is not None:
            result['InvRegionId'] = self.inv_region_id

        if self.ready_retry is not None:
            result['ReadyRetry'] = self.ready_retry

        if self.skipped_object_count is not None:
            result['SkippedObjectCount'] = self.skipped_object_count

        if self.skipped_object_size is not None:
            result['SkippedObjectSize'] = self.skipped_object_size

        if self.total_object_count is not None:
            result['TotalObjectCount'] = self.total_object_count

        if self.total_object_size is not None:
            result['TotalObjectSize'] = self.total_object_size

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('CopiedObjectCount') is not None:
            self.copied_object_count = m.get('CopiedObjectCount')

        if m.get('CopiedObjectSize') is not None:
            self.copied_object_size = m.get('CopiedObjectSize')

        if m.get('FailedObjectCount') is not None:
            self.failed_object_count = m.get('FailedObjectCount')

        if m.get('InvAccessId') is not None:
            self.inv_access_id = m.get('InvAccessId')

        if m.get('InvAccessSecret') is not None:
            self.inv_access_secret = m.get('InvAccessSecret')

        if m.get('InvBucket') is not None:
            self.inv_bucket = m.get('InvBucket')

        if m.get('InvDomain') is not None:
            self.inv_domain = m.get('InvDomain')

        if m.get('InvLocation') is not None:
            self.inv_location = m.get('InvLocation')

        if m.get('InvPath') is not None:
            self.inv_path = m.get('InvPath')

        if m.get('InvRegionId') is not None:
            self.inv_region_id = m.get('InvRegionId')

        if m.get('ReadyRetry') is not None:
            self.ready_retry = m.get('ReadyRetry')

        if m.get('SkippedObjectCount') is not None:
            self.skipped_object_count = m.get('SkippedObjectCount')

        if m.get('SkippedObjectSize') is not None:
            self.skipped_object_size = m.get('SkippedObjectSize')

        if m.get('TotalObjectCount') is not None:
            self.total_object_count = m.get('TotalObjectCount')

        if m.get('TotalObjectSize') is not None:
            self.total_object_size = m.get('TotalObjectSize')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

