# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetInstanceUpDownStreamRequest(DaraModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_id: main_models.GetInstanceUpDownStreamRequestInstanceId = None,
        op_tenant_id: int = None,
        project_id: int = None,
        up_stream_depth: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id
        self.up_stream_depth = up_stream_depth

    def validate(self):
        if self.instance_id:
            self.instance_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth

        if self.env is not None:
            result['Env'] = self.env

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.up_stream_depth is not None:
            result['UpStreamDepth'] = self.up_stream_depth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('InstanceId') is not None:
            temp_model = main_models.GetInstanceUpDownStreamRequestInstanceId()
            self.instance_id = temp_model.from_map(m.get('InstanceId'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UpStreamDepth') is not None:
            self.up_stream_depth = m.get('UpStreamDepth')

        return self

class GetInstanceUpDownStreamRequestInstanceId(DaraModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

