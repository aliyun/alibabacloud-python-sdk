# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DescribeDifyAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: main_models.DescribeDifyAttributeResponseBodyRoot = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.DescribeDifyAttributeResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDifyAttributeResponseBodyRoot(DaraModel):
    def __init__(
        self,
        app_uuid: str = None,
        billing_instance_id: str = None,
        charge_type: str = None,
        expire_time: int = None,
        replicas: str = None,
        resource_quota: str = None,
        security_group_id: str = None,
        status: str = None,
        storage_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.app_uuid = app_uuid
        self.billing_instance_id = billing_instance_id
        self.charge_type = charge_type
        self.expire_time = expire_time
        self.replicas = replicas
        self.resource_quota = resource_quota
        self.security_group_id = security_group_id
        self.status = status
        self.storage_type = storage_type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_uuid is not None:
            result['AppUuid'] = self.app_uuid

        if self.billing_instance_id is not None:
            result['BillingInstanceId'] = self.billing_instance_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.resource_quota is not None:
            result['ResourceQuota'] = self.resource_quota

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUuid') is not None:
            self.app_uuid = m.get('AppUuid')

        if m.get('BillingInstanceId') is not None:
            self.billing_instance_id = m.get('BillingInstanceId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ResourceQuota') is not None:
            self.resource_quota = m.get('ResourceQuota')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

