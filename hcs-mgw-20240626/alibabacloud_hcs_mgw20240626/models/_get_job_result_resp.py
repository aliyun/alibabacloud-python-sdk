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
        self.address_type = address_type
        self.copied_object_count = copied_object_count
        self.copied_object_size = copied_object_size
        self.failed_object_count = failed_object_count
        self.inv_access_id = inv_access_id
        self.inv_access_secret = inv_access_secret
        self.inv_bucket = inv_bucket
        self.inv_domain = inv_domain
        self.inv_location = inv_location
        self.inv_path = inv_path
        self.inv_region_id = inv_region_id
        self.ready_retry = ready_retry
        self.skipped_object_count = skipped_object_count
        self.skipped_object_size = skipped_object_size
        self.total_object_count = total_object_count
        self.total_object_size = total_object_size
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

