# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetConnectionTicketRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        app_id: str = None,
        app_instance_group_id_list: List[str] = None,
        app_instance_group_set_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        app_policy_id: str = None,
        app_start_param: str = None,
        app_version: str = None,
        biz_region_id: str = None,
        end_user_id: str = None,
        environment_config: str = None,
        product_type: str = None,
        task_id: str = None,
    ):
        # The access type.
        self.access_type = access_type
        # The application ID.
        # 
        # > This parameter is required for the initial call and optional for subsequent calls.
        self.app_id = app_id
        # The list of delivery groups.
        # 
        # > - If you specify this parameter, application instances are allocated only from the specified and authorized delivery groups.
        # > - If you specify the `AppInstanceId` or `AppInstancePersistentId` parameter, this parameter is required.
        self.app_instance_group_id_list = app_instance_group_id_list
        # The delivery group set ID used to obtain the connection credential.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The application instance ID.
        # 
        # > 
        # > - If you specify this parameter, only the specified application instance is allocated.
        # > - If you specify this parameter, you must also specify the `AppInstanceGroupIdList` parameter, and the number of delivery group IDs in `AppInstanceGroupIdList` must be 1.
        self.app_instance_id = app_instance_id
        # The persistent session ID.
        self.app_instance_persistent_id = app_instance_persistent_id
        # The policy ID.
        self.app_policy_id = app_policy_id
        # The application startup parameter. This parameter is optional. You can refer to the method for specifying startup parameters in the image creation documentation and manually verify the startup parameters during image creation. This field is suitable for startup parameters with variable content, allowing API callers to set them flexibly. For more information about how to obtain startup parameters, see [How to obtain application installation parameters and startup parameters](https://help.aliyun.com/document_detail/426045.html).
        self.app_start_param = app_start_param
        # The application version. If you specify this parameter, only the specified version of the application is opened. If you do not specify this parameter, any authorized version of the application is opened.
        self.app_version = app_version
        # The region ID.
        # 
        # > If you specify this parameter, application instances are allocated only from delivery groups in the specified region.
        self.biz_region_id = biz_region_id
        # The username.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The environment configuration.
        self.environment_config = environment_config
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The node ID.
        # 
        # > This parameter is required for non-initial calls. Use this parameter query to invoke the node status and connection credential retrieval.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id_list is not None:
            result['AppInstanceGroupIdList'] = self.app_instance_group_id_list

        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        if self.app_start_param is not None:
            result['AppStartParam'] = self.app_start_param

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.environment_config is not None:
            result['EnvironmentConfig'] = self.environment_config

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupIdList') is not None:
            self.app_instance_group_id_list = m.get('AppInstanceGroupIdList')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        if m.get('AppStartParam') is not None:
            self.app_start_param = m.get('AppStartParam')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EnvironmentConfig') is not None:
            self.environment_config = m.get('EnvironmentConfig')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

