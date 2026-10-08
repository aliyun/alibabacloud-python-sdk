# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class InsertDeployGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        deploy_group_entity: main_models.InsertDeployGroupResponseBodyDeployGroupEntity = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The information about the instance group.
        self.deploy_group_entity = deploy_group_entity
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.deploy_group_entity:
            self.deploy_group_entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.deploy_group_entity is not None:
            result['DeployGroupEntity'] = self.deploy_group_entity.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DeployGroupEntity') is not None:
            temp_model = main_models.InsertDeployGroupResponseBodyDeployGroupEntity()
            self.deploy_group_entity = temp_model.from_map(m.get('DeployGroupEntity'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InsertDeployGroupResponseBodyDeployGroupEntity(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        cluster_id: str = None,
        create_time: int = None,
        group_name: str = None,
        group_type: int = None,
        id: str = None,
        package_version_id: str = None,
        update_time: int = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The version of the deployment package for the application.
        # 
        # - If the application is deployed, a string of random numbers is returned.
        # 
        # - If the application is not deployed, the return value is empty.
        self.app_version_id = app_version_id
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The time when the instance group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The name of the instance group.
        self.group_name = group_name
        # The type of the instance group. Valid values:
        # 
        # - 0: the default group.
        # 
        # - 1: a group for which canary traffic management is not enabled.
        # 
        # - 2: a group for which canary traffic management is enabled.
        self.group_type = group_type
        # The ID of the instance group.
        self.id = id
        # The version of the deployment package that was used to deploy an application in the instance group.
        # 
        # - If an application is deployed in the instance group, a string of random numbers is returned.
        # 
        # - If no application is deployed in the instance group, the return value is empty.
        self.package_version_id = package_version_id
        # The time when the instance group was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.id is not None:
            result['Id'] = self.id

        if self.package_version_id is not None:
            result['PackageVersionId'] = self.package_version_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PackageVersionId') is not None:
            self.package_version_id = m.get('PackageVersionId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

