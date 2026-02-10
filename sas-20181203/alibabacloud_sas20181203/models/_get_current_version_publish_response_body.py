# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCurrentVersionPublishResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCurrentVersionPublishResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetCurrentVersionPublishResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCurrentVersionPublishResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_upgrade: int = None,
        big_customer: bool = None,
        cur_version: str = None,
        force_upgrade_time: int = None,
        gray_switch_status: int = None,
        latest_version: str = None,
        latest_version_create: int = None,
        latest_version_desc: str = None,
        publish_status: int = None,
        upgrade_version: str = None,
    ):
        # Indicates whether automatic upgrade is enabled. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        self.auto_upgrade = auto_upgrade
        # Indicates whether you can enable custom upgrade for the Security Center agent. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.big_customer = big_customer
        # The version of the Security Center agent.
        self.cur_version = cur_version
        # The timestamp when the Security Center agent was forcibly upgraded.
        self.force_upgrade_time = force_upgrade_time
        # Indicates whether the canary release policy is enabled. Valid values:
        # 
        # *   **1**: yes.
        # *   .**0**: no.
        self.gray_switch_status = gray_switch_status
        # The latest version of the Security Center agent.
        self.latest_version = latest_version
        # The timestamp when the latest version of the Security Center agent was created.
        self.latest_version_create = latest_version_create
        # The description of about the latest version.
        self.latest_version_desc = latest_version_desc
        # The publish status of the Security Center agent. Valid values:
        # 
        # *   **0**: not started.
        # *   **1**: publishing.
        # *   **2**: published.
        # *   **3**: publish suspended.
        # *   **4**: forcibly upgrading.
        self.publish_status = publish_status
        # The destination version of the Security Center agent.
        self.upgrade_version = upgrade_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade is not None:
            result['AutoUpgrade'] = self.auto_upgrade

        if self.big_customer is not None:
            result['BigCustomer'] = self.big_customer

        if self.cur_version is not None:
            result['CurVersion'] = self.cur_version

        if self.force_upgrade_time is not None:
            result['ForceUpgradeTime'] = self.force_upgrade_time

        if self.gray_switch_status is not None:
            result['GraySwitchStatus'] = self.gray_switch_status

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.latest_version_create is not None:
            result['LatestVersionCreate'] = self.latest_version_create

        if self.latest_version_desc is not None:
            result['LatestVersionDesc'] = self.latest_version_desc

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpgrade') is not None:
            self.auto_upgrade = m.get('AutoUpgrade')

        if m.get('BigCustomer') is not None:
            self.big_customer = m.get('BigCustomer')

        if m.get('CurVersion') is not None:
            self.cur_version = m.get('CurVersion')

        if m.get('ForceUpgradeTime') is not None:
            self.force_upgrade_time = m.get('ForceUpgradeTime')

        if m.get('GraySwitchStatus') is not None:
            self.gray_switch_status = m.get('GraySwitchStatus')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('LatestVersionCreate') is not None:
            self.latest_version_create = m.get('LatestVersionCreate')

        if m.get('LatestVersionDesc') is not None:
            self.latest_version_desc = m.get('LatestVersionDesc')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')

        return self

