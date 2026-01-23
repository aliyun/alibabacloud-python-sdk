# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class PublishStandardRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        publish_command: main_models.PublishStandardRequestPublishCommand = None,
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
            temp_model = main_models.PublishStandardRequestPublishCommand()
            self.publish_command = temp_model.from_map(m.get('PublishCommand'))

        return self

class PublishStandardRequestPublishCommand(DaraModel):
    def __init__(
        self,
        auto_publish_after_approval: bool = None,
        comment: str = None,
        id: int = None,
        reviewer_id_list: List[str] = None,
        standard_stage: str = None,
        version: int = None,
    ):
        self.auto_publish_after_approval = auto_publish_after_approval
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.id = id
        self.reviewer_id_list = reviewer_id_list
        self.standard_stage = standard_stage
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_publish_after_approval is not None:
            result['AutoPublishAfterApproval'] = self.auto_publish_after_approval

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.id is not None:
            result['Id'] = self.id

        if self.reviewer_id_list is not None:
            result['ReviewerIdList'] = self.reviewer_id_list

        if self.standard_stage is not None:
            result['StandardStage'] = self.standard_stage

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishAfterApproval') is not None:
            self.auto_publish_after_approval = m.get('AutoPublishAfterApproval')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ReviewerIdList') is not None:
            self.reviewer_id_list = m.get('ReviewerIdList')

        if m.get('StandardStage') is not None:
            self.standard_stage = m.get('StandardStage')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

