# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOssBucketResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListOssBucketResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListOssBucketResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOssBucketResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        message: str = None,
        region_id: str = None,
        storage_class: str = None,
        support: bool = None,
        support_config: str = None,
    ):
        # The name of the bucket.
        self.bucket_name = bucket_name
        # The reason why the bucket cannot be checked.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # The storage class of the bucket. Valid values:
        # 
        # *   Standard (default)
        # *   IA
        # *   Archive
        # *   ColdArchive
        self.storage_class = storage_class
        # Indicates whether the bucket can be checked. Valid values:
        # 
        # *   true
        # *   false
        self.support = support
        # Whether to support config. Valid values:
        # 
        # * true
        # * false
        self.support_config = support_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.support is not None:
            result['Support'] = self.support

        if self.support_config is not None:
            result['SupportConfig'] = self.support_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('Support') is not None:
            self.support = m.get('Support')

        if m.get('SupportConfig') is not None:
            self.support_config = m.get('SupportConfig')

        return self

