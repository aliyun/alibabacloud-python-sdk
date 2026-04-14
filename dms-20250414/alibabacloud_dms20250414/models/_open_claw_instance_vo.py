# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class OpenClawInstanceVO(DaraModel):
    def __init__(
        self,
        aliyun_account_uid: str = None,
        auth_type: str = None,
        basic_auth_password: str = None,
        basic_auth_username: str = None,
        charge_type: str = None,
        cpu: float = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_info: main_models.OpenClawInstanceVOImageInfo = None,
        instance_desc: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_region: str = None,
        last_active_time: str = None,
        lock_time: str = None,
        memory_size: int = None,
        openclaw_token: str = None,
        owner_uid: str = None,
        public_domain: str = None,
        status: int = None,
        status_desc: str = None,
        status_message: str = None,
        trial_expire_time: str = None,
        variables: str = None,
    ):
        self.aliyun_account_uid = aliyun_account_uid
        self.auth_type = auth_type
        self.basic_auth_password = basic_auth_password
        self.basic_auth_username = basic_auth_username
        self.charge_type = charge_type
        self.cpu = cpu
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.image_info = image_info
        self.instance_desc = instance_desc
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_region = instance_region
        self.last_active_time = last_active_time
        self.lock_time = lock_time
        self.memory_size = memory_size
        self.openclaw_token = openclaw_token
        self.owner_uid = owner_uid
        self.public_domain = public_domain
        self.status = status
        self.status_desc = status_desc
        self.status_message = status_message
        self.trial_expire_time = trial_expire_time
        self.variables = variables

    def validate(self):
        if self.image_info:
            self.image_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_account_uid is not None:
            result['AliyunAccountUid'] = self.aliyun_account_uid

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.basic_auth_password is not None:
            result['BasicAuthPassword'] = self.basic_auth_password

        if self.basic_auth_username is not None:
            result['BasicAuthUsername'] = self.basic_auth_username

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()

        if self.instance_desc is not None:
            result['InstanceDesc'] = self.instance_desc

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region

        if self.last_active_time is not None:
            result['LastActiveTime'] = self.last_active_time

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.openclaw_token is not None:
            result['OpenclawToken'] = self.openclaw_token

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.public_domain is not None:
            result['PublicDomain'] = self.public_domain

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunAccountUid') is not None:
            self.aliyun_account_uid = m.get('AliyunAccountUid')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('BasicAuthPassword') is not None:
            self.basic_auth_password = m.get('BasicAuthPassword')

        if m.get('BasicAuthUsername') is not None:
            self.basic_auth_username = m.get('BasicAuthUsername')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageInfo') is not None:
            temp_model = main_models.OpenClawInstanceVOImageInfo()
            self.image_info = temp_model.from_map(m.get('ImageInfo'))

        if m.get('InstanceDesc') is not None:
            self.instance_desc = m.get('InstanceDesc')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')

        if m.get('LastActiveTime') is not None:
            self.last_active_time = m.get('LastActiveTime')

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('OpenclawToken') is not None:
            self.openclaw_token = m.get('OpenclawToken')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('PublicDomain') is not None:
            self.public_domain = m.get('PublicDomain')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self



class OpenClawInstanceVOImageInfo(DaraModel):
    def __init__(
        self,
        image_id: int = None,
        name: str = None,
        namespace: str = None,
        tag: str = None,
        version_desc: str = None,
    ):
        self.image_id = image_id
        self.name = name
        self.namespace = namespace
        self.tag = tag
        self.version_desc = version_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.version_desc is not None:
            result['VersionDesc'] = self.version_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('VersionDesc') is not None:
            self.version_desc = m.get('VersionDesc')

        return self

