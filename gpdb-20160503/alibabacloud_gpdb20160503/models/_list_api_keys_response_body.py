# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListApiKeysResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of API keys.
        self.items = items
        # The maximum number of records to return in this query.
        self.max_results = max_results
        # The token for the next page in a paged query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListApiKeysResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListApiKeysResponseBodyItems(DaraModel):
    def __init__(
        self,
        auth_services: List[main_models.ListApiKeysResponseBodyItemsAuthServices] = None,
        create_time: str = None,
        description: str = None,
        key_id: str = None,
        key_name: str = None,
        key_prefix: str = None,
    ):
        # The service IDs.
        self.auth_services = auth_services
        # The creation time.
        self.create_time = create_time
        # The description of the API key.
        self.description = description
        # The ID of the API key.
        self.key_id = key_id
        # The name of the API key.
        self.key_name = key_name
        # The prefix of the API key.
        self.key_prefix = key_prefix

    def validate(self):
        if self.auth_services:
            for v1 in self.auth_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthServices'] = []
        if self.auth_services is not None:
            for k1 in self.auth_services:
                result['AuthServices'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_services = []
        if m.get('AuthServices') is not None:
            for k1 in m.get('AuthServices'):
                temp_model = main_models.ListApiKeysResponseBodyItemsAuthServices()
                self.auth_services.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')

        return self

class ListApiKeysResponseBodyItemsAuthServices(DaraModel):
    def __init__(
        self,
        service_id: str = None,
        service_type: str = None,
    ):
        # The service IDs.
        self.service_id = service_id
        # The service type.
        # 
        # Valid values:
        # - memory
        # - drama
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

