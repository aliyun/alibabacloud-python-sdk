# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpgradeInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpgradeInfoResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpgradeInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class UpgradeInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        upgrade_info: main_models.UpgradeInfoResponseBodyResultUpgradeInfo = None,
    ):
        self.upgrade_info = upgrade_info

    def validate(self):
        if self.upgrade_info:
            self.upgrade_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.upgrade_info is not None:
            result['UpgradeInfo'] = self.upgrade_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpgradeInfo') is not None:
            temp_model = main_models.UpgradeInfoResponseBodyResultUpgradeInfo()
            self.upgrade_info = temp_model.from_map(m.get('UpgradeInfo'))

        return self

class UpgradeInfoResponseBodyResultUpgradeInfo(DaraModel):
    def __init__(
        self,
        cur_repo_version: str = None,
        update_repo_version: str = None,
        upgrade: bool = None,
        cur_apack_version: str = None,
        cur_es_version: str = None,
        upgrade_apack_version: str = None,
        upgrade_es_version: str = None,
    ):
        self.cur_repo_version = cur_repo_version
        self.update_repo_version = update_repo_version
        self.upgrade = upgrade
        self.cur_apack_version = cur_apack_version
        self.cur_es_version = cur_es_version
        self.upgrade_apack_version = upgrade_apack_version
        self.upgrade_es_version = upgrade_es_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_repo_version is not None:
            result['CurRepoVersion'] = self.cur_repo_version

        if self.update_repo_version is not None:
            result['UpdateRepoVersion'] = self.update_repo_version

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        if self.cur_apack_version is not None:
            result['curApackVersion'] = self.cur_apack_version

        if self.cur_es_version is not None:
            result['curEsVersion'] = self.cur_es_version

        if self.upgrade_apack_version is not None:
            result['upgradeApackVersion'] = self.upgrade_apack_version

        if self.upgrade_es_version is not None:
            result['upgradeEsVersion'] = self.upgrade_es_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurRepoVersion') is not None:
            self.cur_repo_version = m.get('CurRepoVersion')

        if m.get('UpdateRepoVersion') is not None:
            self.update_repo_version = m.get('UpdateRepoVersion')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        if m.get('curApackVersion') is not None:
            self.cur_apack_version = m.get('curApackVersion')

        if m.get('curEsVersion') is not None:
            self.cur_es_version = m.get('curEsVersion')

        if m.get('upgradeApackVersion') is not None:
            self.upgrade_apack_version = m.get('upgradeApackVersion')

        if m.get('upgradeEsVersion') is not None:
            self.upgrade_es_version = m.get('upgradeEsVersion')

        return self

