# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAppInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        instance_list: List[main_models.DescribeAppInstanceListResponseBodyInstanceList] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The application instances.
        self.instance_list = instance_list
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.DescribeAppInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAppInstanceListResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        canary: bool = None,
        group_id: str = None,
        group_name: str = None,
        node_labels: str = None,
        node_name: str = None,
        pod_raw: str = None,
        version: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # Indicates whether the application was released in canary release mode.
        # 
        # - `true`: The application was released in canary release mode.
        # 
        # - `false`: The application was not released in canary release mode
        self.canary = canary
        # The ID of the instance group to which the application is deployed.
        self.group_id = group_id
        # The name of the instance group to which the application is deployed.
        self.group_name = group_name
        # The labels of the node. The value is a JSON string.
        self.node_labels = node_labels
        # The name of the node.
        self.node_name = node_name
        # The information about the pod. The value is a JSON string.
        self.pod_raw = pod_raw
        # The deployment package version of the node.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.canary is not None:
            result['Canary'] = self.canary

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.node_labels is not None:
            result['NodeLabels'] = self.node_labels

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod_raw is not None:
            result['PodRaw'] = self.pod_raw

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Canary') is not None:
            self.canary = m.get('Canary')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('NodeLabels') is not None:
            self.node_labels = m.get('NodeLabels')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PodRaw') is not None:
            self.pod_raw = m.get('PodRaw')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

