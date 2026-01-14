# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class PullServicesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.PullServicesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.PullServicesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PullServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        namespace: str = None,
        namespace_show_name: str = None,
        services: List[main_models.PullServicesResponseBodyDataServices] = None,
    ):
        # The name of the group.
        self.group_name = group_name
        # The namespace.
        self.namespace = namespace
        # The alias of the namespace.
        self.namespace_show_name = namespace_show_name
        # The information about services.
        self.services = services

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name

        result['Services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['Services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')

        self.services = []
        if m.get('Services') is not None:
            for k1 in m.get('Services'):
                temp_model = main_models.PullServicesResponseBodyDataServices()
                self.services.append(temp_model.from_map(k1))

        return self

class PullServicesResponseBodyDataServices(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        sae_app_id: str = None,
        source_id: str = None,
        source_id_list: List[int] = None,
        source_type: str = None,
    ):
        # The name of the group.
        self.group_name = group_name
        # The name of the service.
        self.name = name
        # The namespace.
        self.namespace = namespace
        self.sae_app_id = sae_app_id
        # The ID of the service source.
        self.source_id = source_id
        self.source_id_list = source_id_list
        # The type of the service source.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.sae_app_id is not None:
            result['SaeAppId'] = self.sae_app_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_id_list is not None:
            result['SourceIdList'] = self.source_id_list

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SaeAppId') is not None:
            self.sae_app_id = m.get('SaeAppId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceIdList') is not None:
            self.source_id_list = m.get('SourceIdList')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

