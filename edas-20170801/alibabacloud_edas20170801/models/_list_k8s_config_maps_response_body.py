# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListK8sConfigMapsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListK8sConfigMapsResponseBodyResult = None,
    ):
        # The HTTP status code.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The query results that are returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListK8sConfigMapsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListK8sConfigMapsResponseBodyResult(DaraModel):
    def __init__(
        self,
        config_maps: List[main_models.ListK8sConfigMapsResponseBodyResultConfigMaps] = None,
        total: int = None,
    ):
        # The information about ConfigMaps.
        self.config_maps = config_maps
        # The total number of entries that are returned.
        self.total = total

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_maps = []
        if m.get('ConfigMaps') is not None:
            for k1 in m.get('ConfigMaps'):
                temp_model = main_models.ListK8sConfigMapsResponseBodyResultConfigMaps()
                self.config_maps.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListK8sConfigMapsResponseBodyResultConfigMaps(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        creation_time: str = None,
        data: List[main_models.ListK8sConfigMapsResponseBodyResultConfigMapsData] = None,
        name: str = None,
        namespace: str = None,
        related_apps: List[main_models.ListK8sConfigMapsResponseBodyResultConfigMapsRelatedApps] = None,
    ):
        # The ID of the Kubernetes cluster. You can obtain the cluster ID by calling the GetK8sCluster operation. For more information, see [GetK8sCluster](https://help.aliyun.com/document_detail/181437.html).
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The time when the ConfigMaps were created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The information about ConfigMaps.
        self.data = data
        # The name of the ConfigMap.
        self.name = name
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # The related applications.
        self.related_apps = related_apps

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.related_apps:
            for v1 in self.related_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        result['RelatedApps'] = []
        if self.related_apps is not None:
            for k1 in self.related_apps:
                result['RelatedApps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListK8sConfigMapsResponseBodyResultConfigMapsData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        self.related_apps = []
        if m.get('RelatedApps') is not None:
            for k1 in m.get('RelatedApps'):
                temp_model = main_models.ListK8sConfigMapsResponseBodyResultConfigMapsRelatedApps()
                self.related_apps.append(temp_model.from_map(k1))

        return self

class ListK8sConfigMapsResponseBodyResultConfigMapsRelatedApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
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

class ListK8sConfigMapsResponseBodyResultConfigMapsData(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The user-defined key that is stored in the ConfigMap.
        self.key = key
        # The user-defined value that is stored in the ConfigMap.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

