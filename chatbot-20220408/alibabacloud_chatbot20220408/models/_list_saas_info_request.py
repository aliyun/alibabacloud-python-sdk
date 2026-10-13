# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSaasInfoRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        saas_group_codes: str = None,
        saas_name: str = None,
    ):
        # The business space key. If this parameter is not specified, the default business space is accessed. You can obtain the key value from the business management page of the Alibaba Cloud account.
        self.agent_key = agent_key
        # The SaaS permission group codes owned by the user. Separate multiple codes with commas (,).
        self.saas_group_codes = saas_group_codes
        # The username of the business party.
        # 
        # This parameter is required.
        self.saas_name = saas_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.saas_group_codes is not None:
            result['SaasGroupCodes'] = self.saas_group_codes

        if self.saas_name is not None:
            result['SaasName'] = self.saas_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('SaasGroupCodes') is not None:
            self.saas_group_codes = m.get('SaasGroupCodes')

        if m.get('SaasName') is not None:
            self.saas_name = m.get('SaasName')

        return self

