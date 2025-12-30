# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class PublishObjectListRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        publish_command: main_models.PublishObjectListRequestPublishCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.publish_command = publish_command

    def validate(self):
        if self.publish_command:
            self.publish_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.publish_command is not None:
            result['PublishCommand'] = self.publish_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('PublishCommand') is not None:
            temp_model = main_models.PublishObjectListRequestPublishCommand()
            self.publish_command = temp_model.from_map(m.get('PublishCommand'))

        return self

class PublishObjectListRequestPublishCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        project_id: int = None,
        submit_id_list: List[int] = None,
    ):
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.submit_id_list = submit_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.submit_id_list is not None:
            result['SubmitIdList'] = self.submit_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubmitIdList') is not None:
            self.submit_id_list = m.get('SubmitIdList')

        return self

