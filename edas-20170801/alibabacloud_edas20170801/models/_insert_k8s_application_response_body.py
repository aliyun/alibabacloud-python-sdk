# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class InsertK8sApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application_info: main_models.InsertK8sApplicationResponseBodyApplicationInfo = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details of the application.
        self.application_info = application_info
        # The status code of the interface or the POP error code.
        self.code = code
        # The additional information.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_info:
            self.application_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_info is not None:
            result['ApplicationInfo'] = self.application_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationInfo') is not None:
            temp_model = main_models.InsertK8sApplicationResponseBodyApplicationInfo()
            self.application_info = temp_model.from_map(m.get('ApplicationInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InsertK8sApplicationResponseBodyApplicationInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        change_order_id: str = None,
        cluster_type: int = None,
        dockerize: bool = None,
        edas_id: str = None,
        owner: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The ID of the change process. You can call the GetChangeOrderInfo operation to query the ID. For more information, see [GetChangeOrderInfo](https://help.aliyun.com/document_detail/62072.html).
        self.change_order_id = change_order_id
        # The type of the cluster in which the application is deployed.
        # 
        # - 0: regular Docker cluster.
        # 
        # - 1: Swarm cluster (discontinued).
        # 
        # - 2: ECS cluster.
        # 
        # - 3: self-managed Kubernetes cluster in EDAS (discontinued).
        # 
        # - 4: cluster for applications that are automatically registered with Pandora.
        # 
        # - 5: Kubernetes clusters and Serverless Kubernetes clusters.
        self.cluster_type = cluster_type
        # Indicates whether the application is a Docker application.
        # 
        # - true: The application is a Docker application.
        # 
        # - false: The application is not a Docker application.
        self.dockerize = dockerize
        # The ID of the user account.
        self.edas_id = edas_id
        # The owner of the application.
        self.owner = owner
        # The ID of the region.
        self.region_id = region_id
        # The Alibaba Cloud account that is used to create the application.
        self.user_id = user_id

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

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.dockerize is not None:
            result['Dockerize'] = self.dockerize

        if self.edas_id is not None:
            result['EdasId'] = self.edas_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Dockerize') is not None:
            self.dockerize = m.get('Dockerize')

        if m.get('EdasId') is not None:
            self.edas_id = m.get('EdasId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

