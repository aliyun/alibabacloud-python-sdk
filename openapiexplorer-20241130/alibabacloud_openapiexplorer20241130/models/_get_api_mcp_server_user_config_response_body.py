# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetApiMcpServerUserConfigResponseBody(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        enable_public_access: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        vpc_whitelists: List[str] = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id
        # Specifies whether to enable public network access for all API MCP Servers, including system MCP Servers, under your account. By default, this feature is enabled. If you disable it, you can access the servers only through VPC domain names.
        self.enable_public_access = enable_public_access
        # The time when the configuration was created.
        self.gmt_create = gmt_create
        # The time when the configuration was last updated.
        self.gmt_modified = gmt_modified
        # The request ID.
        self.request_id = request_id
        # The whitelist of source VPCs that are allowed to send requests after public network access is disabled. If you do not set this parameter or leave it empty, requests from all sources are allowed.
        self.vpc_whitelists = vpc_whitelists

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.enable_public_access is not None:
            result['enablePublicAccess'] = self.enable_public_access

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vpc_whitelists is not None:
            result['vpcWhitelists'] = self.vpc_whitelists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('enablePublicAccess') is not None:
            self.enable_public_access = m.get('enablePublicAccess')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vpcWhitelists') is not None:
            self.vpc_whitelists = m.get('vpcWhitelists')

        return self

