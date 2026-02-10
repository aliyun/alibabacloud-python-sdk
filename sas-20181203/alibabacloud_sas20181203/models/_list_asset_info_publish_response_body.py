# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAssetInfoPublishResponseBody(DaraModel):
    def __init__(
        self,
        asset_list: List[main_models.ListAssetInfoPublishResponseBodyAssetList] = None,
        request_id: str = None,
    ):
        # The servers.
        self.asset_list = asset_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.asset_list:
            for v1 in self.asset_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetList'] = []
        if self.asset_list is not None:
            for k1 in self.asset_list:
                result['AssetList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_list = []
        if m.get('AssetList') is not None:
            for k1 in m.get('AssetList'):
                temp_model = main_models.ListAssetInfoPublishResponseBodyAssetList()
                self.asset_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAssetInfoPublishResponseBodyAssetList(DaraModel):
    def __init__(
        self,
        cur_version: str = None,
        last_upgrade_time: int = None,
        status: int = None,
        upgrade_enable: bool = None,
        uuid: str = None,
    ):
        # The version of the Security Center agent.
        self.cur_version = cur_version
        # The time when the Security Center agent was last upgraded.
        self.last_upgrade_time = last_upgrade_time
        # The publish status of the Security Center agent. Valid values:
        # 
        # *   **0**: not started.
        # *   **1**: publishing.
        # *   **2**: published.
        # *   **3**: publish suspended.
        # *   **4**: forcibly upgrading.
        self.status = status
        # Indicates whether automatic upgrade is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.upgrade_enable = upgrade_enable
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_version is not None:
            result['CurVersion'] = self.cur_version

        if self.last_upgrade_time is not None:
            result['LastUpgradeTime'] = self.last_upgrade_time

        if self.status is not None:
            result['Status'] = self.status

        if self.upgrade_enable is not None:
            result['UpgradeEnable'] = self.upgrade_enable

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurVersion') is not None:
            self.cur_version = m.get('CurVersion')

        if m.get('LastUpgradeTime') is not None:
            self.last_upgrade_time = m.get('LastUpgradeTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpgradeEnable') is not None:
            self.upgrade_enable = m.get('UpgradeEnable')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

