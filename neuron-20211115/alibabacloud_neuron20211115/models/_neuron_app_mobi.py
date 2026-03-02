# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronAppMobi(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        artifact_url: str = None,
        commit_id: str = None,
        enterprise_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        mobi_user_id: str = None,
        module_id: str = None,
        module_name: str = None,
        schema_version: str = None,
        status: str = None,
        store_url: str = None,
        token: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.artifact_url = artifact_url
        # This parameter is required.
        self.commit_id = commit_id
        self.enterprise_id = enterprise_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mobi_user_id = mobi_user_id
        self.module_id = module_id
        self.module_name = module_name
        self.schema_version = schema_version
        self.status = status
        self.store_url = store_url
        # This parameter is required.
        self.token = token
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.artifact_url is not None:
            result['artifactUrl'] = self.artifact_url

        if self.commit_id is not None:
            result['commitId'] = self.commit_id

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.mobi_user_id is not None:
            result['mobiUserId'] = self.mobi_user_id

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.status is not None:
            result['status'] = self.status

        if self.store_url is not None:
            result['storeUrl'] = self.store_url

        if self.token is not None:
            result['token'] = self.token

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('artifactUrl') is not None:
            self.artifact_url = m.get('artifactUrl')

        if m.get('commitId') is not None:
            self.commit_id = m.get('commitId')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('mobiUserId') is not None:
            self.mobi_user_id = m.get('mobiUserId')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('storeUrl') is not None:
            self.store_url = m.get('storeUrl')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

