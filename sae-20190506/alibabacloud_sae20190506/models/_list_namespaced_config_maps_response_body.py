# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListNamespacedConfigMapsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListNamespacedConfigMapsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A client error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The data returned by the request.
        self.data = data
        # The error code.
        # 
        # -
        # 
        # - This parameter is returned only if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The response message. Valid values:
        # 
        # - Returns **success** if the request is successful.
        # 
        # - Returns an error message if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID. You can use this ID to trace the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListNamespacedConfigMapsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ListNamespacedConfigMapsResponseBodyData(DaraModel):
    def __init__(
        self,
        config_maps: List[main_models.ListNamespacedConfigMapsResponseBodyDataConfigMaps] = None,
    ):
        # The list of ConfigMap instances.
        self.config_maps = config_maps

    def validate(self):
        if self.config_maps:
            for v1 in self.config_maps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigMaps'] = []
        if self.config_maps is not None:
            for k1 in self.config_maps:
                result['ConfigMaps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_maps = []
        if m.get('ConfigMaps') is not None:
            for k1 in m.get('ConfigMaps'):
                temp_model = main_models.ListNamespacedConfigMapsResponseBodyDataConfigMaps()
                self.config_maps.append(temp_model.from_map(k1))

        return self

class ListNamespacedConfigMapsResponseBodyDataConfigMaps(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        create_time: int = None,
        data: Dict[str, Any] = None,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        relate_apps: List[main_models.ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps] = None,
        update_time: int = None,
    ):
        # The ID of the ConfigMap instance.
        self.config_map_id = config_map_id
        # The creation time.
        self.create_time = create_time
        # The key-value pairs of the ConfigMap instance.
        # 
        # For more information about the ConfigMap, see [Manage and use configuration items](https://help.aliyun.com/document_detail/171326.html).
        self.data = data
        # The description of the instance.
        self.description = description
        # The name of the instance.
        self.name = name
        # The namespace ID.
        self.namespace_id = namespace_id
        # The associated applications.
        self.relate_apps = relate_apps
        # The last update time.
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for v1 in self.relate_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data is not None:
            result['Data'] = self.data

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k1 in self.relate_apps:
                result['RelateApps'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k1 in m.get('RelateApps'):
                temp_model = main_models.ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps()
                self.relate_apps.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

