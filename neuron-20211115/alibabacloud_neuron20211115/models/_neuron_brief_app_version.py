# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronBriefAppVersion(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        app_id: int = None,
        enterprise_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        manage_type: str = None,
        mobi_commit_id: str = None,
        mobi_id: int = None,
        mobi_module_id: str = None,
        mobi_url: str = None,
        product_id: int = None,
        status: str = None,
        version: str = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.app_id = app_id
        self.enterprise_id = enterprise_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.manage_type = manage_type
        self.mobi_commit_id = mobi_commit_id
        self.mobi_id = mobi_id
        self.mobi_module_id = mobi_module_id
        self.mobi_url = mobi_url
        self.product_id = product_id
        self.status = status
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.manage_type is not None:
            result['manageType'] = self.manage_type

        if self.mobi_commit_id is not None:
            result['mobiCommitId'] = self.mobi_commit_id

        if self.mobi_id is not None:
            result['mobiId'] = self.mobi_id

        if self.mobi_module_id is not None:
            result['mobiModuleId'] = self.mobi_module_id

        if self.mobi_url is not None:
            result['mobiUrl'] = self.mobi_url

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('manageType') is not None:
            self.manage_type = m.get('manageType')

        if m.get('mobiCommitId') is not None:
            self.mobi_commit_id = m.get('mobiCommitId')

        if m.get('mobiId') is not None:
            self.mobi_id = m.get('mobiId')

        if m.get('mobiModuleId') is not None:
            self.mobi_module_id = m.get('mobiModuleId')

        if m.get('mobiUrl') is not None:
            self.mobi_url = m.get('mobiUrl')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

