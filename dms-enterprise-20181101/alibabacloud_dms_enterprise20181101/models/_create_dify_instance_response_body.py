# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDifyInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateDifyInstanceResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateDifyInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateDifyInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        app_uuid: str = None,
        instance_id: str = None,
        instance_name: str = None,
        replicas: int = None,
        resource_quota: str = None,
        security_group_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.app_uuid = app_uuid
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.replicas = replicas
        self.resource_quota = resource_quota
        self.security_group_id = security_group_id
        self.status = status
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.resource_quota is not None:
            result['ResourceQuota'] = self.resource_quota

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ResourceQuota') is not None:
            self.resource_quota = m.get('ResourceQuota')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

