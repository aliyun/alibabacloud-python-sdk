# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class GetProtocolMountTargetResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        protocol_mount_target: main_models.GetProtocolMountTargetResponseBodyProtocolMountTarget = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.protocol_mount_target = protocol_mount_target
        self.request_id = request_id

    def validate(self):
        if self.protocol_mount_target:
            self.protocol_mount_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.protocol_mount_target is not None:
            result['ProtocolMountTarget'] = self.protocol_mount_target.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProtocolMountTarget') is not None:
            temp_model = main_models.GetProtocolMountTargetResponseBodyProtocolMountTarget()
            self.protocol_mount_target = temp_model.from_map(m.get('ProtocolMountTarget'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProtocolMountTargetResponseBodyProtocolMountTarget(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        create_time: str = None,
        description: str = None,
        export_id: str = None,
        fset_id: str = None,
        path: str = None,
        protocol_mount_target_domain: str = None,
        protocol_type: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.access_group_name = access_group_name
        self.create_time = create_time
        self.description = description
        self.export_id = export_id
        # Fileset ID。
        self.fset_id = fset_id
        self.path = path
        self.protocol_mount_target_domain = protocol_mount_target_domain
        self.protocol_type = protocol_type
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.export_id is not None:
            result['ExportId'] = self.export_id

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        if self.path is not None:
            result['Path'] = self.path

        if self.protocol_mount_target_domain is not None:
            result['ProtocolMountTargetDomain'] = self.protocol_mount_target_domain

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProtocolMountTargetDomain') is not None:
            self.protocol_mount_target_domain = m.get('ProtocolMountTargetDomain')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

