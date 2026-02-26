# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyCreateVulWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vul_whitelist_list: main_models.ModifyCreateVulWhitelistResponseBodyVulWhitelistList = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the information about the whitelist.
        self.vul_whitelist_list = vul_whitelist_list

    def validate(self):
        if self.vul_whitelist_list:
            self.vul_whitelist_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vul_whitelist_list is not None:
            result['VulWhitelistList'] = self.vul_whitelist_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VulWhitelistList') is not None:
            temp_model = main_models.ModifyCreateVulWhitelistResponseBodyVulWhitelistList()
            self.vul_whitelist_list = temp_model.from_map(m.get('VulWhitelistList'))

        return self

class ModifyCreateVulWhitelistResponseBodyVulWhitelistList(DaraModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

