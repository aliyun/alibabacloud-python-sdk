# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListAllSwimmingLaneGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAllSwimmingLaneGroupsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code or the error code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # Responses.
        self.data = data
        # The status code. Value values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # Additional information. Valid values:
        # 
        # *   The error message returned because the request is normal and **success** is returned.
        # *   If the request is abnormal, the specific exception error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: Valid values:
        # 
        # *   **true**: The information was queried.
        # *   **false**: The information failed to be queried.
        self.success = success
        # The ID of the trace. This parameter is used to query the exact call information.
        self.trace_id = trace_id

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAllSwimmingLaneGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListAllSwimmingLaneGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_ids: List[str] = None,
        apps: List[main_models.ListAllSwimmingLaneGroupsResponseBodyDataApps] = None,
        canary_model: int = None,
        entry_app: main_models.ListAllSwimmingLaneGroupsResponseBodyDataEntryApp = None,
        entry_app_id: str = None,
        entry_app_type: str = None,
        group_id: int = None,
        group_name: str = None,
        mse_namespace_id: str = None,
        namespace_id: str = None,
        swim_version: str = None,
    ):
        # The IDs of the applications associated with the lane group.
        self.app_ids = app_ids
        # The application information.
        self.apps = apps
        # Full-link Grayscale Mode:
        # 
        # *   0: The request is routed based on the content of the request.
        # *   1: Proportional routing
        self.canary_model = canary_model
        # The entry application.
        self.entry_app = entry_app
        # The ID of the gateway.
        self.entry_app_id = entry_app_id
        # The application entry type (gateway type).
        # 
        # *   **apig:** cloud-native API Gateway
        # *   **mse-gw:** an MSE cloud original gateway
        # *   **mse:** Java Services Gateway
        self.entry_app_type = entry_app_type
        # The ID of the lane group.
        self.group_id = group_id
        # The name of a lane group.
        self.group_name = group_name
        # The ID of the namespace to which the MSE instance belongs.
        self.mse_namespace_id = mse_namespace_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The end-to-end grayscale version. Valid values: 0 and 2 (recommended).
        self.swim_version = swim_version

    def validate(self):
        if self.apps:
            for v1 in self.apps:
                 if v1:
                    v1.validate()
        if self.entry_app:
            self.entry_app.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        result['Apps'] = []
        if self.apps is not None:
            for k1 in self.apps:
                result['Apps'].append(k1.to_map() if k1 else None)

        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.entry_app is not None:
            result['EntryApp'] = self.entry_app.to_map()

        if self.entry_app_id is not None:
            result['EntryAppId'] = self.entry_app_id

        if self.entry_app_type is not None:
            result['EntryAppType'] = self.entry_app_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.swim_version is not None:
            result['SwimVersion'] = self.swim_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.ListAllSwimmingLaneGroupsResponseBodyDataApps()
                self.apps.append(temp_model.from_map(k1))

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('EntryApp') is not None:
            temp_model = main_models.ListAllSwimmingLaneGroupsResponseBodyDataEntryApp()
            self.entry_app = temp_model.from_map(m.get('EntryApp'))

        if m.get('EntryAppId') is not None:
            self.entry_app_id = m.get('EntryAppId')

        if m.get('EntryAppType') is not None:
            self.entry_app_type = m.get('EntryAppType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SwimVersion') is not None:
            self.swim_version = m.get('SwimVersion')

        return self

class ListAllSwimmingLaneGroupsResponseBodyDataEntryApp(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        mse_app_id: str = None,
        mse_app_name: str = None,
        mse_namespace_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The type of the application.
        self.app_type = app_type
        # The ID of the MSE instance.
        self.mse_app_id = mse_app_id
        # MSE Instance Name
        self.mse_app_name = mse_app_name
        # The ID of the namespace to which the MSE instance belongs.
        self.mse_namespace_id = mse_namespace_id

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

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.mse_app_id is not None:
            result['MseAppId'] = self.mse_app_id

        if self.mse_app_name is not None:
            result['MseAppName'] = self.mse_app_name

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('MseAppId') is not None:
            self.mse_app_id = m.get('MseAppId')

        if m.get('MseAppName') is not None:
            self.mse_app_name = m.get('MseAppName')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        return self

class ListAllSwimmingLaneGroupsResponseBodyDataApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        mse_app_id: str = None,
        mse_app_name: str = None,
        mse_namespace_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The ID of the MSE instance.
        self.mse_app_id = mse_app_id
        # The name of the MSE instance.
        self.mse_app_name = mse_app_name
        # The ID of the namespace to which the MSE instance belongs.
        self.mse_namespace_id = mse_namespace_id

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

        if self.mse_app_id is not None:
            result['MseAppId'] = self.mse_app_id

        if self.mse_app_name is not None:
            result['MseAppName'] = self.mse_app_name

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('MseAppId') is not None:
            self.mse_app_id = m.get('MseAppId')

        if m.get('MseAppName') is not None:
            self.mse_app_name = m.get('MseAppName')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        return self

