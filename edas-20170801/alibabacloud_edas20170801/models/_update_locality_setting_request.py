# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLocalitySettingRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enabled: bool = None,
        namespace_id: str = None,
        region: str = None,
        threshold: float = None,
    ):
        # The ID of the application. You can call the [ListApplication](https://help.aliyun.com/document_detail/149390.html) operation to obtain this ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether the setting is active:
        # 
        # - true: The setting is active.
        # 
        # - false: The setting is not active.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The ID of the namespace. This ID cannot be changed after the namespace is created. The format is [unk]physical space identifier[unk].
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The ID of the region where the elastic compute unit (ECU) is located.
        # 
        # This parameter is required.
        self.region = region
        # The total number of items that satisfy the threshold expression.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.region is not None:
            result['Region'] = self.region

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

