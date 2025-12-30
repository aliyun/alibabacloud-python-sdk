# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class FixDataRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        fix_data_command: main_models.FixDataRequestFixDataCommand = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.fix_data_command = fix_data_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.fix_data_command:
            self.fix_data_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.fix_data_command is not None:
            result['FixDataCommand'] = self.fix_data_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FixDataCommand') is not None:
            temp_model = main_models.FixDataRequestFixDataCommand()
            self.fix_data_command = temp_model.from_map(m.get('FixDataCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class FixDataRequestFixDataCommand(DaraModel):
    def __init__(
        self,
        contain_root_instance: bool = None,
        down_stream_instance_id_list: List[main_models.FixDataRequestFixDataCommandDownStreamInstanceIdList] = None,
        downstream_range: str = None,
        force_rerun: bool = None,
        project_id: int = None,
        root_instance_id: main_models.FixDataRequestFixDataCommandRootInstanceId = None,
    ):
        self.contain_root_instance = contain_root_instance
        self.down_stream_instance_id_list = down_stream_instance_id_list
        self.downstream_range = downstream_range
        self.force_rerun = force_rerun
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.root_instance_id = root_instance_id

    def validate(self):
        if self.down_stream_instance_id_list:
            for v1 in self.down_stream_instance_id_list:
                 if v1:
                    v1.validate()
        if self.root_instance_id:
            self.root_instance_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contain_root_instance is not None:
            result['ContainRootInstance'] = self.contain_root_instance

        result['DownStreamInstanceIdList'] = []
        if self.down_stream_instance_id_list is not None:
            for k1 in self.down_stream_instance_id_list:
                result['DownStreamInstanceIdList'].append(k1.to_map() if k1 else None)

        if self.downstream_range is not None:
            result['DownstreamRange'] = self.downstream_range

        if self.force_rerun is not None:
            result['ForceRerun'] = self.force_rerun

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.root_instance_id is not None:
            result['RootInstanceId'] = self.root_instance_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainRootInstance') is not None:
            self.contain_root_instance = m.get('ContainRootInstance')

        self.down_stream_instance_id_list = []
        if m.get('DownStreamInstanceIdList') is not None:
            for k1 in m.get('DownStreamInstanceIdList'):
                temp_model = main_models.FixDataRequestFixDataCommandDownStreamInstanceIdList()
                self.down_stream_instance_id_list.append(temp_model.from_map(k1))

        if m.get('DownstreamRange') is not None:
            self.downstream_range = m.get('DownstreamRange')

        if m.get('ForceRerun') is not None:
            self.force_rerun = m.get('ForceRerun')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RootInstanceId') is not None:
            temp_model = main_models.FixDataRequestFixDataCommandRootInstanceId()
            self.root_instance_id = temp_model.from_map(m.get('RootInstanceId'))

        return self

class FixDataRequestFixDataCommandRootInstanceId(DaraModel):
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

class FixDataRequestFixDataCommandDownStreamInstanceIdList(DaraModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
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

