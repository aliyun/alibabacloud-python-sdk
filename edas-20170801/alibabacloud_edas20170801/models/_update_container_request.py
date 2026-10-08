# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContainerRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        build_pack_id: int = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The build package number of EDAS Container. You can obtain the build package number in the Build package number column in the EDAS Container release notes table. For more information, see [Release notes for EDAS Container](https://help.aliyun.com/document_detail/92614.html).
        # 
        # This parameter is required.
        self.build_pack_id = build_pack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.build_pack_id is not None:
            result['BuildPackId'] = self.build_pack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BuildPackId') is not None:
            self.build_pack_id = m.get('BuildPackId')

        return self

