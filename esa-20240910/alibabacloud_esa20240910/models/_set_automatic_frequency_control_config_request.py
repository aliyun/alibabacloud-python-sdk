# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAutomaticFrequencyControlConfigRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        enable: str = None,
        level: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The action to perform. Valid values:
        # - **observe**: Monitor.
        # - **deny**: Block.
        # - **js**: JavaScript Challenge.
        # 
        # This parameter is required.
        self.action_type = action_type
        # Specifies whether to enable the feature. Valid values:
        # 
        #  - **on**: Enabled.
        # 
        #  - **off**: Disabled.
        # 
        # This parameter is required.
        self.enable = enable
        # The protection level. Valid values:
        # - **loose**: Loose.
        # - **normal**: Medium.
        # - **strict**: Strict.
        # 
        # This parameter is required.
        self.level = level
        # The ID of the site. You can obtain the ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site. For sites with version management enabled, you can use this parameter to specify the site version to which the configuration applies. Default value: 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.level is not None:
            result['Level'] = self.level

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

