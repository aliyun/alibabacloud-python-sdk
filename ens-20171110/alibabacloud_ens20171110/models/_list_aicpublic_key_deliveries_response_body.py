# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class ListAICPublicKeyDeliveriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        public_key_deliver_info: List[main_models.ListAICPublicKeyDeliveriesResponseBodyPublicKeyDeliverInfo] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Current page number when paging
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # Public Key List
        self.public_key_deliver_info = public_key_deliver_info
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.public_key_deliver_info:
            for v1 in self.public_key_deliver_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PublicKeyDeliverInfo'] = []
        if self.public_key_deliver_info is not None:
            for k1 in self.public_key_deliver_info:
                result['PublicKeyDeliverInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.public_key_deliver_info = []
        if m.get('PublicKeyDeliverInfo') is not None:
            for k1 in m.get('PublicKeyDeliverInfo'):
                temp_model = main_models.ListAICPublicKeyDeliveriesResponseBodyPublicKeyDeliverInfo()
                self.public_key_deliver_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAICPublicKeyDeliveriesResponseBodyPublicKeyDeliverInfo(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        instance_id: str = None,
        key_group: str = None,
        key_name: str = None,
        key_type: str = None,
    ):
        # The creation time.
        self.creation_time = creation_time
        # The instance ID.
        self.instance_id = instance_id
        # Public Key Grouping
        self.key_group = key_group
        # Public Key Name
        self.key_name = key_name
        # Public key type
        self.key_type = key_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_group is not None:
            result['KeyGroup'] = self.key_group

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyGroup') is not None:
            self.key_group = m.get('KeyGroup')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        return self

