# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateQosRuleRequest(DaraModel):
    def __init__(
        self,
        auth_android_id: List[str] = None,
        auth_desktop_id: List[str] = None,
        download: int = None,
        network_package_id: str = None,
        qos_rule_name: str = None,
        upload: int = None,
    ):
        self.auth_android_id = auth_android_id
        self.auth_desktop_id = auth_desktop_id
        # This parameter is required.
        self.download = download
        # This parameter is required.
        self.network_package_id = network_package_id
        # This parameter is required.
        self.qos_rule_name = qos_rule_name
        # This parameter is required.
        self.upload = upload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_android_id is not None:
            result['AuthAndroidId'] = self.auth_android_id

        if self.auth_desktop_id is not None:
            result['AuthDesktopId'] = self.auth_desktop_id

        if self.download is not None:
            result['Download'] = self.download

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.qos_rule_name is not None:
            result['QosRuleName'] = self.qos_rule_name

        if self.upload is not None:
            result['Upload'] = self.upload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAndroidId') is not None:
            self.auth_android_id = m.get('AuthAndroidId')

        if m.get('AuthDesktopId') is not None:
            self.auth_desktop_id = m.get('AuthDesktopId')

        if m.get('Download') is not None:
            self.download = m.get('Download')

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('QosRuleName') is not None:
            self.qos_rule_name = m.get('QosRuleName')

        if m.get('Upload') is not None:
            self.upload = m.get('Upload')

        return self

