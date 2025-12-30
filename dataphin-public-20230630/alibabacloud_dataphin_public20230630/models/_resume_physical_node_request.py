# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ResumePhysicalNodeRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        resume_command: main_models.ResumePhysicalNodeRequestResumeCommand = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.resume_command = resume_command

    def validate(self):
        if self.resume_command:
            self.resume_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.resume_command is not None:
            result['ResumeCommand'] = self.resume_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ResumeCommand') is not None:
            temp_model = main_models.ResumePhysicalNodeRequestResumeCommand()
            self.resume_command = temp_model.from_map(m.get('ResumeCommand'))

        return self

class ResumePhysicalNodeRequestResumeCommand(DaraModel):
    def __init__(
        self,
        node_id_list: List[str] = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.node_id_list = node_id_list
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

