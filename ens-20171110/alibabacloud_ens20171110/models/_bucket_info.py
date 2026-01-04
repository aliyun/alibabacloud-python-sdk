# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BucketInfo(DaraModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        create_time: str = None,
        data_redundancy_type: str = None,
        dispatcher_type: str = None,
        endpoint: str = None,
        ens_region_id: str = None,
        modify_time: str = None,
        resource_type: str = None,
        storage_class: str = None,
    ):
        self.bucket_acl = bucket_acl
        # This parameter is required.
        self.bucket_name = bucket_name
        self.comment = comment
        self.create_time = create_time
        self.data_redundancy_type = data_redundancy_type
        self.dispatcher_type = dispatcher_type
        self.endpoint = endpoint
        self.ens_region_id = ens_region_id
        self.modify_time = modify_time
        self.resource_type = resource_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type

        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')

        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

