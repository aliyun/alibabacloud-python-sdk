# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListSourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListSourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSourcesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The list of sources.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListSourcesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListSourcesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        association_reason: str = None,
        association_status: str = None,
        create_timestamp: int = None,
        k_8s_source_info: main_models.ListSourcesResponseBodyDataItemsK8sSourceInfo = None,
        nacos_source_info: main_models.ListSourcesResponseBodyDataItemsNacosSourceInfo = None,
        name: str = None,
        resource_group_id: str = None,
        source_id: str = None,
        update_timestamp: int = None,
    ):
        self.association_reason = association_reason
        self.association_status = association_status
        # The creation timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The source information when the source type is K8S.
        self.k_8s_source_info = k_8s_source_info
        # The source information when the source type is MSE_NACOS.
        self.nacos_source_info = nacos_source_info
        # The source name. If the source type is K8S, the name is the container cluster name. If the source type is MSE_NACOS, the name is the Nacos instance name.
        self.name = name
        self.resource_group_id = resource_group_id
        # The source ID.
        self.source_id = source_id
        # The update timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.k_8s_source_info:
            self.k_8s_source_info.validate()
        if self.nacos_source_info:
            self.nacos_source_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_reason is not None:
            result['associationReason'] = self.association_reason

        if self.association_status is not None:
            result['associationStatus'] = self.association_status

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.k_8s_source_info is not None:
            result['k8sSourceInfo'] = self.k_8s_source_info.to_map()

        if self.nacos_source_info is not None:
            result['nacosSourceInfo'] = self.nacos_source_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('associationReason') is not None:
            self.association_reason = m.get('associationReason')

        if m.get('associationStatus') is not None:
            self.association_status = m.get('associationStatus')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('k8sSourceInfo') is not None:
            temp_model = main_models.ListSourcesResponseBodyDataItemsK8sSourceInfo()
            self.k_8s_source_info = temp_model.from_map(m.get('k8sSourceInfo'))

        if m.get('nacosSourceInfo') is not None:
            temp_model = main_models.ListSourcesResponseBodyDataItemsNacosSourceInfo()
            self.nacos_source_info = temp_model.from_map(m.get('nacosSourceInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class ListSourcesResponseBodyDataItemsNacosSourceInfo(DaraModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        # The endpoint of the Nacos instance.
        self.address = address
        # The registry ID.
        self.cluster_id = cluster_id
        # The Nacos instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

class ListSourcesResponseBodyDataItemsK8sSourceInfo(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        return self

