# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class CheckUpgradeItemResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upgrade_item: main_models.CheckUpgradeItemResponseBodyUpgradeItem = None,
    ):
        self.request_id = request_id
        self.upgrade_item = upgrade_item

    def validate(self):
        if self.upgrade_item:
            self.upgrade_item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upgrade_item is not None:
            result['UpgradeItem'] = self.upgrade_item.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpgradeItem') is not None:
            temp_model = main_models.CheckUpgradeItemResponseBodyUpgradeItem()
            self.upgrade_item = temp_model.from_map(m.get('UpgradeItem'))

        return self



class CheckUpgradeItemResponseBodyUpgradeItem(DaraModel):
    def __init__(
        self,
        check_result: str = None,
        check_status: str = None,
        upgrade_item_id: str = None,
    ):
        self.check_result = check_result
        self.check_status = check_status
        self.upgrade_item_id = upgrade_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.upgrade_item_id is not None:
            result['UpgradeItemId'] = self.upgrade_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('UpgradeItemId') is not None:
            self.upgrade_item_id = m.get('UpgradeItemId')

        return self

