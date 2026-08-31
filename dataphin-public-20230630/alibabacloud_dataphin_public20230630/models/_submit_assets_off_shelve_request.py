# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitAssetsOffShelveRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        submit_command: main_models.SubmitAssetsOffShelveRequestSubmitCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id
        # The delisting submit command.
        # 
        # This parameter is required.
        self.submit_command = submit_command

    def validate(self):
        if self.submit_command:
            self.submit_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.submit_command is not None:
            result['SubmitCommand'] = self.submit_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('SubmitCommand') is not None:
            temp_model = main_models.SubmitAssetsOffShelveRequestSubmitCommand()
            self.submit_command = temp_model.from_map(m.get('SubmitCommand'))

        return self

class SubmitAssetsOffShelveRequestSubmitCommand(DaraModel):
    def __init__(
        self,
        guid_list: List[str] = None,
        off_shelve_description: str = None,
    ):
        # The list of asset GUIDs to be delisted. A maximum of 50 GUIDs can be specified per request.
        # 
        # This parameter is required.
        self.guid_list = guid_list
        # The delisting description. The value must be 1 to 100 characters in length.
        # 
        # This parameter is required.
        self.off_shelve_description = off_shelve_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guid_list is not None:
            result['GuidList'] = self.guid_list

        if self.off_shelve_description is not None:
            result['OffShelveDescription'] = self.off_shelve_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuidList') is not None:
            self.guid_list = m.get('GuidList')

        if m.get('OffShelveDescription') is not None:
            self.off_shelve_description = m.get('OffShelveDescription')

        return self

