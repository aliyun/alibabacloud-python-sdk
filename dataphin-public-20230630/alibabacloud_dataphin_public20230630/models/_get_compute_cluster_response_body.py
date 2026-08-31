# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetComputeClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster_config: main_models.GetComputeClusterResponseBodyClusterConfig = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The cluster details.
        self.cluster_config = cluster_config
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.cluster_config:
            self.cluster_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_config is not None:
            result['ClusterConfig'] = self.cluster_config.to_map()

        if self.code is not None:
            result['Code'] = self.code

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
        if m.get('ClusterConfig') is not None:
            temp_model = main_models.GetComputeClusterResponseBodyClusterConfig()
            self.cluster_config = temp_model.from_map(m.get('ClusterConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetComputeClusterResponseBodyClusterConfig(DaraModel):
    def __init__(
        self,
        cluster_safety_control: main_models.GetComputeClusterResponseBodyClusterConfigClusterSafetyControl = None,
        des: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        type_version: str = None,
    ):
        # The cluster security control configuration.
        self.cluster_safety_control = cluster_safety_control
        # The cluster description.
        self.des = des
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The cluster ID.
        self.id = id
        # The cluster name.
        self.name = name
        # The cluster owner.
        self.owner = owner
        # The cluster version.
        self.type_version = type_version

    def validate(self):
        if self.cluster_safety_control:
            self.cluster_safety_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_safety_control is not None:
            result['ClusterSafetyControl'] = self.cluster_safety_control.to_map()

        if self.des is not None:
            result['Des'] = self.des

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.type_version is not None:
            result['TypeVersion'] = self.type_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSafetyControl') is not None:
            temp_model = main_models.GetComputeClusterResponseBodyClusterConfigClusterSafetyControl()
            self.cluster_safety_control = temp_model.from_map(m.get('ClusterSafetyControl'))

        if m.get('Des') is not None:
            self.des = m.get('Des')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TypeVersion') is not None:
            self.type_version = m.get('TypeVersion')

        return self

class GetComputeClusterResponseBodyClusterConfigClusterSafetyControl(DaraModel):
    def __init__(
        self,
        cluster_safety_auth_type: str = None,
        user_group_ids: List[str] = None,
        user_group_names: List[str] = None,
        user_ids: List[str] = None,
        user_names: List[str] = None,
    ):
        # The control mode.
        self.cluster_safety_auth_type = cluster_safety_auth_type
        # The list of whitelisted user group IDs.
        self.user_group_ids = user_group_ids
        # The list of whitelisted user group names.
        self.user_group_names = user_group_names
        # The list of whitelisted user IDs.
        self.user_ids = user_ids
        # The list of whitelisted usernames.
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_safety_auth_type is not None:
            result['ClusterSafetyAuthType'] = self.cluster_safety_auth_type

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_group_names is not None:
            result['UserGroupNames'] = self.user_group_names

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.user_names is not None:
            result['UserNames'] = self.user_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSafetyAuthType') is not None:
            self.cluster_safety_auth_type = m.get('ClusterSafetyAuthType')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserGroupNames') is not None:
            self.user_group_names = m.get('UserGroupNames')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')

        return self

