# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyAppInstanceGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        network: main_models.ModifyAppInstanceGroupAttributeRequestNetwork = None,
        node_pool: main_models.ModifyAppInstanceGroupAttributeRequestNodePool = None,
        per_session_per_app: bool = None,
        pre_open_app_id: str = None,
        pre_open_mode: str = None,
        product_type: str = None,
        security_policy: main_models.ModifyAppInstanceGroupAttributeRequestSecurityPolicy = None,
        session_timeout: int = None,
        storage_policy: main_models.ModifyAppInstanceGroupAttributeRequestStoragePolicy = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # The network settings.
        # 
        # >  If you want to use this parameter, submit a ticket.
        self.network = network
        # The information about the resource group.
        self.node_pool = node_pool
        # Specifies whether only one application can be opened in a session.
        # 
        # *   After you enable this feature, the system assigns a session to each application if you open multiple applications in a delivery group. This consumes a larger number of sessions.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.per_session_per_app = per_session_per_app
        # The application ID of the pre-open application. If you set `PreOpenMode` to `SINGLE_APP`, you cannot leave this parameter empty.``
        self.pre_open_app_id = pre_open_app_id
        # The pre-open mode.
        # 
        # Valid values:
        # 
        # *   SINGLE_APP: enables the pre-open mode for a single application.
        # *   OFF: disables the pre-open mode. This is the default value.
        self.pre_open_mode = pre_open_mode
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The security policy.
        self.security_policy = security_policy
        # The duration for which sessions are retained after disconnection. Unit: minutes. After an end user disconnects from a session, the session is closed only after the specified duration elapses. If you want to permanently retain sessions, set this parameter to `-1`. Valid values:-1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy = storage_policy

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()

        if self.per_session_per_app is not None:
            result['PerSessionPerApp'] = self.per_session_per_app

        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id

        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('Network') is not None:
            temp_model = main_models.ModifyAppInstanceGroupAttributeRequestNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('NodePool') is not None:
            temp_model = main_models.ModifyAppInstanceGroupAttributeRequestNodePool()
            self.node_pool = temp_model.from_map(m.get('NodePool'))

        if m.get('PerSessionPerApp') is not None:
            self.per_session_per_app = m.get('PerSessionPerApp')

        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')

        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SecurityPolicy') is not None:
            temp_model = main_models.ModifyAppInstanceGroupAttributeRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m.get('SecurityPolicy'))

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('StoragePolicy') is not None:
            temp_model = main_models.ModifyAppInstanceGroupAttributeRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m.get('StoragePolicy'))

        return self

class ModifyAppInstanceGroupAttributeRequestStoragePolicy(DaraModel):
    def __init__(
        self,
        storage_type_list: List[str] = None,
        user_profile: main_models.ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfile = None,
        user_profile_follow: main_models.ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfileFollow = None,
    ):
        # The storage types.
        self.storage_type_list = storage_type_list
        # The configurations of user data roaming.
        self.user_profile = user_profile
        self.user_profile_follow = user_profile_follow

    def validate(self):
        if self.user_profile:
            self.user_profile.validate()
        if self.user_profile_follow:
            self.user_profile_follow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list

        if self.user_profile is not None:
            result['UserProfile'] = self.user_profile.to_map()

        if self.user_profile_follow is not None:
            result['UserProfileFollow'] = self.user_profile_follow.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')

        if m.get('UserProfile') is not None:
            temp_model = main_models.ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfile()
            self.user_profile = temp_model.from_map(m.get('UserProfile'))

        if m.get('UserProfileFollow') is not None:
            temp_model = main_models.ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfileFollow()
            self.user_profile_follow = temp_model.from_map(m.get('UserProfileFollow'))

        return self

class ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfileFollow(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        profile_follow_switch: bool = None,
    ):
        self.file_system_id = file_system_id
        self.profile_follow_switch = profile_follow_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.profile_follow_switch is not None:
            result['ProfileFollowSwitch'] = self.profile_follow_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProfileFollowSwitch') is not None:
            self.profile_follow_switch = m.get('ProfileFollowSwitch')

        return self

class ModifyAppInstanceGroupAttributeRequestStoragePolicyUserProfile(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        user_profile_switch: bool = None,
    ):
        # The ID of the File Storage NAS (NAS) file system used to store user data.
        self.file_system_id = file_system_id
        # Specifies whether user data roaming is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.user_profile_switch = user_profile_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.user_profile_switch is not None:
            result['UserProfileSwitch'] = self.user_profile_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('UserProfileSwitch') is not None:
            self.user_profile_switch = m.get('UserProfileSwitch')

        return self

class ModifyAppInstanceGroupAttributeRequestSecurityPolicy(DaraModel):
    def __init__(
        self,
        reset_after_unbind: bool = None,
        skip_user_auth_check: bool = None,
    ):
        # Specifies whether to reset after unbinding from a delivery group.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.reset_after_unbind = reset_after_unbind
        # Specifies whether to skip user permission verification.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: This is the default value.
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reset_after_unbind is not None:
            result['ResetAfterUnbind'] = self.reset_after_unbind

        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResetAfterUnbind') is not None:
            self.reset_after_unbind = m.get('ResetAfterUnbind')

        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')

        return self

class ModifyAppInstanceGroupAttributeRequestNodePool(DaraModel):
    def __init__(
        self,
        node_capacity: int = None,
        node_pool_id: str = None,
    ):
        # The maximum number of sessions to which a resource can connect at the same time. If a resource connects to a large number of sessions at the same time, user experience can be compromised. The value range varies based on the resource type. The following items describe the value ranges of different resource types:
        # 
        # *   appstreaming.general.4c8g: 1 to 2
        # *   appstreaming.general.8c16g: 1 to 4
        # *   appstreaming.vgpu.8c16g.4g: 1 to 4
        # *   appstreaming.vgpu.8c31g.16g: 1 to 4
        # *   appstreaming.vgpu.14c93g.12g: 1 to 6
        self.node_capacity = node_capacity
        # The ID of the resource group.
        self.node_pool_id = node_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        return self

class ModifyAppInstanceGroupAttributeRequestNetwork(DaraModel):
    def __init__(
        self,
        domain_rules: List[main_models.ModifyAppInstanceGroupAttributeRequestNetworkDomainRules] = None,
    ):
        # The domain name rules.
        self.domain_rules = domain_rules

    def validate(self):
        if self.domain_rules:
            for v1 in self.domain_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k1 in self.domain_rules:
                result['DomainRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k1 in m.get('DomainRules'):
                temp_model = main_models.ModifyAppInstanceGroupAttributeRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k1))

        return self

class ModifyAppInstanceGroupAttributeRequestNetworkDomainRules(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The policy used for the domain name.
        # 
        # Valid values:
        # 
        # *   allow
        # *   block
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

