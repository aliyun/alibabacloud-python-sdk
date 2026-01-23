# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListArtifactLifecycleRuleRequest(DaraModel):
    def __init__(
        self,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # Specifies whether to enable lifecycle management for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The ID of the Container Registry Enterprise Edition instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

