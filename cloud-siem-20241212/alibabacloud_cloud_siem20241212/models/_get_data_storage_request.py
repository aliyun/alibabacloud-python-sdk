# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataStorageRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
        with_auto_key_detect: bool = None,
    ):
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # 
        # Note: This parameter is required in actual API calls. If it is not provided, the service returns a 400 error with the message "The specified Lang can not be empty." Explicitly pass the language code.
        self.lang = lang
        # The region where the data management center for threat analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # Specifies whether to read the auto-discovered index configuration of each Logstore. This operation requires accessing Simple Log Service (SLS) for each Logstore. Default value: false. Set this parameter to true only on the storage management page.
        self.with_auto_key_detect = with_auto_key_detect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.with_auto_key_detect is not None:
            result['WithAutoKeyDetect'] = self.with_auto_key_detect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('WithAutoKeyDetect') is not None:
            self.with_auto_key_detect = m.get('WithAutoKeyDetect')

        return self

