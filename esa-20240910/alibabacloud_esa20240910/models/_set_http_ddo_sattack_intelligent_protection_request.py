# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetHttpDDoSAttackIntelligentProtectionRequest(DaraModel):
    def __init__(
        self,
        ai_mode: str = None,
        ai_template: str = None,
        site_id: int = None,
    ):
        # The HTTP DDoS depth learning and defense pattern. Valid values:
        # - **observe**: Monitor.
        # - **defense**: Block.
        # 
        # This parameter is required.
        self.ai_mode = ai_mode
        # The HTTP DDoS deep learning and protection level. Valid values:
        # - **level0**: Very loose.
        # - **level30**: Loose.
        # - **level60**: Normal.
        # - **level90**: Strict.
        # 
        # This parameter is required.
        self.ai_template = ai_template
        # The ID of the site. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode

        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')

        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

